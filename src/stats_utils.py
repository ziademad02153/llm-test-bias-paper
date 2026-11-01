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


def _norm_cdf(z: float) -> float:
    """Standard normal cumulative distribution function."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def compute_tost_paired_proportions(
    arm_a_outcomes: List[int],
    arm_b_outcomes: List[int],
    margin: float = 0.05,
    alpha: float = 0.05
) -> Dict[str, Any]:
    """
    Two One-Sided Tests (TOST) for equivalence of paired binary proportions.
    Used when failing to reject H0 in McNemar's test, to rigorously test whether
    the difference in detection rates is bounded within [-margin, +margin].
    
    H01: p_A - p_B <= -margin
    H02: p_A - p_B >= +margin
    Rejection of both H01 and H02 at level alpha establishes statistical equivalence.
    """
    if len(arm_a_outcomes) != len(arm_b_outcomes):
        raise ValueError("Arms must have identical lengths for paired evaluation.")

    n = len(arm_a_outcomes)
    if n == 0:
        return {"equivalent": False, "p_tost": 1.0}

    b = sum(1 for x, y in zip(arm_a_outcomes, arm_b_outcomes) if x == 1 and y == 0)
    c = sum(1 for x, y in zip(arm_a_outcomes, arm_b_outcomes) if x == 0 and y == 1)

    diff = (b - c) / n
    # Paired standard error for difference in proportions
    var_diff = (b + c - ((b - c) ** 2) / n) / (n ** 2)
    se_diff = math.sqrt(max(var_diff, 1e-9))

    # Two one-sided Z statistics
    z1 = (diff + margin) / se_diff
    z2 = (margin - diff) / se_diff

    p1 = 1.0 - _norm_cdf(z1)
    p2 = 1.0 - _norm_cdf(z2)
    p_tost = max(p1, p2)

    is_equivalent = (p_tost < alpha)
    # 100*(1 - 2*alpha)% confidence interval corresponding to TOST
    z_crit = 1.644853  # for alpha = 0.05 (90% CI covers two one-sided alpha tests)
    ci_tost_lower = diff - z_crit * se_diff
    ci_tost_upper = diff + z_crit * se_diff

    return {
        "n": n,
        "diff_proportions": round(diff, 4),
        "margin": margin,
        "se_diff": round(se_diff, 4),
        "z1": round(z1, 4),
        "z2": round(z2, 4),
        "p_tost": round(p_tost, 5),
        "is_equivalent": is_equivalent,
        "ci_tost_90": (round(ci_tost_lower, 4), round(ci_tost_upper, 4))
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

