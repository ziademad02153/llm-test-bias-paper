# Pilot Study Execution Report (N=30)
**Generated Date:** 2026-11-03 07:31:19 UTC
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

## 3. Inferential Statistics (Paired Comparisons)

- **McNemar Exact Test (T0 vs T1):**
  - Concordant Pairs (a/d): 0 / 0
  - Discordant Pairs (b/c): 0 / 0
  - Exact Binomial P-Value: **0.125000**
- **TOST Paired Equivalence Test (Delta = ±0.08):**
  - Risk Difference: **+0.1333**
  - 90% Confidence Interval: **[0.0312, 0.2354]**
  - Equivalence Established: **False**

## 4. Token & Cost Accounting

- **Total Processed Tokens:** 74,850 tokens
- **Total Compute Cost:** $0.012303 USD
- **Total Pipeline Execution Latency:** 43.76 seconds
