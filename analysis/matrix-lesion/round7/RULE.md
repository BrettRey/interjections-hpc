# Round 7 fake-data harness: the analysis plan, written in advance
<!-- SUMMARY: what the Round 7 harness simulates, computes and shows, fixed before any full run; no pass/fail thresholds: recovery, what the study would report in each world, cluster-versus-bonds overlap, a Type S/M design analysis, and M2 against simple comparators, for Brett to judge · status: v2, written before any full run · updated: 2026-11-05 -->

Fixed before any full run. Its SHA-256 is logged in `../../../DECISIONS.md`.
After the full run, the worlds, documentation grid, quantities and
displays below don't change; any analysis added after the run is
labelled exploratory. The earlier version of this file and why it was
replaced are under **Versions** at the end.

## What the harness is for

To find out what the exact FREEZE-v4 procedure can and can't recover
when documentation is as thin as the real record appears to be, and
whether the numbers it would report could tell a cluster from diffuse
association. The logic is the one in Gelman et al., "Bayesian Workflow"
(arXiv:2011.01808, 2020, §4.1, p. 16): a procedure that can't recover
the truth from fake data shaped like the real data can't be trusted on
the real data, while one that can may still fail there. Where recovery
fails, the same section's advice is to simplify the model until it
works.

Nothing here is a pass/fail test. The results are distributions and
displays, and the decision on the yield audit is Brett's after reading
them. What's fixed in advance is what gets computed and shown.

## Procedure simulated

FREEZE-v4 sections 2 and 4 as drafted on 2026-11-04:

- 46 rows with the tiers and universes of `../items-v4.csv` (INTJ: the
  41 single-word rows; EXPRESSIVE: all 46).
- v4 columns P01 to P09, P10S, P11N (with INAPPLICABLE), P12, P13.
  P10M and P14 are outside v1.
- Membership: a two-class latent-class model per grouping, fitted by EM
  with cell weights, MAP with add-one smoothing (Beta(2,2) rates,
  Dirichlet(2) sizes), 8 random starts.
- Testimony units weighted by **split**: the visible cells that one unit
  supplies to a fit share a total weight of 1 (the FREEZE section 2
  default). **Cap** weighting (each inherited cell weighted 0.5) is a
  sensitivity.
- Concealment by dependence, applied to reference rows as well as target
  rows, with the membership model refitted per projection:
  - **same inclusion**: a diagnostic cell inherited through the same
    testimony unit as the row's target cell;
  - **same observation**: 5% of a row's item-level source–target pairs;
  - **entailed**: a use with no host (P11N INAPPLICABLE) is standalone,
    not a supplement and not integrated, so P11N's state is entailed by
    P01, P02 and P03. EXPRESSIVE projections onto those three targets
    conceal P11N on every row.
- Estimability checks a to d, run **per projection on the
  post-concealment record**, at the draft numbers in FREEZE section 2:
  (a) 10 rows with three or more visible diagnostics, a testimony unit
  counted once; (b) every diagnostic pair jointly visible on 5 rows;
  (c) median correlation of 0.8 between bootstrap and full-record member
  posteriors over 50 refits of 8 starts; (d) member-class rate on the
  anchor (INTJ: P01 or P02; EXPRESSIVE: P08) at least 0.3 above the
  other class's. These are FREEZE's own draft checks, simulated as
  FREEZE states them; the harness reports how they behave.
- Scoring: every scored cell with at least one reference outcome is
  scored once. A target is computable when its scored cells include both
  values (FREEZE section 8). A predictor whose reference outcomes all
  share one value predicts the smoothed reference rate.
- Predictors M0, M1 (value plus missingness indicator per source), M2,
  M3, and the comparators: each single diagnostic used alone, and the
  unthresholded convergence score (the unweighted mean of signed visible
  diagnostics, as FREEZE section 2 words it).
- Candidate targets as in the FREEZE section 5 table. INTJ: P06, P08,
  P09, P10S, P11N, P12, P13. EXPRESSIVE: P01 to P06, P09, P12, P13.
- Cross-inquiry comparison on the shared targets P06, P09, P12 and P13:
  both groupings scored on the 41 single-word rows with the same scored
  cells and reference outcomes; each grouping's membership is fitted on
  its own universe.

## Worlds

1. **Crosscutting cluster.** Every row has an INTJ class A and an
   EXPRESSIVE class B, drawn independently with probabilities set by its
   tier (assumed: core 0.95 / 0.7; boundary 0.5 / 0.5; control 0.05 /
   0.1; extension 0.3 / 0.3; expr-core 0.2 / 0.95; expr-control 0.05 /
   0.05). INTJ diagnostics depend on A (P01, P02 high; P03, P04, P05
   low); EXPRESSIVE diagnostics on B (P08, P10S, P11N high); P07 on
   either. Targets: P06 low for A, intermediate for B without A; P12
   high for A, intermediate for B without A; P13 raised for A; P09
   follows an unrelated class, so P09 is a null target for both
   groupings.
