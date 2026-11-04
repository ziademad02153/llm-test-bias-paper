# Disentangling Code Exposure from Model Diversity in Automated LLM Test Generation: A 2x2 Factorial Empirical Study

[![Replication Package](https://img.shields.io/badge/Replication-Package-blue.svg)](https://github.com/ziademad02153/llm-test-bias-paper)
[![R Statistical Analysis](https://img.shields.io/badge/Analysis-R%20%7C%20lme4-success.svg)](scripts/fit_interaction_glmm.R)
[![Data Sources: MIT / GPL-3.0](https://img.shields.io/badge/Data%20Sources-MIT%20%2F%20GPL--3.0-brightgreen.svg)](data/licenses/)

**Author:** Ziad Emad Allam  
*Independent Researcher, Benha, Egypt*  
*Email:* ziademadbts@gmail.com  
*Target Journal:* Information and Software Technology (Elsevier)

---

## Abstract

Automated unit test generation using Large Language Models (LLMs) is increasingly adopted in continuous integration pipelines. However, exposing reference implementation code to the test-generating model risks producing tests that confirm rather than challenge existing bugs. To rigorously isolate this phenomenon, we conducted a preregistered $2 \times 2$ factorial experiment ($N = 225$ matched quadruplets, 900 test generation evaluations) crossing **Code Exposure** (Specification Only vs. Implementation-Aware) with **Model Diversity** (Same Model vs. Distinct Model) across 15 verified, natural software logic defects. 

Evaluating the synthesized test suites on unmutated, human-authored bug-fix commits, we analyze defect detection with exact McNemar tests, Two One-Sided Tests (TOST) for equivalence, and a Generalized Linear Mixed-Effects Model (GLMM) with logit link controlling for task- and coder-level clustering. Implementation exposure significantly degraded defect detection (33.78% vs. 24.44%, $\Delta = -9.33$ pp, exact McNemar $p = 0.0046$, odds ratio $\text{OR} = 2.400$). Employing a distinct model without code exposure yielded no significant advantage over the same model under implementation exposure (24.44% vs. 18.22%, exact McNemar $p = 0.0649$), and statistical equivalence was firmly rejected ($p_{\text{TOST}} = 0.2841$). The GLMM revealed a statistically significant negative interaction between code exposure and model diversity ($\beta = -1.0358, SE = 0.3887, z = -2.665, p = 0.0077$, odds ratio $\text{OR} = 0.355$, 95% CI $[0.166, 0.760]$), confirmed by a likelihood ratio test ($\chi^2 = 7.213, p = 0.0072$). 

Operational deconstruction indicates that this degradation is substantially driven by a concurrent drop in test oracle validity and execution yield on the reference code (usable test suites drop from 86.2% to 64.9%), demonstrating that test execution breakdown contributes directly to the observed deficit without requiring an unverified psychological confirmation bias mechanism.

---

## Data Availability & Reproduction

### Reproduction of Statistical Findings (Zero Setup / Zero Secrets)
The complete set of all 900 empirical observation outcomes across 225 matched trials on 15 tasks is openly provided in `data/main_experiment_results/main_glmm_dataset.csv`.

To reproduce the exact GLMM model, odds ratios, diagnostics, and p-values reported in the paper:

```bash
# Requires R and lme4
Rscript scripts/fit_interaction_glmm.R data/main_experiment_results/main_glmm_dataset.csv
```

This statistical analysis:
- Requires **no API keys** or network access.
- Executes in under 5 seconds.
- Exactly reproduces the GLMM coefficients, standard errors, $z$-values, likelihood ratio test, and random effects.

### Data Partitioning and Licensing Policy
The supplementary public package (`supplementary_material_public.zip`) contains:
- All 900 recorded condition outcomes across 225 matched trials on 15 tasks.
- The R reproduction script (`scripts/fit_interaction_glmm.R`) and GLMM output logs.
- Source implementations, task specifications, and 540 generated test suites for the 9 tasks with documented open-source licenses (8 MIT, 1 GPL-3.0).
- Upstream metadata pointers (`data/task_source_metadata.json`) recording the repository URL, author, and commit hash for all 15 tasks.

Source-bearing artifacts and test suites for six tasks (`REAL_TASK_004`, `006`, `010`, `011`, `019`, and `020`) originating from public repositories without explicit license files are withheld from the public redistribution package pending formal licensing permission. Consequently, the public package supports complete statistical reanalysis of the entire study, while test execution re-evaluation is directly available for the 9 licensed tasks.

---

## Benchmark Composition & Provenance

| Task ID | Function Name | Upstream Repository | License Status |
| :--- | :--- | :--- | :--- |
| `REAL_TASK_001` | `parse_github_url` | TryMightyAI/mighty-security | MIT License |
| `REAL_TASK_002` | `split_by_positions` | mpryor/nothing-less | MIT License |
| `REAL_TASK_004` | `validate_tags` | Danau5tin/tbench-agentic-data-pipeline | Public (Source withheld) |
| `REAL_TASK_005` | `split_host_port` | ShatakVPN/ConfigForge-V2Ray | GPL-3.0 |
| `REAL_TASK_006` | `get_consistent_hash_node` | alphaparkinc/genpark-consistent-hash-ring-vnodes-skill | Public (Source withheld) |
| `REAL_TASK_010` | `find_conflicting_reservations` | bhavatharaniselvaraj/EV-charging-Allocation-System_Python | Public (Source withheld) |
| `REAL_TASK_011` | `check_half_open_overlap` | bhavatharaniselvaraj/EV-charging-Allocation-System_Python | Public (Source withheld) |
| `REAL_TASK_013` | `intersect_intervals` | ashenfad/calgebra | MIT License |
| `REAL_TASK_014` | `compute_exponential_backoff_sequence` | Llucs/backon | MIT License |
| `REAL_TASK_015` | `compute_fibonacci_backoff_sequence` | Llucs/backon | MIT License |
| `REAL_TASK_016` | `evaluate_token_bucket` | vladlen-codes/ratelink | MIT License |
| `REAL_TASK_017` | `check_sliding_window_rate_limit` | vladlen-codes/ratelink | MIT License |
| `REAL_TASK_018` | `evaluate_circuit_breaker_transition` | Llucs/backon | MIT License |
| `REAL_TASK_019` | `merge_overlapping_intervals` | bhavatharaniselvaraj/EV-charging-Allocation-System_Python | Public (Source withheld) |
| `REAL_TASK_020` | `detect_dag_cycle_and_ancestors` | Alpha-Park/genpark-dag-topological-sort-dependency-resolver-skill | Public (Source withheld) |

See `data/licenses/COPYRIGHT_NOTICES.txt` for detailed attribution and licensing notices.

---

## Directory Structure

```text
├── paper.tex                      # Manuscript LaTeX source (Elsevier-ready)
├── paper.pdf                      # Compiled manuscript (11 pages)
├── references.bib                 # BibTeX bibliography
├── cover_letter.txt               # Journal cover letter to IST Editor-in-Chief
├── supplementary_material_public.zip # Public supplementary archive
├── scripts/
│   ├── fit_interaction_glmm.R     # R GLMM model fitting script
│   └── build_public_package.py    # Public package packaging and verification tool
├── data/
│   ├── main_experiment_results/   # 900 empirical observations & GLMM outputs
│   │   ├── main_glmm_dataset.csv
│   │   ├── GLMM_OUTPUT.txt
│   │   └── GLMM_COEFFICIENTS.csv
│   └── licenses/                  # Open-source license texts and notices
└── scratch/
    └── PERMISSION_REQUEST_TEMPLATES.md # Author permission inquiry drafts
```

---

## Citation

```bibtex
@article{allam2026disentangling,
  title={Disentangling Code Exposure from Model Diversity in Automated LLM Test Generation: A $2 \times 2$ Factorial Empirical Study},
  author={Allam, Ziad Emad},
  journal={Information and Software Technology},
  year={2026},
  note={Under Review}
}
```

