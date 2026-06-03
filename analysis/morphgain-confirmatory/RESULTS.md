# Morphology-Gain COHA Confirmatory Run

Status: complete.

Preregistration lock: `f1a2193` (`Preregister morphology gain COHA test`).
Extraction date: 2026-05-27.
Corpus: COHA, 1820-2019.

## Extraction

Fixed target families and derivatives:

- `wow`: `wowed`, `wowing`, `wows`
- `boo`: `booed`, `booing`, `boos`
- `ooh`: `oohed`, `oohing`, `oohs`
- `shoo`: `shooed`, `shooing`, `shoos`

Token-level coding uses parsed KWIC exports in `raw/`.
Chart requests for `oohed` and `oohing` returned server errors, but KWIC
exports loaded and were used for token-level analysis. Minor chart/KWIC
row-count discrepancies are retained in `morphgain-extraction-summary.csv`.

Raw deduplicated tokens by family:

| family | raw deduplicated tokens | raw decades with 3+ | raw go/no-go |
|---|---:|---:|---|
| wow | 168 | 9 | GO |
| boo | 759 | 13 | GO |
| ooh | 95 | 8 | GO |
| shoo | 440 | 15 | GO |

## Primary Coding

After exclusions, analyzable tokens:

| family | analyzable tokens | decades with 3+ | go/no-go |
|---|---:|---:|---|
| boo | 364 | 10 | GO |
| ooh | 52 | 6 | GO |
| shoo | 410 | 13 | GO |
| wow | 143 | 9 | GO |

Exclusion counts by term and reason are in
`morphgain-coding-summary.csv`.

## Confirmatory Test

Confirmatory success is `verbal_syntax = 1` and `semantic_residue = 1` in
the earliest analyzable window. The support criterion is Jeffreys 95%
lower bound above 0.5.

| family | earliest window decades | n | successes | Jeffreys 95% interval | supported |
|---|---|---:|---:|---|---|
| boo | 1920 | 17 | 17 | [0.865, 1.000] | yes |
| ooh | 1960 1970 1980 | 10 | 10 | [0.783, 1.000] | yes |
| shoo | 1890 1900 | 16 | 16 | [0.857, 1.000] | yes |
| wow | 1930 1940 | 11 | 11 | [0.800, 1.000] | yes |

Primary-coding result: all four source-form families support the
predicted ordering in their earliest analyzable derivative windows.

## Secondary Analysis

The secondary diachronic model was not estimated. Among included tokens
with `verbal_syntax = 1`, `semantic_residue` has no variation.

## Reliability

Brett completed the blind 10% recode (`n = 97`, seed 2026). The
primary codes are stored separately in `morphgain-reliability-key.csv`;
agreement statistics are in `morphgain-reliability-results.csv`.

| code | n | agreement | Cohen's kappa |
|---|---:|---:|---:|
| `exclude` | 97 | 1.000 | 1.000 |
| `verbal_syntax` | 97 | 1.000 | 1.000 |
| `semantic_residue` | 97 | 1.000 | 1.000 |
| `interactional_residue` | 97 | 0.887 | 0.297 |
| `targeted_entity` | 97 | 0.557 | 0.025 |

Confirmatory codes (`exclude`, `verbal_syntax`, `semantic_residue`) are
fully reliable in the blind recode. `interactional_residue` has high
agreement but low kappa because the code is heavily skewed toward 1 and
disagreements are concentrated in marginal `wow` cases and metaphorical
or reporting uses. `targeted_entity` is coding-unstable and should be
treated as descriptive only.

Flagged borderline cases from the second-pass recode:

- `mgc0853`: `shooing` occurs inside a simile ("as if shooing away a
  fly"); coded 1 for interactional residue because the verb still uses
  the directive sense, though the described event is a hand gesture.
- `mgc0468`: scare-quoted `wowed` has a metalinguistic flavour, but is
  syntactically verbal and embedded in a live banquet context.
- `mgc1202`: `wowed by the sphere` describes live viewing but is framed
  as an impression state rather than overt uptake.
- `mgc0793`, `mgc1005`, and `mgc1275` are the clearest
  `interactional_residue = 0` cases.

To recompute reliability:

```bash
python3 analysis/morphgain-confirmatory-reliability.py
```