2. **Bonds null** (Thomson's sampling model applied to properties). Each
   row holds each of 40 bonds with probability 0.5; each property draws
   its own subset of bonds; a property's probability rises with the
   share of its bonds the row holds, oriented to world 1's signs. There
   are no classes. **Calibration, declared in advance:** the properties
   anchored in INTJ's field (P01 to P06, P12, P13) draw their subsets at
   overlap s_I, EXPRESSIVE's (P08, P10S, P11N) at s_E, and P07 at their
   mean; P09 is independent. (s_I, s_E) is chosen by grid search so that
   each grouping's mean sign-oriented pairwise phi among its diagnostics,
   on complete matrices, is within 0.02 of world 1's. One shared overlap
   can't do this: checked on 300 complete matrices before this plan was
   written, 0.75 leaves INTJ 0.03 short and 0.80 puts EXPRESSIVE 0.03
   over. If the grid can't match both, the harness stops.
3. **Independence null.** Every property independent, with world 1's
   marginal rates.
4. **Grade of membership.** World 1 with Beta-distributed grades (mean
   set by tier, concentration 2) in place of A and B.

## Documentation

Item-level knownness first, then class-level testimony. Only three
properties have a measured rate, from the 12-item target audit, whose
sample predates the 11 expressive rows added in v4. The others are
assumed, so they run on a grid.

| Property | Audit-like | Stress | Basis |
|---|---|---|---|
| P10S | 0.33 | 0.15 | measured: pass-weak item-direct 4 of 12 (strict: 2 of 12), `../target-audit/AUDIT-tables.md` |
| P11N | 0.33 of applicable rows | 0.15 | measured: item-direct 2 and class-inherited 2 of 12; that audit predates the INAPPLICABLE state |
| P12 | 0.05 | 0.05 | measured: item-direct 0 of 12; its 7 class-inherited cells come in through testimony below |
| P01 to P09, P13 (P08 included) | 0.40, 0.55, 0.70 | 0.40, 0.55, 0.70 | **assumed**; 0.65 was the convention in `../CONVERGENCE-CHECK.md`, not a measurement |

Six documentation regimes: the measured properties at the audit-like or
stress level, crossed with the three assumed rates.

- **Value-dependent documentation** in every regime: a presence is
  documented at 4/3 of the rate above, an absence at 2/3.
- **Testimony.** Three fake sources state class properties: a grammar
  (INTJ class: P01 Y, P02 Y, P03 N, P04 N, P05 N, P06 N, P12 Y); a
  second grammar (INTJ class: P05 N, P07 Y, P13 Y; includes fewer rows);
  an expressive source (EXPRESSIVE class: P07 Y, P08 Y, P10S Y, P11N Y).
  A source includes a row with a probability that rises with the row's
  true sign-oriented diagnostic profile (assumed). An included row's
  undocumented cells take the stated class value, so inherited cells are
  wrong for wrongly included rows. All cells one source attributes to
  one row form one testimony unit. The stress level multiplies inclusion
  probabilities by 0.6.
- **INAPPLICABLE.** P11N is INAPPLICABLE for rows whose true use is
  standalone only (true P01 = Y and P02 = N). It is neither visible nor
  missing, and such rows aren't scored on P11N.
- Coding error: 5% of item-level cells flipped.

Datasets: 100 for each of worlds 1 to 3 in each of the six regimes; 100
for world 4 and 100 for each of worlds 1 to 3 under cap weighting, both
at the audit-like level with the assumed rate at 0.55.

## True values for the design analysis

For world 1, each grouping and each target, the true gain D is the
mutual information between the row's true class for that grouping and
its true target value, over the declared inventory, in nats: the
log-loss reduction an oracle that knew every row's class and the true
class rates would get over the true base rate. It is computed by Monte
Carlo from 4,000 complete fake inventories. P09's D is zero by
construction. For the cross-inquiry comparison the true difference is
D(INTJ) − D(EXPRESSIVE) on the 41 shared rows. The estimate the study
reports, loss(M0) − loss(M2) on the documented record, is compared with
D; the gap between them combines noise, thin documentation, selective
documentation and the model's own error, which is the point.

## What is computed and shown

For every regime, both groupings, and every world unless stated.

1. **Recovery** (worlds 1 and 4). The Brier skill score of the member
   posterior against true membership (grades in world 4), relative to
   predicting the true member share for every row: its distribution
   across datasets, for the full-record fit and for each projection's
   post-concealment fit. A calibration plot: posterior binned in fifths
   against the observed member share. How often the member class ranks
   true members above nonmembers. How often each estimability check
   passes, and the distribution of recovery in projections that pass
   against those that fail.
2. **What the study would report.** For each target: the share of
   datasets in which it is computable, the number of scored cells, and
   the distributions (median, 5th and 95th percentiles) of loss(M0)
   minus the loss of M1, M1 without indicators, M1 with indicators for
   never-documented cells only, M2, M3, each single diagnostic, and the
   convergence score, plus the sufficiency gap loss(M2) − loss(M3). The
   same for the equal-weight family mean over computable targets. Worlds
   1 to 3 side by side.
3. **Cluster against bonds.** Overlaid distributions, in worlds 1, 2 and
   3, of the posterior predictive p-value for pairwise residual
   dependence among a grouping's diagnostics (FREEZE section 2's
   residual-dependence check), the family sufficiency gap, and the
   family record gain. Each pair of distributions is summarized by the
   probability that a world 2 dataset scores further toward "no cluster"
   than a world 1 dataset (an AUC, reported as a description of overlap).
