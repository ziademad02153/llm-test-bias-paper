# Benchmark Task Provenance, Licensing, and Attribution Manifest

This document provides the full provenance, source repository, commit hash, commit date, author, category, and license attribution for the 15 benchmark tasks evaluated in the paper:
**"Disentangling Code Exposure from Model Diversity in Automated LLM Test Generation: A 2x2 Factorial Empirical Study"**
Author: **Ziad Emad Allam** (*Independent Researcher, Benha, Egypt*)

---

## 1. Complete Task Provenance Table

| Task ID | Function Name | Category | Source Repository | Commit Hash | Commit Date | Author | License / Legal Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `REAL_TASK_001` | `parse_github_url` | Parsing/String | [TryMightyAI/mighty-security](https://github.com/TryMightyAI/mighty-security) | `197847a934` | 2025-08-19 | Johnny Hung | **MIT License** |
| `REAL_TASK_002` | `split_by_positions` | Parsing/String | [mpryor/nothing-less](https://github.com/mpryor/nothing-less) | `cc15dd737b` | 2026-05-08 | mpryor | **MIT License** |
| `REAL_TASK_004` | `validate_tags` | Parsing/String | [Danau5tin/tbench-agentic-data-pipeline](https://github.com/Danau5tin/tbench-agentic-data-pipeline) | `4489453eb3` | 2025-07-28 | Dan Austin | *Unlicensed Public Repo (Fair Use)* |
| `REAL_TASK_005` | `split_host_port` | Parsing/String | [ShatakVPN/ConfigForge-V2Ray](https://github.com/ShatakVPN/ConfigForge-V2Ray) | `4e20866a32` | 2026-11-01 | ShatakVPN | **GNU GPL-3.0 License** |
| `REAL_TASK_006` | `get_consistent_hash_node` | Algorithms/Search | [alphaparkinc/genpark-consistent-hash-ring-vnodes-skill](https://github.com/alphaparkinc/genpark-consistent-hash-ring-vnodes-skill) | `7dd66023eb` | 2026-09-10 | GenPark | *Unlicensed Public Repo (Fair Use)* |
| `REAL_TASK_010` | `find_conflicting_reservations` | Graphs/Trees | [bhavatharaniselvaraj/EV-charging-Allocation-System_Python](https://github.com/bhavatharaniselvaraj/EV-charging-Allocation-System_Python) | `efd356a973` | 2026-10-21 | Bhavatharani Selvaraj | *Unlicensed Public Repo (Fair Use)* |
| `REAL_TASK_011` | `check_half_open_overlap` | Scheduling/Intervals | [bhavatharaniselvaraj/EV-charging-Allocation-System_Python](https://github.com/bhavatharaniselvaraj/EV-charging-Allocation-System_Python) | `efd356a973` | 2026-10-21 | Bhavatharani Selvaraj | *Unlicensed Public Repo (Fair Use)* |
| `REAL_TASK_013` | `intersect_intervals` | Scheduling/Intervals | [ashenfad/calgebra](https://github.com/ashenfad/calgebra) | `476c3e65da` | 2026-03-20 | Adam Ashenfelter | **MIT License** |
| `REAL_TASK_014` | `compute_exponential_backoff_sequence` | State Machines/Retries | [Llucs/backon](https://github.com/Llucs/backon) | `9b685085d5` | 2026-10-31 | Llucs | **MIT License** |
| `REAL_TASK_015` | `compute_fibonacci_backoff_sequence` | Algorithms/Search | [Llucs/backon](https://github.com/Llucs/backon) | `9b685085d5` | 2026-10-31 | Llucs | **MIT License** |
| `REAL_TASK_016` | `evaluate_token_bucket` | State Machines/Retries | [vladlen-codes/ratelink](https://github.com/vladlen-codes/ratelink) | `eb17878fa3` | 2026-03-13 | Vladlen | **MIT License** |
| `REAL_TASK_017` | `check_sliding_window_rate_limit` | State Machines/Retries | [vladlen-codes/ratelink](https://github.com/vladlen-codes/ratelink) | `eb17878fa3` | 2026-03-13 | Vladlen | **MIT License** |
| `REAL_TASK_018` | `evaluate_circuit_breaker_transition` | State Machines/Retries | [Llucs/backon](https://github.com/Llucs/backon) | `9b685085d5` | 2026-10-31 | Llucs | **MIT License** |
| `REAL_TASK_019` | `merge_overlapping_intervals` | Scheduling/Intervals | [bhavatharaniselvaraj/EV-charging-Allocation-System_Python](https://github.com/bhavatharaniselvaraj/EV-charging-Allocation-System_Python) | `efd356a973` | 2026-10-21 | Bhavatharani Selvaraj | *Unlicensed Public Repo (Fair Use)* |
| `REAL_TASK_020` | `detect_dag_cycle_and_ancestors` | Graphs/Trees | [Alpha-Park/genpark-dag-topological-sort-dependency-resolver-skill](https://github.com/Alpha-Park/genpark-dag-topological-sort-dependency-resolver-skill) | `1c28477ff9` | 2026-09-29 | GenPark | *Unlicensed Public Repo (Fair Use)* |

---

## 2. Licensing Compliance & Legal Analysis

### A. Permissive Open-Source (MIT License)
Eight tasks (`REAL_TASK_001`, `002`, `013`, `014`, `015`, `016`, `017`, `018`) originate from explicitly MIT-licensed software repositories (`nothing-less`, `backon`, `mighty-security`, `calgebra`, `ratelink`). Full copyright notices and the MIT License text are preserved in `data/licenses/LICENSE-MIT.txt` and `data/licenses/COPYRIGHT_NOTICES.txt`.

### B. Copyleft Licensing (GNU General Public License v3.0)
Task `REAL_TASK_005` originates from `ShatakVPN/ConfigForge-V2Ray`, licensed under GNU GPL v3.0.
* **GPL-3.0 Compliance:** In accordance with Section 5 of the GPL-3.0, the isolated helper function `split_host_port` was extracted from the upstream repository, preserving signature and parsing logic for test generation benchmarks.
* The complete text of the GNU General Public License v3.0 is provided in `data/licenses/LICENSE-GPL3.txt`.
* Any test suites and artifacts derived from this task are made available under GPL-3.0.

### C. Unlicensed Public Repositories (Transformative Fair Use in Scientific Research)
Six tasks (`REAL_TASK_004`, `006`, `010`, `011`, `019`, `020`) originate from public GitHub repositories that do not provide an explicit root license file.
* **GitHub Terms of Service (ToS):** Under Section D.4 of GitHub's Terms of Service, public repositories grant other GitHub users the right to view and fork the content.
* **Copyright & Non-Copyrightable Ideas (17 U.S.C. § 102(b)):** Standard computer science algorithmic concepts (such as Kahn's topological sort, MD5 hash ring bisecting, and half-open interval overlap checks) are non-copyrightable functional principles and algorithms.
* **Fair Use Doctrine (17 U.S.C. § 107):** The inclusion of isolated, concise functional code snippets (< 25 lines) and natural-language docstrings in an academic benchmark constitutes transformative **Fair Use** exclusively for non-profit scientific research, peer review, and empirical reproducibility. The benchmark does not serve as a commercial substitute for the original projects.
* **Author Contact Channel:** Original repository authors may contact the corresponding author (`ziademadbts@gmail.com`) to request attribution updates, explicit licensing clarifications, or exclusion from future releases.
