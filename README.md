# Supplementary materials: English Interjections as a Homeostatic Property Cluster

Data and analysis code for Reynolds (in preparation), "English Interjections as a Homeostatic Property Cluster," submitted to *Journal of Historical Pragmatics*.

## Contents

- `data/glowbe-interjection-frequencies.csv` — Frequency per million words for 18 interjection items across 20 countries in GloWbE (Davies & Fuchs 2015)
- `data/glowbe-raw-counts.csv` — Raw counts and POS-tag information
- `analysis/conditioning-model.R` — Bayesian multilevel model (brms) testing whether geographic conditioning recovers structure in interjection frequency (HPC Prediction P5)

## The test

HPC theory predicts that apparent gradience at category boundaries decomposes under social conditioning (Prediction P5). If knowing the country of origin helps predict interjection frequency beyond what the item identity alone provides, the variation is structured, not noise.

The analysis fits four nested negative binomial models:

1. **Unconditional**: item random effects only
2. **Conditioned**: item + country random effects
3. **Item-type**: fixed effect for item type (core/regional/filler/boundary) + random effects
4. **Full crossed**: item + country random slopes by item type

Model comparison via LOO-CV determines whether conditioning on country improves prediction.

## Requirements

R 4.5+ with packages: `brms`, `tidyverse`, `here`, `loo`

## Running

```r
source("analysis/conditioning-model.R")
```

## License

CC-BY 4.0

## Citation

Reynolds, B. (in preparation). English interjections as a homeostatic property cluster. *Journal of Historical Pragmatics*.
