# Direction for 2026-11-05, after the new literature
<!-- SUMMARY: synthesis of independent Codex and Muse answers on what to work on next in light of the eight 2026-11-04 readings; both say paper first, cheap FREEZE-v4 text fixes, no new models; they split on whether the yield audit or a fake-data harness comes first; their agreement is correlated by a shared brief and shared notes · status: for Brett to read, nothing applied · updated: 2026-11-05 -->

Brett asked (2026-11-04, late): "Consult with codex and muse on a direction for tomorrow in light of the new lit". Both answered the same brief (`prompt.md`) independently: Codex through the read-only wrapper, Muse in a fresh headless session with writes disabled. Their full answers are in `REPORT-codex.md` and `REPORT-muse.md`. Nothing has been applied to any file.

## Where they agree

Count this agreement as less than two independent votes. Both answered the same brief, and both worked from the same eight reading notes, which Claude subagents wrote; they opened the sources only to spot-check (Codex several PDFs, Muse Breiman p. 206). The brief also leaned toward doing less. Its question 3 asked whether the literature shows the design "over-built for 46 rows" or that "a different or simpler analysis would answer the paper's question better", and it quoted your request for proportionate effort (`prompt.md`, lines 37 and 43). Their verdicts on edits a–h start from my list too. So treat item 4 below as one opinion the brief helped shape. Codex did resist the premise: "No source establishes a general prohibition on modelling 46 rows." The case for simplifying that doesn't come from the brief is the project's own fake-data result in `CONVERGENCE-CHECK.md`, which both cite. Judge the simplification on that.

1. **The paper comes first, and narrowly.** Write the Magnus (enquiry relativity) and Franklin-Hall (categorical bottlenecks) distinctions into `inquiry-relative-categories.tex`, roughly two paragraphs, and log both in DECISIONS as *deliberately distinguished*. Muse: Magnus's kinds are relative to domains of phenomena and must be indispensable, while these categories are relative to inquiries and are assessed one projection at a time; Franklin-Hall reserves naturalness for service across inquiries, while category standing here is local to an inquiry. Muse also wants Magnus's pages checked against the published edition, since the held file is the author's final draft. Don't let this grow into a philosophy-of-science section.
2. **FREEZE-v4 needs only cheap text fixes now:**
   - (a) report M1 without missingness indicators;
   - (b) call the M3–M2 gap predictive sufficiency at this n, not sufficiency;
   - (c) cut "the closer match to HPC" (line 310);
   - (g, part) report every EM start near the best likelihood and whether the partitions differ, extend stability check (c) to the class-conditional rates, and report the null distribution of the sufficiency gap in the bonds world.
   - No coding, and no freeze.
3. **No new models tomorrow.** Reject Kemp & Tenenbaum's chain-versus-classes check as a study task (f). Grade-of-membership becomes a fake-data world at most, not a model fitted to the real data (d). Don't implement CrossCat. Codex would also leave the two-feature Round 7 model alone; Muse would keep it as the one extra model worth testing for estimability, but not tomorrow.
4. **The study is over-built for its evidence.** The limit is not the 46 rows as such. It's that there are few informative diagnostics, documentation is sparse, testimony is shared, and few targets are shared. Both cite the project's own fake-data result: when P10 and P11 are thin, EXPRESSIVE effectively has two diagnostics, and the model "can't settle which split is the stance class" (`CONVERGENCE-CHECK.md`). Both propose a simpler primary analysis. Per target, compare M0 against each single diagnostic and against an unthresholded convergence score, then ask whether latent-class M2 adds anything beyond them. Codex calls the result an "evidence profile", Muse a "descriptive lesion study".
5. **Leave main.tex alone tomorrow.**

## Where they split

- **What comes first.** Codex: estimate the yield audit's real coding load, run it if acceptable, and stop at its outputs. Muse: don't run or approve the 552-packet audit tomorrow. First write and run a fake-data harness that uses the exact procedure, including worlds where documentation depends on the value, with a rule written in advance: if EXPRESSIVE membership or the bonds separation fails, the study goes descriptive or stops.

  Both noticed the same circularity. FREEZE-v4 §2 bases the harness's knownness on "the yield audit's sealed counts", yet the audit's checks (c) and (d) need a fitted model whose settings are calibrated only afterwards. **My recommendation is Muse's order.** The harness is a script, while the audit means 552 packets coded by several routes. Its knownness can come from the 12-item target audit's rates, plus a stress level. If the procedure can't recover anything even when documentation is realistic, the audit is moot.

  Muse's advance rule is a go/no-go for the study's design, not an outcome label, so it doesn't bring back the gates you removed. But that's your call.
