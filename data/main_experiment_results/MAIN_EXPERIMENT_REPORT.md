# Main Empirical Experiment Report: 2x2 Factorial Investigation
**Generated Date:** 2026-11-04 11:15:13 UTC
**Methodological Reference:** Konstantinou et al. (arXiv:2607.05139) & Leu et al. (ESEM 2026)
**Data Provenance:** Aggregated from full dataset `main_glmm_dataset.csv` (Unified across checkpoint sessions)
**Total Tasks Recorded:** 225 | **Total Executions:** 900 | **Recorded generation cost:** $0.1335 USD
**API error rows retained in this CSV:** 0
These are matched trials on 15 distinct problems, rather than 225 distinct tasks.
Earlier HTTP 402 failures and retries occurred. Some error rows were removed before resumption, so this final CSV does not recover all attempts or total historical cost.

## 1. Executive Summary: Primary Findings

| Research Question | Paired Comparison | Valid Pairs (N) | Excluded Trials | Observed Metric | Statistical Test | p-value | Empirical Conclusion |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **RQ1 (Code-First Bias)** | $T_0$ vs $T_1$ | **N = 225** | 0 | $T_0=33.8\%$ vs $T_1=24.4\%$ | McNemar Exact | $p=0.0046$ | Difference detected in trial-level paired analysis |
| **RQ2 (Model Diversity)** | $T_1$ vs $T_2$ | **N = 225** | 0 | $T_1=24.4\%$ vs $T_2=18.2\%$ | McNemar Exact | $p=0.0649$ | Difference not demonstrated |
| **RQ2 (TOST Equivalence)** | $T_1$ vs $T_2$ | **N = 225** | 0 | Bounds $\pm 0.08$ | TOST (Two One-Sided) | $p=0.2841$ | NOT DEMONSTRABLY EQUIVALENT |

## 2. RQ1: Confirmatory Replication of Code-First Bias (T0 vs T1)
- **Valid Matched Pairs (N):** 225 (Strictly matched on same `trial_id`)
- **Excluded Trials:** 0

### 2x2 Paired Contingency Matrix:
```
                     T1 (Code-First) Detect | T1 (Code-First) Miss
T0 (Spec-Only) Detect:          40          |          36 (T0 only)
T0 (Spec-Only) Miss  :          15          |         134 (Both miss)
```
- **Discordant Pairs:** 51 (36 vs 15)
- **Odds Ratio:** 2.400 (95% CI: [1.314, 4.383])
- **McNemar two-sided exact p:** 0.00460131
- **Detection difference T0 minus T1:** 9.33 percentage points. The matched odds ratio describes discordant pairs.

## 3. RQ2: Cross-Family Model Diversity & Equivalence (T1 vs T2)
- **Valid Matched Pairs (N):** 225 (Strictly matched on same `trial_id`)
- **Excluded Trials:** 0

### 2x2 Paired Contingency Matrix:
```
                      T2 (Cross-Model) Detect | T2 (Cross-Model) Miss
T1 (Same-Model) Detect:          23           |          32
T1 (Same-Model) Miss  :          18           |         152
```
- **TOST Equivalence Margin:** $\theta = \pm 0.08$
- **Observed Proportion Difference:** $\hat{d} = 0.0622$
- **90% Confidence Interval:** $[0.0110, 0.1135]$
- **Equivalence Assessment:** BOUNDS EXCEED MARGIN

## 4. RQ3 mixed logistic interaction
Model fitted by lme4 with binomial logit, coder fixed effects and a problem random intercept.
Formula is detected ~ exposure * cross_model + coder + (1 | problem_id).

| Term | Coefficient | SE | Wald p | Odds ratio | 95% OR interval |
| --- | --- | --- | --- | --- | --- |
| (Intercept) | -0.5051 | 1.3844 | 0.71524 | 0.6035 | [0.0400, 9.1003] |
| exposure | -0.7402 | 0.2690 | 0.00592345 | 0.4770 | [0.2816, 0.8081] |
| cross_model | 0.4506 | 0.2550 | 0.077243 | 1.5693 | [0.9520, 2.5871] |
| codermeta-llama/llama-3.3-70b-instruct | -0.9878 | 1.5168 | 0.514923 | 0.3724 | [0.0190, 7.2805] |
| coderqwen/qwen-2.5-7b-instruct | 0.8309 | 2.3802 | 0.727012 | 2.2954 | [0.0216, 243.7061] |
| coderqwen/qwen-2.5-coder-32b-instruct | 0.1484 | 1.9505 | 0.939359 | 1.1600 | [0.0254, 53.0482] |
| exposure:cross_model | -1.0358 | 0.3887 | 0.00770477 | 0.3549 | [0.1657, 0.7604] |

