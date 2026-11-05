# Round 7 results
<!-- SUMMARY: what the Round 7 fake-data displays show under RULE.md v2, descriptive only; check (b) fails by construction for EXPRESSIVE P01-P03 under whole-column P11N concealment; gain doesn't separate cluster from bonds (bonds' larger gains are largely built in by its calibration); M2's edge over comparators also appears with no structure; corrections after the Codex and Muse consult at the end · status: for Brett to read, no verdicts · updated: 2026-11-05 -->

**Provenance.**
- Plan: `RULE.md` v2 (SHA-256 910cd8cb…).
- Simulation: harness 80066ea7…, copied to `as-run-v2/harness-80066ea7.py`, with its own summaries and figures in `as-run-v2/`. It ran 2,200 datasets in 6,524 s.
- True values, summaries and figures were rebuilt from the raw records by harness c241d009…. That version applies the four summary fixes from Codex's v2 review (`review-codex-v2-2026-11-05/`) and leaves the simulation unchanged.
- Bonds calibration matched. With κ = 4, s_I = 0.825 and s_E = 0.75, the bonds world's oriented phi is 0.48 (INTJ) and 0.44 (EXPRESSIVE), against 0.47 and 0.44 in world 1 (maximum error 0.008).

**Reading the numbers.**
- A gain is loss(M0) − loss(model), in nats per scored cell. Positive means better than the base rate.
- Brackets are the 5th and 95th percentiles across 100 datasets.
- A regime is a documentation level (audit-like or stress) crossed with an assumed rate (0.40, 0.55 or 0.70).
- Unless stated, figures are for world 1 (cluster), audit-like, assumed rate 0.55, split weighting.
- Concealed-cell counts in the raw records leave out the entailed P11N cells.
- The worlds encode assumptions. A display here says how the procedure behaves if the record looks like this, not whether the real record does.

## 1. Membership recovery and the estimability checks (figures 1, 2)

**Full-record Brier skill score against true membership (medians).**

| | audit 0.40 | audit 0.55 | audit 0.70 | stress 0.40 | stress 0.55 | stress 0.70 |
|---|---|---|---|---|---|---|
| INTJ | 0.64 | 0.72 | 0.78 | 0.55 | 0.68 | 0.77 |
| EXPRESSIVE | 0.20 | 0.24 | 0.28 | −0.02 | 0.08 | 0.16 |

- EXPRESSIVE's 5th percentile is at or below zero in every regime.
- In both groupings, the member class ranks true members above nonmembers (AUC > 0.5) in every world-1 dataset, including those where the skill score is near zero.

**Calibration.**
- INTJ: posteriors of 0.4–0.6 correspond to 0.30–0.44 true members, and the top fifth to 0.93–0.96.
- EXPRESSIVE: posteriors of 0.6–0.8 correspond to 0.27–0.40 true members, and the top fifth to 0.73–0.83.
- Grade of membership (world 4): calibration is flatter. Skill against grades is 0.39 [0.10, 0.64] for INTJ and −0.12 [−0.58, 0.22] for EXPRESSIVE.

**All four checks passing (share of projections).**

| | audit 0.40 / 0.55 / 0.70 | stress 0.40 / 0.55 / 0.70 |
|---|---|---|
| INTJ | 0.86 / 0.98 / 0.99 | 0.79 / 0.99 / 0.99 |
| EXPRESSIVE | 0.48 / 0.59 / 0.58 | 0.03 / 0.24 / 0.42 |

- EXPRESSIVE can pass on at most 6 of its 9 targets (section 2).
- Under stress, check (a) is the main failure: it passes in 0.06 of EXPRESSIVE projections at assumed 0.40.

**The checks barely separate cluster from bonds data.**

| Checks pass rate at audit 0.55 | INTJ | EXPRESSIVE |
|---|---|---|
| Cluster world | 0.98 | 0.59 |
| Bonds world | 0.96 | 0.51 |
| Independence world | 0.37 | 0.26 |

**Projection-fit recovery, passing against failing.**
- INTJ: 0.70 [0.46, 0.88] passing (687 projections) against 0.54 [0.33, 0.72] failing (13).
- EXPRESSIVE: 0.24 [−0.02, 0.55] passing (528) against 0.11 [−0.17, 0.44] failing (372). The structural failures of P01–P03 account for 300 of the 372.

