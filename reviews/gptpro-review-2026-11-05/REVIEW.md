<!-- Saved verbatim by the parent session (Claude Opus 5.5) from Brett's paste, 2026-11-05 18:20 EST. Route: GPT-Pro (ChatGPT), reviewing matrix-lesion-review-2026-11-05.zip (SHA-256 09f1d49d…). Sandbox links in the original pointed into the reviewer's own workspace and are kept as pasted. Brett also attached ~/Downloads/rows-wiktionary.tsv, byte-identical to analysis/matrix-lesion/wiktionary-2026-11-05/rows-wiktionary.tsv. -->

## Summary

I wouldn’t freeze v4 or run the 552-packet sealed yield audit as currently designed. I’d first repair the evidence record, use it to strengthen the paper’s literature-based argument, and decide whether one narrower empirical test would add enough to justify pursuing it.

The archived Round 7 summaries reproduce from the raw records. The larger problems concern what was simulated and what the resulting comparisons mean. In particular, M2 introduces additional attenuation even with correct membership probabilities; its baseline smoothing differs from M0’s; and every informative shared target was generated to favour INTJ.

The source matrix is useful, but its headline counts aren’t measures of usable evidence for the proposed study. The 13 principal columns contain 168 populated cells, including 61 supported only by Wiktionary. Several transformations lose qualifications, confuse page-level evidence with evidence about a specified use, or preserve values incompatible with the revised definitions.

Some supposedly logical repairs also need reconsideration. The written position definitions don’t establish that N/N/N is impossible; strengthening and redundancy aren’t exhaustive repetition outcomes; and P07D and P11E don’t record one fact for mixed-content expressions.

Finally, the search for form properties has imposed too strong a criterion. Expressives needn’t possess a form property that separates them from interjections: the proposed categories overlap. Quirk’s focus-related placement is also not the only reported cross-slot candidate.

These findings warrant changing the empirical strategy. They don’t warrant abandoning the paper.

## 1. The evidence matrix: useful extraction, unreliable conversion in consequential places

The strongest aspect of this work is its preservation of source reports, quotations, rejected rows, and development history. That makes the errors below discoverable. The advertised totals also match the JSON, and all 131 entries in the archive’s checksum manifest matched.

However, **the matrix is currently a finding aid with partially normalized claims, rather than a dataset ready to support v4’s analysis**.

### What the planned columns actually contain

I counted the following directly from matrix.json[matrix.json](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/04-source-matrix/expressive-sources/matrix.json), using `rows[].cells` and their constituent `entries`.

These are counts of what the file stores, before correcting the substantive problems below. *Conflict* means that the cell contains both Y and N. *W-only* means that all its entries come from Wiktionary. The final column counts the script’s configured publication families after excluding Wiktionary; it doesn’t certify independent observations.

| Property | Y-only | N-only | Conflict | W-only | At least two non-W families |
|---|---:|---:|---:|---:|---:|
| P01: standalone | 22 | 1 | 0 | 2 | 9 |
| P02: supplement | 23 | 0 | 0 | 2 | 5 |
| P03: integrated | 15 | 3 | 0 | 3 | 9 |
| P04: dependents | 12 | 0 | 0 | 5 | 1 |
| P05: inflection | 4 | 0 | 1 | 4 | 0 |
| P06: determiner/plural combination | 5 | 0 | 0 | 2 | 0 |
| P07D: descriptive content | 12 | 6 | 1 | 11 | 4 |
| P08: stance | 19 | 0 | 1 | 10 | 2 |
| P09: depiction | 0 | 0 | 0 | 0 | 0 |
| P10S: strengthening under repetition | 7 | 2 | 0 | 0 | 1 |
| P11E: interpretation under negation | 0 | 0 | 0 | 0 | 0 |
| P12S: hosted prosodic separation | 3 | 0 | 0 | 0 | 0 |
| P13: anomalous phonology | 6 | 25 | 0 | 22 | 0 |
| **Total** | **128** | **37** | **3** | **61** | **31** |

