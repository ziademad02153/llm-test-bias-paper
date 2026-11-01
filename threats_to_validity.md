# Threats to Validity

This document provides a comprehensive, pre-registered analysis of the threats to validity for our empirical investigation: **"Disentangling Code Exposure from Model Diversity in Automated LLM Test Generation"**, structured according to ACM/IEEE standard empirical guidelines (Wohlin et al., 2012).

---

## 1. Internal Validity (Causal Inference & Confounders)

Internal validity concerns whether the observed differences in fault detection rates can be definitively attributed to our manipulated factors (Code Exposure and Model Family) rather than confounding experimental artifacts.

### 1.1 Model Stochasticity and Temperature Settings
- **Threat:** LLM outputs are non-deterministic. Variations in defect detection between conditions could potentially arise from sampling variance rather than the experimental treatment.
- **Mitigation:**
  - In our protocol, test generation in all conditions ($T_0, T_1, T_2, T_3$) is conducted with a deterministic low temperature ($T = 0.2$) to minimize sampling noise while preserving generative validity.
  - Fault harvesting is conducted at $T = 0.8$ across 10 sequential attempts per task to explore diverse defect modes, followed by deterministic selection (Primary: first valid fault; Sensitivity: hardest fault).
  - Exact system fingerprints, provider metadata, and generation parameters are logged immutably for every call.

### 1.2 Fault Selection & Cherry-Picking Bias
- **Threat:** Subjectively selecting which generated buggy implementation to test could artificially inflate or deflate detection rates.
- **Mitigation:**
  - We pre-register two automated, objective selection heuristics:
    1. **Primary Heuristic:** The *first-harvested valid fault* ($k=1 \dots 10$) meeting the inclusion criteria (fails $\ge 1$ and $\le 50\%$ reference tests without unhandled runtime crashes).
    2. **Secondary Heuristic (Sensitivity Analysis):** The *hardest-to-detect fault* (failing the fewest reference assertions, matching Konstantinou et al.).
  - The manual audit decision (`data/fault_audit.json`) is strictly finalized *before* executing the test generators under conditions $T_0–T_3$.

### 1.3 Dataset Extraction & Task Selection Bias
- **Threat:** Non-random or manual selection of benchmark tasks could bias the benchmark toward domains where code-first bias is disproportionately severe or muted.
- **Mitigation:**
  - Automated mining pipeline (`src/github_miner.py`) retrieves candidate tasks from public GitHub repositories meeting objective filters (`created:>=2025-07-01`, `stars:>=5`, `fork:false`).
  - Tasks are sampled deterministically using a fixed, pre-registered pseudo-random seed (`random_seed = 42`) across a balanced five-category taxonomy (Parsing, Pure Algorithms, Data Structures & Graphs, Scheduling, State Machines).
  - Every examined task—whether accepted or excluded—is permanently recorded in `data/dataset_decisions.csv` (Audit Trail) with full technical justification.

---

## 2. External Validity (Generalizability)

External validity concerns the extent to which our empirical findings generalize to software engineering practice and broader model ecosystems.

### 2.1 Language Scope (Python Specialization)
- **Threat:** All experimental tasks are implemented in Python. Findings may not generalize identically to statically typed or functional languages (e.g., Elixir as studied by Leu et al., or Java/Rust).
- **Limitation & Disclosure:** We explicitly scope our empirical claims to Python standalone algorithmic and utility components. Python represents the primary language in LLM code generation benchmarks (HumanEval, MBPP, BigCodeBench), maximizing comparability with foundational literature. Cross-language replication is formally declared as future work.

### 2.2 Temporal Cutoff & Model Checkpoint Age
- **Threat:** Models evaluated in this study (Llama 3.3 70B, DeepSeek-V3, Qwen 2.5 Coder 32B) were released in late 2024. As proprietary frontier models advance, newer architectures might exhibit different reasoning capabilities.
- **Trade-off & Disclosure:** We intentionally traded commercial snapshot volatility for scientific reproducibility. Using frozen, open-weight models with public weight checkpoints guarantees that the study can be reproduced indefinitely without commercial API retirement risks. We explicitly state that findings demonstrate structural exposure bias in modern open architectures, but should be re-evaluated as newer open foundation models emerge.

### 2.3 Unit-Level Standalone Functional Scope
- **Threat:** Real-world software systems involve complex database connections, framework state, network I/O, and UI event loops.
- **Limitation & Disclosure:** Evaluating unit test oracle generation on standalone functions isolated in Docker sandboxes is a deliberate construct choice to eliminate execution non-determinism (flaky network/database dependencies). While this mirrors standard benchmarks, integration-level exposure bias remains an open research horizon.

---

## 3. Construct Validity (Alignment of Metrics with Real Defect Detection)

Construct validity assesses whether our operationalized measurements accurately reflect the real-world phenomena of oracle validity and bug detection.

### 3.1 Defect Detection vs. Syntax / Runtime Crashes
- **Threat:** If an LLM-generated test causes the program to crash due to a `TypeError` or invalid parameter type, counting this as "bug detection" conflates interface mismatch with genuine logic fault detection.
- **Mitigation:**
  - We strictly enforce dual validation: Every generated test suite is decomposed into individual test cases ($\{t_1, \dots, t_k\}$) and executed first on the clean reference implementation ($C_{\text{ref}}$).
  - Only test cases that pass $100\%$ on $C_{\text{ref}}$ ($T_{\text{valid}}$) are permitted to evaluate the faulty implementation ($C_{\text{faulty}}$).
  - Non-viable faulty candidates (those causing syntax errors or runtime exceptions during reference tests) are excluded from the primary logic-fault benchmark, in direct alignment with Konstantinou et al.

### 3.2 Test-Case Slicing vs. Suite-Level Validity
- **Threat:** Rejecting an entire test suite because a single assertion fails on $C_{\text{ref}}$ could artificially depress valid suite yield. Conversely, ignoring reference failures could introduce false positives.
- **Mitigation:** We report results at two granularities:
  1. *Usable Suite Validity ($|T_{\text{valid}}| \ge 1$)*: Slices valid assertions and tests $C_{\text{faulty}}$.
  2. *Strict Suite Validity ($|T_{\text{valid}}| == |T_{\text{gen}}|)$*: Requires zero false alarms on $C_{\text{ref}}$.
  Primary conclusions are tested and reported across both levels.

---

## 4. Conclusion & Statistical Validity

Conclusion validity assesses whether the statistical analysis and power are sufficient to support the conclusions drawn.

### 4.1 Paired Nominal Comparison & Continuity Correction
- **Mitigation:** We avoid independent-samples tests ($t$-test, Mann-Whitney $U$) because conditions are evaluated on identical problem subjects. We employ **McNemar's test with Edwards continuity correction**, with exact binomial tests automatically applied when discordant pairs $b + c < 25$.

### 4.2 Equivalence Testing & Non-Significance Pitfalls
- **Mitigation:** We do not commit the common empirical fallacy of claiming "no difference" implies "equivalence". Equivalence is tested independently via **Two One-Sided Tests (TOST)** with a pre-registered primary equivalence margin $\Delta = \pm 0.08$ (powered at $\ge 80\%$ for $N = 200–250$), and a secondary sensitivity margin $\Delta = \pm 0.05$.
