# Experimental Protocol: Replication & Extension Study

## Title
**Does a Second LLM Really Help? A 2×2 Factorial Replication and Cross-Family Extension on Code-First Test Generation Bias in Python**

---

## 1. Research Questions (RQs)

- **RQ1 (Replication of Code-First Bias):** Does test-generation fault detection decrease when the testing LLM is exposed to faulty implementation code compared to generating tests from the specification alone ($T_0$ vs. $T_1$)?
- **RQ2 (Primary Conflict - Cross-Model Effect):** Holding code-first exposure constant, does an LLM from a distinct architectural family improve fault detection compared to the model that wrote the code ($T_1$ vs. $T_2$)?
- **RQ3 (Factorial Interaction):** Is there a statistically significant interaction between model diversity (Intra vs. Cross) and code exposure (Spec-only vs. Code-first)? That is, does cross-family diversity provide benefits only under code exposure, or also under specification-only generation ($T_0, T_1, T_2, T_3$)?
- **RQ4 (Fault Taxonomy & Economic Cost):** What specific categories of faults (e.g., off-by-one, boundary inversion, implicit type coercion, mutable default state) systematically bypass the test oracles across each condition? What is the token and compute cost per detected fault across each strategy?

---

## 2. Experimental Design (2×2 Factorial)

The experiment follows a full $2 \times 2$ factorial within-subjects design across four conditions:

| Exposure \ Model Family | Same Model Family (Coder) | Distinct Cross-Family Model |
| :--- | :---: | :---: |
| **Specification Only** (Docstring + Signature only) | **$T_0$** | **$T_3$** |
| **Code-First Exposure** (Docstring + Faulty Code) | **$T_1$** | **$T_2$** |

### 2.1 Symmetric Cross-Over Role Swap (Disentangling Family vs Capability)
To guarantee that observed differences are driven by architectural/training diversity rather than one model simply being superior in capability, the evaluation employs a **symmetric reciprocal crossover**:
- **Pair Configuration (A ↔ B):**
  - **Direction 1:** Model A acts as Coder. Same-Model ($T_0, T_1$) = Model A; Cross-Model ($T_2, T_3$) = Model B.
  - **Direction 2:** Model B acts as Coder. Same-Model ($T_0, T_1$) = Model B; Cross-Model ($T_2, T_3$) = Model A.
- Results are reported both disaggregated by direction ($A \to B$ vs. $B \to A$) and aggregated in the GLMM with model capability as a fixed factor.

### 2.2 Statistical Hypotheses:
- **$H_0^{(1)}$ (RQ1):** $P(\text{Detect} \mid T_0) = P(\text{Detect} \mid T_1)$
- **$H_0^{(2)}$ (RQ2):** $P(\text{Detect} \mid T_1) = P(\text{Detect} \mid T_2)$
- **$H_0^{(3)}$ (RQ3):** $\text{logit}(P) = \beta_0 + \beta_1 \cdot \text{CodeExposure} + \beta_2 \cdot \text{ModelFamily} + \beta_3 \cdot (\text{Exposure} \times \text{Family}) + \beta_4 \cdot \text{CoderModel} + u_{\text{problem}}$, with $H_0: \beta_3 = 0$.

---

## 3. Materials & Operational Definitions

### 3.1 Problem Sampling & Anti-Contamination Protocol
- **Temporal Filter with Safety Margin:** Python functions are selected strictly from public open-source repositories with commit dates occurring **at least 6 months after the officially declared pre-training cutoffs** of all evaluated models.
- **Provenance Logging:** For every problem instance, the repository URL, commit hash, verified commit timestamp (via `git log`), author, and source file path are logged in `dataset_manifest.json`.
- **Reference Ground Truth:** Each problem must possess:
  1. An unambiguous natural-language specification (`docstring`).
  2. A typed function signature.
  3. A human-authored reference implementation ($C_{\text{ref}}$).
  4. An independent, comprehensive human-authored unit test suite ($T_{\text{ref}}$) that passes 100% on $C_{\text{ref}}$.

### 3.2 Faulty Code Generation & Inclusion Criteria
1. The **Coder Model** is prompted with the specification to produce candidate implementations.
2. Each candidate implementation ($C_{\text{cand}}$) is executed against $T_{\text{ref}}$.
3. An implementation is classified as **Faulty ($C_{\text{faulty}}$)** if and only if it fails at least one assertion or raises an unexpected exception under $T_{\text{ref}}$.
4. Sampling continues until the target quota of verified distinct faulty implementations is reached.

### 3.3 Unit of Oracle Validity (Test-Case Slicing vs. Suite Validity)
To prevent a single flaky assertion from invalidating an entire test suite while strictly guaranteeing that invalid tests never trigger false detections:
1. **Test-Case Decomposition:** Generated test suites are parsed into individual test cases $\{t_1, t_2, \dots, t_k\}$.
2. **Individual Validity Filtering:** Each test case $t_j$ is executed against $C_{\text{ref}}$.
   $$t_j \text{ is Valid} \iff \text{Execute}(C_{\text{ref}}, t_j) == \text{PASSED}$$
   The filtered valid suite is $T_{\text{valid}} = \{ t_j \in T_{\text{gen}} \mid t_j \text{ is Valid} \}$.