## 2. EXPRESSIVE projections onto P01, P02 and P03

- **Check (b) fails in every dataset, world and regime.** With P11N concealed on every row, each pair involving P11N has no jointly visible rows. FREEZE §2 requires every pair of diagnostics to be jointly visible on at least 5 rows, and says "A failure is a finding, never a reason to fall back". So the procedure as drafted would report these three projections as insufficient information on any record.
- **FREEZE's rule is narrower than the harness's.** §4 conceals an entailed source value "for the target row … unless it has an independent supporting observation". The harness conceals the whole column on every row, which is stronger than that text.
- **Comparison with P04 and P05.** These two have the same true gain and no entailed concealment:

| Regime | Measure | P01–P03 | P04–P05 |
|---|---|---|---|
| Audit 0.55 | Recovery in the projection's fit (median) | 0.11–0.13 | 0.22–0.23 |
| Audit 0.55 | Check (d) pass rate | 0.74–0.76 | 0.87 |
| Audit 0.55 | M2 gain (median) | +0.002 to +0.003 | +0.002 |
| Audit 0.40 | Check (a) pass rate | 0.53–0.57 | 0.91–0.92 |
| Audit 0.40 | Recovery (median) | 0.05–0.07 | 0.16–0.18 |
| Stress 0.55 | Check (a) pass rate | 0.16–0.19 | 0.47–0.55 |
| Stress 0.55 | Recovery (median) | 0.05–0.06 | 0.06–0.07 |

- **In world 1 there is little target gain to lose.** All five targets have D of 0.0075–0.0080 nats, because P01–P05 depend on INTJ membership and reach EXPRESSIVE only through the tiers' correlation between the two. The bonds world gives these targets larger gains: medians +0.016 to +0.048 (figure 3).
- Figure 1 shows full-record fits, which conceal nothing for any target, so it does not show this cost. The per-projection values are in `results-round7.json`.

## 3. Would the reported gains have the right sign and size? (figures 3, 5)

**INTJ targets with sizeable true gains.**

| Target | D | M2 gain | Type S | Estimate / D |
|---|---|---|---|---|
| P06 | 0.11 | +0.089 [0.000, 0.25] | 0.05 | 0.80 [0.003, 2.2] |
| P13 | 0.076 | +0.085 [−0.015, 0.24] | 0.11 | 1.1 [−0.20, 3.2] |

- Across regimes, the medians run 0.026–0.10 for P06 and 0.030–0.085 for P13. They are lowest at assumed 0.40.
- **INTJ P12 has the largest true gain (D = 0.19).** It is computable in 42% of datasets, and when computable gains +0.015 [−0.024, 0.067], with estimate/D = 0.08. A median of 33 cells per projection are concealed, mostly by same-inclusion with grammar1, which carries P12 = Y together with the INTJ diagnostics.
- **INTJ targets with small true gains** (P08, P10S, P11N; D about 0.014): medians −0.005 to −0.012, Type S 0.54–0.65.
- **EXPRESSIVE:** every target's D is at most 0.047. M2 medians run −0.002 to +0.009, with Type S 0.31–0.55.
- **P09 (true gain zero):** INTJ −0.019 [−0.046, 0.096]; EXPRESSIVE −0.000.
- **The best-looking target in each dataset:**
  - INTJ: it is P09 in 0.01–0.09 of datasets. Its estimate exceeds its D by a median of 0.006–0.054 across regimes (0.052 [−0.059, 0.18] at audit 0.55).
  - EXPRESSIVE: it is P09 in 0.07–0.19 of datasets, with overstatement medians of 0.004–0.022.

## 4. Could the residual-dependence statistic or the sufficiency gap tell a cluster from bonds? (figure 4)

The AUC here is the probability that a bonds dataset scores further toward "no cluster" than a cluster dataset; 0.5 means neither tends to rank above the other, which two different distributions can also give.

**AUC ranges across the six regimes.**

| Statistic | INTJ | EXPRESSIVE |
|---|---|---|
| Family record gain | 0.09–0.21 | 0.03–0.18 |
| PPC p-value | 0.47–0.58 | 0.50–0.63 |
| Sufficiency gap | 0.56–0.63 | 0.82–0.92 |

