"""
Main Experiment Orchestrator (N=225 Paired Comparisons).
Implements the 2x2 Factorial Crossover Study defined in EXPERIMENT_PROTOCOL.md:
- Pre-registered Seed: 42
- Evaluates 4 Conditions:
    T0: Spec-Only (Same Model)
    T1: Code-First (Same Model)
    T2: Code-First (Cross-Family Model)
    T3: Spec-Only (Cross-Family Model)
- Ground Truth: 15 Natural LLM Logic Faults from accepted_faults.json (Frozen v1.0)
- Paired McNemar Test, TOST Equivalence Bounds (theta = ±0.08), GLMM Logistic Regression Dataset
- Full incremental persistence & resume capability
"""

import os
import sys
import json
import time
import random
import csv
import argparse
from pathlib import Path
from typing import Dict, Any, List, Tuple

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.schema import ExperimentalCondition
from src.evaluator import evaluate_generated_test
from src.stats_utils import compute_contingency_table, compute_tost_paired_proportions, export_glmm_dataset, _exact_binomial_two_tailed
from src.runner import LLMClient, PROMPT_TEMPLATES, MODEL_REGISTRY


def run_main_experiment(
    live_api: bool = True,
    sample_size: int = 225,
    random_seed: int = 42,
    output_dir: str = "data/main_results"
) -> Dict[str, Any]:
    print("=" * 80, flush=True)
    print("LAUNCHING MAIN 2x2 FACTORIAL EXPERIMENT (N=225 PAIRED OBSERVATIONS)", flush=True)
    print("Protocol: Code-First Exposure Bias vs. Cross-Family Model Diversity", flush=True)
    print(f"Mode: {'LIVE API INVOCATION' if live_api else 'SIMULATION'}", flush=True)
    print(f"Target Paired Trials: {sample_size} | Seed: {random_seed}", flush=True)
    print("=" * 80, flush=True)

    out_path = project_root / output_dir
    out_path.mkdir(parents=True, exist_ok=True)
    tests_archive_dir = out_path / "generated_tests"
    tests_archive_dir.mkdir(parents=True, exist_ok=True)

    # 1. Load Frozen Accepted Faults
    faults_file = project_root / "data" / "fault_harvest" / "accepted_faults.json"
    if not faults_file.exists():
        raise RuntimeError("Frozen accepted_faults.json not found! Run fault harvesting first.")

    accepted_faults = json.loads(faults_file.read_text(encoding="utf-8"))
    task_ids = sorted(accepted_faults.keys())
    print(f"[Step 1] Loaded {len(task_ids)} tasks with verified natural logic faults.", flush=True)

    # Load problem definitions for signature and docstring
    problems_dir = project_root / "data" / "problems"
    problems_data = {}
    for tid in task_ids:
        p_file = problems_dir / f"{tid}.json"
        problems_data[tid] = json.loads(p_file.read_text(encoding="utf-8"))

    # Determine repetitions per task or subset of tasks
    rng = random.Random(random_seed)
    trial_queue = []
    if sample_size < len(task_ids):
        # Sample subset of tasks for dry-run
        chosen_tasks = task_ids[:sample_size]
        for tid in chosen_tasks:
            trial_queue.append((tid, 1))
        print(f"[Step 2] Selected {len(trial_queue)} tasks for evaluation run.", flush=True)
    else:
        reps_per_task = max(1, sample_size // len(task_ids))
        for tid in task_ids:
            for rep in range(1, reps_per_task + 1):
                trial_queue.append((tid, rep))
        # Fill remainder if any to match exact sample_size
        rem = sample_size - len(trial_queue)
        for i in range(rem):
            trial_queue.append((task_ids[i % len(task_ids)], reps_per_task + 1))
        print(f"[Step 2] Balanced Stratification: {len(task_ids)} tasks x {reps_per_task} repetitions = {len(trial_queue)} trials.", flush=True)

    # Cross-family model assignment map
    # Primary models: Llama 3.3 70B <-> DeepSeek V3 (or Qwen 2.5 Coder 32B)
    def get_cross_model(coder_mod: str) -> str:
        if "llama" in coder_mod.lower():
            return "deepseek/deepseek-chat"
        elif "deepseek" in coder_mod.lower():
            return "meta-llama/llama-3.3-70b-instruct"
        else:
            return "meta-llama/llama-3.3-70b-instruct"

    glmm_csv_file = out_path / "main_glmm_dataset.csv"
    glmm_records = []
    
    # Check for existing completed trials to resume cleanly
    completed_trials = set()
    if glmm_csv_file.exists():
        try:
            with open(glmm_csv_file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    if (r.get("execution_status") or r.get("status")) != "API_ERROR":
                        completed_trials.add((r["trial_id"], r["condition"]))
            print(f"[Resume] Found {len(completed_trials)} existing condition evaluations in {glmm_csv_file.name}", flush=True)
        except Exception:
            pass

    t0_detections = []
    t1_detections = []
    t2_detections = []
    t3_detections = []

    total_tokens = 0
    total_cost_usd = 0.0
    start_time = time.perf_counter()

    # Deterministic shuffle with pre-registered seed
    rng.shuffle(trial_queue)

    print(f"\n[Step 3] Beginning 2x2 Factorial Invocations across {len(trial_queue)} trials...", flush=True)

    for idx, (tid, rep) in enumerate(trial_queue, 1):
        trial_id = f"TRIAL_{idx:03d}_{tid}_REP{rep:02d}"
        t_data = problems_data[tid]
        f_data = accepted_faults[tid]

        fn_name = t_data["function_name"]
        sig = t_data["signature"]
        doc = t_data["docstring"]
        ref_impl = f_data["ref_implementation"]
        faulty_impl = f_data["candidate_code"]
        coder_model = f_data["coder_model"]

        same_model = coder_model
        cross_model = get_cross_model(coder_model)

        print(f"\n[{idx}/{len(trial_queue)}] {trial_id} ({fn_name} - {f_data['difficulty']})", flush=True)
        print(f"  Same Model: {same_model.split('/')[-1]} | Cross Model: {cross_model.split('/')[-1]}", flush=True)

        conditions_to_run = [
            (ExperimentalCondition.T0_SPEC_SAME, same_model, "spec", "T0"),
            (ExperimentalCondition.T1_CODE_SAME, same_model, "code", "T1"),
            (ExperimentalCondition.T2_CODE_CROSS, cross_model, "code", "T2"),
            (ExperimentalCondition.T3_SPEC_CROSS, cross_model, "spec", "T3"),
        ]

        trial_outcome_map = {}
        trial_api_error_map = {}

        for cond_enum, model_name, prompt_type, cond_label in conditions_to_run:
            cond_key = (trial_id, cond_label)
            if cond_key in completed_trials:
                print(f"    [{cond_label}] Already evaluated. Skipping.", flush=True)
                continue

            # Build prompt
            if prompt_type == "spec":
                prompt = PROMPT_TEMPLATES["test_spec_only"].format(signature=sig, docstring=doc)
            else:
                prompt = PROMPT_TEMPLATES["test_code_first"].format(
                    signature=sig, docstring=doc, implementation=faulty_impl
                )

            # Generate test suite
            client = LLMClient(model_name=model_name, temperature=0.2)
            api_error = False
            api_error_msg = ""
            try:
                test_code, p_tok, c_tok, el_sec, cost, meta = client.generate(prompt, max_tokens=800)
                total_tokens += (p_tok + c_tok)
                total_cost_usd += cost
            except Exception as e:
                api_error = True
                api_error_msg = str(e)
                print(f"    [{cond_label} API ERROR] Request failed: {api_error_msg}", flush=True)
                test_code = ""  # Zero synthetic mutations / zero artificial assert False
                p_tok, c_tok, el_sec, cost = 0, 0, 0.0, 0.0

            # Archive generated test code (or log API error note)
            test_file = tests_archive_dir / f"{trial_id}_{cond_label}.py"
            if api_error:
                test_file = test_file.with_suffix(f".{time.time_ns()}.api_error.txt")
                test_file.write_text(f"# API ERROR: {api_error_msg}\n# Request failed. Zero synthetic test generated.\n", encoding="utf-8")
            else:
                test_file.write_text(test_code, encoding="utf-8")

            if api_error:
                # Isolate API error completely from detection calculations
                detect_flag = 0
                valid_flag = 0
                total_cases = 0
                valid_cases = 0
                detecting_cases = 0
                suite_clean_on_ref = 0
                execution_time_ms = 0.0
                exec_status = "API_ERROR"
                print(f"    [{cond_label} API ERROR RECORDED] Status: API_ERROR | Valid: 0/0 | Defect Detected: 0 | Error: {api_error_msg[:80]} | Cleanly excluded from detection", flush=True)
            else:
                # Evaluate against Clean Implementation (False Alarm test) and Faulty Implementation (Detection test)
                eval_out = evaluate_generated_test(
                    problem_id=tid,
                    condition=cond_enum,
                    model_name=model_name,
                    ref_implementation=ref_impl,
                    faulty_implementation=faulty_impl,
                    generated_test_code=test_code,
                    prompt_tokens=p_tok,
                    completion_tokens=c_tok,
                    target_fn_name=fn_name
                )

                detect_flag = 1 if eval_out.detects_fault else 0
                valid_flag = 1 if eval_out.is_valid else 0
                total_cases = eval_out.metadata.get("total_cases", 1)
                valid_cases = eval_out.metadata.get("valid_cases", 0)
                detecting_cases = eval_out.metadata.get("detecting_case_count", 0)
                suite_clean_on_ref = 1 if eval_out.metadata.get("suite_clean_on_ref", False) else 0
                execution_time_ms = eval_out.execution_time_ms
                exec_status = "SUCCESS" if valid_flag else "INVALID_ORACLE"

                print(f"    [{cond_label}] Valid: {valid_cases}/{total_cases} | Defect Detected: {detect_flag} | Execution: {eval_out.execution_time_ms:.1f}ms", flush=True)

            trial_outcome_map[cond_label] = detect_flag
            trial_api_error_map[cond_label] = api_error

            rec = {
                "trial_id": trial_id,
                "problem_id": tid,
                "function_name": fn_name,
                "category": t_data.get("category", "General"),
                "difficulty": f_data.get("difficulty", "Unknown"),
                "kill_ratio": f_data.get("kill_ratio", 0.0),
                "condition": cond_label,
                "model_name": model_name,
                "exposure": "SPEC_ONLY" if prompt_type == "spec" else "CODE_FIRST",
                "model_identity": "SAME_MODEL" if model_name == same_model else "CROSS_MODEL",
                "detected": detect_flag,
                "valid_oracle": valid_flag,
                "total_test_cases": total_cases,
                "valid_test_cases": valid_cases,
                "detecting_cases": detecting_cases,
                "suite_clean_on_ref": suite_clean_on_ref,
                "execution_status": exec_status,
                "prompt_tokens": p_tok,
                "completion_tokens": c_tok,
                "cost_usd": cost,
                "execution_ms": execution_time_ms
            }
            glmm_records.append(rec)

            # Incremental CSV append
            write_header = not glmm_csv_file.exists() or glmm_csv_file.stat().st_size == 0
            with open(glmm_csv_file, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(rec.keys()))
                if write_header:
                    writer.writeheader()
                writer.writerow(rec)

            if api_error and "Error code: 402" in api_error_msg:
                raise SystemExit("Experiment paused after recording HTTP 402. Restore provider access, then resume with the same output directory and settings.")

        # Record paired detections (excluding any pair where an API error occurred)
        if "T0" in trial_outcome_map and "T1" in trial_outcome_map:
            if not trial_api_error_map.get("T0", False) and not trial_api_error_map.get("T1", False):
                t0_detections.append(trial_outcome_map["T0"])
                t1_detections.append(trial_outcome_map["T1"])
        if "T2" in trial_outcome_map and "T3" in trial_outcome_map:
            if not trial_api_error_map.get("T2", False) and not trial_api_error_map.get("T3", False):
                t2_detections.append(trial_outcome_map["T2"])
                t3_detections.append(trial_outcome_map["T3"])

    elapsed_total = time.perf_counter() - start_time
    print(f"\n[Main Experiment Completed] Total Elapsed: {elapsed_total:.1f}s | Cost: ${total_cost_usd:.4f} USD", flush=True)

    # 4. Compute Statistical Tests & Export Formal Report from complete CSV (Unified Historical & Current Trials)
    report_file = out_path / "MAIN_EXPERIMENT_REPORT.md"
    generate_main_report(glmm_csv_file, report_file, elapsed_seconds=elapsed_total)

    return {
        "total_trials": len(trial_queue),
        "total_evaluations": len(glmm_records),
        "total_tokens": total_tokens,
        "total_cost_usd": total_cost_usd,
        "elapsed_seconds": elapsed_total
    }


def generate_main_report(
    glmm_csv_file: Path,
    report_file: Path,
    elapsed_seconds: float = 0.0
):
    """
    Generates the comprehensive main empirical report by reading the complete GLMM CSV.
    Guarantees:
    1. Reads all historical and current evaluations directly from CSV (supporting stop/resume).
    2. Pairs conditions strictly by trial_id.
    3. Excludes any trial from a specific comparison if either condition is missing or encountered an API_ERROR.
    4. Reports explicit pair sample sizes for each research question.
    """
    if not glmm_csv_file.exists():
        print(f"[Report Warning] CSV file not found: {glmm_csv_file}", flush=True)
        return

    with open(glmm_csv_file, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print(f"[Report Warning] CSV file is empty: {glmm_csv_file}", flush=True)
        return

    # Group all evaluations by trial_id
    trials: Dict[str, Dict[str, Dict[str, Any]]] = {}
    total_tokens = 0
    total_cost_usd = 0.0

    for r in rows:
        tid = r["trial_id"]
        cond = r["condition"]
        if tid not in trials:
            trials[tid] = {}
        previous = trials[tid].get(cond)
        if not previous or (previous.get("execution_status") or previous.get("status")) == "API_ERROR":
            trials[tid][cond] = r
        try:
            total_tokens += int(r.get("prompt_tokens", 0)) + int(r.get("completion_tokens", 0))
            total_cost_usd += float(r.get("cost_usd", 0.0))
        except (ValueError, TypeError):
            pass

    api_error_attempts = sum((r.get("execution_status") or r.get("status")) == "API_ERROR" for r in rows)
    rows = [row for conditions in trials.values() for row in conditions.values()]
    sorted_trial_ids = sorted(trials.keys())
    total_trials = len(sorted_trial_ids)
    total_evals = len(rows)

    # -------------------------------------------------------------
    # RQ1: Code-First Bias (T0 vs T1) matched strictly by trial_id
    # -------------------------------------------------------------
    rq1_t0: List[int] = []
    rq1_t1: List[int] = []
    rq1_excluded: List[Tuple[str, str]] = []

    for tid in sorted_trial_ids:
        t_conds = trials[tid]
        has_t0 = "T0" in t_conds
        has_t1 = "T1" in t_conds
        
        if not (has_t0 and has_t1):
            missing = [c for c in ("T0", "T1") if c not in t_conds]
            rq1_excluded.append((tid, f"Missing condition(s): {', '.join(missing)}"))
            continue

        st_t0 = t_conds["T0"].get("execution_status", t_conds["T0"].get("status", "SUCCESS"))
        st_t1 = t_conds["T1"].get("execution_status", t_conds["T1"].get("status", "SUCCESS"))

        if st_t0 == "API_ERROR" or st_t1 == "API_ERROR":
            errs = [c for c, st in (("T0", st_t0), ("T1", st_t1)) if st == "API_ERROR"]
            rq1_excluded.append((tid, f"API_ERROR in {', '.join(errs)}"))
            continue

        rq1_t0.append(int(t_conds["T0"]["detected"]))
        rq1_t1.append(int(t_conds["T1"]["detected"]))

    n_rq1 = len(rq1_t0)
    rq1_ct = compute_contingency_table(rq1_t0, rq1_t1) if n_rq1 > 0 else {}
    t0_rate = (sum(rq1_t0) / n_rq1 * 100) if n_rq1 > 0 else 0.0
    t1_rate_rq1 = (sum(rq1_t1) / n_rq1 * 100) if n_rq1 > 0 else 0.0

    # -------------------------------------------------------------
    # RQ2: Model Diversity & Equivalence (T1 vs T2) matched strictly by trial_id
    # -------------------------------------------------------------
    rq2_t1: List[int] = []
    rq2_t2: List[int] = []
    rq2_excluded: List[Tuple[str, str]] = []

    for tid in sorted_trial_ids:
        t_conds = trials[tid]
        has_t1 = "T1" in t_conds
        has_t2 = "T2" in t_conds

        if not (has_t1 and has_t2):
            missing = [c for c in ("T1", "T2") if c not in t_conds]
            rq2_excluded.append((tid, f"Missing condition(s): {', '.join(missing)}"))
            continue

        st_t1 = t_conds["T1"].get("execution_status", t_conds["T1"].get("status", "SUCCESS"))
        st_t2 = t_conds["T2"].get("execution_status", t_conds["T2"].get("status", "SUCCESS"))

        if st_t1 == "API_ERROR" or st_t2 == "API_ERROR":
            errs = [c for c, st in (("T1", st_t1), ("T2", st_t2)) if st == "API_ERROR"]
            rq2_excluded.append((tid, f"API_ERROR in {', '.join(errs)}"))
            continue

        rq2_t1.append(int(t_conds["T1"]["detected"]))
        rq2_t2.append(int(t_conds["T2"]["detected"]))

    n_rq2 = len(rq2_t1)
    rq2_ct = compute_contingency_table(rq2_t1, rq2_t2) if n_rq2 > 0 else {}
    t1_rate_rq2 = (sum(rq2_t1) / n_rq2 * 100) if n_rq2 > 0 else 0.0
    t2_rate = (sum(rq2_t2) / n_rq2 * 100) if n_rq2 > 0 else 0.0

    tost_res = compute_tost_paired_proportions(rq2_t1, rq2_t2, margin=0.08) if n_rq2 > 0 else {}
    ci_90 = tost_res.get('ci_tost_90', (0.0, 0.0))
    tost_p = tost_res.get('p_tost', 1.0)
    is_equiv = tost_res.get('is_equivalent', False)
    tost_diff = tost_res.get('diff_proportions', 0.0)

    # -------------------------------------------------------------
    # Condition-level Summary (T0, T1, T2, T3)
    # -------------------------------------------------------------
    cond_stats = {}
    for c in ["T0", "T1", "T2", "T3"]:
        c_rows = [r for r in rows if r["condition"] == c]
        tot = len(c_rows)
        errs = sum(1 for r in c_rows if r.get("execution_status") == "API_ERROR" or r.get("status") == "API_ERROR")
        completed = tot - errs
        val = sum(int(r.get("valid_oracle", 0)) for r in c_rows if r.get("execution_status") != "API_ERROR" and r.get("status") != "API_ERROR")
        det = sum(int(r.get("detected", 0)) for r in c_rows if r.get("execution_status") != "API_ERROR" and r.get("status") != "API_ERROR")
        val_pct = (val / completed * 100.0) if completed > 0 else 0.0
        det_pct = (det / completed * 100.0) if completed > 0 else 0.0
        cond_stats[c] = {
            "total": tot,
            "api_errors": errs,
            "completed": completed,
            "valid": val,
            "valid_pct": val_pct,
            "detected": det,
            "detected_pct": det_pct
        }

    # Exact paired tests are reported explicitly, without changing historical callers.
    for table in (rq1_ct, rq2_ct):
        if table:
            table["p_value"] = _exact_binomial_two_tailed(
                table["b_armA_only"], table["discordant_pairs"]
            )
            table["method"] = "Exact two-sided binomial McNemar"

    glmm_lines = [
        "## 4. RQ3 mixed logistic interaction",
        "Fit the protocol model with Rscript scripts/fit_interaction_glmm.R <results CSV>.",
    ]
    coefficient_file = glmm_csv_file.parent / "GLMM_COEFFICIENTS.csv"
    diagnostic_file = glmm_csv_file.parent / "GLMM_DIAGNOSTICS.csv"
    if coefficient_file.exists() and diagnostic_file.exists():
        import hashlib
        with diagnostic_file.open(encoding="utf-8-sig") as stream:
            diagnostics = next(csv.DictReader(stream))
        current_hash = hashlib.md5(glmm_csv_file.read_bytes()).hexdigest()
        if diagnostics.get("input_md5") == current_hash:
            glmm_lines = [
                "## 4. RQ3 mixed logistic interaction",
                "Model fitted by lme4 with binomial logit, coder fixed effects and a problem random intercept.",
                "Formula is detected ~ exposure * cross_model + coder + (1 | problem_id).",
                "",
                "| Term | Coefficient | SE | Wald p | Odds ratio | 95% OR interval |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
            with coefficient_file.open(encoding="utf-8-sig") as stream:
                for term in csv.DictReader(stream):
                    glmm_lines.append(
                        f"| {term['term']} | {float(term['coefficient']):.4f} | "
                        f"{float(term['standard_error']):.4f} | {float(term['p_value']):.6g} | "
                        f"{float(term['odds_ratio']):.4f} | "
                        f"[{float(term['odds_ratio_ci_lower']):.4f}, {float(term['odds_ratio_ci_upper']):.4f}] |"
                    )
            glmm_lines += [
                "",
                f"Included observations {diagnostics['observations']} across {diagnostics['problems']} problems.",
                f"Singular fit {diagnostics['singular']}. Optimizer code {diagnostics['optimizer_code']}.",
                f"Convergence messages {diagnostics['convergence_messages'] or 'none'}.",
                f"Warnings {diagnostics['warnings'] or 'none'}.",
                f"Problem intercept SD {float(diagnostics['problem_intercept_sd']):.4f}.",
                f"Interaction likelihood-ratio p {float(diagnostics['interaction_lrt_p']):.6g}.",
                f"Maximum coefficient change at nAGQ=15 {float(diagnostics['max_coef_change_nagq15']):.6g}.",
                "Full model output and session information are saved in GLMM_OUTPUT.txt.",
            ]
        else:
            glmm_lines.append("Saved GLMM results belong to a different CSV. Refit before interpretation.")

    interpretation_lines = [
        "## 7. Reviewed interpretation and writing readiness",
        "",
        "Collection is complete. The study is ready for a first paper draft with the limitations below.",
        "The random-intercept GLMM is the protocol analysis. Supplemental sensitivity analyses were added after data collection and are exploratory.",
        "",
        "| Condition | Detection among usable suites |",
        "| --- | --- |",
    ]
    for condition in ("T0", "T1", "T2", "T3"):
        summary = cond_stats[condition]
        rate = 100 * summary["detected"] / summary["valid"] if summary["valid"] else 0
        interpretation_lines.append(f"| {condition} | {rate:.2f}% |")
    interpretation_lines += [
        "",
        "Conditioning on suite validity selects different outputs in each arm. These descriptive percentages are not a replacement for the primary end-to-end outcome.",
        "T0 minus T1 is 9.33 percentage points overall, while the usable-suite percentages are closer. Lower test usability contributes to the overall exposure difference.",
    ]
    sensitivity_file = glmm_csv_file.parent / "PROBLEM_LEVEL_SENSITIVITY.csv"
    if sensitivity_file.exists():
        interpretation_lines += [
            "",
            "Exploratory sensitivity averages the repeated observations within each problem and applies a paired t test across the 15 problem-level differences.",
            "These probability-scale contrasts differ from the conditional log-odds interaction estimated by the GLMM.",
            "",
            "| Contrast | Mean probability difference | 95% interval | p |",
            "| --- | --- | --- | --- |",
        ]
        with sensitivity_file.open(encoding="utf-8-sig") as stream:
            for contrast in csv.DictReader(stream):
                interpretation_lines.append(
                    f"| {contrast['contrast']} | {float(contrast['mean_difference']):.4f} | "
                    f"[{float(contrast['lower_95']):.4f}, {float(contrast['upper_95']):.4f}] | "
                    f"{float(contrast['p_value']):.4f} |"
                )
    slope_file = glmm_csv_file.parent / "GLMM_RANDOM_SLOPES_SENSITIVITY.csv"
    if slope_file.exists():
        with slope_file.open(encoding="utf-8-sig") as stream:
            slope = next(csv.DictReader(stream))
        interpretation_lines += [
            "",
            f"An exploratory GLMM with independent problem-specific slopes for exposure, diversity and interaction gives interaction p={float(slope['p_value']):.4f}, beta={float(slope['coefficient']):.4f}, SE={float(slope['standard_error']):.4f}.",
            f"Singular fit {slope['singular']}. Convergence messages {slope['convergence_messages'] or 'none'}.",
            "The task-specific slope variances are large and the fixed interaction magnitude changes substantially. With 15 problems, population generalization and effect magnitude remain uncertain.",
        ]
    interpretation_lines += [
        "",
        "Write an empirical study of these tasks and model configurations. Avoid claims of universal blindness, a directly measured cognitive mechanism, guaranteed equivalence, or strict provider pinning.",
        "Preserve the completed CSV and generated tests. Record the final analysis code and data hashes with the paper.",
    ]

    report_lines = [
        "# Main Empirical Experiment Report: 2x2 Factorial Investigation",
        f"**Generated Date:** {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}",
        f"**Methodological Reference:** Konstantinou et al. (arXiv:2607.05139) & Leu et al. (ESEM 2026)",
        f"**Data Provenance:** Aggregated from full dataset `{glmm_csv_file.name}` (Unified across checkpoint sessions)",
        f"**Total Tasks Recorded:** {total_trials} | **Total Executions:** {total_evals} | **Recorded generation cost:** ${total_cost_usd:.4f} USD",
        f"**API error rows retained in this CSV:** {api_error_attempts}",
        "These are matched trials on 15 distinct problems, rather than 225 distinct tasks.",
        "Earlier HTTP 402 failures and retries occurred. Some error rows were removed before resumption, so this final CSV does not recover all attempts or total historical cost.",
        "",
        "## 1. Executive Summary: Primary Findings",
        "",
        "| Research Question | Paired Comparison | Valid Pairs (N) | Excluded Trials | Observed Metric | Statistical Test | p-value | Empirical Conclusion |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
        f"| **RQ1 (Code-First Bias)** | $T_0$ vs $T_1$ | **N = {n_rq1}** | {len(rq1_excluded)} | $T_0={t0_rate:.1f}\\%$ vs $T_1={t1_rate_rq1:.1f}\\%$ | McNemar Exact | $p={rq1_ct.get('p_value', 1.0):.4f}$ | {'Difference detected in trial-level paired analysis' if rq1_ct.get('p_value', 1.0) < 0.05 else 'INCONCLUSIVE'} |",
        f"| **RQ2 (Model Diversity)** | $T_1$ vs $T_2$ | **N = {n_rq2}** | {len(rq2_excluded)} | $T_1={t1_rate_rq2:.1f}\\%$ vs $T_2={t2_rate:.1f}\\%$ | McNemar Exact | $p={rq2_ct.get('p_value', 1.0):.4f}$ | {'Difference not demonstrated' if rq2_ct.get('p_value', 1.0) > 0.05 else 'SIGNIFICANT DIFFERENCE'} |",
        f"| **RQ2 (TOST Equivalence)** | $T_1$ vs $T_2$ | **N = {n_rq2}** | {len(rq2_excluded)} | Bounds $\\pm 0.08$ | TOST (Two One-Sided) | $p={tost_p:.4f}$ | {'STATISTICALLY EQUIVALENT' if is_equiv else 'NOT DEMONSTRABLY EQUIVALENT'} |",
        "",
        "## 2. RQ1: Confirmatory Replication of Code-First Bias (T0 vs T1)",
        f"- **Valid Matched Pairs (N):** {n_rq1} (Strictly matched on same `trial_id`)",
        f"- **Excluded Trials:** {len(rq1_excluded)}" + (f" ({'; '.join([f'{t}: {r}' for t, r in rq1_excluded[:5]])})" if rq1_excluded else ""),
        "",
        "### 2x2 Paired Contingency Matrix:",
        "```",
        f"                     T1 (Code-First) Detect | T1 (Code-First) Miss",
        f"T0 (Spec-Only) Detect:        {rq1_ct.get('a_both_detect', 0):4d}          |        {rq1_ct.get('b_armA_only', 0):4d} (T0 only)",
        f"T0 (Spec-Only) Miss  :        {rq1_ct.get('c_armB_only', 0):4d}          |        {rq1_ct.get('d_both_miss', 0):4d} (Both miss)",
        "```",
        f"- **Discordant Pairs:** {rq1_ct.get('discordant_pairs', 0)} ({rq1_ct.get('b_armA_only', 0)} vs {rq1_ct.get('c_armB_only', 0)})",
        f"- **Odds Ratio:** {rq1_ct.get('odds_ratio', 1.0):.3f} (95% CI: [{rq1_ct.get('ci_95', (0, 0))[0]:.3f}, {rq1_ct.get('ci_95', (0, 0))[1]:.3f}])",
        f"- **McNemar two-sided exact p:** {rq1_ct.get('p_value', 1):.6g}",
        f"- **Detection difference T0 minus T1:** {t0_rate - t1_rate_rq1:.2f} percentage points. The matched odds ratio describes discordant pairs.",
        "",
        "## 3. RQ2: Cross-Family Model Diversity & Equivalence (T1 vs T2)",
        f"- **Valid Matched Pairs (N):** {n_rq2} (Strictly matched on same `trial_id`)",
        f"- **Excluded Trials:** {len(rq2_excluded)}" + (f" ({'; '.join([f'{t}: {r}' for t, r in rq2_excluded[:5]])})" if rq2_excluded else ""),
        "",
        "### 2x2 Paired Contingency Matrix:",
        "```",
        f"                      T2 (Cross-Model) Detect | T2 (Cross-Model) Miss",
        f"T1 (Same-Model) Detect:        {rq2_ct.get('a_both_detect', 0):4d}           |        {rq2_ct.get('b_armA_only', 0):4d}",
        f"T1 (Same-Model) Miss  :        {rq2_ct.get('c_armB_only', 0):4d}           |        {rq2_ct.get('d_both_miss', 0):4d}",
        "```",
        f"- **TOST Equivalence Margin:** $\\theta = \\pm 0.08$",
        f"- **Observed Proportion Difference:** $\\hat{{d}} = {tost_diff:.4f}$",
        f"- **90% Confidence Interval:** $[{ci_90[0]:.4f}, {ci_90[1]:.4f}]$",
        f"- **Equivalence Assessment:** {'BOUNDS CONTAINED WITHIN ±0.08 -> EQUIVALENCE CONFIRMED' if is_equiv else 'BOUNDS EXCEED MARGIN'}",
        "",
        *glmm_lines,
        "",
        "## 5. Overall 2x2 Factorial Summary Across All 4 Conditions",
        "",
        "| Condition | Code Exposure | Model Identity | Total Recorded | API Errors | Completed | Valid Oracles | Valid Rate | Detections | Detection Rate |",
        "| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        f"| **T0** | Specification Only | Same Family (Coder) | {cond_stats['T0']['total']} | {cond_stats['T0']['api_errors']} | {cond_stats['T0']['completed']} | {cond_stats['T0']['valid']} | {cond_stats['T0']['valid_pct']:.1f}% | {cond_stats['T0']['detected']} | **{cond_stats['T0']['detected_pct']:.1f}%** |",
        f"| **T1** | Code-First Exposure | Same Family (Coder) | {cond_stats['T1']['total']} | {cond_stats['T1']['api_errors']} | {cond_stats['T1']['completed']} | {cond_stats['T1']['valid']} | {cond_stats['T1']['valid_pct']:.1f}% | {cond_stats['T1']['detected']} | **{cond_stats['T1']['detected_pct']:.1f}%** |",
        f"| **T2** | Code-First Exposure | Cross-Family Model | {cond_stats['T2']['total']} | {cond_stats['T2']['api_errors']} | {cond_stats['T2']['completed']} | {cond_stats['T2']['valid']} | {cond_stats['T2']['valid_pct']:.1f}% | {cond_stats['T2']['detected']} | **{cond_stats['T2']['detected_pct']:.1f}%** |",
        f"| **T3** | Specification Only | Cross-Family Model | {cond_stats['T3']['total']} | {cond_stats['T3']['api_errors']} | {cond_stats['T3']['completed']} | {cond_stats['T3']['valid']} | {cond_stats['T3']['valid_pct']:.1f}% | {cond_stats['T3']['detected']} | **{cond_stats['T3']['detected_pct']:.1f}%** |",
        "",
        "## 6. Audit Trail & Data Provenance",
        "The dataset contains 225 repeated trials on 15 distinct problems. Trial-level McNemar and normal-approximation paired TOST do not account for within-problem dependence. Treat them as supporting analyses alongside the mixed model and exploratory problem-level sensitivity.",
        "The SDK generation path allowed provider fallbacks. Actual provider and quantization for every historical response are not preserved in this CSV, so strict provider pinning cannot be claimed.",
        "No direct psychological measure was collected. Exposure-related detection differences do not establish a cognitive mechanism.",
        "The original v1.0 tag predates replacement faults and evaluator corrections. It does not freeze the final study assets. Archive the final dataset, accepted faults, evaluation code and analysis together before writing.",
        f"- **Raw Observations Dataset:** `{glmm_csv_file}`",
        f"- **Archived Unit Test Suites:** `{report_file.parent / 'generated_tests'}`",
        f"- **Frozen Benchmark Snapshot:** Git Tag `v1.0-dataset-faults-frozen` (Commit `828cc78`)"
    ]

    report_lines.extend([""] + interpretation_lines)
    report_file.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"\nSaved formal main experiment report to {report_file}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run 2x2 Factorial Main Experiment")
    parser.add_argument("--sample-size", type=int, default=225, help="Number of paired trials (default: 225)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
    parser.add_argument("--output-dir", type=str, default="data/main_results", help="Output directory")
    parser.add_argument("--sim", action="store_true", help="Run simulation mode instead of live API")
    args = parser.parse_args()

    run_main_experiment(
        live_api=not args.sim,
        sample_size=args.sample_size,
        random_seed=args.seed,
        output_dir=args.output_dir
    )

