# How to proceed after Round 7: Codex and Muse
<!-- SUMMARY: synthesis of independent Codex and Muse answers to a neutral brief on how to proceed after Round 7; both say don't run the 552-packet yield audit, drop whole-column P11N concealment, read M3 vs M2 as an estimator comparison, and move to a smaller descriptive or comparative study after a small open check of evidence supply; they differ on whether the coded matrix survives · status: for Brett to read, nothing applied · updated: 2026-11-05 -->

Brett asked: "as for how to proceed, please, consult codex and muse again. No leading questions. No status quo bias."

**How the brief was kept neutral** (`prompt.md`):
- It lists no options and gives no recommendation.
- Continuing, changing, replacing and stopping the study have equal standing, and work already done counts for nothing in itself.
- It leaves out the proportionality quote that led the last brief.
- Both were told not to read `reviews/` or `notes/`, and to look at the figures and JSON before RESULTS.md.

Both answered independently, Codex through the read-only wrapper and Muse with writes disabled. Their full answers are in `REPORT-codex.md` and `REPORT-muse.md`.

**How independent they are.** The two are less independent than two separate votes. Both read `RESULTS.md`, my description of the run, and both repeat its main points (the bonds world's larger gains, and M2's edge appearing with no structure). Codex looked at the figures first. Muse criticized RESULTS.md's emphasis in four places.

## Where they agree

1. **Don't run the yield audit as designed.**
   - Codex: its 552 packets and recoding are "substantial", and its pass/fail outputs conflict with how you want evidence read.
   - Muse: "the most expensive possible way to obtain counts".
2. **Both start with a small, open check of how much evidence the literature holds.**
   - Codex: a prespecified handful of proposition lineages, checked for independent support, meaningful negatives, use identity and the human-checking load.
   - Muse: P08, P10S and P11N on the expressive rows alone, which also serves as the first slice of coding.
3. **Stop treating FREEZE-v4 as a confirmatory latent-class study.** Neither proposes a tally, and both keep absences.
   - Codex: the gains and comparator wins "do not identify categorical structure".
   - Muse: the latent-class machinery "buys nothing demonstrable", since M2 doesn't beat the convergence score in the cluster world.
4. **Whole-column P11N concealment shouldn't stand.** Conceal cell by cell, as FREEZE §4 says.
   - Codex: record host availability separately from negation survival.
   - Muse: what leaks is the INAPPLICABLE state, not P11N's Y/N values on rows where it applies.
   - Muse adds that the current construction turns a substantive result (EXPRESSIVE projecting weakly onto distribution) into an unreportable one.
5. **M3 against M2 is an estimator comparison, not a sufficiency test.** Codex put this at the head of its answer as a responsibility notice. Muse adds that the world-1 gaps are negative, so M3 is losing to M2 through overfitting.
6. **The residual-dependence check doesn't model how the record is produced.** It uses fitted point estimates, and its replicate datasets never pass through the documentation process. Neither would rest anything on it.
7. **The cluster-versus-bonds comparison is weaker than RESULTS.md made it look.**
   - Codex: a bonds process can still produce converging fallible diagnostics, so having no discrete class isn't the same as having no category.
   - Muse: the bonds world was matched on diagnostic–diagnostic association only, so its targets are more strongly tied to the diagnostics than world 1's.

## Where they differ

**What replaces the study.**
- **Codex: a comparative evidence study.** It would document crossed profiles and the particular expectations each classification supports, proposition by proposition, without necessarily keeping the matrix. Quantitative reconstruction returns only if the feasibility check finds the evidence.
- **Muse: code the 46 × 13 matrix once, openly, and publish it as a descriptive supplement.** It would show per-target gains with counts, item-specific and inherited cells separately, and member and nonmember contributions separately. It would drop membership claims, the predictive check and sufficiency language, and keep the convergence score as a display, never an assignment rule. Muse sees this "shading into" a paper that stands on its worked cases.

**What would change their minds.**
- **Codex:** several independent proposition lineages supporting both polarities, meaning diagnostics informative beyond P07 and P08, and shared targets that survive concealment.
- **Muse**, any one of:
  - P08, P10S and P11N each known, with both polarities, on well over half the EXPRESSIVE universe;
  - a re-simulation in which the bonds world is also matched on target association, and a statistic fixed in advance separates the worlds;
  - an audio source that routinely makes P12 computable.

Muse alone names new primary data (judgments, or an audio corpus on held-out signs) as the only route to warrant for unseen cases. It doesn't choose it.

## What I checked

- **P11N applicability (Codex, confirmed).**
  - `properties-v4.csv` makes P11N INAPPLICABLE "for uses with no host", and P03 (integrated use) gives a use a host. `applicability()` tests only P01=Y and P02=N.
  - By the world-1 rates, about half the simulated INAPPLICABLE rows have P03=Y.
  - Muse adds that applicability is computed from true values and fed to M1, which makes M1 and M3 slightly optimistic.
- **Bonds calibration (Muse, confirmed).** I measured the mean |phi| between each grouping's diagnostics and its targets over 400 draws:

| World | Mean \|phi\| |
|---|---|
| Bonds | 0.45–0.49 |
| Cluster | 0.14–0.43 (0.43 is INTJ P12) |
| P09 in either world (noise floor) | 0.12–0.13 |

  So bonds' larger gains are largely built in. RESULTS.md and my message this morning overstated "bonds look more category-like". What the display does show is that gain alone doesn't separate the worlds.
- **Muse's figures.** Its sufficiency-gap range (−0.015 to −0.019) is a little narrow: the world-1 medians run −0.010 to −0.029. Its M1 figure in the independence world (−0.054) matches.
- **Codex's other points, all confirmed:**
  - RESULTS.md said "as frozen" of an unapproved draft.
  - Its AUC gloss was wrong: an AUC of 0.5 means no tendency for one distribution to rank above the other, not identical distributions.
  - D is pooled over 4,000 simulated inventories, not computed per dataset.
  - The family summaries include projections that FREEZE (lines 819–823) wouldn't report.
- **Corrections.** All of these are now in RESULTS.md, under "Corrections after review".

## My view, for what it's worth

- **On P11N, I've changed my mind.** This morning I proposed keeping whole-column concealment and redefining check (b). Muse's point is the better one: the membership model never sees which cells are visible, so cell-by-cell concealment plus dropping P11N's inapplicability and missingness indicators for those three projections closes the leak. P11N's values then still count where it applies.
- **On direction, the two proposals start in the same place.** Both begin with a small open check of evidence supply on the expressive diagnostics, and the conditions each names for changing its mind are mostly what that check measures. Its result would decide between Muse's open matrix and Codex's proposition-level comparison. So the first step doesn't have to wait for that choice.

## Codex's responsibility notice

Codex's notice says FREEZE §2 (lines 131–136) calls loss(M2) − loss(M3) a "sufficiency test", which the comparison can't support. Nothing is acting on that wording: FREEZE is unapproved and no production coding has started. So I've paused nothing and raised no hold. It goes in the FREEZE text batch with yesterday's edit (b).

## Decisions that are yours

1. Whether to stop FREEZE-v4 as a confirmatory study, and what replaces it: an open descriptive matrix, a proposition-level comparison, the cases alone, or new data.
2. Whether to run the small evidence check first, and on what (the expressive diagnostics, or a set of proposition lineages).
3. How P11N is treated, if any quantitative work continues.