- **Bonds datasets show larger family gains than cluster datasets.** At audit 0.55, M2's family gain is +0.067 in the bonds world against +0.028 in the cluster world for INTJ, and +0.034 against +0.005 for EXPRESSIVE.
- **The PPC p-value depends on the documentation rate in every world, the independence world included.**

| INTJ PPC p-value (medians) | 0.40 | 0.55 | 0.70 |
|---|---|---|---|
| Cluster, audit | 0.000 | 0.030 | 0.35 |
| Independence, audit | 0.040 | 0.51 | 0.98 |
| Cluster, stress | 0.005 | 0.15 | 0.71 |
| Independence, stress | 0.35 | 0.86 | 1.00 |

  - At assumed 0.40 and 0.55, most cluster-world datasets give INTJ p-values below 0.05.
  - The cluster-versus-independence AUC is 0.04–0.13 for INTJ and 0.06–0.23 for EXPRESSIVE. The statistic flags the cluster world more often than the world with no structure.

## 5. Does M2 recover anything the comparators don't? (figure 7)

Each entry is M2's family gain minus the comparator's: the median range across the six regimes, with the share of datasets where the difference is positive in brackets.

**Against the anchor diagnostic** (INTJ: the better of P01 and P02 in each dataset; EXPRESSIVE: P08).

| World | INTJ | EXPRESSIVE |
|---|---|---|
| Cluster | +0.008 to +0.018 (0.64–0.84) | +0.015 to +0.020 (0.83–0.96) |
| Bonds | +0.010 to +0.041 (0.66–0.97) | −0.005 to +0.013 (0.43–0.76) |
| Independence | +0.004 to +0.008 (0.62–0.76) | +0.014 to +0.019 (0.89–0.96) |

**Against the convergence score.**

| World | INTJ | EXPRESSIVE |
|---|---|---|
| Cluster | −0.004 to +0.003 (0.41–0.61) | −0.001 to +0.007 (0.49–0.64) |
| Bonds | −0.017 to −0.008 (0.21–0.32) | −0.031 to −0.021 (0.06–0.24) |
| Independence | +0.003 to +0.017 (0.57–0.81) | +0.013 to +0.022 (0.88–0.93) |

- **In the independence world:**
  - M2's family gain is +0.000 to +0.004.
  - The anchor and the convergence score are below zero (−0.002 to −0.019).
  - So M2's margin there comes from losing less to M0, not from gaining.
- **That margin matches or exceeds its cluster-world counterpart,** with one exception: INTJ against its anchor, where the cluster-world margin is larger. A side agent flagged this pattern, and the figures above confirm it.

## 6. INTJ − EXPRESSIVE on the shared targets (figure 6)

**True differences:** P06 0.074, P12 0.137, P13 0.072, P09 0; mean 0.071.

**At audit 0.55.**

| Target | Estimated difference | Type S |
|---|---|---|
| P06 | +0.065 [−0.018, 0.20] | 0.12 |
| P13 | +0.079 [−0.020, 0.21] | 0.13 |
| P12 | +0.013 [−0.036, 0.065], computable for both in 42% | 0.26 |
| P09 | −0.019 | |

- **The mean over the four shared targets** is computable in 0.42–0.54 of datasets, limited by P12. When computable at audit 0.55, it is +0.038 [0.007, 0.087], with Type S 0.05.
- Across regimes, the mean's Type S runs 0.02–0.25, highest at assumed 0.40. With n = 42–54, these shares resolve to about 0.05.
- **Grade of membership (world 4):** the mean is +0.009 [−0.019, 0.050].

## 7. Sensitivities and diagnostics

- **Cap and split weighting give similar displays.**

| Measure | Cap | Split |
|---|---|---|
| INTJ recovery | 0.72 | 0.72 |
| EXPRESSIVE recovery | 0.20 | 0.24 |
| Shared-mean Type S | 0.15 (n = 54) | 0.05 (n = 42) |

