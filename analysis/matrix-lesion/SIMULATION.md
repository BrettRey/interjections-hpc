# Fake-data design check: results (2026-11-03, pre-freeze)

Gelman-style fake-data simulation run before any real cell is coded.
Code: `lesion.py` (pipeline core), `simulate.py` (generators + L2/L4
runners), `run_l4.py`, `diagnose.py`. Environment:
`analysis/matrix-lesion/.venv` (numpy, scipy, scikit-learn).
Run: `.venv/bin/python lesion.py` (leakage test), then
`.venv/bin/python simulate.py` and `.venv/bin/python run_l4.py`.

Binary simplification in simulation only: P10 = STRENGTHENS (1) vs
other, P14 = has sequential action (1) vs none. All simulated coded
matrices were degraded with fill rate 0.65 (35% of cells unknown) and
consensus-coding error 0.05 unless stated. Sim-tiers use the draft
thresholds from FREEZE section 8 without the bootstrap-CI condition.

## Data-generating processes

- **null:** all properties independent at plausible base rates.
- **latent_class:** three classes (interjection-core-like 40%,
  ordinary-word 40%, expressive-integrated 20%) with strongly
  class-dependent property probabilities.
- **crosscutting:** two independent latent anchors. A (distributional)
  drives P01, P02, P12, P13 and negatively P03-P05; B (stance) drives
  P08, P10, P11; P07 depends on A or B. Closest to the paper's own
  anchored-cluster model.
- **hub (adversarial):** P07 alone drives all other properties. The
  category step should add nothing beyond visible properties.

## Round 1: the drafted design fails its own structured worlds

L2 at 60% masking, assignment v1 (absolute score >= 3), targets pooled
P10-P13. Median M2-vs-M0 target log-loss gain (d20) was +0.010 in
latent_class, +0.006 in crosscutting, -0.009 under null; no condition
tiered. Diagnosis: at fill 0.65 and 60% masking a row shows ~1.6
assignment-eligible cells, so score >= 3 is nearly unreachable;
per-column reference sets shrink to ~9 rows; all predictors collapse to
base rate. The EXPRESSIVE v1 rule (both P07 and P08 required visible)
left 83% of rows unresolved.

## Round 2: sparsity-aware assignment, 40% masking

Assignment v2 (score normalized by visible eligible cells, at least 2
visible; EXPRESSIVE needs P08=Y and no visible P07=N). Signals appear
but stay small (latent_class n=33: d20 +0.014; n=100: +0.037).
Diagnostics (`diagnose.py`, n=200) localized the loss:

- Assignment is accurate when it fires (mask 0.4: 48% of true-core rows
  MEMBER, 4% of others); unresolved rows fall back to base rate and
  dilute the pooled gain.
- P13 carries almost no signal even for an oracle knowing the true
  class (gain -0.017 to +0.017 across masks). It is a rare,
  "possibility"-strength property (the draft itself describes unusual
  phonology as a recurrent possibility, not a characteristic).
- Random cell-masking also degrades every reference row, which does not
  match the intended use (a new item's partial profile against intact
  descriptions of the others).

## Round 3: L4 sparse-row regime as primary (k=4 visible, others intact)

Targets P10-P12. 40 simulated datasets per condition.
d20 = M0 minus M2 log loss (positive favours the category predictor);
d20|res restricts to rows whose assignment resolved;
d31 = M1 minus M3 (positive favours adding the category step).

| World | n | Tier 1 | Tier <=2 | d20 (med) | d20\|res | d31 | Unres |
|---|---|---|---|---|---|---|---|
| null | 33 | 0.00 | 0.00 | -0.012 | -0.020 | -0.008 | 0.55 |
| latent_class | 33 | 0.30 | 0.35 | +0.035 | +0.063 | +0.003 | 0.53 |
| latent_class | 60 | 0.15 | 0.38 | +0.040 | +0.080 | +0.001 | 0.53 |
| latent_class, k=6 | 33 | 0.47 | 0.57 | +0.062 | +0.087 | +0.013 | 0.30 |
| latent_class, k=2 | 33 | 0.00 | 0.00 | +0.006 | +0.032 | -0.009 | 0.86 |
| latent_class, fill 0.45 | 33 | 0.12 | 0.15 | +0.003 | +0.006 | +0.005 | 0.54 |
| crosscutting (INTJ) | 33 | 0.05 | 0.10 | +0.007 | +0.013 | -0.007 | 0.50 |
| crosscutting (EXPR) | 33 | 0.10 | 0.10 | +0.009 | +0.031 | -0.001 | 0.71 |
| hub | 33 | 0.10 | 0.15 | +0.024 | +0.044 | -0.008 | 0.51 |

Readings:

- The null never tiers. The hub world is correctly kept out of Tier 1
  by the d31 increment condition (median d31 negative).
- Crosscutting scores low on the pooled P10-P12 target because each
  anchor drives only some of those columns. Since crosscutting is the
  paper's own model, the tier test needs per-grouping primary targets
  (INTJ: P12 primary; EXPRESSIVE: P10, P11 primary), fixed in the
  freeze, or the study is set up to fail exactly the world the paper
  describes.
- Visible cells per item (k, fill) matter more than item count
  (n=33 k=6 beats n=60 k=4). Coding completeness is where power lives.
- Unresolved rates around 0.5 at k=4 are pessimistic relative to real
  use, where an analyst's first observations are usually distributional,
  not a random 4 of 14. Reported, not modelled away.

