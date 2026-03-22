# fie-confirmatory-model.R
# Pre-registered Bayesian logistic decline for fie in COHA.
# Follows fie-coha-preregistration.md exactly.

library(brms)
library(dplyr)
library(readr)
library(ggplot2)
library(loo)

# --- Load and merge data ---

coding <- read_csv(here::here("analysis", "fie-coding-sheet-annotated.csv"),
                   show_col_types = FALSE)
decade_key <- read_csv(here::here("analysis", "fie-decade-key.csv"),
                       show_col_types = FALSE)

d <- coding %>%
  left_join(decade_key, by = "coding_id") %>%
  mutate(
    syn = as.integer(human_syn),
    sem = as.integer(human_sem),
    intj = as.integer(human_int)
  ) %>%
  filter(!is.na(syn))  # should be 616

cat(sprintf("Total coded tokens: %d\n", nrow(d)))

# --- Descriptive statistics (reported before modelling per prereg) ---

decade_summary <- d %>%
  group_by(decade) %>%
  summarise(
    n = n(),
    syn_prop = mean(syn),
    sem_prop = mean(sem),
    int_prop = mean(intj),
    .groups = "drop"
  )

cat("\n=== Per-decade counts and proportions ===\n")
print(decade_summary, n = 25)

# Jeffreys intervals for proportions
jeffreys_ci <- function(k, n, alpha = 0.05) {
  lo <- qbeta(alpha / 2, k + 0.5, n - k + 0.5)
  hi <- qbeta(1 - alpha / 2, k + 0.5, n - k + 0.5)
  c(lo, hi)
}

decade_detail <- d %>%
  group_by(decade) %>%
  summarise(
    n = n(),
    syn_k = sum(syn), sem_k = sum(sem), int_k = sum(intj),
    .groups = "drop"
  ) %>%
  rowwise() %>%
  mutate(
    syn_lo = jeffreys_ci(syn_k, n)[1],
    syn_hi = jeffreys_ci(syn_k, n)[2],
    sem_lo = jeffreys_ci(sem_k, n)[1],
    sem_hi = jeffreys_ci(sem_k, n)[2],
    int_lo = jeffreys_ci(int_k, n)[1],
    int_hi = jeffreys_ci(int_k, n)[2],
  ) %>%
  ungroup()

cat("\n=== Jeffreys 95% intervals ===\n")
print(decade_detail, n = 25)

# --- Raw proportion plots (before model, per prereg) ---

plot_data <- d %>%
  group_by(decade) %>%
  summarise(
    n = n(),
    syn = mean(syn), sem = mean(sem), int = mean(intj),
    .groups = "drop"
  ) %>%
  tidyr::pivot_longer(cols = c(syn, sem, int),
                      names_to = "property", values_to = "proportion") %>%
  mutate(property = factor(property,
    levels = c("int", "sem", "syn"),
    labels = c("interjection_int", "interjection_sem", "interjection_syn")))

p_raw <- ggplot(plot_data, aes(x = decade, y = proportion, colour = property)) +
  geom_point(size = 2) +
  geom_line() +
  scale_y_continuous(limits = c(0, 1), labels = scales::percent) +
  labs(x = "Decade", y = "Proportion coded 1",
       title = "Raw proportions of fie properties by decade (COHA)",
       colour = "Property") +
  theme_minimal(base_size = 12)

ggsave(here::here("analysis", "fie-raw-proportions.pdf"), p_raw,
       width = 10, height = 6)
cat("\nRaw proportion plot saved.\n")

# --- Aggregate to decade-level binomial counts ---

decade_bin <- d %>%
  group_by(decade) %>%
  summarise(
    n = n(),
    syn_k = sum(syn),
    sem_k = sum(sem),
    int_k = sum(intj),
    .groups = "drop"
  ) %>%
  mutate(
    t = (decade - mean(decade)) / 10  # centred and scaled in 10-year units
  )

# --- Confirmatory model: Bayesian logistic decline ---
# Per prereg: logit(theta) = alpha + beta * t, beta < 0

cat("\n=== Fitting confirmatory models ===\n")

fit_decline <- function(k_col, n_col, data, label) {
  cat(sprintf("Fitting %s...\n", label))

  formula <- bf(paste0(k_col, " | trials(", n_col, ") ~ t"))

  priors <- c(
    prior(normal(0, 1.5), class = "Intercept"),
    prior(normal(0, 0.5), class = "b", lb = NA, ub = 0)  # beta < 0
  )

  fit <- brm(
    formula,
    data = data,
    family = binomial(),
    prior = priors,
    chains = 4, cores = 4, iter = 4000, warmup = 2000,
    seed = 2026,
    silent = 2
  )

  fit
}

