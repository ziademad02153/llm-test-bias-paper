"""
Statistical analysis tools for paired binary outcomes and GLMM dataset export.
Implements McNemar's Test (Exact Binomial when n < 25), Odds Ratio with 95% CI,
and contingency table diagnostics using pure Python standard library.
(Renamed from statistics.py to avoid shadowing Python standard library module).
"""

import math
from typing import List, Tuple, Dict, Any, Optional
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
    margin: float = 0.08,
    alpha: float = 0.05
) -> Dict[str, Any]:
    """
    Two One-Sided Tests (TOST) for statistical equivalence of paired binary proportions.
    
    CRITICAL METHODOLOGICAL NOTE:
    Equivalence is an independent statistical hypothesis and is NEVER inferred
    merely from a non-significant McNemar test (p >= 0.05). A failure to reject
    McNemar's H0 only indicates lack of evidence for a difference. Equivalence is
    demonstrated ONLY IF both one-sided null hypotheses are simultaneously rejected:
    
      H01: p_A - p_B <= -margin
      H02: p_A - p_B >= +margin
      
    Rejection of both H01 and H02 (p_TOST = max(p1, p2) < alpha) bounds the true
    difference within (-margin, +margin) at (1 - 2*alpha) confidence.
    
    Sample size note: For N ~ 200-250 and ~25% discordant pairs, margin = 0.08 is
    powered at 80% (alpha = 0.05). A tighter margin of 0.05 requires N ~ 500-600.
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


def fit_interaction_logistic_regression(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Fits a 2x2 Factorial Logistic Regression model with Interaction Term:
        logit(P(Detect)) = beta_0 + beta_exposure*Exposure + beta_model*Model + beta_interaction*(Exposure*Model)
    
    Encoding:
        Exposure: 1 = Code-First (T1, T2), 0 = Spec-Only (T0, T3)
        Model: 1 = Cross-Model (T2, T3), 0 = Same-Model (T0, T1)
        Interaction: Exposure * Model (T2 = 1, others = 0)
    
    Returns:
        Dictionary with coefficients, SEs, Wald z, p-values, Odds Ratios (95% CI),
        and explicit substantive interpretation of the interaction effect.
    """
    # Filter valid completed records (exclude API errors)
    valid_records = [
        r for r in records
        if r.get("execution_status") != "API_ERROR" and r.get("status") != "API_ERROR"
    ]
    n = len(valid_records)
    if n < 4:
        return {"error": "Insufficient valid observations to fit model"}

    # Construct design matrix X (n x 4) and outcome vector y (n)
    X: List[List[float]] = []
    y: List[float] = []

    for r in valid_records:
        exp = 1.0 if r.get("exposure") == "CODE_FIRST" or r.get("condition") in ("T1", "T2") else 0.0
        mod = 1.0 if r.get("model_identity") == "CROSS_MODEL" or r.get("condition") in ("T2", "T3") else 0.0
        inter = exp * mod
        X.append([1.0, exp, mod, inter])
        y.append(float(r.get("detected", 0)))

    # Newton-Raphson IRLS solver
    p_dim = 4
    beta = [0.0] * p_dim
    inv_J = None

    for iteration in range(25):
        # Compute probabilities p_i = 1 / (1 + exp(-X_i * beta))
        p = []
        for row in X:
            eta = sum(row[j] * beta[j] for j in range(p_dim))
            eta = max(min(eta, 20.0), -20.0)  # numerical clipping
            p.append(1.0 / (1.0 + math.exp(-eta)))

        # Weights w_i = p_i * (1 - p_i)
        w = [max(pi * (1.0 - pi), 1e-6) for pi in p]

        # Gradient: g = X^T * (y - p)
        grad = [0.0] * p_dim
        for i in range(n):
            err = y[i] - p[i]
            for j in range(p_dim):
                grad[j] += X[i][j] * err

        # Hessian: H = - X^T * W * X
        # Information matrix J = -H = X^T * W * X
        J = [[0.0] * p_dim for _ in range(p_dim)]
        for i in range(n):
            wi = w[i]
            for j in range(p_dim):
                for k in range(p_dim):
                    J[j][k] += X[i][j] * wi * X[i][k]

        # Regularization ridge to avoid singular matrix if any cell is 0
        for j in range(p_dim):
            J[j][j] += 1e-4

        # Invert J to obtain Covariance matrix
        inv_J = _invert_matrix_4x4(J)
        if inv_J is None:
            break

        # Update step: delta = inv_J * grad
        delta = [sum(inv_J[j][k] * grad[k] for k in range(p_dim)) for j in range(p_dim)]
        beta = [beta[j] + delta[j] for j in range(p_dim)]

        # Check convergence
        if max(abs(d) for d in delta) < 1e-6:
            break

    # Extract standard errors, z-scores, p-values, odds ratios
    var_covar = inv_J if inv_J is not None else [[0.0]*4 for _ in range(4)]
    term_names = ["Intercept", "Exposure (Code-First)", "Model Diversity (Cross-Model)", "Exposure x Model Interaction"]
    param_keys = ["intercept", "exposure", "model_diversity", "interaction"]
    
    results: Dict[str, Any] = {
        "n_observations": n,
        "iterations": iteration + 1,
        "terms": {}
    }

    for idx, (name, key) in enumerate(zip(term_names, param_keys)):
        b = beta[idx]
        se = math.sqrt(max(var_covar[idx][idx], 1e-9))
        z = b / se
        pval = 2.0 * (1.0 - _norm_cdf(abs(z)))
        odds_ratio = math.exp(b)
        ci_lower = math.exp(b - 1.96 * se)
        ci_upper = math.exp(b + 1.96 * se)

        results["terms"][key] = {
            "name": name,
            "coef": round(b, 4),
            "se": round(se, 4),
            "z": round(z, 4),
            "p_value": round(pval, 5),
            "odds_ratio": round(odds_ratio, 4),
            "ci_95": (round(ci_lower, 4), round(ci_upper, 4))
        }

    # Substantive interaction interpretation
    inter_res = results["terms"]["interaction"]
    if inter_res["p_value"] < 0.05:
        if inter_res["coef"] > 0:
            results["substantive_conclusion"] = (
                f"Significant Positive Interaction (beta={inter_res['coef']:.3f}, p={inter_res['p_value']:.4f}): "
                "Changing the model provides a significantly LARGER defect detection advantage when inspecting code (Code-First) "
                "than when working from specification alone."
            )
        else:
            results["substantive_conclusion"] = (
                f"Significant Negative Interaction (beta={inter_res['coef']:.3f}, p={inter_res['p_value']:.4f}): "
                "The benefit of changing the model is significantly attenuated under code-first exposure."
            )
    else:
        results["substantive_conclusion"] = (
            f"No Statistically Significant Interaction (beta={inter_res['coef']:.3f}, p={inter_res['p_value']:.4f}, OR={inter_res['odds_ratio']:.3f}, 95% CI: [{inter_res['ci_95'][0]:.3f}, {inter_res['ci_95'][1]:.3f}]): "
            "The effect of cross-model diversity operates additively and does not significantly depend on whether the model is exposed to code."
        )

    return results


def _invert_matrix_4x4(A: List[List[float]]) -> Optional[List[List[float]]]:
    """Inverts a 4x4 matrix using Gauss-Jordan elimination with partial pivoting."""
    n = 4
    M = [A[i][:] + [float(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot = M[i][i]
        pivot_row = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(pivot):
                pivot = M[k][i]
                pivot_row = k
        if pivot_row != i:
            M[i], M[pivot_row] = M[pivot_row], M[i]
        if abs(pivot) < 1e-12:
            return None
        for j in range(2 * n):
            M[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = M[k][i]
                for j in range(2 * n):
                    M[k][j] -= factor * M[i][j]
    return [[M[i][j + n] for j in range(n)] for i in range(n)]

