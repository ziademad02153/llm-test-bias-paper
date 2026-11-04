# SUBMISSION AUDIT REPORT
**Manuscript:** *Disentangling Code Exposure from Model Diversity in Automated LLM Test Generation: A $2 \times 2$ Factorial Empirical Study*  
**Target Journal:** *Information and Software Technology* (IST), Elsevier  
**Author:** Ziad Emad Allam (`ziademadbts@gmail.com`), Independent Researcher, Benha, Egypt  
**Audit Timestamp:** 2026-11-04 15:45:00 UTC+02:00  
**Audit Status:** AUDITED WITH EMPIRICAL VERIFICATION (NO MARKETING CLAIMS)

---

## 1. Executive Summary & Audit Verdict

### Why the Reviewer's Skepticism Was 100% Justified
The advisory reviewer was completely right to reject claims of "100% Ready" without independent, cold verification. Prior turns in this workflow exhibited real discrepancies that required remediation:
1. An earlier archive omitted the 900 test suites because of an incomplete file glob.
2. Initial provenance reviews labeled all tasks as MIT/Apache-2.0, whereas detailed repo audits revealed 6 tasks had no root license file.
3. A subsequent draft attempted to dismiss the missing licenses with an informal "Academic Fair Use" assertion, which is an affirmative legal defense rather than an open-source redistribution license.
4. In the most recent edit, replacing the Data Availability statement inadvertently dropped the explicit GitHub URL from `paper.tex` and `cover_letter.txt`.

**Remediation has now been executed and empirically tested.** This report documents the exact state of every file, byte size, cryptographic hash, and editorial requirement.

---

## 2. Actual Submission Files for Elsevier Editorial Manager

When submitting to Elsevier's Editorial Manager for *Information and Software Technology* (`submit.elsevier.com/INFSOF`), the following files constitute the submission payload:

| File Role on Editorial Manager | File Name | Format | Purpose |
| :--- | :--- | :--- | :--- |
| **Manuscript (Compiled PDF)** | `paper.pdf` | PDF | Primary review document containing full text, 3 tables, 1 figure, equations, and references. |
| **LaTeX Source Files** | `paper.tex` | TeX | Typesetting source required by Elsevier for post-acceptance production. |
| **Bibliography Source** | `references.bib` | BibTeX | BibTeX citations matching all 11 references cited in `paper.tex`. |
| **Cover Letter** | `cover_letter.txt` | Plain Text | Formal submission letter addressed to IST Editor-in-Chief. |
| **Highlights** | `highlights.txt` | Plain Text | 5 mandatory core finding bullet points (each $\le 85$ characters). |
| **Supplementary Material** | `supplementary_material_public.zip` | ZIP | Public replication package containing 900 rows of data, R scripts, 9 licensed tasks, and 540 tests. |

---

## 3. File Locations, Byte Sizes, and SHA-256 Checksums

All files reside in the working directory `E:\paper2`. The following table lists their exact sizes and cryptographic hashes:

