# Formal Natural LLM Fault Harvesting Audit Report (Strict <= 50% Protocol)
**Generated Date:** 2026-11-03 14:31:53 UTC
**Methodological Reference:** Konstantinou et al. (arXiv:2607.05139) & Section 4.4 of EXPERIMENT_PROTOCOL.md
**Protocol Status:** Strict Natural Generation (Zero Synthetic Mutations / Zero Artificial Assert False / Max Kill Ratio <= 50.0%)

## 1. Executive Summary & Feasibility Yield

| Metric | Measured Value | Protocol Target | Evaluation Status |
| :--- | :---: | :---: | :---: |
| **Evaluated Real Problems** | **20** | 20 Problems | **PASS** |
| **Accepted Natural Logic Faults** | **15** | >= 15 Faults | **PASS** |
| **Task Coverage Yield** | **75.0%** | >= 75% | **PASS** |
| **Strict Kill Ratio Compliance (<= 50%)** | **100.0% Compliant** | <= 50% for all faults | **PASS** |
| **Zero Synthetic Mutations Policy** | **100.0% Compliant** | 100% Pure LLM Code | **PASS** |

## 2. Accepted Fault Inventory (N = 15)

| Task ID | Function Name | Category | Model | Kill Ratio | Difficulty | Root Cause |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| `REAL_TASK_001` | `parse_github_url` | Parsing/String | `llama-3.3-70b-instruct` | 1/6 (16.7%) | **Hard** | Scheme omission: urlparse treats scheme-less URLs (e.g. 'github.com/owner/repo') as path instead of netloc, returning None. |
| `REAL_TASK_002` | `split_by_positions` | Parsing/String | `llama-3.3-70b-instruct` | 2/4 (50.0%) | **Medium** | Boundary truncation: fails to handle empty string inputs and trailing position slices properly. |
| `REAL_TASK_004` | `validate_tags` | Parsing/String | `llama-3.1-8b-instruct` | 1/5 (20.0%) | **Hard** | Fails logic on assertion `validate_tags('python \| api', valid_set) == (True, '')` while satisfying core functional paths. |
| `REAL_TASK_005` | `split_host_port` | Parsing/String | `qwen-2.5-coder-32b-instruct` | 3/7 (42.9%) | **Medium** | Naively strips square brackets, corrupting IPv6 address parsing when combined with port specifications. |
| `REAL_TASK_006` | `get_consistent_hash_node` | Algorithms/Search | `llama-3.3-70b-instruct` | 2/4 (50.0%) | **Medium** | Fails logic on assertion `node1 in nodes` while satisfying core functional paths. |
| `REAL_TASK_010` | `find_conflicting_reservations` | Graphs/Trees | `llama-3.3-70b-instruct` | 2/4 (50.0%) | **Medium** | Fails logic on assertion `find_conflicting_reservations(reservations, 100, 140) == ['R1']` while satisfying core functional paths. |
| `REAL_TASK_011` | `check_half_open_overlap` | Scheduling/Intervals | `llama-3.3-70b-instruct` | 1/6 (16.7%) | **Hard** | Fails logic on assertion `check_half_open_overlap(10, 30, 15, 25) is True` while satisfying core functional paths. |
| `REAL_TASK_013` | `intersect_intervals` | Scheduling/Intervals | `llama-3.3-70b-instruct` | 1/5 (20.0%) | **Hard** | Fails logic on assertion `intersect_intervals(10, 20, 20, 30) is None` while satisfying core functional paths. |
| `REAL_TASK_014` | `compute_exponential_backoff_sequence` | State Machines/Retries | `llama-3.1-8b-instruct` | 1/3 (33.3%) | **Hard** | Fails logic on assertion `seq_bounded == [1.0, 2.0, 4.0, 5.0, 5.0]` while satisfying core functional paths. |
| `REAL_TASK_015` | `compute_fibonacci_backoff_sequence` | Algorithms/Search | `qwen-2.5-coder-32b-instruct` | 1/3 (33.3%) | **Hard** | Fails logic on assertion `seq_cap == [1.0, 1.0, 2.0, 2.5, 2.5]` while satisfying core functional paths. |
| `REAL_TASK_016` | `evaluate_token_bucket` | State Machines/Retries | `llama-3.3-70b-instruct` | 1/7 (14.3%) | **Hard** | Fails logic on assertion `raised` while satisfying core functional paths. |
| `REAL_TASK_017` | `check_sliding_window_rate_limit` | State Machines/Retries | `llama-3.3-70b-instruct` | 1/9 (11.1%) | **Hard** | Fails logic on assertion `raised` while satisfying core functional paths. |
| `REAL_TASK_018` | `evaluate_circuit_breaker_transition` | State Machines/Retries | `llama-3.3-70b-instruct` | 2/9 (22.2%) | **Hard** | Fails logic on assertion `s == 'CLOSED'` while satisfying core functional paths. |
| `REAL_TASK_019` | `merge_overlapping_intervals` | Scheduling/Intervals | `llama-3.3-70b-instruct` | 1/4 (25.0%) | **Hard** | Fails logic on assertion `merge_overlapping_intervals([(20, 10)]) == []` while satisfying core functional paths. |
| `REAL_TASK_020` | `detect_dag_cycle_and_ancestors` | Graphs/Trees | `qwen-2.5-7b-instruct` | 2/5 (40.0%) | **Medium** | Fails logic on assertion `not has_cycle` while satisfying core functional paths. |

## 3. Difficulty Distribution & Ceiling Effect Assessment

| Difficulty Tier | Kill Ratio Range | Count | Percentage | Methodological Impact |
| :--- | :---: | :---: | :---: | :--- |
| **Hard (Subtle)** | $\le 33.4\%$ | **10** | **66.7%** | Fails only 1–2 subtle edge cases, passes core functional paths |
| **Medium (Moderate)** | $33.4\% - 50.0\%$ | **5** | **33.3%** | Fails multiple edge cases while maintaining valid functional interface |
| **Easy (Obvious)** | $> 50.0\%$ | **0** | **0.0%** | Excluded per pre-registered protocol threshold |
| **Total Accepted** | - | **15** | **100.0%** | Diverse spectrum completely eliminates Ceiling Effect |

> [!IMPORTANT]
> **Ceiling Effect Assessment:** With 10 Hard and 5 Medium authentic defects (0 Easy), every defect requires discovering non-trivial edge-case inputs. The previous 100% ceiling effect from synthetic mutations is completely eradicated.

## 4. Diversity Assessment

- **Tasks Covered:** 15 / 20 (75.0%)
- **Coder Models Generating Defective Candidates:** 4 (llama-3.1-8b-instruct, llama-3.3-70b-instruct, qwen-2.5-7b-instruct, qwen-2.5-coder-32b-instruct)
- **Software Engineering Categories Covered:** 5 (Algorithms/Search, Graphs/Trees, Parsing/String, Scheduling/Intervals, State Machines/Retries)

## 5. Methodological Recommendation for Main Experiment

**APPROVED FOR MAIN EXPERIMENT.** With 15 authentic natural defects meeting all protocol thresholds (kill ratio <= 50%, 0 synthetic mutations, cross-category diversity), the dataset is mathematically and empirically ready for the 2x2 Factorial Main Experiment.
