# Conditioning model with measurement error on `ha`.
#
# The published model treats every count as exact. The 2026-07-27 audit shows
# that is false for `ha`: hand-coding the tagged concordance for all twenty
# sections puts the share of tagged tokens that are genuine interjections
# between 34.5% and 84.0%, and the shortfall is regionally patterned (hectare in
# East Africa and South Asia, personal names in Singapore). A point-estimate
# correction would understate the uncertainty, so the validity rate enters as a
# beta posterior per country and is propagated by refitting over draws.
#
# Two questions:
#   1. Does the country random effect survive correcting `ha`?
#   2. Does the model comparison (m1 over m0) survive it?
#
# Note the audit measures precision only. Tokens the tagger missed are not
# recoverable from a tagged concordance, so this corrects false positives and
# not false negatives.

library(brms)
library(dplyr)
library(tidyr)
library(loo)

set.seed(2026)
here <- function(...) file.path("..", ...)

raw <- read.csv(here("data", "glowbe-raw-counts.csv"), check.names = FALSE)
validity <- read.csv(here("data", "ha-validity-rates.csv"))

corpus_sizes <- tibble(
  country = c("US","CA","GB","IE","AU","NZ","IN","LK","PK","BD",
              "SG","MY","PH","HK","ZA","NG","GH","KE","TZ","JM"),
  words_m = c(386.8, 134.8, 387.6, 101.0, 148.2, 81.4, 96.4, 46.6,
              51.4, 39.5, 43.0, 41.6, 43.2, 40.5, 45.4, 42.6, 38.8,
              41.1, 35.2, 39.6)
)

long <- raw %>%
  pivot_longer(cols = -c(item, tag), names_to = "country", values_to = "count") %>%
  left_join(corpus_sizes, by = "country") %>%
  mutate(offset = log(words_m))

# One replicate: draw each country's validity rate from Beta(k+1, n-k+1),
# thin `ha`'s count by it, leave every other item untouched.
make_replicate <- function(spec) {
  if (spec == "uncorrected") return(long)
  k <- if (spec == "laughter_in") validity$k_laughter_in else validity$k_laughter_out
  p <- rbeta(nrow(validity), k + 1, validity$n_coded - k + 1)
  draw <- tibble(country = validity$country, rate = p)
  long %>%
    left_join(draw, by = "country") %>%
    mutate(count = if_else(item == "ha", as.integer(round(count * rate)), count)) %>%
    select(-rate)
}

fit_pair <- function(d) {
  m0 <- brm(count ~ 1 + offset(offset) + (1 | item), data = d,
            family = negbinomial(), chains = 2, cores = 2, iter = 1500,
            warmup = 750, seed = 2026, save_pars = save_pars(all = TRUE),
            silent = 2, refresh = 0)
  m1 <- brm(count ~ 1 + offset(offset) + (1 | item) + (1 | country), data = d,
            family = negbinomial(), chains = 2, cores = 2, iter = 1500,
            warmup = 750, seed = 2026, save_pars = save_pars(all = TRUE),
            silent = 2, refresh = 0)
  l0 <- loo(m0); l1 <- loo(m1)
  # Compute the difference directly rather than from loo_compare's row order,
  # which is sorted by fit and so cannot be indexed positionally with a fixed
  # sign. Positive means the country model predicts better.
  d_point <- l1$pointwise[, "elpd_loo"] - l0$pointwise[, "elpd_loo"]
  adv <- sum(d_point)
  se  <- sqrt(length(d_point)) * sd(d_point)
  sd_country <- as.data.frame(m1)[["sd_country__Intercept"]]
  list(elpd_diff = adv, se_diff = se,
       sd_med = median(sd_country),
       sd_lo = quantile(sd_country, .025), sd_hi = quantile(sd_country, .975))
}

R <- as.integer(Sys.getenv("REPLICATES", "8"))
out <- list()
for (spec in c("uncorrected", "laughter_in", "laughter_out")) {
  for (r in seq_len(R)) {
    res <- fit_pair(make_replicate(spec))
    out[[length(out) + 1]] <- tibble(spec = spec, rep = r,
      elpd_diff = res$elpd_diff, se_diff = res$se_diff,
      sd_med = res$sd_med, sd_lo = res$sd_lo, sd_hi = res$sd_hi)
    cat(sprintf("  %s rep %d: dELPD %.1f (SE %.1f), country SD %.2f [%.2f, %.2f]\n",
                spec, r, res$elpd_diff, res$se_diff, res$sd_med, res$sd_lo, res$sd_hi))
  }
}
res <- bind_rows(out)
write.csv(res, here("analysis", "ha-measurement-error-results.csv"), row.names = FALSE)

cat("\n=== Across replicates ===\n")
res %>%
  group_by(spec) %>%
  summarise(elpd = mean(elpd_diff), elpd_sd = sd(elpd_diff),
            se = mean(se_diff), sd_country = mean(sd_med),
            sd_lo = mean(sd_lo), sd_hi = mean(sd_hi), .groups = "drop") %>%
  as.data.frame() %>%
  print()
