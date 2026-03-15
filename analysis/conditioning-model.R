# conditioning-model.R
# Multilevel model testing whether geographic conditioning recovers
# structure in interjection frequency (HPC Prediction P5).
#
# Data: GloWbE corpus (Davies & Fuchs 2015), 1.9 billion words, 20 countries.
# Model: Bayesian negative binomial with crossed random effects for
#         item and country, plus an item-type fixed effect.

library(brms)
library(dplyr)
library(tidyr)
library(readr)
library(ggplot2)

# --- Data ---

raw <- read_csv(here::here("data", "glowbe-raw-counts.csv"))

# GloWbE subcorpus sizes (millions of words)
corpus_sizes <- tibble(
  country = c("US","CA","GB","IE","AU","NZ","IN","LK","PK","BD",
              "SG","MY","PH","HK","ZA","NG","GH","KE","TZ","JM"),
  words_m = c(386.8, 134.8, 387.6, 101.0, 148.2, 81.4, 96.4, 46.6,
              51.4, 39.5, 43.0, 41.6, 43.2, 40.5, 45.4, 42.6, 38.8,
              41.1, 35.2, 39.6)
)

# Reshape to long format
d <- raw %>%
  pivot_longer(cols = -c(item, tag), names_to = "country", values_to = "count") %>%
  left_join(corpus_sizes, by = "country") %>%
  mutate(
    offset = log(words_m),
    item_type = case_when(
      item %in% c("lah", "yaar", "haba") ~ "regional",
      item %in% c("um", "uh") ~ "filler",
      item %in% c("bye", "cheers") ~ "boundary",
      item %in% c("eh") ~ "semi-regional",
      TRUE ~ "core"
    ),
    item_type = factor(item_type,
      levels = c("core", "semi-regional", "boundary", "filler", "regional"))
  )

# --- Descriptive statistics ---

cv_table <- d %>%
  mutate(per_mil = count / words_m) %>%
  group_by(item, item_type) %>%
  summarise(
    mean_pm = mean(per_mil),
    sd_pm = sd(per_mil),
    cv = sd_pm / mean_pm,
    max_pm = max(per_mil),
    min_pm = min(per_mil),
    max_country = country[which.max(per_mil)],
    min_country = country[which.min(per_mil)],
    ratio = max_pm / max(min_pm, 0.01),  # avoid division by zero
    .groups = "drop"
  ) %>%
  arrange(desc(cv))

cat("\n=== Coefficient of Variation by Item ===\n")
print(cv_table %>% select(item, item_type, cv, max_country, max_pm, min_country, min_pm, ratio), n = 20)

# --- Model 1: Unconditional (pooled) ---
# Negative binomial with only item random effects (no country structure)

cat("\n=== Fitting unconditional model (item only) ===\n")
m0 <- brm(
  count ~ 1 + offset(offset) + (1 | item),
  data = d,
  family = negbinomial(),
  chains = 4, cores = 4, iter = 2000, warmup = 1000,
  seed = 2026,
  silent = 2
)

# --- Model 2: Conditioned (item + country) ---
# Crossed random effects: item varies across countries, countries vary
# across items. This is the "conditioning recovers structure" model.

cat("\n=== Fitting conditioned model (item + country) ===\n")
m1 <- brm(
  count ~ 1 + offset(offset) + (1 | item) + (1 | country),
  data = d,
  family = negbinomial(),
  chains = 4, cores = 4, iter = 2000, warmup = 1000,
  seed = 2026,
  silent = 2
)

# --- Model 3: Conditioned with item-type fixed effect ---
# Does knowing the item type (core/regional/filler/boundary) help?

cat("\n=== Fitting item-type model ===\n")
m2 <- brm(
  count ~ 1 + item_type + offset(offset) + (1 | item) + (1 | country),
  data = d,
  family = negbinomial(),
  chains = 4, cores = 4, iter = 2000, warmup = 1000,
  seed = 2026,
  silent = 2
)

# --- Model 4: Full crossed random slopes ---
# Item-by-country interaction: each item has its own country profile

cat("\n=== Fitting full crossed model (random slopes) ===\n")
m3 <- brm(
  count ~ 1 + offset(offset) + (1 | item) + (1 + item_type | country),
  data = d,
  family = negbinomial(),
  chains = 4, cores = 4, iter = 2000, warmup = 1000,
  seed = 2026,
  silent = 2
)

# --- Model comparison ---

cat("\n=== LOO comparison ===\n")
loo0 <- loo(m0)
loo1 <- loo(m1)
loo2 <- loo(m2)
loo3 <- loo(m3)
comp <- loo_compare(loo0, loo1, loo2, loo3)
print(comp)

# --- Random effects: country-level variance ---

cat("\n=== Country random effect (SD) ===\n")
cat("This is the key number: how much does knowing the country help?\n")
cat("If SD ≈ 0, conditioning adds nothing (P5 defeated).\n")
cat("If SD >> 0, conditioning recovers structure (P5 supported).\n\n")
print(summary(m1)$random$country)

cat("\n=== Item random effect (SD) ===\n")
print(summary(m1)$random$item)

# --- Save results ---

save(m0, m1, m2, m3, comp, cv_table, d,
     file = here::here("analysis", "conditioning-results.RData"))

cat("\n=== Done. Results saved to analysis/conditioning-results.RData ===\n")

# --- Quick plot ---

p <- d %>%
  mutate(per_mil = count / words_m) %>%
  ggplot(aes(x = reorder(country, per_mil), y = per_mil)) +
  geom_point(alpha = 0.4) +
  stat_summary(fun = median, geom = "point", colour = "red", size = 2) +
  facet_wrap(~ item, scales = "free_y", ncol = 4) +
  coord_flip() +
  labs(x = NULL, y = "Frequency per million words",
       title = "Interjection frequency by country (GloWbE)",
       subtitle = "Red = median across items") +
  theme_minimal(base_size = 10)

ggsave(here::here("analysis", "country-variation.pdf"), p,
       width = 12, height = 10)

cat("Plot saved to analysis/country-variation.pdf\n")