| File Path | Byte Size | SHA-256 Checksum |
| :--- | :---: | :--- |
| `paper.pdf` | 252,613 | `a28558a326e4e764494a76a84fb94916d0a02e08a2ee93c725a763a1edc0c97a` |
| `paper.tex` | 35,330 | `0970e4c7d08d3dbb6bd903cca8551e5457fe40f6a9ab804cc0fb5ad5c19cfa11` |
| `references.bib` | 4,051 | `ecd62a384f08a3d7eecfc835e0b543ae54de71ccdd5a2e6a5c2aa14672139e76` |
| `cover_letter.txt` | 4,123 | `d42efb20ccbad6acd5b3a54c2f10cbdfbe1b660c747c2a4e5ac89b34bd88446e` |
| `highlights.txt` | 408 | `1336594599f64b93ca9e7b83c359a6af2e6c847516141261c426cc93a51ba801` |
| `supplementary_material_public.zip` | 391,118 | `a88c6124d09f0e5b0646658dd9ad05902e4aaf6086ce11363db44a4e07f04858` |
| `supplementary_material.zip` | 391,118 | `a88c6124d09f0e5b0646658dd9ad05902e4aaf6086ce11363db44a4e07f04858` |
| `README.md` | 7,619 | `809e52ae1ab3af139353b969fc94994ee9e52c91e8341dc8953161e9ff7855c4` |
| `PUBLIC_DATA_AVAILABILITY.txt` | 775 | `327cd273dd2b14c9e86db0267243b8c052f4c426df4035d0ef831a002e53c781` |
| `data/main_experiment_results/main_glmm_dataset.csv` | 194,141 | `fb868b71e713aceb0f6fb0d641d79162014f0b5c7ae58497671698838907e699` |
| `scripts/fit_interaction_glmm.R` | 6,508 | `255c686723cbb362197f311d84d7fa66b2a2fb44d7c267fff1cb1aa6af6ebc03` |
| `scripts/build_public_package.py` | 6,774 | `42c9e693a5b4ff79f648f7e0b96d5795b0a651041e915b907380a78a3932339f` |
| `data/licenses/COPYRIGHT_NOTICES.txt` | 6,761 | `1b9f8a29dd01902e0f463ace464cfa3612f188ac5a9bd58138e3811c6db0bae3` |
| `data/licenses/LICENSE-MIT.txt` | 1,037 | `92798b9082a3ffab53ad3495460f53abcf0ac30e1408f2edd88d5119726ff6c4` |
| `data/licenses/LICENSE-GPL3.txt` | 35,823 | `230184f60bae2feaf244f10a8bac053c8ff33a183bcc365b4d8b876d2b7f4809` |

> [!NOTE]
> `supplementary_material.zip` has been updated to be identical to `supplementary_material_public.zip` (both 391,118 bytes, identical SHA-256 hash). This guarantees that anyone downloading the archive under either name accesses the compliant public partition.

---

## 4. GitHub Links & Verification Status

| URL | Target Document | HTTP Status | Git Remote Commit |
| :--- | :--- | :---: | :---: |
| `https://github.com/ziademad02153/llm-test-bias-paper` | `paper.tex` (Line 385), `cover_letter.txt` (Line 28), `README.md` | **HTTP 200 OK** | `6cad93b` (HEAD on `origin/main`) |

- **Verification Method:** Verified live over network via `curl -I -L -k` and `git ls-remote`.
- **Text in Manuscript (`paper.tex`):**
  > *"The supplementary public package is openly available at \url{https://github.com/ziademad02153/llm-test-bias-paper}. It contains all 900 recorded condition outcomes across 225 matched trials on 15 tasks and the R scripts and outputs needed to reproduce the statistical analyses..."*

---

## 5. Licensing Breakdown of All 15 Benchmark Tasks

