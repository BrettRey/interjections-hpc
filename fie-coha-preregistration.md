# Draft Preregistration: `fie` in COHA, 1820-2019

## Status and Scope

This is a preregistered analysis plan for an existing corpus, not a preregistration before data collection. The confirmatory commitments here concern extraction, coding, modeling, and reporting for one target item, `fie`, in COHA from 1820 to 2019.

The analysis is conditional on attested `fie` tokens. It is not a model of the overall frequency decline of `fie` in COHA, though raw token counts by decade will be reported.

## Research Question and Prediction

**Research question:** Within attested COHA tokens of `fie`, do the interactional, semantic, and syntactic properties associated with interjectionhood decline at different rates across time?

**Pre-committed prediction:** The properties should fray in the order interactional first, semantic second, syntactic last. In terms of ED50 parameters, the predicted ordering is:

```text
tau_int < tau_sem < tau_syn
```

where each `tau` is the calendar year at which the model-estimated probability of a property falls below 0.5.

## Data Source and Extraction

- Corpus: Corpus of Historical American English (COHA), 1820-2019.
- Target item: the orthographic token `fie`, matched case-insensitively as a standalone word.
- No variant pooling: forms such as `fye`, `fy`, `fieh`, or longer strings containing `fie` are excluded unless they are tokenized as the exact word `fie`.
- Unit of analysis: one attested token of `fie` in running text.
- Time bin: decade.
- Context for coding: the sentence containing the token, plus the immediately preceding and following sentence when available.

Duplicate hits created by export or query artifacts will be removed by document ID, year, and concordance context. Repeated uses of `fie` within the same document remain separate tokens.

## Go/No-Go Threshold

Before coding or modelling, the following minimum data requirement must be met:

- **Total analysable tokens:** at least 50
- **Decade coverage:** at least 3 decades with 3+ tokens each

If either threshold is not met, the study is reported as pre-registered but untested due to data sparsity. The prediction remains on the record. No modelling, no hand-waving, no exploratory substitution.

These thresholds are set before data extraction and will not be revised after inspecting token counts.

## Inclusion and Exclusion Rules

Included:

- Tokens of `fie` used in running English text, including dialogue and quoted speech.

Excluded:

- Metalinguistic mention rather than use, as in discussion of "the word `fie`"
- Dictionary headwords, glossaries, bibliographies, page headers, running heads, advertisements, and other metadata
- Non-English passages
- OCR noise or unreadable hits
- Hits with too little readable context to apply the coding rubric

All exclusions will be counted and reported.

## Coding Protocol

Each analyzable token will receive three binary codes, assigned independently:

| Property | Code `1` if... | Code `0` if... |
|---|---|---|
| `interjection_syn` | `fie` is syntactically non-integrated: it does not fill an argument, complement, or modifier slot in the surrounding clause, and its removal leaves no grammatical gap. Standalone uses and clause-peripheral exclamations count as `1`. | `fie` is syntactically integrated, metalinguistically quoted, or otherwise functions as part of ordinary clause structure. |
| `interjection_sem` | `fie` contributes expressive or evaluative stance without referential or truth-conditional lexical content. | `fie` refers to the word itself, contributes descriptive lexical content, or is unusable as an expressive token in context. |
| `interjection_int` | `fie` functions as an interactional move or stance display directed at the speech situation, addressee, or prior talk, such as exclamation, reproach, reaction, or turn-level stance marking. | `fie` does not function as an interactional move in context. |

Additional coding rules:

- The three properties are coded independently. A `1` on one property does not force a `1` on the others.
- For `interjection_int`, code the represented speech act, not the author's act of writing it. A character saying *fie* to another character in a novel counts as a live interactional move if it functions as stance display within the fictional dialogue.
- Coding will be done from a randomized coding sheet with the decade column hidden, so the coder is blind to time period during coding. Note: archaic syntax in concordance lines may partially reveal period; this is unavoidable but mitigated by randomisation.
- The full rubric and token-level coding sheet will be published in the supplement.

## Coding Reliability

Brett will complete a blind second-pass recode on a simple random 10% subset of analyzable tokens, rounded up to the next whole token. The subset will be sampled with random seed 2026 and presented in randomized order with original codes hidden.

This is an intra-coder stability check, not an external inter-coder validation. The following will be reported for each property:

- Percent agreement
- Cohen's kappa

If disagreement exceeds 20% on any property, that coding criterion will be flagged as underdetermined. The main analysis will still be reported under the preregistered rubric; the rubric will not be revised after inspecting disagreement patterns except to correct clerical errors.

## Descriptive Reporting Before Modeling

Before fitting any model, the paper will report:

- Total analyzable `N`
- Per-decade `N`
- Raw proportion per decade for each property
- 95% Jeffreys intervals for the decade-level proportions

The raw proportion plots come first, before any model-based estimates.

Decades with `N = 0` will be shown in the count table and count plot but will not enter the property model because there is no denominator for a property proportion.

## Confirmatory Statistical Model

For each property separately, let:

- `n_d` = number of analyzable `fie` tokens in decade `d`
- `y_pd` = number of those tokens coded `1` on property `p`

The confirmatory model is a Bayesian logistic decline fitted to decade-level binomial counts:

```text
y_pd ~ Binomial(n_d, theta_pd)
logit(theta_pd) = alpha_p + beta_p * t_d
beta_p < 0
```

where `t_d` is decade midpoint, centered and scaled in 10-year units.

The `beta_p < 0` constraint assumes monotone decline: `fie` can only lose properties over time, not rebound. This is a substantive assumption, not just regularisation. Both the confirmatory and sensitivity models are monotonic; neither can detect a revival period.

