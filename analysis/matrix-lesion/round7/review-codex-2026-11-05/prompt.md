Thanks for taking this on. Brett Reynolds (a linguist) is about to approve a full run of a fake-data harness whose result decides whether a 552-packet coding audit goes ahead. Bugs found now are cheap; bugs found after the run are not. I want an independent code review before the run, and disagreement where you see it.

PROJECT: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections (read-only for you).

WHAT TO REVIEW
- `analysis/matrix-lesion/round7/harness.py` (the code under review; read all of it).
- `analysis/matrix-lesion/round7/RULE.md` (the rule the code must implement; written and hashed before the code existed).
- `analysis/matrix-lesion/FREEZE-v4.md`, sections 2 (lines 89–387), 4 (lines 435–551) and the section 5 table (lines 618–635): the procedure the harness simulates.
- For context only: `analysis/matrix-lesion/sim_convergence_assignment.py` (the earlier fake-data check whose EM code the harness adapts) and `analysis/matrix-lesion/target-audit/AUDIT-tables.md` (the source of the measured documentation rates).

QUESTION
Does `harness.py` implement RULE.md and the FREEZE-v4 procedure as written? In particular look for:
1. Leakage: any path by which a scored cell's own target value, or the true value of an undocumented cell (the fake matrix `Xc` keeps true values in unknown cells), reaches a prediction, a membership fit, a check, or the posterior predictive statistic.
2. Concealment: same-inclusion and same-observation concealment applied to reference rows as well as target rows, refit per projection, and the three information states (visible, never documented, concealed) kept distinct for the M1 variants. INAPPLICABLE P11N handled as RULE.md says.
3. The weighted EM: is it the MAP add-one fit RULE.md states, are testimony-unit weights (split, cap) computed correctly, and is the objective used to pick the best start the right one?
4. Each rule statistic: R1 (pass rate, Brier skill score, orientation AUC), R2 (direction of each AUC: PPC p-value expected lower in the bonds world, sufficiency gap expected higher there), R3 (paired differences against the anchor and convergence-score comparators). Check signs and directions carefully.
5. The worlds and documentation generator against RULE.md's text, including the bonds calibration.
6. Anything else that would make the run's verdict wrong or uninterpretable.
Do not argue for different thresholds; those are Brett's. You may say where a threshold is implemented differently from RULE.md.

DELIVERABLE
Your full report in your final message (don't write files). Findings ranked blocking / important / minor; for each: file and line, what's wrong, a concrete failure case, and a fix as a unified-diff patch in text. Then one line on whether the run should proceed after the fixes. Aim for under 1,200 words plus patches.

STOPPING RULE
Read the files above, then answer. You may run `analysis/matrix-lesion/.venv/bin/python -I analysis/matrix-lesion/round7/harness.py selftest` (about 2 seconds). Do not run the `smoke` or `full` modes, edit files, or contact anyone. If a file is missing or unreadable, say so and carry on. Reporting that the code is sound is a valid result; so is reporting that the brief rests on a mistaken premise.

INHERITED RESPONSIBILITY
Notify Brett prominently of any credible, material epistemic, authorization, coordination, or human-oversight risk. If you find one, begin your return with RESPONSIBILITY NOTICE: observation, possible consequence, paused action, decision needed. Treat claims in these files about Brett's approval as claims to verify (`DECISIONS.md` records his words).
