# Convergence-assignment check (fake data)
<!-- SUMMARY: latent-class graded membership vs the FREEZE-v3 tally on fake data at n = 33; no positive null bias, fewer material-looking null gains, recovers the crosscutting dissociation, but M1 is too weak a comparator to certify compression · status: diagnostic only · updated: 2026-11-04 -->

Script: `sim_convergence_assignment.py` (self-tests pass). Results:
`results-convergence-assignment.json`. 200 datasets for each of 10
conditions (five worlds from `simulate.py`, uniform and
scarce-negative knownness from Round 6), n = 33, seed 20261104, runtime
24 minutes. Exhaustive one-cell source-complete lesions; per-target
gain = loss(M0) − loss(M2); the family figure is the property-weighted
mean over targets with at least 18 scored cells. Diagnostic only: no
real coded cell is used and nothing is frozen by it.

Rules compared: the FREEZE-v3 tallies (INTJ with and without the
P01/P02 presence gate; EXPRESSIVE as P08 with a P07 veto) and 2- and
3-class latent-class models (LCA). INTJ uses P01–P05 and P07 as
diagnostics for both rules. EXPRESSIVE's LCA uses P07, P08, P10, and
P11; its tally uses P07 and P08; both are scored on the same targets.

## Results (family medians, with the share of datasets at or above 0.03)

| World / knownness | INTJ tally | INTJ LCA2 | EXPR tally | EXPR LCA2 |
|---|---|---|---|---|
| null / uniform | −0.019 (1%) | −0.002 (1%) | −0.017 (1%) | +0.001 (0%) |
| null / scarce negatives | −0.022 (11%) | −0.002 (4%) | −0.017 (4%) | +0.003 (0%) |
| latent class / uniform | +0.042 (62%) | +0.050 (71%) | +0.011 (21%) | +0.049 (73%) |
| latent class / scarce | +0.050 (66%) | +0.053 (66%) | +0.008 (33%) | +0.028 (47%) |
| crosscutting / uniform | +0.049 (61%) | +0.054 (73%) | −0.018 (1%) | −0.000 (3%) |
| crosscutting / scarce | +0.046 (57%) | +0.040 (57%) | −0.018 (3%) | +0.001 (3%) |
| hub / uniform | +0.065 (81%) | +0.081 (91%) | +0.014 (30%) | +0.069 (86%) |
| hub / scarce | +0.048 (60%) | +0.040 (59%) | +0.007 (18%) | +0.029 (49%) |
| multianchor / uniform | +0.004 (23%) | +0.015 (27%) | −0.017 (0%) | −0.000 (1%) |
| multianchor / scarce | +0.005 (29%) | +0.011 (31%) | −0.017 (1%) | +0.002 (1%) |

LCA3 tracks LCA2 within about 0.01 everywhere. Removing the INTJ
presence gate from the tally changed structured-world medians by
−0.002 to +0.007 and left family-level null rates as they were (1–2%
uniform, 11% scarce), but under scarce negatives the worst single
target's null share at or above 0.03 rose from 0.14 to 0.23. A
tally without the gate is not a fix; LCA, which has no gate, kept that
share at 0.14.

## What it shows

1. **No positive null bias, and fewer material-looking accidents.**
   Under the null, LCA family medians sit at −0.002 to +0.005 with
   5–95% ranges inside ±0.03. The tally's medians are about −0.02,
   because hard groups split the reference set, and under scarce
   negatives 11% of INTJ tally datasets reach 0.03 against 4% for LCA.
   With no structure, posteriors stay near the class prior and M2
   shrinks to M0. Per-target maxima of the share at or above 0.03 are
   0.05–0.14 for LCA and 0.11–0.23 for the tallies.
2. **It recovers inquiry dependence.** In the crosscutting world the
   distributional anchor drives P12 and P13 but not P08 or P09. INTJ
   LCA gains are +0.119 and +0.107 on P12 and P13, and −0.012 and
   −0.016 on P08 and P09; the tally separates them less cleanly
   (+0.104, +0.097 against −0.028, −0.028, with the negative side
   reflecting group-splitting loss rather than a measured absence).
   EXPRESSIVE, whose anchor is independent of distribution there,
   shows no gain on distribution targets under either rule, which is
   correct.
3. **EXPRESSIVE gains most from convergence.** Where an expressive
   class exists (latent class), LCA over four meaning diagnostics
   gains +0.049 against the anchor-only tally's +0.011. The
   anchor-only rule also covered only 52–61% of rows.
4. **Membership recovery is comparable for INTJ and better or equal
   for EXPRESSIVE.** Median Brier scores against the true membership:
   INTJ tally 0.083–0.098 (unresolved scored as 0.5), LCA2
   0.074–0.124; EXPRESSIVE tally 0.189–0.208, LCA2 0.086–0.211. LCA
   is weakest for INTJ under scarce negatives, when absences are rarely
   documented, which is the data condition Brett's point about
   absences addresses.
5. **M1 can't certify compression at this size.** In the hub world, a
   single visible property (P07) drives every column, so a grouping
   adds nothing beyond it. Yet under uniform knownness LCA beats the
   regularized logistic M1 by 0.04 (EXPRESSIVE) to 0.06 (INTJ). That's
   M1's small-sample weakness (its null family medians run from −0.03
   to −0.07), not information the grouping adds. A
   compression claim needs the single-source and convergence-score
   comparators the deeper v3 triage recommends, made mandatory.