This simple logistic form is the confirmatory model for two reasons:

- it removes the researcher degree of freedom involved in choosing between a smoother and a simple decline
- it makes the ED50 parameter exact rather than interpolation-dependent

### Priors

- `alpha_p ~ Normal(0, 1.5)`
- `beta_p ~ Normal(0, 0.5)`, truncated to negative values

These are weakly regularizing priors on the log-odds scale. They allow shallow or steep decline but rule out implausibly erratic trajectories for a single item observed by decade.

### Estimation and Diagnostics

- 4 chains
- 2000 warmup iterations and 2000 post-warmup iterations per chain
- random seed: 2026

Convergence criteria:

- no divergent transitions
- `Rhat <= 1.01` for population parameters
- bulk ESS and tail ESS of at least 400 for population parameters

If the confirmatory model fails these diagnostics after standard tuning adjustments, that failure will be reported explicitly. It will not trigger a post hoc change in the confirmatory model.

## Confirmatory Estimand

For each posterior draw and each property, define:

```text
tau_p = -alpha_p / beta_p
```

and transform `tau_p` back to calendar year. This is the ED50: the year at which the model-estimated probability of the property equals 0.5.

If `tau_p < 1820`, it will be reported as "before 1820." If `tau_p > 2019`, it will be reported as "after 2019." These are not treated as failures of estimation; they mean the 0.5 crossing lies outside the observed window.

The primary confirmatory quantity is:

```text
Pr(tau_int < tau_sem < tau_syn)
```

This probability will be reported as a posterior quantity, not converted into a binary success/failure decision.

## Sensitivity Analysis

As a robustness check, I will also fit a Bayesian logistic model with decade treated as an ordered monotonic predictor rather than a linear slope. Because ED50 is not exact under this parameterisation, the sensitivity model will report the posterior distribution of the decade at which each property's predicted probability crosses 0.5, obtained by numerical interpolation of the fitted curve. The following will be reported:

- Posterior distributions of the interpolated crossing decades for each property
- `Pr(tau_int < tau_sem < tau_syn)` computed from the interpolated posteriors
- Visual comparison of the fitted curves with the confirmatory model

This sensitivity analysis will be reported regardless of outcome. It is not the confirmatory model, and it will not replace the confirmatory model on the basis of fit, sparsity, or substantive convenience.

## Sparse Data and Uninformative Results

No decade will be excluded because of low token count. If any decade has fewer than 5 tokens, it remains in the analysis.

If posterior intervals are wide or order probabilities are diffuse, that will be reported as an informative outcome rather than treated as a failed analysis. The primary result is always `Pr(tau_int < tau_sem < tau_syn)`. The following labels are informal glosses on that probability, not independent judgments:

- "consistent with the predicted ordering": `Pr(tau_int < tau_sem < tau_syn) > 0.75`
- "consistent but uninformative": `Pr(tau_int < tau_sem < tau_syn)` between 0.25 and 0.75
- "inconsistent with the predicted ordering": `Pr(tau_int < tau_sem < tau_syn) < 0.25`

## What Will Be Reported Regardless of Outcome

- Total analyzable `N`
- Per-decade `N`
- Exclusion counts by reason
- Raw proportions by decade with 95% Jeffreys intervals
- Posterior distributions of `tau_int`, `tau_sem`, and `tau_syn`
- `Pr(tau_int < tau_sem < tau_syn)`
- Convergence diagnostics
- Reliability statistics for all three coding variables

No post hoc threshold-based exclusion beyond the preregistered go/no-go rule, no post hoc model switching, and no selective reporting will be used.

## Archiving

The supplement will include:

- the full coding rubric
- the token-level dataset
- the reliability subset
- the analysis code used to fit the confirmatory and sensitivity models

## Coding Clarification: Multiple *fie* per Line

Some COHA concordance lines contain more than one *fie* token (e.g., "Fie! A fie upon each of you!"). The coding sheet has one row per concordance line, not per token. In such cases, code the **first** *fie* in the concordance context — this is the KWIC target that COHA centred the hit on.

## Coding Notes: Edge Cases Adjudicated with Extended Context

The following tokens required extended COHA context beyond the concordance line to code reliably. Full context and reasoning are recorded here for the supplement.

- **F362** (DrSevier, 1884): Narrator breaks fourth wall — "Shall we follow? Fie!" Addressed to reader as mock-reproach. Coded (1,1,1).
- **F450** (Bk:DropZone, 2016): "Tee fie!" — nonsense syllables, no interjection properties. Coded (0,0,0).
- **F522** (VelvetDoublet, 1953): "A fie on conscience!" — noun use with article. Coded (0,1,0).
- **F545** (AmWhigRev, 1849): "the subordination, that cries fie! continually to his pride of place" — political essay, fie as object of speech verb but retaining full interjection force in the represented speech act. Coded (1,1,1).
- **F568** (VelvetDoublet, 1953): "a fie for a Portuguese parvenu" — noun use. Coded (0,1,0).
- **F579** (Chicago, 1929): "Pee, fie, fo, furry" — fee-fi-fo-fum variant, garbled. Coded (1,0,0).
- **F597** (Play:AmIGoIllSaySo, 1923): Gertrude Stein — "shame shame fie for shame" embedded in phonological/rhythmic chain. Not an interjection; a sound unit in assonance pattern. Coded (0,0,0).
- **F604** (CopperStreakTrail, 1922): "Fie! A fie upon each of you!" — first fie is standalone exclamation. Coded (1,1,1).
