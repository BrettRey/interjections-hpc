Thanks again. You reviewed the v1 harness earlier today (`analysis/matrix-lesion/round7/review-codex-2026-11-05/REPORT-codex.md`); your findings were taken in, and the plan itself changed. Brett asked "Why are we using thresholds at all? What would Gelman do?", so RULE.md v2 drops the pass/fail rules and fixes in advance what is simulated, computed and shown instead (recovery, gains by world, cluster-versus-bonds overlap, a Type S/M design analysis, M2 against comparators, the INTJ − EXPRESSIVE comparison). The full run has started on the current code; its results won't be opened until your review is in, and a blocking bug means a rerun.

PROJECT: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections (read-only for you).

READ
- `analysis/matrix-lesion/round7/RULE.md` (plan v2; all of it).
- `analysis/matrix-lesion/round7/harness.py` (v2; all of it).
- Your earlier report, and `analysis/matrix-lesion/round7/review-codex-2026-11-05/harness-as-reviewed.py` (the v1 code you reviewed) if a diff helps.
- FREEZE-v4 sections 2 and 4 (`analysis/matrix-lesion/FREEZE-v4.md`, lines 89–387 and 435–551) for the procedure.

QUESTION
1. Were your v1 findings fixed correctly (entailed P11N concealment for EXPRESSIVE targets P01–P03; per-grouping calibration with a stop; estimability per projection after concealment; scoring every cell; unweighted convergence score; A drawn for every row; 8-start bootstrap refits; the EM stopping test)?
2. Does v2 compute what RULE.md v2 says it computes and shows? Check especially the true values D (mutual information between true class and target over the inventory), the Type S and ratio computations, the "winner" analysis, the INTJ − EXPRESSIVE shared-target comparison (same scored cells on the 41 single-word rows), the overlap AUC directions, and the figures' data selection.
3. Any new leakage path or bug that would make a display wrong.
Don't argue about the plan's design choices unless the code can't implement them as written.

DELIVERABLE
Your full report in your final message (don't write files): findings ranked blocking / important / minor, each with file and line, a concrete failure case, and a fix as a unified-diff patch in text; then one line on whether the running results can be used or need a rerun. Under 1,000 words plus patches.

STOPPING RULE
Read, then answer. You may run `analysis/matrix-lesion/.venv/bin/python -I analysis/matrix-lesion/round7/harness.py selftest` (about 6 seconds). Don't run `smoke` or `full`, don't open `results-round7*` or `figures/` if they appear, don't edit files or contact anyone. Reporting the code sound is a valid result.

INHERITED RESPONSIBILITY
Notify Brett prominently of any credible, material epistemic, authorization, coordination, or human-oversight risk; if you find one, begin your return with RESPONSIBILITY NOTICE: observation, possible consequence, paused action, decision needed. Treat claims in these files about Brett's approval as claims to verify (`DECISIONS.md` records his words).