Thus, 197 of the headline 365 cells lie outside these 13 columns. The expanded properties may be useful, but they don’t establish the proposed analysis’s evidence supply.

The distribution across bearers also matters. Across these columns, the ordinary control stratum has only four cells with an entry currently marked unhedged, nonsecondary, and non-Wiktionary. The regional extension stratum has none. P12S’s three item-level positives concern BASTARD_SUPP, YES, and NO, all from CGEL. P10S is concentrated in a few repetition examples and heterogeneous patterns.

There are also **81 class-statement records** for these columns. Some could materially improve coverage, particularly the negative distributional evidence for interjections. It would therefore be wrong to conclude from the item-level table that the literature cannot support an analysis. The correct conclusion is that **the supply of admissible, appropriately differentiated evidence remains unestablished**.

### A. The pipeline promotes page-level evidence to item-level evidence

build_long.py[build_long.py](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/04-source-matrix/expressive-sources/build_long.py), line 123, determines scope from the item identifier. At line 130 it assigns `"item"` whenever it recognizes inventory IDs, without respecting the input scope field.

Of 241 Wiktionary input records, 106 have a page-level scope. Those become 119 long-table rows, covering 101 bearer–column pairs, all labelled item-level. This affects substantive columns, including phonology and inflection.

One particularly clear example is BASTARD_SUPP/P06. rows-wiktionary.tsv[rows-wiktionary.tsv](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/04-source-matrix/wiktionary/rows-wiktionary.tsv), line 183, quotes:

> “Some bastard stole my car while I was helping an injured person.”

The same record explicitly warns:

> “This is the argument (subject) use, not the supplementary epithet”.

That warning disappears. In `matrix.json`, `rows[id=BASTARD_SUPP].cells.P06` presents the Wiktionary entry without a hedge and counts it alongside CGEL as two primary families.

The quoted example genuinely contains a determiner. It doesn’t independently establish the property for the specified supplementary use. The error concerns bearer identity and corroboration, even if other evidence ultimately supports the cell’s value.

### B. A token-specific absence becomes a universal negative

REPORT-ljung2011.md[REPORT-ljung2011.md](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/04-source-matrix/expressive-sources/REPORT-ljung2011.md), line 66, records FUCKING_PRENOM/P08 as **“N (one token)”** and explains that Ljung excludes dislike for that token only.

`build_long.py`, line 120, reduces this to N. The hedge detector doesn’t recognize *one token*, and the explanatory note is discarded.

The resulting matrix reports an unhedged Y/N conflict. Under the revised possibility claim, however, an occurrence without affect doesn’t contradict evidence that the use can convey affect. This is a false conflict introduced by normalization.

### C. The P10 migration hasn’t been completed

The two item-level P10S negatives are OUCH and OOPS. Their evidence is Gutzmann’s odd distributed repetition examples, together with the statement that isolated UCIs aren’t repeatable without sounding odd. See REPORT-gutzmann2013.md[REPORT-gutzmann2013.md](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/04-source-matrix/expressive-sources/REPORT-gutzmann2013.md), lines 27 and 34.

But the revised schema explicitly distinguishes:

- repetition being unavailable;
- repetition being available but never strengthening the contribution.

Under that scheme, evidence of unavailability belongs under P10A and makes P10S inapplicable for that pattern. The matrix instead retains both as unhedged P10S=N.

Moreover, neither the long table nor the JSON has the structured repetition-pattern field that the protocol requires. Adjacent repetition, distributed recurrence, and recurrence across different uses therefore remain liable to aggregation.

Both apparent negative cells for this diagnostic need reconsideration.

### D. P13’s apparently abundant negatives don’t meet the stated standard

Of the 25 negative P13 cells:

- 20 are supported only by Wiktionary pronunciation records;
- five are secondary Ljung statements already hedged because they don’t transcribe the forms or establish the required exclusion.

