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
  *Pre-registered Hypothesis:* Replicate Konstantinou et al.; $P(\text{Detect} \mid T_0) > P(\text{Detect} \mid T_1)$.

- **RQ2 (Primary Inquiry - Cross-Family Model Diversity):**  
  Holding code exposure constant, does employing a model from a distinct architectural family significantly alter fault detection ($T_1$ vs. $T_2$ under code exposure, and $T_0$ vs. $T_3$ under spec-only)?  
  *Pre-registered Hypothesis ($H_0^{(2)}$):* Holding white-box exposure constant, cross-family models will not demonstrate a statistically significant or practically meaningful difference beyond equivalence bounds.

- **RQ3 (Factorial Interaction):**  
  Is there a statistically significant interaction between Code Exposure and Model Family? Does cross-family diversity provide recovery specifically when code is visible, or is the code-first masking effect model-invariant?

- **RQ4 (Fault Taxonomy & Economic Trade-offs):**  
  Which categories of programming defects (e.g., boundary inversion, off-by-one, None-handling, state mutation) systematically evade test oracles across conditions? What is the token cost per detected defect across intra-model vs. cross-model strategies?

---

## 3. Experimental Design (2×2 Factorial Crossover)

| Exposure \ Model Identity | Same Model (Coder) | Cross-Family Model |
| :--- | :---: | :---: |
| **Specification Only** (Docstring + Signature) | **$T_0$** | **$T_3$** |
| **Code-First Exposure** (Docstring + Faulty Code) | **$T_1$** | **$T_2$** |

### 3.1 Model Selection: Frozen Open-Weight Checkpoints
To eliminate commercial API deprecation carousel risks (such as the shutdown of commercial API snapshots) and guarantee permanent scientific reproducibility, the study utilizes frozen **Open-Weight Models** with immutable cryptographic weight hashes:
1. **Llama Family (Meta AI):** `meta-llama/Llama-3.3-70B-Instruct` (Cutoff: December 2023).
2. **DeepSeek Family (DeepSeek):** `deepseek-ai/DeepSeek-V3` (Release: December 2024; Cutoff bound: Dec 2024).
3. **Qwen Family (Alibaba):** `Qwen/Qwen2.5-Coder-32B-Instruct` (Release: November 2024; Cutoff bound: Nov 2024).

Models are evaluated in symmetric reciprocal crossover ($A \leftrightarrow B$):
- Direction 1: Model A = Coder; Intra = Model A, Cross = Model B.
- Direction 2: Model B = Coder; Intra = Model B, Cross = Model A.

### 3.2 Operational Differentiation in Condition $T_1$
In Konstantinou et al., the code-first exposure was implemented within a multi-turn conversation session ("Agentic" exposure). In our protocol, $T_1$ provides specification + implementation in an explicit single-turn prompt. This design is necessary because cross-model condition $T_2$ cannot share internal multi-turn conversation sessions across heterogeneous model APIs. Disclosing this operational design ensures clarity in cross-study comparisons.

---

## 4. Materials, Fault Harvesting, and Contamination Control

### 4.1 Temporal Cutoff & Candidate Window
- Conservative Upper Bound: The latest model release date is December 2024 (DeepSeek-V3 / Llama 3.3).
- **Temporal Filter Boundary:** Commits must be strictly dated on or after **June 1, 2025** (6 months after December 2024).
- **Candidate Evaluation Window:** June 1, 2025 to November 1, 2026 (~17 months of open-source Python commits).

### 4.2 4-Stage Contamination Screening Protocol
1. **Timestamp Verification:** Commit timestamp verified via `git log --format="%ci"` to be $\ge$ June 1, 2025.
2. **Net-New Body Provenance (`git log -L`):** The entire function body must be a net-new addition introduced in that commit, rejecting legacy library patches.
3. **Pre-2024 Clone & Derivation Screening:** Syntactic and semantic cross-referencing against pre-2024 repositories to eliminate refactored legacy clones.
4. **AI-Authorship Exclusion:** Audit of commits, PRs, and comments for AI co-authorship markers (`Copilot`, `cursor`, `devin`, `Generated by`). Discard any candidate suspected of non-human origination. (Note: The absence of AI markers is recorded as a construct validity limitation, not absolute proof of human provenance).
5. **Standalone Functional Purity:** Functions rely solely on Python standard library modules (`math`, `re`, `json`, `collections`), rejecting complex framework state or mocks.