## Threshold calibration (150 datasets each, L4 k=4, n=33)

| d20 threshold | P(hit) under null | P(hit) under latent_class |
|---|---|---|
| >= 0.02 | 0.053 | 0.640 |
| >= 0.03 | 0.013 | 0.547 |
| >= 0.05 (draft placeholder) | 0.007 | 0.367 |

Null quantiles for d20: q90 +0.013, q95 +0.020, q99 +0.036.
Latent-class quantiles: q50 +0.035, q90 +0.094.
The resolved-conditional gain is larger under the alternative but
noisier under the null (q95 +0.040), so it suits a secondary,
coverage-reported measure, not the primary trigger.

## Design changes carried into the FREEZE draft (all pre-approval)

1. Assignment rules v2 (sparsity-aware), as now in `lesion.py`.
2. Primary tier regime: L4 sparse-row (k=4 and k=6), not L2 at 60%.
   L2 remains a stress test, reported secondarily.
3. P13 leaves the primary pooled target set; it is reported per
   property. Primary pooled targets: P10, P11, P12, with per-grouping
   primary targets to be fixed at freeze (proposal above).
4. Threshold proposal, from the null distribution: d20 >= 0.03 for the
   Tier-2 gate (false-tier ~1%, power ~55% in a strongly clustered
   world at n=33, k=4). Still Brett's call, but now an informed one.
5. Report unresolved rate and resolved-conditional gain alongside
   every tier verdict.
6. Unchanged: the go/no-go fill gate. At fill 0.45 power collapses
   (d20 +0.003), so the gate is doing real work.

What fake data cannot check: packet construction, coder behaviour,
quote fidelity, whether the literature fills the matrix at all. That
remains the pilot's job (FREEZE section 10).

## Round 4: rotations over groupings (2026-11-03)

At Brett's suggestion the design was generalized from one grouping to
rotations: a frozen triple of assignment rule, source properties and
target properties, each run through the same lesion machinery with its
own tier verdict. Four rotations were implemented (`lesion.py`
ASSIGNERS; `run_rotations.py`, `run_rotations_sc.py`):

| Rotation | Sources | Primary targets |
|---|---|---|
| INTJ (lexical category) | P01-P05, P07 (R-INTJ-1 v2) | P12 |
| EXPRESSIVE | P08, P07 (R-EXPR-1 v2) | P10, P11 |
| SUPPLEMENT-capable | P02 | P12 |
| DEPICTIVE | P09 | P10, P13 |

Two lesion regimes were compared. Under random-k (round 3's regime),
single-source rotations nearly vanish: the source cell must be both
known and among the k randomly kept cells, leaving ~10 scored resolved
cells per 33-row dataset. That regime also misstates the use case. A
projective claim observes its sources on purpose, so round 4 added a
**source-complete regime**: the target row keeps all known source
cells, targets are masked, reference rows intact. Results in the
multianchor world (each grouping given its own latent anchor; 40
datasets, n=33, fill 0.65, error 0.05):

| Rotation | Own targets d20 | Hit@.03 | Foreign targets d20 | n=100 own d20 / hit |
|---|---|---|---|---|
| INTJ | +0.029 | 0.50 | -0.020 | +0.041 / 0.60 |
| EXPRESSIVE | +0.003 | 0.25 | -0.027 | +0.028 / 0.50 |
| SUPPLEMENT | +0.001 | 0.40 | -0.049 | +0.079 / 0.90 |
| DEPICTIVE | -0.025 | 0.10 | -0.026 | -0.004 / 0.07 |

Null-world own-target d20 medians: -0.034 to -0.017, but hit rates at
the 0.03 gate run 0.03-0.15 depending on rotation, so thresholds must
be calibrated per rotation against its own simulated null, not shared.

Readings:

- Discrimination is clean: every grouping's gain on foreign targets
  sits at or below null levels in the multianchor world. Rotations do
  not promiscuously "find" each other's structure.
- Power tracks source convergence, as the paper's own account would
  predict: INTJ pools six diagnostics and is the strongest rotation at
  n=33; single-cell sources (P02, P09) are noisy indicators of their
  anchors and need either more items or converging source columns.
- SUPPLEMENT has an obvious converging-source upgrade available from
  the draft itself: the non-prosodic supplement tests of sec. 2.2
  (anchor completeness is P02's definition; add it-cleft resistance
  and negation-scope exemption as source columns P15/P16). That also
  protects the P12 target from source-target contamination, since
  supplement status would then rest partly on syntactic tests rather
  than on packaging.
- DEPICTIVE is handicapped by the simulation's binary P10. In the real
  matrix P10 is three-valued and depictive's prediction is MULTIPLIES
  specifically; the binary collapse (strengthens vs the rest) destroys
  exactly that contrast. Its P13 target worked in diagnostics (+0.045
  in one n=100 dataset, member-conditional +0.104). Verdict on this
  rotation awaits the categorical implementation.
- Bearer note: SUPPLEMENT's bearer is an expression in a construction,
  not a sign-type. The rotation as simulated classifies sign-types by
  supplement capability, which is the sign-type shadow of the paper's
  functional claim. A faithful supplement rotation needs
  expression-use rows (appositive NP, non-restrictive relative,
  supplementary adverbial) whose non-supplement cells are mostly U and
  which are scored only within this rotation. Drafted as a FREEZE
  amendment for Brett, not yet added to items.csv.