m_syn <- fit_decline("syn_k", "n", decade_bin, "interjection_syn")
m_sem <- fit_decline("sem_k", "n", decade_bin, "interjection_sem")
m_int <- fit_decline("int_k", "n", decade_bin, "interjection_int")

# --- Convergence diagnostics ---

cat("\n=== Convergence diagnostics ===\n")
for (label in c("syn", "sem", "int")) {
  m <- get(paste0("m_", label))
  s <- summary(m)
  cat(sprintf("\n%s:\n", label))
  print(s$fixed)
  cat(sprintf("  Max Rhat: %.4f\n", max(s$fixed$Rhat)))
  cat(sprintf("  Min Bulk ESS: %.0f\n", min(s$fixed$Bulk_ESS)))
  cat(sprintf("  Min Tail ESS: %.0f\n", min(s$fixed$Tail_ESS)))
}

# --- ED50: tau_p = -alpha / beta ---

cat("\n=== ED50 (tau) posterior distributions ===\n")

compute_tau <- function(fit, label) {
  posts <- as_draws_df(fit)
  alpha <- posts$b_Intercept
  beta <- posts$b_t

  # tau in centred/scaled units, convert back to calendar year
  mean_decade <- mean(decade_bin$decade)
  tau_scaled <- -alpha / beta
  tau_year <- mean_decade + tau_scaled * 10

  cat(sprintf("\n%s:\n", label))
  cat(sprintf("  tau median: %.0f\n", median(tau_year)))
  cat(sprintf("  tau 95%% CrI: [%.0f, %.0f]\n",
              quantile(tau_year, 0.025), quantile(tau_year, 0.975)))

  if (median(tau_year) < 1820) cat("  Note: tau < 1820 (before observed window)\n")
  if (median(tau_year) > 2019) cat("  Note: tau > 2019 (after observed window)\n")

  tau_year
}

tau_int <- compute_tau(m_int, "interjection_int")
tau_sem <- compute_tau(m_sem, "interjection_sem")
tau_syn <- compute_tau(m_syn, "interjection_syn")

# --- Primary confirmatory quantity ---

pr_ordered <- mean(tau_int < tau_sem & tau_sem < tau_syn)
cat(sprintf("\n=== PRIMARY RESULT ===\n"))
cat(sprintf("Pr(tau_int < tau_sem < tau_syn) = %.3f\n", pr_ordered))

# Interpretive label per prereg
if (pr_ordered > 0.75) {
  cat("Label: consistent with the predicted ordering\n")
} else if (pr_ordered > 0.25) {
  cat("Label: consistent but uninformative\n")
} else {
  cat("Label: inconsistent with the predicted ordering\n")
}

# --- All pairwise orderings ---

cat(sprintf("\nPr(tau_int < tau_sem) = %.3f\n", mean(tau_int < tau_sem)))
cat(sprintf("Pr(tau_sem < tau_syn) = %.3f\n", mean(tau_sem < tau_syn)))
cat(sprintf("Pr(tau_int < tau_syn) = %.3f\n", mean(tau_int < tau_syn)))

# --- Tau density plot ---

tau_df <- data.frame(
  tau = c(tau_int, tau_sem, tau_syn),
  property = rep(c("interjection_int", "interjection_sem", "interjection_syn"),
                 each = length(tau_int))
)

p_tau <- ggplot(tau_df, aes(x = tau, fill = property)) +
  geom_density(alpha = 0.4) +
  coord_cartesian(xlim = c(1700, 2200)) +
  labs(x = "ED50 (calendar year)", y = "Posterior density",
       title = "Posterior distributions of ED50 (tau) for each property",
       fill = "Property") +
  theme_minimal(base_size = 12)

ggsave(here::here("analysis", "fie-tau-posteriors.pdf"), p_tau,
       width = 10, height = 6)
cat("\nTau posterior plot saved.\n")

# --- Save results ---

save(m_syn, m_sem, m_int,
     tau_syn, tau_sem, tau_int,
     pr_ordered, decade_bin, decade_detail,
     file = here::here("analysis", "fie-confirmatory-results.RData"))

cat("\n=== Done. Results saved to analysis/fie-confirmatory-results.RData ===\n")
