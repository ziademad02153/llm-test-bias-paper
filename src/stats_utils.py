"""
Statistical analysis tools for paired binary outcomes and GLMM dataset export.
Implements McNemar's Test (Exact Binomial when n < 25), Odds Ratio with 95% CI,
and contingency table diagnostics using pure Python standard library.
(Renamed from statistics.py to avoid shadowing Python standard library module).
"""

import math
from typing import List, Tuple, Dict, Any
import csv


def _binomial_cdf(k: int, n: int, p: float = 0.5) -> float:
    """Exact cumulative distribution function for Binomial(n, p)."""
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    total = 0.0
    for i in range(k + 1):
        total += math.comb(n, i) * (p ** i) * ((1.0 - p) ** (n - i))
    return total


def _exact_binomial_two_tailed(k: int, n: int) -> float:
    """Two-tailed exact binomial test p-value for H0: p = 0.5."""
    if n == 0:
        return 1.0
    k_min = min(k, n - k)
    prob_one_tail = _binomial_cdf(k_min, n, 0.5)
    return min(1.0, 2.0 * prob_one_tail)


def _chi2_sf_df1(x: float) -> float:
    """Survival function (1 - CDF) for Chi-Square distribution with df=1 using erf."""
    if x <= 0:
        return 1.0
    return math.erfc(math.sqrt(x / 2.0))


def compute_contingency_table(
    arm_a_outcomes: List[int],
    arm_b_outcomes: List[int]
) -> Dict[str, Any]:
    """
    Computes 2x2 paired contingency table for two arms across the same subjects/problems:
    
                   Arm B Detect (1) | Arm B Miss (0)
    Arm A Detect(1)        a        |       b
    Arm A Miss  (0)        c        |       d
    
    Discordant pairs:
    b: Arm A detected, Arm B missed.
    c: Arm A missed, Arm B detected.
    """
    if len(arm_a_outcomes) != len(arm_b_outcomes):
        raise ValueError("Arms must have identical lengths for paired evaluation.")

    a = sum(1 for x, y in zip(arm_a_outcomes, arm_b_outcomes) if x == 1 and y == 1)
    b = sum(1 for x, y in zip(arm_a_outcomes, arm_b_outcomes) if x == 1 and y == 0)
    c = sum(1 for x, y in zip(arm_a_outcomes, arm_b_outcomes) if x == 0 and y == 1)
    d = sum(1 for x, y in zip(arm_a_outcomes, arm_b_outcomes) if x == 0 and y == 0)
    n = len(arm_a_outcomes)

    discordant = b + c

    # McNemar Statistic & P-Value
    if discordant == 0:
        p_val = 1.0
        stat = 0.0
        method = "Exact (no discordant pairs)"
    elif discordant < 25:
        p_val = _exact_binomial_two_tailed(b, discordant)
        stat = float(b)
        method = "Exact Binomial Test (discordant < 25)"
    else:
        # Edwards continuity correction
        stat = (abs(b - c) - 1.0) ** 2 / discordant
        p_val = _chi2_sf_df1(stat)
        method = "McNemar Chi-Square (with continuity correction)"

    # Odds Ratio (b / c)
    if b == 0 or c == 0:
        adj_b = b + 0.5
        adj_c = c + 0.5
        odds_ratio = adj_b / adj_c
        se_log_or = math.sqrt(1.0 / adj_b + 1.0 / adj_c)
    else:
        odds_ratio = b / c
        se_log_or = math.sqrt(1.0 / b + 1.0 / c)

    ci_lower = math.exp(math.log(odds_ratio) - 1.96 * se_log_or)
    ci_upper = math.exp(math.log(odds_ratio) + 1.96 * se_log_or)

    return {
        "n_total": n,
        "a_both_detect": a,
        "b_armA_only": b,
        "c_armB_only": c,
        "d_both_miss": d,
        "discordant_pairs": discordant,
        "statistic": round(stat, 4),
        "p_value": round(p_val, 5),
        "method": method,
        "odds_ratio": round(odds_ratio, 3),
        "ci_95": (round(ci_lower, 3), round(ci_upper, 3)),
        "arm_a_detection_rate": round((a + b) / n, 4) if n > 0 else 0.0,
        "arm_b_detection_rate": round((a + c) / n, 4) if n > 0 else 0.0,
    }


def export_glmm_dataset(
    records: List[Dict[str, Any]],
    output_csv_path: str
) -> None:
    """
    Exports full trial results to CSV formatted for Generalized Linear Mixed Models (GLMM):
    Fields: problem_id, condition, code_exposure (0=spec, 1=code), model_family (0=same, 1=cross),
            is_valid (0/1), detects_fault (0/1), execution_time_ms
    """
    fields = [
        "problem_id",
        "condition",
        "code_exposure",
        "model_family",
        "is_valid",
        "detects_fault",
        "execution_time_ms"
    ]
    with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in records:
            writer.writerow({
                "problem_id": r["problem_id"],
                "condition": r["condition"],
                "code_exposure": 1 if "Code" in r["condition"] else 0,
                "model_family": 1 if "Cross" in r["condition"] else 0,
                "is_valid": 1 if r["is_valid"] else 0,
                "detects_fault": 1 if r["detects_fault"] else 0,
                "execution_time_ms": round(r.get("execution_time_ms", 0.0), 2)
            })