An ordinary pronunciation establishes the availability of that pronunciation. It doesn’t establish that the specified use lacks every conventional anomalous variant in the stated community.

The protocol itself recognizes this distinction: FREEZE-v4.md[FREEZE-v4.md](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/02-protocol/FREEZE-v4.md), line 754, requires evidence “excluding all such variants”.

The pronunciation information should be retained. It could support a different, accurately scoped property such as *an ordinary variant is documented*. It shouldn’t supply the current universal negative merely because a dictionary lists no anomalous variant.

Consequently, the strongest-looking two-polarity target in the table is much weaker than its counts suggest.

### E. Qualifications are lost from both individual and class records

There’s a deterministic bug in build_matrix.py[build_matrix.py](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/04-source-matrix/expressive-sources/build_matrix.py):

- Line 49 registers the OH/Gutzmann use-mismatch hedge under P07.
- Line 66 converts P07 to P07D.
- Line 79 looks up the hedge using the converted identifier.

The hedge therefore disappears from OH/P07D, even though the source concerns surprise and the inventory specifies change-of-state/receipt.

The class-record problem is broader. At line 89, the JSON writer retains only class, column, value, source, page, and quotation. It drops hedge and secondary-source fields. The long file contains 15 hedged class rows and seven flagged secondary class rows; those qualifications aren’t preserved in the JSON representation.

Keeping class statements separate is good. Keeping them separate **while dropping the information needed to interpret or inherit them** is insufficient.

### What I’d retain and change

The publication-family grouping is a reasonable coarse sensitivity convention. It isn’t an observation genealogy: shared authorship doesn’t establish that every observation is dependent, and different publications don’t establish independence. The headline “64 cells supported by two or more families” should be described accordingly.

The grammar hand mapping also makes several sound decisions. For example, `normalize_grammar.py`, line 215, declines to turn *in general* into N; line 218 drops an N restricted to the combinations shown. That care needs to be applied consistently across extraction branches.

Finally, the quotation checks establish less than the production protocol requires. `check_quotes.py`, line 55, accepts ellipsis-separated pieces whenever all occur on the page, without checking their order or continuity. FREEZE-v4, line 504, says ellipsis-joined text isn’t a quotation. This doesn’t demonstrate fabricated quotations, but it means a passed check doesn’t certify the stricter rule.

The original books and page images are absent from the bundle. I could verify transformations against the supplied reports, but couldn’t independently rerun most original-source quotation checks.

## 2. Several revised definitions still need conceptual repair

### POSITION: N/N/N hasn’t been shown to be impossible

The complement note says:

> “N/N/N is impossible, because a use occurs somewhere.”

FREEZE-v4 adopts that claim at line 791. But the actual columns cover:

- conventional standalone utterances;
- occurrence beside a complete clause without entering its construction;
- argument, complement, or modifier positions.

Those aren’t demonstrably exhaustive of the declared bearer universe, which includes subword expressions. BLOODY_INFIX is the immediate test case: an inserted subword doesn’t automatically occupy an argument, complement, or modifier position in the relevant syntactic sense. P02’s wording also doesn’t cover every supplementary relation to a subclausal expression.

I’m not claiming that BLOODY_INFIX has a verified N/N/N profile. I’m saying that **the exclusion doesn’t follow from the written definitions**.

You could broaden P03 into an explicitly exhaustive residual category, or retain the more informative distinctions and allow uncovered environments. That choice precedes any decision to forbid a simulated state.

There’s also an implementation mismatch: the current harness removes N/N/N from generated matrices, while its fitted latent-class likelihood still assigns positive probability to it. First settle the linguistic definitions; then align generation and fitting, or explicitly investigate the consequences of their disagreement.

### Repetition: there is a fourth admissible state

FREEZE-v4, line 796, treats P10S/P10R like a complementary possibility pair and states that there’s no fourth state.