- **The MNAR sensitivity (e).** Codex: later, before any claim reaches undocumented cells. Muse: now, inside the harness, as value-dependent documentation worlds; a formal treatment after Little & Rubin. If the harness is built, Muse's version costs almost nothing extra.
- **Tuning M1's C.** Codex: later, by inner cross-validation. Muse: reject; with 20–30 scored cells and likely separation, tuning adds selection noise, and a fixed-C sensitivity is cheaper. I side with Muse.

## Additions worth taking

- **Concealed versus missing (Muse).** Separate cells that were never documented from cells concealed because they're entailed by, or share an inclusion with, the target. Only the first are ordinary missing data. The second can leak the target's pattern into M1's missingness indicator, which goes beyond edit (a).
- **Posterior predictive pairwise checks (Muse).** Make these, not the M3 gap, the main evidence for sufficiency.
- **P12 mismatch (Codex; I confirmed it).** FREEZE-v4 §5 lists hosted P12 as a candidate target for both groupings, and §8 reports every candidate target, but `yield-audit/DESIGN.md:36` leaves P12 out. One of the two has to change.
- **The paper's table (Codex; I confirmed it).** In `tab:inquiry-record` (`inquiry-relative-categories.tex:827`), the Grouping cell for the expressive grouping is the single property "Deployment conventionally conveys evaluative or affective stance". That contradicts the convergence account in the surrounding prose. The cell should name the anchor and the other diagnostics.
- **CrossCat contrast (Muse).** One sentence for the paper: CrossCat assigns each feature to exactly one system, whereas these categories include properties of other kinds in their clusters.
- **Tier B (Muse, from Gries & Divjak).** Record the source of every token, and hold genre and variety constant where possible.

## Checks on the answers

- **Muse §5 is wrong on the algebra; Codex has the right caveat.** Muse objects that M1 has "two coefficients for three states", so the latent-class log-odds isn't in M1's span. With M1's intercept it is, exactly. A numerical check (random parameters, mean imputation, half the cells missing) gives a residual of 1e-14. It stops being exact only if row-specific testimony or absence-strength weights enter the membership fit (residual 1.6). Codex's point is what matters: M2 maps the posterior through a nonlinear link, and it fits its parameters without the target. So the span identity doesn't make M1 and M2 equivalent, and (b) should be worded as predictive sufficiency at this n.
- **Muse is right that the Shmueli note is stale on one point.** Reference-row concealment is no longer "a Brett decision": FREEZE-v4 line 549 applies it to reference rows.
- **Both say two reading notes overgeneralize.** In the Erosheva note, "will follow the prior" at 46 rows is the agent's prediction, not the source's finding; the source's caution concerns one 5,000 × 10 simulation (reprint p. 19). In the Kemp & Tenenbaum note, "a partition result is close to the default" generalizes from one animal dataset (Fig. 5). Treat both as conjectures.
- **Every quotation the eight notes attribute to a source** was string-checked against the PDF text tonight, and all were found.

## Codex's responsibility notice

Codex opened with a RESPONSIBILITY NOTICE. FREEZE-v4 §2 calls M3 against M2 a "sufficiency test", but a small gap can reflect estimation limits. Nothing is acting on that wording (the draft is unapproved, and the audit hasn't run), so I've paused nothing and raised no hold. Edit (b), which both models endorse, resolves it.

## A day that fits both answers

1. Paper: the Magnus and Franklin-Hall paragraphs, the table's Grouping cell, and optionally the CrossCat sentence; then DECISIONS adjudications.
2. FREEZE-v4 text fixes: a (with the concealed-versus-missing split), b, c, the g items above, posterior predictive checks as the main sufficiency evidence, and the P12 fix.
3. Your decision on the order: harness first (Muse, and my recommendation) or audit first (Codex).
4. Your decision on simplifying: make the single-diagnostic and convergence-score comparators co-primary, with M2 kept only if it beats them in the harness.

Not tomorrow: the 552-packet audit (Muse's "one thing not to do"), CrossCat or the two-feature model (Codex's), and grade-of-membership fitted to the real data (both).