Included observations 900 across 15 problems.
Singular fit FALSE. Optimizer code 0.
Convergence messages none.
Warnings none.
Problem intercept SD 1.9223.
Interaction likelihood-ratio p 0.00723786.
Maximum coefficient change at nAGQ=15 2.42103e-05.
Full model output and session information are saved in GLMM_OUTPUT.txt.

## 5. Overall 2x2 Factorial Summary Across All 4 Conditions

| Condition | Code Exposure | Model Identity | Total Recorded | API Errors | Completed | Valid Oracles | Valid Rate | Detections | Detection Rate |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **T0** | Specification Only | Same Family (Coder) | 225 | 0 | 225 | 194 | 86.2% | 76 | **33.8%** |
| **T1** | Code-First Exposure | Same Family (Coder) | 225 | 0 | 225 | 146 | 64.9% | 55 | **24.4%** |
| **T2** | Code-First Exposure | Cross-Family Model | 225 | 0 | 225 | 192 | 85.3% | 41 | **18.2%** |
| **T3** | Specification Only | Cross-Family Model | 225 | 0 | 225 | 218 | 96.9% | 90 | **40.0%** |

## 6. Audit Trail & Data Provenance
The dataset contains 225 repeated trials on 15 distinct problems. Trial-level McNemar and normal-approximation paired TOST do not account for within-problem dependence. Treat them as supporting analyses alongside the mixed model and exploratory problem-level sensitivity.
The SDK generation path allowed provider fallbacks. Actual provider and quantization for every historical response are not preserved in this CSV, so strict provider pinning cannot be claimed.
No direct psychological measure was collected. Exposure-related detection differences do not establish a cognitive mechanism.
The original v1.0 tag predates replacement faults and evaluator corrections. It does not freeze the final study assets. Archive the final dataset, accepted faults, evaluation code and analysis together before writing.
- **Raw Observations Dataset:** `data\main_experiment_results\main_glmm_dataset.csv`
- **Archived Unit Test Suites:** `data\main_experiment_results\generated_tests`
- **Frozen Benchmark Snapshot:** Git Tag `v1.0-dataset-faults-frozen` (Commit `828cc78`)

## 7. Reviewed interpretation and writing readiness

Collection is complete. The study is ready for a first paper draft with the limitations below.
The random-intercept GLMM is the protocol analysis. Supplemental sensitivity analyses were added after data collection and are exploratory.

| Condition | Detection among usable suites |
| --- | --- |
| T0 | 39.18% |
| T1 | 37.67% |
| T2 | 21.35% |
| T3 | 41.28% |

Conditioning on suite validity selects different outputs in each arm. These descriptive percentages are not a replacement for the primary end-to-end outcome.
T0 minus T1 is 9.33 percentage points overall, while the usable-suite percentages are closer. Lower test usability contributes to the overall exposure difference.

Exploratory sensitivity averages the repeated observations within each problem and applies a paired t test across the 15 problem-level differences.
These probability-scale contrasts differ from the conditional log-odds interaction estimated by the GLMM.

| Contrast | Mean probability difference | 95% interval | p |
| --- | --- | --- | --- |
| T0_minus_T1 | 0.0933 | [-0.0468, 0.2334] | 0.1750 |
| T1_minus_T2 | 0.0622 | [-0.1112, 0.2356] | 0.4544 |
| T3_minus_T2 | 0.2178 | [-0.0320, 0.4676] | 0.0826 |
| probability_interaction | -0.1244 | [-0.4017, 0.1528] | 0.3521 |

An exploratory GLMM with independent problem-specific slopes for exposure, diversity and interaction gives interaction p=0.0317, beta=-7.2365, SE=3.3689.
Singular fit FALSE. Convergence messages none.
The task-specific slope variances are large and the fixed interaction magnitude changes substantially. With 15 problems, population generalization and effect magnitude remain uncertain.

Write an empirical study of these tasks and model configurations. Avoid claims of universal blindness, a directly measured cognitive mechanism, guaranteed equivalence, or strict provider pinning.
Preserve the completed CSV and generated tests. Record the final analysis code and data hashes with the paper.