But strengthening and redundancy aren’t exhaustive. The schema itself recognizes event multiplication. It permits this description:

- repetition is available;
- it adds depicted events;
- it doesn’t strengthen the same contribution;
- it isn’t redundant.

Thus P10A=Y, P10M=Y, P10S=N, P10R=N is coherent under the project’s distinctions. Leaving P10M outside v1 doesn’t make that combination impossible.

The three-state logic for complementary predicates has been transferred to predicates that aren’t complements.

### P07D and P11E don’t record “one fact”

FREEZE-v4, line 251, says:

> “A family declared to record one fact (TRUTH_CONDITIONAL: P07D and P11E) counts once”.

But P07D concerns whether the **use** contributes descriptive content, whereas P11E concerns whether the **specified contribution** falls within negation’s scope.

A mixed expression can contribute descriptive content while its expressive contribution remains outside negation. P07D=Y and P11E=N are therefore compatible without constituting an exception or coding error.

Conservative pooling of related evidence might be sensible. Its justification should distinguish:

- shared observations;
- shared theoretical derivation;
- correlated but distinct properties;
- genuinely equivalent propositions.

Those aren’t interchangeable reasons for assigning one total likelihood weight.

### “Never” and finite non-occurrence need different evidential treatment

FREEZE-v4, line 779, defines N as *never*, while line 529 retains a rule assigning N after K opportunities with no occurrence.

Finite non-occurrence is informative negative evidence. It doesn’t by itself distinguish impossibility from a low occurrence rate. For illustration, a property occurring on 5% of independent opportunities still yields zero occurrences in 20 opportunities about 36% of the time.

The solution isn’t to discard absences. Preserve the opportunities, conditions, counts, and uncertainty, and distinguish them from an attributed categorical exclusion. A numerical K cannot resolve the difference between those evidential objects.

Similarly, a starred example bears on its specified construction. A question mark or pragmatic infelicity mark shouldn’t automatically become a universal N for a broader possibility claim.

### Some proposed targets are already embedded in bearer identity

The inventory describes DAMN_REACT as a “standalone and supplementary stance use”, DAMN_NP as “complement-taking”, and BLOODY_INFIX as “infix (tmesis)”. See items-v4.csv[items-v4.csv](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/02-protocol/items-v4.csv), lines 14, 15, and 42.

Those may be appropriate ways to distinguish uses. But predicting those identifying properties doesn’t test an independent projection merely because the corresponding quotation has been concealed.

For every proposed inference, distinguish a property used to identify the bearer from a property investigated in another environment or realization. This is a design issue that proposition-level concealment alone can’t solve.

## 3. What Round 7 establishes—and what it doesn’t

The numerical work is more reliable than the measurement pipeline.

Every numerical summary was reproducible from the 2,200 archived raw calculation records using the saved true values. There were no discrepancies at a tolerance of 10⁻¹³. The central figures in RESULTS.md[RESULTS.md](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/03-round7/RESULTS.md) are therefore not invented or arithmetically misreported.

At `summary["cross/audit/q=0.55/split"]` in results-round7.json[results-round7.json](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/03-round7/results-round7.json):

| Quantity | INTJ | EXPRESSIVE |
|---|---:|---:|
| Median full-record membership Brier skill | 0.718 | 0.243 |
| Median family M2 gain | 0.0276 | 0.0050 |
| Proportion of projection fits passing all four checks | 0.981 | 0.587 |

Selected INTJ projections illustrate the limits:

| Target | Oracle gain D | Median estimated gain | 5th–95th simulation percentiles | Computable datasets |
|---|---:|---:|---:|---:|
| P06 | 0.1119 | 0.0892 | 0.0003 to 0.2476 | 100/100 |
| P13 | 0.0758 | 0.0848 | −0.0153 to 0.2434 | 100/100 |
| P12 | 0.1885 | 0.0154 | −0.0236 to 0.0673 | 42/100 |

