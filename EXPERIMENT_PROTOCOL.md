# Experimental Protocol: 2×2 Factorial Investigation on Code-First LLM Test Generation

## Title
**Disentangling Code Exposure from Model Diversity: A 2×2 Factorial Investigation on the Limits of LLM Test Generation**

---

## 1. Context, Background, and Research Motivation

Recent empirical literature in Software Engineering highlights two pivotal findings regarding Large Language Models in test generation:
1. **Code-First Exposure Degradation:** Konstantinou et al. (SnT, University of Luxembourg; arXiv:2607.05139) evaluated 5 LLMs on HumanEval+, MBPP, and BigCodeBench, finding that generating unit tests *after* observing implementation code severely degrades fault detection (dropping from 18–33% down to 5–17%). However, their study evaluated single-model workflows and explicitly left multi-model interactions as an open question.
2. **Model Diversity under Code Exposure:** Leu, Oertel, and Hebig (University of Rostock; ESEM 2026, LIPIcs Vol. 394) investigated whether pairing different LLMs on Elixir code mitigates test suite deficiencies, finding no statistically significant difference between same-model and different-model test generators ($U = 540,217, p = 0.152, \text{CLES} = 0.513$). Crucially, all test generation in Leu et al. was conducted white-box (exposed to code), omitting a specification-only baseline.

### The Core Empirical Question
These findings are not contradictory; rather, they vary two distinct factors. If Leu et al. observed no benefit from model diversity under white-box code exposure, this aligns with the hypothesis that **code exposure itself is the dominant driver of oracle degradation**, rendering cross-family model changes secondary.

Our study establishes a full $2 \times 2$ factorial experiment on Python to cleanly separate:
- **Factor A (Code Exposure):** Specification-Only vs. Code-First Exposure.
- **Factor B (Model Diversity):** Intra-Model (Same Coder) vs. Cross-Family Model.

---

## 2. Research Questions (RQs) & Hypotheses

- **RQ1 (Confirmatory Replication of Code-First Bias):**  
  Does exposing the test-generation model to implementation code decrease fault detection relative to generating tests solely from specifications ($T_0$ vs. $T_1$, and $T_3$ vs. $T_2$)?  
  *Pre-registered Hypothesis ($H_1^{(1)}$):* Replicate Konstantinou et al.; $P(\text{Detect} \mid T_0) > P(\text{Detect} \mid T_1)$ and $P(\text{Detect} \mid T_3) > P(\text{Detect} \mid T_2)$ using McNemar's test ($\alpha = 0.05$).

