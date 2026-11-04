args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1L) stop("Usage: Rscript scripts/fit_interaction_glmm.R <results CSV>")
if (!requireNamespace("lme4", quietly = TRUE)) stop("The lme4 package is required.")
output_dir <- dirname(args[[1]])
attempts <- read.csv(args[[1]], stringsAsFactors = FALSE)
status <- if ("execution_status" %in% names(attempts)) attempts$execution_status else attempts$status
if (is.null(status)) status <- rep("SUCCESS", nrow(attempts))
rows <- attempts[status != "API_ERROR" & !is.na(status), ]
rows <- rows[!duplicated(paste(rows$trial_id, rows$condition)), ]
if (anyNA(rows$detected) || !all(rows$detected %in% c(0, 1))) stop("Invalid outcome.")

same_model <- attempts[attempts$condition %in% c("T0", "T1"), ]
coders <- unique(same_model[c("problem_id", "model_name")])
if (anyDuplicated(coders$problem_id)) stop("Conflicting coder models for the same problem.")
rows$coder <- factor(coders$model_name[match(rows$problem_id, coders$problem_id)])
if (anyNA(rows$coder)) stop("Missing coder model.")
if (!all(c("T0", "T1", "T2", "T3") %in% rows$condition)) stop("Missing condition.")
if (!all(c(0, 1) %in% rows$detected)) stop("No outcome variation.")
rows$exposure <- as.integer(rows$condition %in% c("T1", "T2"))
rows$cross_model <- as.integer(rows$condition %in% c("T2", "T3"))
formula <- if (nlevels(rows$coder) > 1L) {
    detected ~ exposure * cross_model + coder + (1 | problem_id)
} else {
    detected ~ exposure * cross_model + (1 | problem_id)
}
warnings_seen <- character()
capture_warning <- function(w) {
    warnings_seen <<- c(warnings_seen, conditionMessage(w))
    invokeRestart("muffleWarning")
}
control <- lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 200000))
fit <- withCallingHandlers(lme4::glmer(formula, data = rows, family = binomial(),
                                     nAGQ = 9, control = control), warning = capture_warning)
reduced <- withCallingHandlers(update(fit, . ~ . - exposure:cross_model), warning = capture_warning)
stability <- withCallingHandlers(update(fit, nAGQ = 15), warning = capture_warning)
tab <- coef(summary(fit))
terms <- data.frame(term = rownames(tab), coefficient = tab[, 1], standard_error = tab[, 2],
                    z = tab[, 3], p_value = tab[, 4], odds_ratio = exp(tab[, 1]),
                    odds_ratio_ci_lower = exp(tab[, 1] - qnorm(.975) * tab[, 2]),
                    odds_ratio_ci_upper = exp(tab[, 1] + qnorm(.975) * tab[, 2]),
                    row.names = NULL)
write.csv(terms, file.path(output_dir, "GLMM_COEFFICIENTS.csv"), row.names = FALSE)
lrt <- anova(reduced, fit, test = "Chisq")
diag <- data.frame(
    input_md5 = unname(tools::md5sum(args[[1]])),
    observations = nobs(fit), problems = length(unique(rows$problem_id)),
    singular = lme4::isSingular(fit),
    optimizer_code = paste(fit@optinfo$conv$opt, collapse = ","),
    convergence_messages = paste(fit@optinfo$conv$lme4$messages, collapse = "; "),
    warnings = paste(unique(warnings_seen), collapse = "; "),
    problem_intercept_sd = as.data.frame(lme4::VarCorr(fit))$sdcor[[1]],
    interaction_lrt_p = lrt[2, "Pr(>Chisq)"],
    max_coef_change_nagq15 = max(abs(lme4::fixef(fit) - lme4::fixef(stability))),
    R_version = R.version.string, lme4_version = as.character(packageVersion("lme4"))
)
write.csv(diag, file.path(output_dir, "GLMM_DIAGNOSTICS.csv"), row.names = FALSE)
saveRDS(fit, file.path(output_dir, "GLMM_MODEL.rds"))
capture.output({
    cat("Formula\n"); print(formula)
    print(summary(fit)); print(terms); print(diag)
    cat("Interaction likelihood-ratio test\n"); print(lrt)
    cat("Numerical stability at nAGQ=15\n"); print(lme4::fixef(stability))
    cat("Session\n"); print(sessionInfo())
}, file = file.path(output_dir, "GLMM_OUTPUT.txt"))
print(terms)
print(diag)

# Exploratory sensitivity using the 15 problems as independent units.
rates <- aggregate(detected ~ problem_id + condition, data = rows, FUN = mean)
wide <- reshape(rates, idvar = "problem_id", timevar = "condition", direction = "wide")
differences <- list(
    T0_minus_T1 = wide$detected.T0 - wide$detected.T1,
    T1_minus_T2 = wide$detected.T1 - wide$detected.T2,
    T3_minus_T2 = wide$detected.T3 - wide$detected.T2,
    probability_interaction = (wide$detected.T2 - wide$detected.T1) -
                              (wide$detected.T3 - wide$detected.T0)
)
sensitivity <- do.call(rbind, lapply(names(differences), function(name) {
    test <- t.test(differences[[name]])
    data.frame(contrast = name, mean_difference = unname(test$estimate),
               lower_95 = test$conf.int[[1]], upper_95 = test$conf.int[[2]],
               p_value = test$p.value, problems = length(differences[[name]]))
}))
write.csv(sensitivity, file.path(output_dir, "PROBLEM_LEVEL_SENSITIVITY.csv"), row.names = FALSE)

# Exploratory sensitivity allowing task-specific effects for both factors and interaction.
rows$exposure_cross <- rows$exposure * rows$cross_model
random_slope_formula <- update(formula, . ~ . - (1 | problem_id) +
    (1 + exposure + cross_model + exposure_cross || problem_id))
slope_warnings <- character()
slope_fit <- tryCatch(withCallingHandlers(
    lme4::glmer(random_slope_formula, data = rows, family = binomial(), nAGQ = 1,
                control = control),
    warning = function(w) {
        slope_warnings <<- c(slope_warnings, conditionMessage(w))
        invokeRestart("muffleWarning")
    }), error = function(e) e)
if (inherits(slope_fit, "error")) {
    writeLines(conditionMessage(slope_fit), file.path(output_dir, "GLMM_RANDOM_SLOPES_ERROR.txt"))
} else {
    slope_term <- coef(summary(slope_fit))["exposure:cross_model", ]
    slope_result <- data.frame(
        coefficient = slope_term[[1]], standard_error = slope_term[[2]],
        p_value = slope_term[[4]], odds_ratio = exp(slope_term[[1]]),
        lower_95_or = exp(slope_term[[1]] - qnorm(.975) * slope_term[[2]]),
        upper_95_or = exp(slope_term[[1]] + qnorm(.975) * slope_term[[2]]),
        singular = lme4::isSingular(slope_fit),
        convergence_messages = paste(slope_fit@optinfo$conv$lme4$messages, collapse = "; "),
        warnings = paste(unique(slope_warnings), collapse = "; ")
    )
    write.csv(slope_result, file.path(output_dir, "GLMM_RANDOM_SLOPES_SENSITIVITY.csv"), row.names = FALSE)
    capture.output(print(summary(slope_fit)), file = file.path(output_dir, "GLMM_RANDOM_SLOPES_OUTPUT.txt"))
}