Those percentiles describe variation across simulated datasets. They aren’t uncertainty intervals for a future empirical result, and the planned paired row-bootstrap uncertainty procedure wasn’t simulated.

The defensible conclusion is that, under these constructed conditions, some INTJ structure is recoverable, EXPRESSIVE recovery is substantially weaker, and a large true association can yield little usable recovery after documentation and concealment.

### A new issue: M2 introduces additional attenuation

FREEZE-v4, line 123, estimates class target rates from reference rows “weighted by their own membership”. harness.py[harness.py](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/03-round7/harness.py), line 553, implements that fractional weighting; line 555 then mixes those rates using the target row’s membership probabilities.

When those probabilities represent uncertainty about a discrete class, this isn’t generally a consistent estimator of the class-specific target rates.

Consider a large-sample example:

| | Lower-membership rows | Higher-membership rows |
|---|---:|---:|
| Correct membership probability | 0.2 | 0.8 |
| Correct target probability, with true class rates 0.1 and 0.9 | 0.26 | 0.74 |
| M2 prediction after fractional rate estimation and mixing | 0.4136 | 0.5864 |

The fractional weighting first attenuates the estimated class contrast; the prediction then mixes those already attenuated rates.

This can be defended as a regularized predictor. It shouldn’t be interpreted as recovering class-specific rates, and its attenuation shouldn’t be attributed entirely to sparse documentation or poor membership recovery.

A more direct alternative is to estimate the two target rates from reference outcomes under the mixture probability `(1−w)θ₀ + wθ₁`, keeping the diagnostic membership fit separate from the held-out outcome. Whether that alternative performs better at this sample size remains an empirical question.

### M2 and M0 have different smoothing even without category information

When all membership probabilities equal 0.5 and the class-mass fallback doesn’t apply:

- M0 predicts `(sum of outcomes + 1)/(n + 2)`;
- M2 predicts `(sum of outcomes + 2)/(n + 4)`.

That follows from harness lines 548 and 553. Thus M2 can differ from M0 solely through stronger smoothing, even when membership distinguishes no rows.

A matched-smoothing baseline is needed to separate that source of performance from information carried by the grouping.

### The oracle comparison deliberately changes the estimand

`RULE.md`, line 145, defines D using the true class and true target. The reported estimator uses inferred memberships and a selectively documented, partly corrupted record.

Comparing them is useful as an end-to-end benchmark. It isn’t ordinary recovery of the same parameter. The gap combines:

- information unavailable in the permitted diagnostics;
- membership-estimation error;
- documentation and coding effects;
- target-rate estimation;
- finite-reference estimation and smoothing.

For that reason, P12’s estimate/D ratio of roughly 0.08 shouldn’t be read as the fraction of a single underlying quantity successfully estimated. I’d describe these as comparisons with an oracle and disentangle the sources of loss if further simulation is justified.

### The shared targets all favour INTJ by construction

The saved `meta.true_values.D_shared` gives INTJ-minus-EXPRESSIVE advantages of:

- P06: 0.0736;
- P12: 0.1375;
- P13: 0.0722;
- P09: zero.

Round 7 therefore tests recovery of one ordering. It doesn’t test whether the procedure recovers different comparative advantages for different inquiries.

A reversal isn’t required for the real categories to be legitimate. But a simulation intended to demonstrate sensitivity to such inquiry-relative advantages needs at least one world in which EXPRESSIVE predicts an independently specified shared target better.

### Several existing caveats are correct and consequential

The corrections at the end of RESULTS.md already acknowledge the unmatched bonds targets, erroneous applicability rule, defective predictive check, inclusion of projections the protocol would suppress, and the limited interpretation of M3 versus M2. Those shouldn’t be presented as new discoveries.

Two further qualifications matter:

- **Cap versus split isn’t a paired comparison.** The reported shared-mean sign-error counts are 8/54 versus 2/42, but the conditions use independently generated datasets. The difference in computability itself cannot be caused by the weighting rule. These results don’t isolate weighting’s effect.
- **Residual checks concern different fits from the scored predictions.** FREEZE-v4, line 346, requires checks after each fit, including diagnostic–target dependence. The harness calls its check only in the full-record fit at line 602, and checks diagnostic pairs only.

Graphical discrepancy checks would suit your evidential policy, but changing the display isn’t enough: the replicated data need to represent the relevant observation process and the fits actually used for prediction. This is consistent with Gelman and Shalizi’s emphasis on comparing observed data with what the fitted model generates. [arxiv.org](https://arxiv.org/html/1006.3868v4?utm_source=chatgpt.com)

### A rerun of the current harness would still not validate current v4

The current code still uses the old P07/P11N/P12 schema and doesn’t implement the revised TRUTH_CONDITIONAL pooling. P11N-to-P11E is explicitly nonmechanical, so the two position fixes aren’t enough.

There’s also a reproducibility defect in `resummarize()`: line 1203 pops `harness_sha256`, which is absent from the supplied rebuilt metadata. Fixing that alone would leave another problem: line 1201 generates new benchmark truths under the revised world while reading raw calculations from the old world.

The archived summaries remain reproducible using the saved truths. The current entry point needs repair before reuse.

## 4. Concealment and thresholds still leave two larger inferential problems

### Holding out a cell doesn’t necessarily hold out a proposition

The harness’s testimony IDs represent source × row. In the as-run code, line 256 assigns `si * N + r`. Same-inclusion concealment compares diagnostics with the target’s unit within that row; target-rate estimation then leaves out only the scored row.

Suppose one grammar states that a class has a property and explicitly includes ten forms. The resulting ten target cells are applications of one generalization. Holding out one while retaining the other nine can test reconstruction of the organized record. It doesn’t create an independent test of that generalization.

FREEZE-v4, line 483, correctly says such cells don’t “multiply independent confirmations”. The harness has no corresponding cross-row assertion representation.

For a stronger claim, withhold the underlying target proposition wherever it supplies the evidence, or score independently obtained target observations. If that leaves no reference outcomes, the evidence contains one generalized assertion rather than multiple independent tests.

This doesn’t justify excluding class-level evidence wholesale. It requires counting and using it at the right level.

### The estimability gates haven’t actually been retired

FREEZE-v4, line 893, promises reporting “without thresholds”, but line 268 withholds grouping interpretation unless all four numerical checks pass. Line 903 calls the conditions “arithmetic, not judgments”.

They aren’t merely arithmetic. Ten supporting rows, five jointly visible rows, correlation of 0.8, and anchor separation of 0.3 are substantive decision rules. Nor does a target with only one observed outcome value make smoothed predictive loss mathematically incalculable; it makes certain comparisons uninformative or dependent on regularization.

Structural identifiability, weak empirical identification, unstable fitting, and an unconvincing class orientation should be distinguished. They aren’t certified by those four thresholds. For example, even the standard latent-class identifiability results depend on the number and structure of observed variables, not a universal row-count floor. [arxiv.org](https://arxiv.org/pdf/0809.5032?utm_source=chatgpt.com)

I’d report continuous diagnostics and the consequences of alternative specifications, while identifying genuine mathematical or evidential nonidentification explicitly. Replacing the thresholds with different thresholds would miss your objection.

## 5. The form-property search asks too much—and overlooks a candidate

### Failure to find an exceptionless separator isn’t failure of a cluster

FINDINGS.md[FINDINGS.md](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/04-source-matrix/grammar-sources/FINDINGS.md), line 6, says:

> “No grammar gives a form property that holds of the expressive uses as a group and fails for the controls and interjections.”

That isn’t the criterion the paper needs.

First, EXPRESSIVE and INTJ deliberately overlap. A form property associated with expressive interjections is potentially relevant evidence, even though it doesn’t separate expressives from interjections.

Second, a fallible cluster needn’t contain a property shared by every member and absent from every nonmember. A control sharing the property changes its diagnostic value; it doesn’t automatically eliminate that value.

The appropriate question is whether a specified expressive profile changes expectations about a form property, in a declared domain, compared with relevant alternatives.

The searched passages haven’t established that comparative enrichment. But they also haven’t established its absence.

### Insertion is untested, and the present bearer builds in the answer

FINDINGS, line 13, correctly says insertion is positive for one bearer and negative for none.

BLOODY_INFIX, however, is identified through insertion. Predicting insertion for it would recover an identifying fact. A useful test would identify candidate expressions or uses independently, then investigate their licensing in specified word-internal and phrase-internal environments.

The inventory’s statement that no non-expressive English infix exists as a control doesn’t settle the design. Comparators can be expressions whose attempted insertion is judged under matched conditions; they needn’t already belong to an established category of non-expressive infixes.

The major alternatives to examine would include host prosody, a particular construction, and expression-family restrictions.

### Quirk’s pre-focus relation deserves a targeted follow-up

The proposed connection between clause-level expletives and tmesis is interesting. It remains incompletely specified.

A rhetorical transition to emotionally coloured focus and immediate placement before the most prominent syllable aren’t identical measurements. The original report acknowledges lost OCR context; FINDINGS relies on a later page-image reading that isn’t included in the bundle.

There’s also a directly relevant passage still unread: REPORT-quirk1985.md[REPORT-quirk1985.md](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/04-source-matrix/grammar-sources/REPORT-quirk1985.md), line 317, lists §8.21, containing “Such preparation for focus may be expletive”, under *Found but not read*.

That passage and its cross-references should be checked before designing a focus-placement study. Then lexical prominence and information focus should be distinguished, with ordinary degree and emphatic expressions included as comparators.

### CGEL supplies another cross-slot candidate

FINDINGS, line 22, calls Quirk’s proposal:

> “The one candidate that crosses slots”.

But REPORT-cgel2002.md[REPORT-cgel2002.md](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/04-source-matrix/grammar-sources/REPORT-cgel2002.md), line 33, reports CGEL’s generalization that certain expletive adjective–adverb pairs “systematically exclude the ·ly suffix”, illustrated by *a bloody disgrace* and *bloody disgraceful*. The report explicitly connects the prenominal and degree uses.

This isn’t an exclusive expressive marker, and it doesn’t yet establish comparative enrichment. It is nevertheless a reported cross-slot form relation.

It belongs on a relation between uses or a base-level object, rather than being copied into several rows as independent corroboration. A useful comparison would examine expressive and non-expressive adjective–adverb correspondences, including ordinary flat-adverb patterns, without first settling whether each pair constitutes one lexeme.

## 6. What follows for the paper

The paper’s central distinction survives: different inquiries can organize the same material through overlapping classifications without one classification superseding the others.

The supplied inquiry-relative-categories.tex[paper](sandbox:/workspace/scratch/b1fc85c40dfc/review-work/matrix-lesion-review-2026-11-05/01-paper-context/inquiry-relative-categories.tex) already distinguishes descriptive achievement, projective warrant, estimator performance, and causal explanation. The study should follow those distinctions more consistently.

Three adjustments are warranted.

1. **Present reported expectations with their actual scope and disagreements.** At line 482, the expressive profile includes strengthening under repetition. The newly assembled Gutzmann material explicitly challenges the generality of that property. Potts’s added *damn* tokens also concern prenominal recurrence, not a demonstration that standalone and prenominal uses respond identically to repetition.

2. **Keep cross-kind associations fallible.** At line 483, lexical-category membership is itself included among the expressive category’s associated properties. That is incompatible with requiring the expressive grouping’s form evidence to exclude interjections.

3. **Make the empirical status explicit.** The literature can warrant a scoped expectation without a new latent-class experiment. But the manuscript should distinguish a source’s generalization, independently documented applications, and a newly tested projection.

The bonds world is relevant here chiefly as a reminder that predictive dependence can arise without the fitted discrete-class mechanism. That doesn’t make the dependence scientifically useless, and it doesn’t negate the paper’s account of categories. RESULTS.md now correctly acknowledges this.

## 7. Realistic ways forward

| Option | What it would let the paper claim | Main additional work | Main risk |
|---|---|---|---|
| **Corrected evidence map plus literature-based paper** | Document crosscutting classifications, scoped expectations, disagreements, and evidential gaps | Repair transformations; preserve assertion scope and inheritance links; adjudicate consequential claims | Prose may still imply demonstrated predictive reliability where only a reported generalization exists |
| **A narrow test on new environments or realizations** | Estimate one specified projection for independently identified uses | Design comparable contexts; obtain independent interpretation or realization evidence; assess constructional alternatives | The pattern may belong to a construction or prosodic relation rather than the broader grouping |
| **A proposition-level documentary study** | Test recovery of genuinely withheld source claims from other evidence | Identify propositions and source lineage; hold out claims or independent observations rather than cells | Success remains about the documentary record, with limited transport beyond it |
| **A study of relations between uses** | Test a morphological or constructional correspondence, such as the adjective–adverb relation | Build the appropriate relation-level inventory and comparators | Shared bases or ordinary flat-adverb patterns may explain the association |
| **Rebuilt whole-matrix lesion study** | Quantify reconstruction within a declared record; stronger warrant only under additional evidence conditions | Resolve schema, inheritance, observation process, estimators, and uncertainty; then simulate the actual procedure | Considerable work may chiefly measure documentation practices and identifying definitions |

The main cost isn’t writing more extraction or simulation code. With the available workflow, that part is relatively cheap. The consequential cost is resolving distinct linguistic claims and obtaining observations that the current sources don’t supply.

### My choice

I’d choose the corrected evidence map and literature-based paper now. I’d treat a narrower empirical study as a separate decision, not as something required to rescue the paper.

The immediate development work should be:

1. Preserve the raw scope, notes, quantification, use identity, pattern, host relation, and speech community throughout the pipeline.
2. Repair the demonstrable conversion errors.
3. Link class claims to explicit inclusion evidence, distinguishing universal, generic, and existential class statements.
4. Review the distinct assertions supporting any proposed empirical target.
5. Inspect the decision-relevant omissions, especially Quirk §8.21 and CGEL’s adjective–adverb correspondence.
6. Reassess evidence supply openly before commissioning a sealed census.

Fresh coding of already inspected evidence doesn’t restore independence from the development process. Conversely, a new test needn’t always use new bearers: independently obtained observations in new environments or realizations can test the corresponding narrower claim. New bearers are necessary when the intended claim concerns generalization to new bearers.

On the outstanding decisions:

- **Class-level “never” claims:** admit them when the source’s scope and the item’s inclusion are explicit. Count the underlying testimony correctly.
- **Adjacent-turn hosts:** decide separately for negation scope and prosodic hosting. Adjacency alone doesn’t establish either opportunity.
- **Morphological relatedness:** retain the transparent string-based metadata, but specify its analytical role. It isn’t fresh evidence for category membership.
- **Lexeme identity:** keep it separate from the existence of relations among use-types; the latter can be studied without settling the former.
- **Convergence model:** don’t settle it before establishing the measurements and targets it must explain.
- **Yield audit:** don’t run the current 552-packet design now.

I’d reconsider the larger matrix study if a corrected, adjudicated subset showed that several targets have informative contrasts, aren’t part of bearer identification, and are supported by observations genuinely distinct from the assignment evidence. I’d also require an implemented analysis whose simulation evaluates those measurements and its actual uncertainty procedure.

That would provide a concrete reason to resume. More populated cells or a cleaner-looking latent partition, by themselves, wouldn’t.