- **RQ2 (Primary Inquiry - Cross-Family Model Diversity & Equivalence):**  
  Holding code exposure constant, does employing a model from a distinct architectural family significantly alter fault detection ($T_1$ vs. $T_2$ under code exposure, and $T_0$ vs. $T_3$ under spec-only)?  
  *Pre-registered Difference Hypothesis ($H_0^{(2)}$):* Cross-family model diversity does not yield a statistically significant difference (tested via McNemar's test, $\alpha = 0.05$).  
  *Pre-registered Equivalence Hypothesis ($H_E^{(2)}$):* Performance between intra-model and cross-family generators is practically equivalent within a pre-registered equivalence bound $\Delta = \pm 0.08$ (8 percentage points) at $\alpha = 0.05$, tested via independent **Two One-Sided Tests (TOST)**.

- **RQ3 (Factorial Interaction):**  
  Is there a statistically significant interaction between Code Exposure and Model Family? Does cross-family diversity provide recovery specifically when code is visible, or is the code-first masking effect model-invariant?  
  *Model:* Generalized Linear Mixed Model (GLMM / Mixed Logistic Regression) with problem random effects.

- **RQ4 (Fault Taxonomy & Economic Trade-offs):**  
  Which categories of programming defects (e.g., boundary inversion, off-by-one, None-handling, state mutation) systematically evade test oracles across conditions? What is the token cost per detected defect across intra-model vs. cross-model strategies?

---

## 3. Experimental Design (2×2 Factorial Crossover)

| Exposure \ Model Identity | Same Model (Coder) | Cross-Family Model |
| :--- | :---: | :---: |
| **Specification Only** (Docstring + Signature) | **$T_0$** | **$T_3$** |
| **Code-First Exposure** (Docstring + Faulty Code) | **$T_1$** | **$T_2$** |

### 3.1 Model Checkpoints, Provenance & Source Verification
To eliminate commercial API deprecation carousel risks (such as vendor snapshot retirement) and guarantee scientific reproducibility, the study utilizes frozen **Open-Weight Models** with verified releases:

| Model Identifier | Family / Creator | Architecture & Quantization | Official Release Date | Cutoff Date / Bound | Reference Links & Documentation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `meta-llama/Llama-3.3-70B-Instruct` | Meta AI | Dense Transformer (BF16 / FP8) | December 6, 2024 | December 2023 | [Meta Announcement](https://ai.meta.com/blog/llama-3-3/) \| [Hugging Face Card](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) |
| `deepseek-ai/DeepSeek-V3` | DeepSeek | MoE 671B (Native FP8) | December 26, 2024 | Dec 2024 bound | [GitHub Repo](https://github.com/deepseek-ai/DeepSeek-V3) \| [Tech Report arXiv:2412.19437](https://arxiv.org/abs/2412.19437) \| [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V3) |
| `Qwen/Qwen2.5-Coder-32B-Instruct` | Alibaba Cloud | Dense Transformer (BF16 / FP8) | November 12, 2024 | Nov 2024 bound | [Qwen Blog](https://qwenlm.github.io/blog/qwen2.5-coder-family/) \| [Hugging Face Card](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) |

### 3.2 Provider Pinning & Hardware Determinism
To prevent silent provider rerouting, load-balancing variations, or unannounced backend quantization changes:
- Invocations specify strict provider pinning via OpenRouter routing parameters (`provider: {order: [PinnedProvider], allow_fallbacks: false}`):
  - **Llama 3.3 70B:** Pinned to `DeepInfra` (quantization: `bf16`).
  - **DeepSeek-V3:** Pinned to `DeepSeek` official backend (quantization: native `fp8`).
  - **Qwen 2.5 Coder 32B:** Pinned to `DeepInfra` (quantization: `bf16`).
- System fingerprints, model response IDs, and provider response metadata are logged immutably for every experimental invocation.

### 3.3 API Pricing Catalog (Access Date: November 1, 2026)
Pricing catalog per 1 Million tokens, verified against public rate schedules:
- **Llama 3.3 70B:** \$0.12 prompt / \$0.30 completion ([OpenRouter Llama 3.3](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct)).
- **DeepSeek-V3:** \$0.14 prompt (\$0.07 cache hit) / \$0.28 completion ([DeepSeek Official API Pricing](https://api-docs.deepseek.com/quick_start/pricing); [OpenRouter DeepSeek-V3](https://openrouter.ai/deepseek/deepseek-chat)).
- **Qwen 2.5 Coder 32B:** \$0.06 prompt / \$0.15 completion ([OpenRouter Qwen 2.5 Coder](https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct)).

---

## 4. Materials, Fault Harvesting, and Contamination Control

### 4.1 Temporal Cutoff Boundary: July 1, 2025
- **Cutoff Justification:** The latest foundational model release among the experimental candidates is DeepSeek-V3 (December 26, 2024) and Llama 3.3 (December 6, 2024).
- Adding the mandatory 6-month post-release safety buffer:
  $$\text{December 26, 2024} + 6\text{ months} = \text{June 26, 2025}$$
- To ensure a conservative, indisputable safety margin, the temporal threshold is set to **July 1, 2025** (1 يوليو 2025).
- **Candidate Evaluation Window:** July 1, 2025 to November 1, 2026 (~16 months of open-source Python commits).

### 4.2 4-Stage Contamination Screening Protocol
Every candidate Python function must pass all four stages before inclusion:
1. **Timestamp Verification:** Commit timestamp verified via `git log --format="%ci"` to be strictly $\ge$ July 1, 2025.
2. **Net-New Body Provenance (`git log -L`):** The entire function body must be a net-new addition introduced in that commit, rejecting modifications or refactorings of pre-existing functions.
3. **Pre-2024 Clone & Derivation Screening:** Syntactic and semantic cross-referencing against pre-2024 repositories to eliminate refactored legacy clones.
4. **AI-Authorship Exclusion:** Audit of commits, PRs, and comments for AI co-authorship markers (`Copilot`, `cursor`, `devin`, `Generated by`). Discard any candidate suspected of non-human origination. (Recorded as a construct validity limitation).
5. **Standalone Functional Purity:** Functions rely solely on Python standard library modules (`math`, `re`, `json`, `collections`), rejecting complex framework state or mocks.

### 4.3 Pre-Registered Deterministic Random Sampling Protocol
To completely prevent researcher cherry-picking and guarantee reproducible selection of benchmark tasks from GitHub:
1. **Candidate Pool Mining:** The automated miner (`src/github_miner.py`) retrieves all standalone Python functions from genuine GitHub repositories meeting the temporal threshold ($\ge$ July 1, 2025) and passing $C_{\text{ref}}/T_{\text{ref}}$ 100% execution validation.
2. **Deterministic Canonical Sorting:** Candidates in the pool are sorted lexicographically by `(repo_url, commit_hash, function_name)`.
3. **Fixed-Seed Sampling:** The evaluation tasks are sampled deterministically using Python's Mersenne Twister pseudo-random generator with a pre-registered seed:
   $$\text{Seed} = 42, \quad N_{\text{pilot}} = 30, \quad N_{\text{full}} = 200–250$$
4. **Immutability:** The sampled task list (`sampled_tasks.json`) is committed and locked prior to running LLM test generation.

### 4.4 Fault Harvesting Protocol (Alignment with Konstantinou et al.)
1. The Coder model generates 10 candidate implementations per task at temperature $T = 0.8$.
2. Each candidate is executed against the reference test suite ($T_{\text{ref}}$).
3. **Inclusion Criteria:**
   - A candidate is classified as a valid faulty implementation ($C_{\text{faulty}}$) if and only if it fails $\ge 1$ reference test and $\le 50\%$ of reference tests.
   - **Exclusion of Non-Logic Failures (Konstantinou et al. alignment):** Candidates that produce syntax errors, unhandled runtime exceptions (`TypeError`, `IndexError`, `ZeroDivisionError`), or infinite loops/timeouts during $T_{\text{ref}}$ execution are discarded. The benchmark strictly targets genuine semantic and logical defects (where the code runs cleanly without crashing but returns an incorrect value, violating assertions).
4. **Pre-Registered Fault Selection Heuristic:**
   - **Primary Heuristic:** **First-Harvested Valid Fault** (the first generated candidate in sequential order meeting the inclusion criteria). This completely eliminates post-hoc selection bias.
   - **Secondary Heuristic (Sensitivity Analysis):** **Hardest-to-Detect Fault** (the candidate failing the fewest reference assertions, matching Konstantinou's selection method for comparability).

### 4.5 Pre-Registered Blinded Fault Audit
Every harvested $C_{\text{faulty}}$ is audited manually:
- The auditor inspects only: (1) `docstring` + `signature`, (2) $C_{\text{faulty}}$ code, and (3) failing assertion from $T_{\text{ref}}$.
- The inclusion/exclusion decision in `fault_audit.json` is **finalized before running conditions $T_0, T_1, T_2, T_3$**, preventing confirmation bias.

---

## 5. Execution Sandbox & Oracle Validity

### 5.1 Docker Sandbox Standard
All benchmark executions reported in the study are performed strictly within a **Docker container with `--network none`**, `--memory 512m`, `--cpus 1.0`, and read-only host mounts. The local subprocess mode is strictly an internal development smoke-tester and explicitly disclaimed in the manuscript.

### 5.2 Dual Validity & Detection Metrics
1. **Test-Case Slicing:** Generated suites are decomposed into individual test cases $\{t_1, \dots, t_k\}$.
2. **Reference Validation:** Each test case is executed on $C_{\text{ref}}$.
   $$T_{\text{valid}} = \{ t_j \in T_{\text{gen}} \mid \text{Execute}(C_{\text{ref}}, t_j) == \text{PASSED} \}$$
3. **Reporting Granularities:**
   - **Test-Case Validity Rate:** $\frac{|T_{\text{valid}}|}{|T_{\text{gen}}|}$.
   - **Strict Suite Validity:** $|T_{\text{valid}}| == |T_{\text{gen}}|$.
   - **Usable Suite Validity:** $|T_{\text{valid}}| \ge 1$.
4. **Detection Definitions:**
   - **Primary Metric (Strict Defect Detection):** $|T_{\text{valid}}| \ge 1 \land \text{Execute}(C_{\text{faulty}}, T_{\text{valid}}) \in \{\text{FAIL}, \text{EXCEPTION}, \text{TIMEOUT}\}$.
   - **Secondary Metric (Fault Triggering Rate):** Execution on $C_{\text{faulty}}$ fails regardless of $C_{\text{ref}}$ validity status.

---

## 6. Statistical Analysis Plan

### 6.1 Paired Nominal Comparisons (RQ1 & RQ2)
- **McNemar's Test** with Edwards continuity correction (or Exact Binomial Test when discordant pairs $b + c < 25$).
- **Odds Ratio (OR)** with 95% Wald Confidence Intervals.

### 6.2 Independent Equivalence Testing (TOST for RQ2)
- **Methodological Principle:** Statistical equivalence is **NEVER** inferred from a non-significant difference test ($p \ge 0.05$ in McNemar). A non-significant McNemar test indicates only an absence of evidence of difference.
- **Two One-Sided Tests (TOST):** Equivalence is tested independently using TOST on paired proportions (Nam 1997, Tango 1998):
  $$H_{01}: p_A - p_B \le -\Delta \quad \text{vs.} \quad H_{11}: p_A - p_B > -\Delta$$
  $$H_{02}: p_A - p_B \ge +\Delta \quad \text{vs.} \quad H_{12}: p_A - p_B < +\Delta$$
- Equivalence is demonstrated **if and only if both one-sided tests reject their respective null hypotheses** at significance level $\alpha = 0.05$ ($p_{\text{TOST}} = \max(p_1, p_2) < 0.05$), which corresponds to the $(1 - 2\alpha) \times 100\% = 90\%$ confidence interval falling entirely within $(-\Delta, +\Delta)$.

### 6.3 Sample Size, Power & Equivalence Margin Justification
- **Power vs. Margin Trade-off:**
  - For paired binary data with expected discordant rate $b + c \approx 25\%$, the sample size required to achieve $80\%$ power at $\alpha = 0.05$ to prove equivalence within $\pm \Delta$ is:
    $$N \approx \frac{(z_{1-\alpha} + z_{1-\beta})^2 \cdot (p_{\text{discordant}})}{\Delta^2} = \frac{(1.645 + 0.842)^2 \cdot 0.25}{\Delta^2} \approx \frac{1.545}{\Delta^2}$$
  - For $\Delta = \pm 0.05$ ($\pm 5$ percentage points): $N \approx \frac{1.545}{0.0025} \approx 618$ pairs. Proving equivalence at $\pm 5\%$ with $N = 200–250$ is heavily underpowered ($\approx 42\%$).
  - For $\Delta = \pm 0.08$ ($\pm 8$ percentage points): $N \approx \frac{1.545}{0.0064} \approx 241$ pairs.
- **Pre-Registered Equivalence Bound Decision:**
  - **Primary Equivalence Margin:** $\Delta = \pm 0.08$ ($\pm 8$ percentage points). Justified because $N \approx 200–250$ provides $\ge 80\%$ power, and empirical variance across LLM sampling runs routinely falls within $5–10\%$.
  - **Secondary Strict Threshold:** $\Delta = \pm 0.05$ reported transparently as sensitivity analysis, acknowledging that if $N \approx 250$, results for $\pm 0.05$ may be statistically inconclusive. If neither difference nor equivalence is proven, the paper will conservatively report: *"The data show no statistically significant difference, but sample size is insufficient to confirm equivalence within a strict $\pm 5\%$ band."*

### 6.4 Factorial Interaction Model (RQ3)
- **Generalized Linear Mixed Model (GLMM / Mixed Logistic Regression):**
  $$\text{logit}(P(\text{Detect}_{ijk})) = \beta_0 + \beta_1 \cdot \text{Exposure}_j + \beta_2 \cdot \text{Family}_k + \beta_3 \cdot (\text{Exposure}_j \times \text{Family}_k) + \beta_4 \cdot \text{CoderModel}_i + u_i$$
  where $u_i \sim \mathcal{N}(0, \sigma_u^2)$ is the problem-level random intercept.

---

## 7. Third-Party Pre-Registration & Cryptographic Notarization

To eliminate post-hoc researcher degrees of freedom and ensure tamper-evident pre-registration:
1. **Local Git Notarization:** All protocol files and scripts committed to Git repository (`git log` history).
2. **GitHub Repository:** Pushed to a private repository prior to launching data collection.
3. **Independent Third-Party Notary:**
   - The frozen repository commit is registered on **Open Science Framework (OSF Preregistration)** (`https://osf.io/prereg/`) or published as an immutable GitHub Release archived on **Zenodo** (`https://zenodo.org`) to generate a persistent Digital Object Identifier (DOI).
   - This provides verifiable cryptographic proof that research questions, equivalence margins ($\Delta = \pm 0.08$), and fault selection heuristics were locked prior to observing experimental results.

---

## 8. Pilot Feasibility Gate (Go / No-Go Criteria)

Before running the full $N \approx 200–250$ benchmark:
1. **Pilot Size:** 5 tasks ($N_{\text{pilot}} = 30$ evaluations across conditions).
2. **Fault Harvest Yield:** At least 20 distinct $C_{\text{faulty}}$ instances successfully isolated.
3. **Oracle Validity Threshold:** Test-case validity rate $\ge 70\%$ on $C_{\text{ref}}$.
4. **Execution Stability:** Docker sandbox timeout / crash rate $< 5\%$.
5. **Economic Feasibility:** Projected cost within budget.

---

## 9. Threats to Validity

1. **Construct Validity (Data Leakage & AI Authorship):** Mitigated by the 4-stage screening protocol. The potential presence of unlabeled AI-generated code on GitHub in 2025/2026 is acknowledged as an unavoidable contemporary construct threat.
2. **External Validity (Model Age as a Methodological Limitation):**  
   The decision to use frozen 2023/2024 open-weight checkpoints (Llama 3.3, DeepSeek-V3, Qwen 2.5 Coder) is an explicit trade-off to eliminate commercial API deprecation carousel risks and guarantee permanent replicability. We explicitly document this limitation: findings demonstrate structural code-first bias in stable open architectures, but cannot be assumed to generalize automatically to newer proprietary frontier systems without subsequent replication.
3. **Internal Validity (Oracle Ambiguity & Selection Bias):** Controlled via pre-registered Blinded Fault Audit and reporting both First-Pass and Hardest-Fault selection heuristics.

---

## 10. Foundational Literature & Replication Packages
- Michael Konstantinou, Florian Tambon, Mike Papadakis. *"On the risk of coding before testing: An empirical study on LLM-based test generation workflow"*, SnT Luxembourg, arXiv:2607.05139 (2026).
- Noah Leu, Julian Oertel, Regina Hebig. *"Don't Bother to Use a Second LLM and Write Tests Yourself! A Study on Elixir"*, ESEM 2026, LIPIcs Vol. 394. Replication Package: Zenodo DOI: `10.5281/zenodo.20157738`.
- J. Nam. *"Establishing equivalence of two paired proportions with application to clinical trials"*, Statistics in Medicine, 16(4):411–417, 1997.
- T. Tango. *"Equivalence test and confidence interval for the difference in proportions for the paired-sample design"*, Statistics in Medicine, 17(8):891–908, 1998.
