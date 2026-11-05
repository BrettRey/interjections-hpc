# Supplementary materials: What English Interjections Let Us Predict

Data and analysis code for Reynolds (in preparation), "What English Interjections Let Us Predict: Stable Causal-Pragmatic Clustering and Path Dependence," targeted to *Journal of Pragmatics*.

## Contents

- `data/glowbe-interjection-frequencies.csv` — Frequency per million words for 18 interjection items across 20 countries in GloWbE (Davies & Fuchs 2015)
- `data/glowbe-raw-counts.csv` — Raw counts and POS-tag information
- `analysis/conditioning-model.R` — Bayesian multilevel model (brms) testing whether geographic conditioning recovers structure in interjection frequency (HPC Prediction P5)

## The test

HPC theory predicts that apparent gradience at category boundaries decomposes under social conditioning (Prediction P5). If knowing the country of origin helps predict interjection frequency beyond what the item identity alone provides, the variation is structured, not noise.

The analysis fits three confirmatory negative binomial models plus one exploratory extension:

1. **Unconditional**: item random effects only
2. **Conditioned**: item + country random effects
3. **Item-type**: fixed effect for item type (core/semi-regional/boundary/filler/regional) + random effects
4. **Exploratory slopes**: country-specific varying slopes by item type

Primary model comparison uses PSIS-LOO with `reloo=TRUE` on the confirmatory models, so problematic observations are handled by exact refits rather than left to approximation. The exploratory slope model is only ranked if its PSIS diagnostics are acceptable; otherwise it is reported as diagnostic-only and should be compared with k-fold CV if needed.

## Requirements

R 4.5+ with packages: `brms`, `tidyverse`, `here`, `loo`

## Running

```r
source("analysis/conditioning-model.R")
```

## License

Brett Reynolds's original text, code, and data in this repository are
licensed under CC BY 4.0 (see `LICENSE`).

The licence does not cover material by others that is included as a
research record:

- quotations and excerpts from published sources, including the coding
  packets and prompts under `analysis/matrix-lesion/` (`pilot*/packets*`,
  `pilot*/prompt-*`), which remain under their owners' copyright;
- the editorial decision letter and referee reports in
  `notes/2026-07-23-jop-decision-letter-and-reviews.md`, which belong to
  their authors;
- any other quoted third-party text, reproduced for scholarly purposes
  only.

Third-party corpora (for example CABNC) are not included in the
repository.

## Citation

Reynolds, B. (in preparation). What English interjections let us predict: Stable causal-pragmatic clustering and path dependence.