4. **Design analysis** (Gelman and Carlin, "Beyond Power Calculations",
   *Perspectives on Psychological Science* 9(6): 641–651, 2014), world 1.
   For each target with D above zero: the share of datasets whose
   estimate has the wrong sign (Type S), and the distribution of the
   estimate divided by D (Type M). Because a write-up will discuss the
   target that looks best, also: in each dataset, the computable target
   with the largest estimated gain; how often that target is P09, whose
   true gain is zero; and the distribution of its estimate minus its D.
   For the cross-inquiry comparison: per shared target and for their
   mean, the share of datasets in which the estimated INTJ − EXPRESSIVE
   difference has the wrong sign, and its distribution against the true
   difference.
5. **M2 against the simple comparators.** The paired difference, M2's
   family gain minus the anchor diagnostic's (INTJ: whichever of P01 and
   P02 does better in each dataset, which favours the comparator;
   EXPRESSIVE: P08) and minus the convergence score's, as distributions
   in worlds 1 to 3.
6. **Sensitivities and diagnostics.** Cap weighting; the M1 indicator
   leak (M1 minus M1 without indicators) in the independence null;
   EM starts within 1 log-likelihood unit of the best and their partition
   agreement; the bootstrap spread of the member class's rates; the
   number of cells concealed per projection; the bonds calibration
   achieved.

The displays are written to `figures/`, the numbers to
`results-round7.json`. A short `RESULTS.md` written after the run says
what the displays show, without verdicts.

## The questions the displays answer

1. Can each grouping's membership be recovered at each documentation
   rate, and do the estimability checks separate fits that recover it
   from fits that don't?
2. Would the gains the real study reports have the right sign and
   roughly the right size, or would they mostly be noise, and how badly
   would the best-looking target overstate its true gain?
3. Could the real study's residual-dependence statistic or sufficiency
   gap tell a cluster from the bonds world?
4. Does M2 recover anything the anchor diagnostic or the convergence
   score doesn't?
5. Would the INTJ − EXPRESSIVE comparison on shared targets come out
   with the right sign?

## Reported, with a provisional choice

**An encoding gap in FREEZE.** Section 2 bars a rotation whose permitted
sources aren't binary until their encoding is frozen, and EXPRESSIVE's
P11N has an INAPPLICABLE state. The harness gives INAPPLICABLE its own
indicator in M1 and treats it as invisible in the membership fit. That
encoding is provisional.

## Not simulated

Absence-strength weights; Tier B; the analyst tier; the three-class and
P07-removed sensitivities; the two-feature model; the paired row
bootstrap; host-relation subtypes of P11N; disputed codings and
inventory reselection.

## What a good result doesn't show

The worlds encode assumptions. Good recovery says the procedure can
work if the record looks like this; it says nothing about whether the
real record does.

## Versions

- **v1** (SHA-256 61cbaff5…, 2026-11-05 06:14 EST) set pass/fail
  thresholds (R1 to R3). Brett asked, "Why are we using thresholds at
  all? What would Gelman do?", and approved this version ("yes rewrite
  RULE.md this way"). v1 was never run beyond a smoke test that printed
  timing only.
- **v2** (this file) replaces the thresholds with the displays above and
  takes in the procedural fixes from Codex's review of the harness
  (`review-codex-2026-11-05/REPORT-codex.md`): entailed concealment of
  P11N, estimability per projection after concealment, calibration per
  grouping with a stop if unmatched, scoring every cell, the unweighted
  convergence score, A drawn for every row, 8 starts for bootstrap
  refits.