| Task ID | Function Target | Lines | Upstream Repository & Author | License Status | Included in Public Zip? |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `REAL_TASK_001` | `parse_github_url` | 23 | TryMightyAI/mighty-security (Johnny Hung) | **MIT** | **Yes** (Code + 60 tests) |
| `REAL_TASK_002` | `split_by_positions` | 21 | mpryor/nothing-less (mpryor) | **MIT** | **Yes** (Code + 60 tests) |
| `REAL_TASK_004` | `validate_tags` | 15 | Danau5tin/tbench-agentic-data-pipeline (Dan Austin) | *Public / Unlicensed* | **No** (Withheld) |
| `REAL_TASK_005` | `split_host_port` | 19 | ShatakVPN/ConfigForge-V2Ray (ShatakVPN) | **GPL-3.0** | **Yes** (Code + 60 tests) |
| `REAL_TASK_006` | `get_consistent_hash_node` | 24 | alphaparkinc/genpark-consistent-hash-ring-vnodes-skill (GenPark) | *Public / Unlicensed* | **No** (Withheld) |
| `REAL_TASK_010` | `find_conflicting_reservations` | 18 | bhavatharaniselvaraj/EV-charging-Allocation-System_Python (Bhavatharani Selvaraj) | *Public / Unlicensed* | **No** (Withheld) |
| `REAL_TASK_011` | `check_half_open_overlap` | 12 | bhavatharaniselvaraj/EV-charging-Allocation-System_Python (Bhavatharani Selvaraj) | *Public / Unlicensed* | **No** (Withheld) |
| `REAL_TASK_013` | `intersect_intervals` | 14 | ashenfad/calgebra (Adam Ashenfelter) | **MIT** | **Yes** (Code + 60 tests) |
| `REAL_TASK_014` | `compute_exponential_backoff_sequence` | 22 | Llucs/backon (Llucs) | **MIT** | **Yes** (Code + 60 tests) |
| `REAL_TASK_015` | `compute_fibonacci_backoff_sequence` | 20 | Llucs/backon (Llucs) | **MIT** | **Yes** (Code + 60 tests) |
| `REAL_TASK_016` | `evaluate_token_bucket` | 23 | vladlen-codes/ratelink (Vladlen) | **MIT** | **Yes** (Code + 60 tests) |
| `REAL_TASK_017` | `check_sliding_window_rate_limit` | 21 | vladlen-codes/ratelink (Vladlen) | **MIT** | **Yes** (Code + 60 tests) |
| `REAL_TASK_018` | `evaluate_circuit_breaker_transition` | 24 | Llucs/backon (Llucs) | **MIT** | **Yes** (Code + 60 tests) |
| `REAL_TASK_019` | `merge_overlapping_intervals` | 16 | bhavatharaniselvaraj/EV-charging-Allocation-System_Python (Bhavatharani Selvaraj) | *Public / Unlicensed* | **No** (Withheld) |
| `REAL_TASK_020` | `detect_dag_cycle_and_ancestors` | 25 | Alpha-Park/genpark-dag-topological-sort-dependency-resolver-skill (GenPark) | *Public / Unlicensed* | **No** (Withheld) |

---

## 6. The 6 Withheld Tasks: Status and Data Partitioning

### What Is Withheld From Public Package
- Raw function implementations (`data/problems/REAL_TASK_004, 006, 010, 011, 019, 020.json`).
- Synthesized test suites generated for these 6 tasks ($6 \times 60 = 360$ test suite files).

### What Remains Included in Public Package
- **All 360 numerical observation rows** in `main_glmm_dataset.csv`.
- Problem identifiers, condition assignments ($T_0, T_1, T_2, T_3$), detection outcomes ($0/1$), execution timing, and coder classifications.
- Full provenance metadata in `data/task_source_metadata.json`:
  - Upstream GitHub repository URLs.
  - Specific commit hashes used for extraction.
  - Original author attribution.

### Impact on Reproducibility
1. **Statistical Re-Analysis (100% Intact):** Anyone can run `Rscript scripts/fit_interaction_glmm.R` on `main_glmm_dataset.csv` and reproduce the complete GLMM model, odds ratios, diagnostics, and p-values for all 900 observations without requiring any source files or API keys.
2. **Test Suite Re-Execution (Partial by Design):** Full test-suite execution is reproducible for the 9 licensed tasks (540 test suites, 60% of benchmark). For the remaining 6 tasks, re-generation requires pulling code from the cited upstream commits.

---

## 7. Known Threats to Validity & Limitations

1. **Task Scope & Complexity:** The benchmark consists of 15 algorithmic Python functions ($\le 25$ lines each) extracted from public software repositories. Findings may not generalize directly to large-scale multi-file object-oriented architectures, compiled languages (C++/Java), or asynchronous systems.
2. **Coder Model Sampling:** The 3 coder models (`Llama-3.3-70B`, `Qwen-2.5-Coder-32B`, `Qwen-2.5-7B`) represent modern open-weight architectures. Closed-source models (such as GPT-4o or Claude 3.5 Sonnet) were not used as code authors, though Claude 3.7 Sonnet was used as a test author in the cross-model condition.
3. **Third-Party Permissions Pending:** Written permission request drafts have been prepared in `scratch/PERMISSION_REQUEST_TEMPLATES.md` for Dan Austin, Bhavatharani Selvaraj, and Alpha-Park/GenPark, but have not yet been submitted or granted.
4. **LLM Generation Sampling:** Tests were synthesized with temperature $T=0.2$, seed $S=42$, and max tokens 800. Stochastic variations could occur under alternative decoding configurations.

---

