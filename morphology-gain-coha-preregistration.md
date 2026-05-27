# Preregistration: Morphology-Gain Perturbations in COHA

## Status and Scope

This is a preregistered analysis plan for an existing corpus, not a
preregistration before data collection. The confirmatory commitments here
concern extraction, coding, exclusion, and reporting for English
interjection-derived verbal forms in COHA.

Lock method: the git commit that first adds this file to the project
repository. No further COHA extraction, KWIC review, coding, or analysis
for these target forms will begin before that lock.

Before this plan was written, a small number of exploratory feasibility
queries were run for `wowed`, `booed`, `booing`, `oohed`, `oohing`,
`shooed`, `shooing`, and `wowing`. Those outputs may be reported only as
pilot/feasibility information. They will not be used as confirmatory
evidence, and no coding or model choice will be based on them. The target
forms below are fixed by the theoretical case set and by regular English
inflection, not by those exploratory results.

## Research Question and Prediction

**Research question:** When interjections gain verbal morphology, does
syntactic interjectionhood disappear before the source interjection's
semantic or interactional residue disappears?

**Pre-committed prediction:** Overtly inflected verbal derivatives should
show syntactic integration while retaining semantic residue from the
source interjection. In the causal-network account, verbal morphology
directly disrupts prosodic-syntactic coupling. It should therefore affect
interjection\_syn before interjection\_sem.

The predicted pattern is:

```text
verbal_syntax = 1
semantic_residue = 1
```

in the earliest analyzable derivative tokens for each source form. If
the earliest analyzable verbal tokens are syntactically integrated but
semantic residue is already absent, the morphology-gain perturbation does
not support the predicted ordering.

## Data Source and Target Forms

- Corpus: Corpus of Historical American English (COHA), 1820--2019.
- Unit of analysis: one KWIC token of a target form in running English
  text.
- Time variable: publication year, with decade used for summary plots.
- Target source interjections: `wow`, `boo`, `ooh`, `shoo`.
- Target verbal derivatives:
  - `wowed`, `wowing`, `wows`
  - `booed`, `booing`, `boos`
  - `oohed`, `oohing`, `oohs`
  - `shooed`, `shooing`, `shoos`

Bare source forms (`wow`, `boo`, `ooh`, `shoo`) are excluded from the
confirmatory dataset because they are ambiguous between interjectional
and verbal uses without overt morphology.

## Go/No-Go Threshold

Before coding, each source-form family will be assessed for data
availability.

For a source-form family to enter confirmatory analysis, it must have:

- at least 20 analyzable derivative tokens, and
- at least two decades with 3+ analyzable derivative tokens.

If fewer than two source-form families meet this threshold, the study
will be reported as preregistered but underpowered. The prediction will
remain on the record. No alternative target forms will be added after
inspecting counts.

## Inclusion and Exclusion Rules

Included:

- Tokens of target forms used in running English text.
- Dialogue, quoted speech, fiction, magazine, newspaper, and nonfiction
  tokens.
- Verbal uses with overt inflection, whether finite or non-finite.

Excluded:

- Metalinguistic mention, dictionary entries, word lists, bibliographies,
  tables, page headers, and other metadata.
- Noun uses, including plural nouns such as `boos` or `oohs` when they
  mean "instances of booing/oohing" rather than a verb.
- Adjectival or participial uses without recoverable verbal syntax, unless
  a verbal predicate is clear in context.
- OCR noise, duplicate export artifacts, and hits with too little readable
  context to code.
- Non-English passages.

Duplicate hits created by export/query artifacts will be removed by
document ID, year, source, and concordance context. Repeated target forms
within the same document remain separate tokens if they correspond to
separate KWIC hits.

## Coding Protocol

Each analyzable token will receive the following binary codes:

| Code | `1` if... | `0` if... |
|---|---|---|
| `verbal_syntax` | The token functions as a verb or verb form: it inflects, heads or belongs to a predicate, takes arguments or modifiers appropriate to verbal syntax, or appears in a progressive/perfect/passive construction. | The token is a noun, adjective, metalinguistic mention, interjection, or otherwise not syntactically verbal. |
| `semantic_residue` | The token preserves the source interjection's meaning profile: impressed/evaluative response for `wow`; disapproval or contempt for `boo`; appreciative/surprised response for `ooh`; directive away-sending for `shoo`. | The token has lost the source interjection's semantic profile or the meaning cannot be recovered. |
| `interactional_residue` | The token represents an interactional act or socially recognizable response, including collective audience response, directed disapproval, admiration, appreciative uptake, or directive action toward an addressee. | The token is purely descriptive, lexicalized, or otherwise lacks recoverable interactional force. |
| `targeted_entity` | The token has a recoverable target, object, addressee, or stimulus. | No target/stimulus is recoverable. |

The confirmatory outcome uses `verbal_syntax` and `semantic_residue`.
`interactional_residue` and `targeted_entity` are secondary descriptive
codes.

Coding will be done from a randomized sheet with year and decade hidden.
The source form family will remain visible because it is required to
apply the semantic-residue rubric.

## Confirmatory Analysis

For each source-form family that passes the go/no-go threshold:

1. Identify the earliest analyzable window: the earliest decade with at
   least 3 analyzable derivative tokens, plus following decades in
   chronological order until the window contains at least 10 analyzable
   tokens. If no decade has at least 3 analyzable derivative tokens, the
   family has already failed the go/no-go threshold.
2. Compute the proportion of early-window tokens with:

```text
verbal_syntax = 1 and semantic_residue = 1
```

3. Compute a Jeffreys 95% interval for that proportion.

The confirmatory prediction is supported for a source-form family only if
the lower bound of the Jeffreys interval is above 0.5. It is not
supported if the interval includes or falls below 0.5.

Across families, the primary summary is the number of source-form
families meeting this criterion. The paper will report all families,
including failures and sparse cases.

## Secondary Diachronic Analysis

If at least one source-form family has 50+ analyzable tokens across 5+
decades, a secondary analysis will model `semantic_residue` over time
among tokens with `verbal_syntax = 1`.

The secondary model is a Bayesian logistic regression:

```text
semantic_residue_i ~ Bernoulli(theta_i)
logit(theta_i) = alpha_family[i] + beta_family[i] * decade_i
```

with weakly regularizing priors. This analysis is descriptive and will
not replace the confirmatory early-window test.

## Reliability

Brett will complete a blind second-pass recode on a simple random 10% of
analyzable tokens, rounded up to the next whole token. The subset will be
sampled with random seed 2026 and presented with original codes hidden.

Report for each code:

- percent agreement
- Cohen's kappa

If disagreement exceeds 20% for `semantic_residue`, the confirmatory
analysis will still be reported, but the interpretation will be flagged
as coding-unstable.

## What Will Be Reported Regardless of Outcome

- Query forms and extraction dates.
- Raw hit counts and analyzable-token counts by source-form family.
- Exclusion counts by reason.
- Earliest analyzable window for each included family.
- Token-level coding sheet.
- Confirmatory early-window proportions with Jeffreys intervals.
- Secondary diachronic model results, if the threshold for that analysis
  is met.
- Reliability statistics.

No target forms, coding rules, thresholds, or confirmatory criteria will
be changed after further COHA extraction begins.