- **M1 indicator leak** (M1 minus M1 without indicators):
  - Independence world: −0.021 to −0.033 for INTJ and −0.018 to −0.023 for EXPRESSIVE. The indicators cost predictive accuracy there.
  - Bonds world, EXPRESSIVE: +0.008 to +0.033.
  - The leak test in `selftest` passed.
- **EM starts:** in the median projection, all 8 fit within 1 log-likelihood unit of the best and agree on the partition.
- **Bootstrap spread:** the standard deviation of the member class's rates averages 0.08–0.11 for INTJ and 0.06–0.08 for EXPRESSIVE (world 1).
- **Concealed cells per projection:** INTJ P06 25 [15, 33] and P12 33 [23, 44]; most other projections 2–5.

## Procedure behaviour the displays expose

- Whole-column P11N concealment combined with FREEZE's check (b) makes EXPRESSIVE's P01–P03 projections non-estimable by construction (section 2).
- P12 is computable in 42–57% of datasets in both groupings. Most of its documented cells come from grammar1's testimony unit, which records every one as Y, so its scored cells are often all one value (sections 3, 6).
- The PPC p-value's distribution shifts with the documentation rate in every world, so a p-value from the real record has no fixed reference (section 4).
- M2's margin over the comparators appears in the world with no structure (section 5).

## Corrections after review (2026-11-05)

These come from the Codex and Muse answers in `../../../reviews/proceed-consult-2026-11-05/`. Each was checked by the parent session against the code, `properties-v4.csv` or a fresh computation.

- **The bonds comparison isn't matched on targets.**
  - The bonds world was calibrated on diagnostic–diagnostic association only, and its targets draw on the same bonds as the diagnostics.
  - Mean |phi| between a grouping's diagnostics and its targets is 0.45–0.49 in the bonds world, against 0.14–0.43 in world 1 (P09, which is pure noise, gives 0.12–0.13). Source: `assoc_check.py`, 400 draws per world.
  - So the bonds world's larger gains (section 4) are largely built in by construction. What the displays show is that gain doesn't separate the two worlds, not which world gives larger gains under a matched alternative. A bonds process can also produce converging fallible diagnostics, so a world without discrete classes isn't a world without categories.
- **P11N applicability is wrong in the simulation.**
  - `properties-v4.csv` makes P11N INAPPLICABLE "for uses with no host", and an integrated use (P03 = Y) has a host. `applicability()` tests only P01 = Y and P02 = N, so about half the simulated INAPPLICABLE rows have P03 = Y.
  - Applicability is also computed from true values and given to M1 as an indicator, which makes M1 and M3 slightly optimistic.
  - The check (b) failure in section 2 doesn't depend on either point.
- **True gains are pooled.** D is pooled over 4,000 simulated inventories. It is the expected gain under the generating process, not each dataset's realized gain, and the estimate/D ratios should be read that way.
- **Some displays include projections the protocol wouldn't report.** The per-target gains and the family summaries count projections that fail the estimability checks. FREEZE (lines 819–823) says that for such projections "no estimate is presented as a grouping result". Sections 3, 5 and 6 therefore describe calculations, not what the study would present.
- **The residual-dependence check doesn't model the observation process.** It uses fitted point estimates, without refitting. Its replicates never pass through the documentation process. It is an unweighted statistic against a split-weighted fit, and it holds visibility fixed although documentation depends on values. Its behaviour in the independence world shows that it responds to the documentation rate. Nothing should rest on it.
- **The sufficiency gap is negative in world 1.** Medians run −0.010 to −0.029, so M3 loses to M2 rather than matching it. The gap compares estimators; it can't certify sufficiency.
- **Cap and split weighting differ on one display.** They are similar on recovery, but the shared-mean Type S is 0.15 under cap and 0.05 under split (n = 54 and 42).
- **Testimony cells are exempt from coding error.** The 5% coding flip is applied before inheritance, so inherited cells never carry it.

## After the 2026-11-05 polarity recode

These results were produced by harness 80066ea7… before the recode in FREEZE-v4 section 6. That harness drew P01–P03 independently, so 7.3% of simulated rows (3.4 of 46) had the impossible N/N/N position state, and it treated a use as hostless whenever P01 = Y and P02 = N, whatever P03. The harness now excludes N/N/N in every world and derives the not-applicable state from all three (hash d6384b8b…). Nothing has been rerun.