3. **Dual Reporting:**
   - **Test-Case Validity Rate:** $\frac{|T_{\text{valid}}|}{|T_{\text{gen}}|}$ (percentage of valid assertions).
   - **Strict Suite Validity:** True iff $|T_{\text{valid}}| == |T_{\text{gen}}|$ (100% pass on $C_{\text{ref}}$).
   - **Usable Suite Validity:** True iff $|T_{\text{valid}}| \ge 1$.
4. **Defect Detection Criterion:**
   If $|T_{\text{valid}}| = 0$, the suite is invalid and **NEVER** credited with defect detection.
   If $|T_{\text{valid}}| \ge 1$, $T_{\text{valid}}$ is executed against $C_{\text{faulty}}$.
   $$\text{Detects Fault} \iff \text{Execute}(C_{\text{faulty}}, T_{\text{valid}}) \in \{\text{FAILED\_ASSERTION}, \text{EXCEPTION}, \text{TIMEOUT}\}$$

---

## 4. Execution Sandbox & Security Isolation

- **Benchmark Execution Standard:** All experimental runs reported in the research paper are executed strictly within a **Docker container with `--network none`**, `--memory 512m`, `--cpus 1.0`, and read-only host mounts. Disabling network interfaces at the OS/container kernel level is the sole mechanism that prevents arbitrary socket access or uncontained subprocess calls (`os.system`, `subprocess`).
- **Development Smoke-Test Backend:** A lightweight local subprocess runner with temporary directories is provided exclusively for quick syntax checks and pipeline sanity testing during local debugging; it is explicitly disclaimed and never represented as a secure sandbox in the manuscript.

---

## 5. Statistical Analysis Plan

1. **Paired Nominal Comparisons (RQ1 & RQ2):**
   - **McNemar's Test** with continuity correction (or Exact Binomial Test on discordant pairs when $b + c < 25$).
   - **Odds Ratio (OR):** $\text{OR} = \frac{b}{c}$ with 95% Wald Confidence Intervals.
2. **Interaction & Full Model (RQ3):**
   - **Generalized Linear Mixed Model (GLMM / Mixed Logistic Regression):**
     $$\text{Detection}_{ij} \sim \text{Bernoulli}(p_{ij})$$
     $$\log\left(\frac{p_{ij}}{1 - p_{ij}}\right) = \beta_0 + \beta_1 \cdot \text{Exposure}_j + \beta_2 \cdot \text{Family}_j + \beta_3 \cdot (\text{Exposure} \times \text{Family})_j + \beta_4 \cdot \text{CoderModel}_j + (1 \mid \text{Problem}_i)$$
   - Random intercept $(1 \mid \text{Problem}_i)$ accounts for varying intrinsic difficulty across coding problems.
3. **No Cliff's Delta:** Binary outcomes (0/1) will not be analyzed using continuous or ordinal rank-effect statistics.

---

## 6. Pilot Study (Feasibility Gate & Pre-Registration)

### Objectives
- Validate the execution sandbox pipeline.
- Determine empirical error generation rates and token costs.
- Measure test-case and suite-level validity rates.

### Pre-Registered Go / No-Go Decision Criteria
Before inspecting comparative detection distributions:
1. **Fault Harvest Yield:** At least 20 distinct $C_{\text{faulty}}$ instances successfully isolated and verified.
2. **Oracle Validity Threshold:** Generated test suites achieve an individual test-case validity rate $\ge 70\%$ when executed on $C_{\text{ref}}$.
3. **Execution Stability:** Sandbox timeout / unhandled crash rate $< 5\%$.
4. **Economic Feasibility:** Projected cost for full benchmark ($N \ge 250$) within budget.

### 6.1 Blinded Fault Audit Protocol
To eliminate observer and confirmation bias:
- Every candidate faulty implementation ($C_{\text{faulty}}$) harvested by the Coder model is audited **blinded** to condition outcomes.
- The auditor inspects only: (1) `docstring` + `signature`, (2) $C_{\text{faulty}}$ code, and (3) the failing assertion log from $T_{\text{ref}}$.
- The auditor classifies the defect as `Genuine_Logic_Bug`, `Docstring_Ambiguity`, or `Unstated_Tref_Assumption`.
- The inclusion/exclusion decision in `fault_audit.json` must be **finalized and timestamped prior to executing the 2×2 test conditions** ($T_0, T_1, T_2, T_3$) on $C_{\text{faulty}}$. Any problem failing due to ambiguous specifications is discarded.

---

## 7. Threats to Validity

1. **Internal Validity (Oracle Ambiguity):** Mitigated by the manual fault audit protocol and test-case slicing.
2. **Construct Validity (Data Leakage):** Addressed by the commit-timestamp filter with a 6-month post-cutoff margin and git verification.
3. **External Validity (Scope):** Findings are scoped to standalone Python functional units. We explicitly document this scope boundary rather than overgeneralizing to repository-level multi-file refactorings.