## 8. Item-by-Item Checklist: Elsevier IST Author Guidelines

| Guideline Item | Elsevier Requirement | Current Manuscript Status | Audit Result |
| :--- | :--- | :--- | :---: |
| **Peer Review Type** | Single-anonymized (Authors known to reviewers) | Author name (Ziad Emad Allam), affiliation (Independent Researcher, Benha, Egypt), and email (`ziademadbts@gmail.com`) included on title page. | **PASS** |
| **Abstract Structure** | Structured under 5 headings: Context, Objectives, Methods, Results, Conclusion | Present in `paper.tex` with all 5 bold headings. | **PASS** |
| **Abstract Word Count** | Maximum 300 words | Exactly **254 words**. | **PASS** |
| **Keywords** | 1 to 7 keywords | Exactly **7 keywords**: *LLM Test Generation, Code-First Bias, Model Diversity, Empirical Software Engineering, Generalized Linear Mixed Models (GLMM), Oracle Problem, Information and Software Technology*. | **PASS** |
| **Highlights** | 3 to 5 bullet points, max 85 characters each (including spaces) | 5 points in `highlights.txt`, lengths: 77, 79, 79, 76, 77 characters. All $\le 85$. | **PASS** |
| **Manuscript Length** | Under 15,000 words for standard research paper | Manuscript spans **11 pages** (~6,200 words including tables and references). | **PASS** |
| **Declaration of Competing Interest** | Explicit statement required | Included in `paper.tex` (Line 381) and `cover_letter.txt`. | **PASS** |
| **Data Availability Statement** | Required under Elsevier Option C | Included in `paper.tex` (Line 384) with active URL to GitHub repository. | **PASS** |
| **Generative AI Declaration** | Required when LLMs assist drafting | Included in `paper.tex` (Line 387), specifically disclosing Claude 3.7 Sonnet and Antigravity assistant. | **PASS** |
| **Funding Disclosure** | Mandatory funding statement | Included in `paper.tex` (Line 390): *"This research did not receive any specific grant..."* | **PASS** |
| **Sole Authorship** | Author list must reflect real contributors | Sole author: Ziad Emad Allam. No fictional committees or unverified co-authors. | **PASS** |

---

## 9. Verification Matrix: What Was Verified vs. What Was Not

### Empirically Verified (Tested & Confirmed)
- [x] **GLMM Execution:** `fit_interaction_glmm.R` ran inside isolated Docker container (`paper2-glmm:local`) using extracted `supplementary_material_public.zip`. Successfully converged without warnings and reproduced:
  - $\beta_{\text{exposure}} = -0.7402, p = 0.0059$
  - $\beta_{\text{diversity}} = +0.4506, p = 0.0772$
  - $\beta_{\text{interaction}} = -1.0358, p = 0.0077, \text{OR} = 0.355$
- [x] **LaTeX Compilation:** `paper.pdf` recompiled cleanly in TeX Live Docker container (`paper2-latex:latest`). 0 errors, 0 overfull hboxes, exactly 11 pages.
- [x] **Package Contents:** `supplementary_material_public.zip` tested via Python archive verification. Exactly 566 files: 900 data rows, 540 licensed tests, 0 withheld tests, 0 credentials.
- [x] **GitHub Remote Sync:** Repository URL `https://github.com/ziademad02153/llm-test-bias-paper` verified active (HTTP 200) and synced with remote commit `6cad93b`.
- [x] **11 Scientific Citations:** All 11 references in `references.bib` verified against official conference proceedings, journals, and DOIs.

### NOT Verified / Manual Human Actions Required
- [ ] **Author Permission Letters:** Drafts in `scratch/PERMISSION_REQUEST_TEMPLATES.md` have **NOT** been transmitted to Dan Austin, Bhavatharani Selvaraj, or Alpha-Park. (Requires manual outreach by Ziad).
- [ ] **Elsevier Portal Account Setup:** Upload to `submit.elsevier.com/INFSOF` has **NOT** been initiated. (Requires Ziad to log in with his Elsevier credentials).
- [ ] **Final Author Review of PDF:** Ziad must visually review `paper.pdf` on his local viewer before clicking submit.