### 4.3 Fault Harvesting Protocol (Alignment with Konstantinou et al.)
1. The Coder model generates 10 candidate implementations per task at temperature $T = 0.8$.
2. Each candidate is executed against the reference test suite ($T_{\text{ref}}$).
3. **Inclusion Criterion:** A candidate implementation is classified as a valid faulty implementation ($C_{\text{faulty}}$) if and only if it fails $\ge 1$ reference test and $\le 50\%$ of reference tests. Candidates failing $> 50\%$ or suffering from total syntax crashes are discarded as trivial non-viable implementations.
4. **Fault Selection Heuristic:** To control for selection bias, the evaluation reports:
   - Primary: The first-harvested valid fault per task.
   - Secondary (Sensitivity Analysis): The hardest-to-detect fault per task (matching Konstantinou's selection heuristic).

### 4.4 Pre-Registered Blinded Fault Audit
Every harvested $C_{\text{faulty}}$ is audited manually:
- The auditor inspects only: (1) `docstring` + `signature`, (2) $C_{\text{faulty}}$ code, and (3) failing assertion from $T_{\text{ref}}$.
- The inclusion/exclusion decision in `fault_audit.json` is **finalized before running conditions $T_0, T_1, T_2, T_3$**, preventing confirmation bias.

---

## 5. Execution Sandbox & Oracle Validity

### 5.1 Docker Sandbox Standard
All benchmark executions reported in the study are performed strictly within a **Docker container with `--network none`**, `--memory 512m`, `--cpus 1.0`, and read-only host mounts. The local subprocess mode is strictly an internal development smoke-tester and explicitly disclaimed in the manuscript.

### 5.2 Dual Validity & Detection Metrics
To maintain comparability with both strict suite-level and relaxed assertion-level studies:
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

1. **Paired Nominal Comparisons (RQ1 & RQ2):**
   - **McNemar's Test** with continuity correction (or Exact Binomial Test when discordant pairs $b + c < 25$).
   - **Odds Ratio (OR)** with 95% Wald Confidence Intervals.
2. **Equivalence Testing (TOST for RQ2):**
   - For comparisons where $H_0$ is not rejected ($p \ge 0.05$), we test for statistical equivalence using **Two One-Sided Tests (TOST)** on paired proportions with a pre-registered equivalence margin $\Delta = \pm 5\%$ percentage points ($\alpha = 0.05$).
3. **Factorial Interaction Model (RQ3):**
   - **Generalized Linear Mixed Model (GLMM / Mixed Logistic Regression):**
     $$\text{logit}(P) = \beta_0 + \beta_1 \cdot \text{Exposure} + \beta_2 \cdot \text{Family} + \beta_3 \cdot (\text{Exposure} \times \text{Family}) + \beta_4 \cdot \text{CoderModel} + (1 \mid \text{Problem}_i)$$
4. **Sample Size & Power Protocol:**
   - The target sample size $N \approx 200 - 250$ refers to **distinct verified faulty implementations ($C_{\text{faulty}}$)**.
   - In the feasibility pilot, empirical fault harvest yield is measured, followed by a Monte Carlo power simulation to establish the exact problem count needed for 80% statistical power at $\alpha = 0.05$ to detect a 10 percentage point effect.

---

## 7. Pilot Feasibility Gate & Pre-Registration

### Pre-Registered Go / No-Go Decision Criteria
1. **Fault Harvest Yield:** At least 20 distinct $C_{\text{faulty}}$ instances successfully isolated.
2. **Oracle Validity Threshold:** Test-case validity rate $\ge 70\%$ on $C_{\text{ref}}$.
3. **Execution Stability:** Docker sandbox timeout / crash rate $< 5\%$.
4. **Economic Feasibility:** Projected cost within budget.

---

## 8. Threats to Validity

1. **Construct Validity (Data Leakage & AI Authorship):** Mitigated by the 4-stage screening protocol. The potential presence of unlabeled AI-generated code on GitHub in 2025/2026 is acknowledged as an unavoidable contemporary construct threat.
2. **External Validity (Model Age as a Methodological Limitation):**  
   The decision to use frozen 2023/2024 open-weight checkpoints (Llama 3.3, DeepSeek-V3, Qwen 2.5 Coder) is an explicit trade-off to eliminate commercial API deprecation carousel risks and guarantee permanent replicability. We explicitly document this limitation: findings demonstrate structural code-first bias in stable open architectures, but cannot be assumed to generalize automatically to newer proprietary frontier systems without subsequent replication.
3. **Internal Validity (Oracle Ambiguity & Selection Bias):** Controlled via pre-registered Blinded Fault Audit and reporting both First-Pass and Hardest-Fault selection heuristics.

---

## 9. Foundational Literature & Replication Packages
- Michael Konstantinou, Florian Tambon, Mike Papadakis. *"On the risk of coding before testing: An empirical study on LLM-based test generation workflow"*, SnT Luxembourg, arXiv:2607.05139 (2026).
- Noah Leu, Julian Oertel, Regina Hebig. *"Don't Bother to Use a Second LLM and Write Tests Yourself! A Study on Elixir"*, ESEM 2026, LIPIcs Vol. 394. Replication Package: Zenodo DOI: `10.5281/zenodo.20157738`.
- Huang et al. *"Bias and Oracle Decay in LLM-Assisted Code Generation"*, ICSE 2026, arXiv:2409.09464.
- Konstantinou et al. arXiv:2410.21136 and arXiv:2601.09695.