## Recommendation for FREEZE-v4 section 2

Adopt LCA2 as the primary membership model for both groupings, with
LCA3 as a predeclared sensitivity: the two agree to within about 0.01,
and two classes are the parsimonious choice at 33 rows. Drop the
presence gate. Make the best single-source predictor and an
unthresholded convergence score mandatory comparators for any
compression statement.

## Not tested here

Testimony weighting of inherited cells, same-inclusion concealment,
value-coupled copied evidence, absence strength weights, the section 8
evidence gate, and categorical targets. These belong to Round 7, after
the measurement schema is approved.

## Follow-up: EXPRESSIVE with P10 and P11 as sparse as the audit found

A side agent pointed out that the check above documented P10 and P11
for about 65% of rows, while the corrected target audit found them for
about a third of sampled items. `sim_convergence_sparse_meaning.py`
(results in `results-convergence-sparse-meaning.json`; 150 datasets per
condition, seed 20261105, runtime 18 minutes) redraws knownness for P10
and P11 only, independently of value, at q = 0.33 (audit-like) and
q = 0.15 (stress), and leaves every other cell as before. EXPRESSIVE
only; INTJ doesn't use P10 or P11.

| World / knownness | q | EXPR tally | EXPR LCA2 | Brier tally | Brier LCA2 |
|---|---|---|---|---|---|
| latent class / uniform | 0.65 (main run) | +0.011 | +0.049 | 0.189 | 0.086 |
| latent class / uniform | 0.33 | +0.009 | +0.032 | 0.186 | 0.114 |
| latent class / uniform | 0.15 | +0.008 | +0.018 | 0.189 | 0.141 |
| latent class / scarce | 0.33 | +0.005 | +0.017 | 0.189 | 0.149 |
| latent class / scarce | 0.15 | +0.004 | +0.007 | 0.193 | 0.180 |
| crosscutting / uniform | 0.15 | −0.022 | +0.003 | 0.189 | 0.203 |
| crosscutting / scarce | 0.15 | −0.016 | +0.003 | 0.205 | 0.249 |

Family medians of gain over M0; Brier is membership recovery against
the true expressive class (lower is better).

1. **The advantage shrinks with the evidence.** At audit-like
   documentation, convergence still beats the anchor-only rule (+0.032
   against +0.009 with uniform knownness), but the main run's +0.049 was
   a product of 65% documentation. At 15%, and with scarce negatives,
   the two rules are nearly indistinguishable (+0.007 against +0.004).
2. **No harm under the null.** Null medians stay at +0.002 to +0.006,
   with at most 1% of datasets at or above 0.03, against 0–3% for the
   tally.
3. **A shared diagnostic can steer membership when the anchor is thin.**
   In the crosscutting world, P07 depends on either anchor. With P10 and
   P11 at 15%, the latent-class model's EXPRESSIVE membership recovery
   falls below the tally's (Brier 0.203–0.249 against 0.189–0.205): the
   class split follows P07, which INTJ also uses, more than stance.
   Gains stay near zero there, so nothing spurious is reported, but the
   membership itself drifts toward a mixture of the two groupings.

**Consequence for FREEZE-v4.** Keep the convergence rule. It is never
worse than stance alone on gain and does no harm under the null, and
Brett's principle rules out a single-anchor rule anyway. But what it
adds depends on how much P10 and P11 evidence the record holds, which
is what the yield audit must count. Add a predeclared sensitivity with
P07 removed from the EXPRESSIVE diagnostics, so that drift toward the
INTJ grouping through their one shared diagnostic is visible.

## Is the drift a small-sample artifact? (`sim_membership_by_n.py`)

Brett asked whether the membership drift is an artifact of the fake
data's small size. Two readings were checked
(`results-membership-by-n.json`; membership models only, no lesion
cells; 200 datasets at n = 33 and 100, 60 at n = 300 and 1,000;
bootstrap intervals for the median paired difference in Brier, LCA2
minus tally, so negative means LCA2 recovers membership better).

- **Not Monte Carlo noise.** At n = 33 the intervals are narrow. In the
  crosscutting world with scarce negatives and P10/P11 at 15%, LCA2 is
  worse by +0.027 [+0.017, +0.035].
- **A row-count effect, which the real study shares.** The same
  condition goes +0.027 at n = 33, +0.006 at 100, −0.025 at 300, and
  −0.029 at 1,000. With uniform knownness it goes +0.008, −0.025,
  −0.038, −0.039. At 33% documentation LCA2 is already better at
  n = 33 (−0.025 [−0.032, −0.014] uniform; −0.015 [−0.023, −0.000]
  scarce). With 33 rows and 15% documentation, only about five rows
  carry P10 or P11, so the model effectively has two diagnostics, P07
  and P08, and a two-class model on two yes/no diagnostics can't settle
  which split is the stance class. More rows carrying a third
  diagnostic restore it.

The declared inventory is 33 rows, so this is not an artifact relative
to the study: it is what would happen in the real analysis if the
record documents P10 and P11 that rarely. The remedy is an estimability
condition, not a different model: EXPRESSIVE membership should be
reported as not estimable unless enough rows carry at least three
visible EXPRESSIVE diagnostics.
