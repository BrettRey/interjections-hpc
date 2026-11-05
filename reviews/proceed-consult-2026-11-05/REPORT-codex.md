# Codex: how to proceed after Round 7 (2026-11-05)
<!-- SUMMARY: verbatim Codex (read-only wrapper) answer to the neutral proceed brief; recommends a comparative evidence study with a bounded feasibility check, not the full yield audit; rejects whole-column P11N concealment; responsibility notice on the M3-vs-M2 "sufficiency test" wording · status: received, not yet synthesized · updated: 2026-11-05 -->

Saved verbatim by the parent session (Claude Opus 5.5) from `codex-stdout.txt`.

---

RESPONSIBILITY NOTICE: FREEZE calls M3 versus M2 a “sufficiency test” (§2, lines 131–136), but the implemented comparison cannot establish conditional sufficiency. Treating it that way could turn estimator weakness into evidence that membership captures everything relevant. Production remains unapproved and should stay paused pending a decision about that interpretation. I made no changes or external contacts.

**I would replace the current confirmatory ambition with a smaller, source-grounded comparative study, preceded by a bounded evidence-feasibility check.** Round 7 supplies reasons to simplify; it doesn’t establish that the paper’s categories fail.

**1. What Round 7 establishes**

I inspected all seven figures before reading `RESULTS.md`, checked the central numbers against JSON, inspected raw records, and compared the current and as-run code.

At audit-like documentation, assumed rate 0.55, split weighting, the JSON’s `summary["cross/audit/q=0.55/split"]` shows:

- Full-record membership Brier skill: INTJ median **0.718**, EXPRESSIVE **0.243**. Recovering an imposed class is substantially easier for INTJ.
- INTJ P06 gain: **0.089**, with simulation percentiles **[0.0003, 0.248]**; P13: **0.085 [−0.015, 0.243]**. Useful recovery is possible, with considerable variation.
- INTJ P12: oracle gain **0.188**, estimated median **0.015**, computable in **42/100** datasets. Strong underlying association needn’t survive the evidence architecture.
- EXPRESSIVE P01–P03 are computed in all 100 raw datasets despite passing the combined estimability checks in **none**. These are diagnostic calculations, not results the protocol would permit presenting as interpretable grouping estimates.

The bonds world produces larger family gains than the cluster world. M2’s advantages over simple predictors also appear under independence. Consequently, reconstruction gain and comparator superiority do **not** identify categorical structure.

But this doesn’t demonstrate that categories lack predictive value. It demonstrates limitations of these procedures under these constructed worlds. Nor does Round 7 measure actual literature yield, coding validity, interval coverage, or performance under disputed codings. Its percentile ranges describe variation across simulated datasets; they aren’t uncertainty intervals for Brett’s eventual record.

A deeper issue: a no-class bonds process can still produce converging, fallible diagnostics. Under Brett’s commitments, absence of a discrete latent class doesn’t itself establish absence of a category. “Cluster versus bonds” is therefore an imperfect proxy for the theoretical dispute.

**2. Where the descriptions or implementation mislead**

- **Sufficiency is overinterpreted.** FREEZE’s “sources add nothing once membership is known” (lines 133–134) isn’t established by a small predictive difference. `harness.py:529,543–547` compares a posterior-weighted mixture with a penalized logistic model using sources and membership. M3 doesn’t nest M2’s prediction rule; regularization, functional form and limited data can prevent improvement despite remaining information. The gap is an estimator comparison, potentially informative but not a sufficiency certificate.

- **“Exact FREEZE-v4 procedure” is too strong** (`RULE.md`, opening purpose). `RESULTS.md:59` says “the procedure as frozen,” although FREEZE explicitly remains unapproved. More substantively, harness summaries include estimates failing checks, whereas FREEZE:819–823 says “no estimate is presented as a grouping result.” `family()` includes every computable target without checking estimability (`harness.py:580–590`). Family displays therefore summarize hypothetical calculations beyond the protocol’s reportable results.

- **P11N’s simulated applicability is not logically faithful.** `applicability()` equates P01=Y and P02=N with “standalone-only” (`harness.py:215–217`). Yet P03 is independently generated conditional on class (`110–141`), so such rows can also have P03=Y. P01/P02 alone don’t establish absence of an integrated host. This weakens the rationale for the blanket concealment described in RULE’s “entailed” bullet.

- **The residual check has a narrower interpretation than its name suggests.** `ppc()` draws at fitted MAP parameters, holds visibility fixed, and doesn’t generate selective documentation or shared testimony (`389–426`). It is a plug-in predictive diagnostic, not a full posterior predictive account of the observation process. Documentation-sensitive discrepancies cannot cleanly diagnose cluster structure. No decision here should rest on its reported p-values.

- **AUC wording is wrong.** `RESULTS.md:96`: “0.5 means the two distributions overlap fully.” It means no directional rank discrimination; distinct distributions can have AUC 0.5.

- **The true-gain benchmark is pooled.** RULE:144–154 describes gain “over the declared inventory”; `_mi()` pools 4,000 inventories (`harness.py:625–665`). This is a superpopulation mixture benchmark, not each dataset’s realized oracle gain. The reported estimate/D ratios should be described accordingly.

**3. Realistic options**

| Route | Defensible contribution | Cost | Main risk |
|---|---|---|---|
| Continue v4 after repairs | Reconstruction within the coded inventory | High: 552 audit packets, production recoding, semantic checking, analysis | Precise-looking results dominated by testimony and documentation |
| Simplify the quantitative study | A few declared projections, with predictive comparisons and coding sensitivity | Medium; requires fresh specification | Too little independent evidence, particularly for EXPRESSIVE |
| Comparative evidence study | Documented crossed profiles and the particular expectations each classification supports | Low–medium; careful proposition-level checking | Establishes examples and local scope, not inventory-wide predictive performance |
| Collect targeted judgments or observations | New evidence for specified environments among declared uses | High; new measurement and sampling design | Judgment effects, use ambiguity, and substantial scope expansion |
| Stop the empirical addition | A theoretical paper supported by checked linguistic cases | Lowest | Some general projective claims must remain proposals |

The third and fourth routes needn’t reproduce the matrix architecture. A coordinated set of test frames or a proposition-centered comparison may answer the linguistic question more directly.

**4. My choice and the open decisions**

Choose the comparative evidence study, with quantitative reconstruction retained only if a bounded feasibility check reveals suitable evidence. Don’t replace latent classes with a tally. Preserve absences as supported negative propositions, distinguish their evidential strength, and keep all conclusions within the declared inventory and coded literature.

**Yield audit:** don’t run the full audit as designed now. Its 552 packets and fresh production recoding are substantial, while its pass/fail estimability outputs (`DESIGN.md:87–90`) conflict with the intended evidential approach. First inspect a small, prespecified set of candidate proposition lineages for independent support, meaningful negatives, use identity and human-checking load. Preserve the agreed sealing constraints; any revision requires Brett’s decision.

**P11N:** reject automatic whole-column concealment as the general rule. Record host availability separately from negation survival; conceal dependencies cell by cell, including applicability metadata where it reveals the target. Independent evidence must actually be independent of the target proposition. If this leaves only three usable diagnostics, name and evaluate that reduced projection rather than retaining an impossible four-diagnostic overlap requirement.

I’d reconsider a quantitative study if checked evidence showed multiple independent proposition lineages supporting both polarities, informative meaning diagnostics beyond P07/P08, and shared targets surviving concealment. More simulated datasets alone wouldn’t change my mind.
