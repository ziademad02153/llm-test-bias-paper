# Pilot Study Execution Report (N=30)
**Generated Date:** 2026-11-03 08:08:33 UTC
**Status:** Completed & Validated

## 1. Pilot Feasibility Gate Criteria (Section 8 Verification)

| Protocol Criterion | Target Threshold | Pilot Outcome | Gate Status |
| :--- | :--- | :--- | :--- |
| **Evaluated Pairs** | N = 30 | **30 Pairs** | **PASS** |
| **Fault Harvest Yield** | >= 20 Defect Instances | **30 Instances** | **PASS** |
| **Oracle Validity (C_ref)** | >= 70% Valid Rate | **100.0%** | **PASS** |
| **Execution Stability** | Timeout/Crash < 5% | **0.0% Crashes** | **PASS** |
| **Economic Feasibility** | Within budget | **$0.0123 USD** | **PASS** |

## 2. Experimental Condition Comparison (Detection Rates)

| Condition | Description | Observations | Detection Rate |
| :--- | :--- | :---: | :---: |
| **T0** | Spec-Only, Same Model | 30 | **100.0%** |
| **T1** | Code-First, Same Model | 30 | **86.7%** |
| **T2** | Code-First, Cross Model | 30 | **93.3%** |
| **T3** | Spec-Only, Cross Model | 30 | **100.0%** |

## 3. Inferential Statistics & 2x2 Contingency Tables

### A. Primary Comparison: T0 (Spec-Same) vs T1 (Code-Same)
Tests H1 (Exposure Bias: Spec-only outperforms Code-first in fault detection):

| | T1 Detect (1) | T1 Miss (0) | Total |
| :--- | :---: | :---: | :---: |
| **T0 Detect (1)** | a = 26 | b = 4 | 30 |
| **T0 Miss (0)** | c = 0 | d = 0 | 0 |
| **Total** | 26 | 4 | 30 |

- **Concordant Pairs (a + d):** 26 (Both detected: 26, Both missed: 0)
- **Discordant Pairs (b + c):** 4 (T0 only: 4, T1 only: 0)
- **McNemar Test:** Exact Binomial Test (discordant < 25), p = **0.125000**
- **Paired Proportion Difference (T0 - T1):** **+0.1333** (90% CI: [+0.0312, +0.2354])
- **TOST Equivalence (Margin = ±0.08):** p_TOST = 0.80492 -> Equivalence: **False**

### B. Cross-Model Attenuation: T0 (Spec-Same) vs T2 (Code-Cross)
Tests H2 (Cross-model mitigation of code exposure):

| | T2 Detect (1) | T2 Miss (0) | Total |
| :--- | :---: | :---: | :---: |
| **T0 Detect (1)** | a = 28 | b = 2 | 30 |
| **T0 Miss (0)** | c = 0 | d = 0 | 0 |
| **Total** | 28 | 2 | 30 |

- **Discordant Pairs (b/c):** b = 2 (T0 only), c = 0 (T2 only) -> Total: 2
- **McNemar Test:** p = **0.500000**
- **Paired Proportion Difference (T0 - T2):** **+0.0667** (90% CI: [-0.0082, +0.1416])

### C. Model-Family Effect: T1 (Code-Same) vs T2 (Code-Cross)
Direct comparison of same-family vs cross-family under identical code exposure:

| | T2 Detect (1) | T2 Miss (0) | Total |
| :--- | :---: | :---: | :---: |
| **T1 Detect (1)** | a = 26 | b = 0 | 26 |
| **T1 Miss (0)** | c = 2 | d = 2 | 4 |
| **Total** | 28 | 2 | 30 |

- **Discordant Pairs (b/c):** b = 0 (T1 only), c = 2 (T2 only) -> Total: 2
- **McNemar Test:** p = **0.500000**
- **Paired Proportion Difference (T1 - T2):** **-0.0667** (90% CI: [-0.1416, +0.0082])

### D. Baseline Model Equivalence: T0 (Spec-Same) vs T3 (Spec-Cross)
Verifies that tester models have equivalent baseline capability in the absence of code exposure:

| | T3 Detect (1) | T3 Miss (0) | Total |
| :--- | :---: | :---: | :---: |
| **T0 Detect (1)** | a = 30 | b = 0 | 30 |
| **T0 Miss (0)** | c = 0 | d = 0 | 0 |
| **Total** | 30 | 0 | 30 |

- **Discordant Pairs:** b = 0, c = 0 -> Total: 0
- **TOST Equivalence (Margin = ±0.08):** p_TOST = **0.00000** -> Equivalence: **True**

## 4. Token & Cost Accounting

- **Total Processed Tokens:** 74,850 tokens
- **Total Compute Cost:** $0.012303 USD
- **Total Pipeline Execution Latency:** 49.36 seconds
