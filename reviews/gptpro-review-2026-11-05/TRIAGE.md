# Triage: GPT-Pro review of the 2026-11-05 bundle, and a naive property list
<!-- SUMMARY: triage of GPT-Pro's review of matrix-lesion-review-2026-11-05.zip (most checkable claims confirmed against the files; pipeline bugs A, B, E fixed; C and D proposed; protocol, harness and paper points deferred to Brett) and of a context-free GPT-Pro property list for the seven expressive bearers, mapped onto properties-v4 · status: for Brett · updated: 2026-11-05 -->

Review: `REVIEW.md` (verbatim). Naive list: `NAIVE-PROPERTY-LIST.md` (Brett's prompt and the reply, verbatim). Triaged by Claude Opus 5.5 against the bundle's files and the repository. A model's review is a set of claims to check, not evidence.

## Bottom line

Most of the review's checkable claims are right, and several are about the extraction code I wrote:
- the code turned page-level evidence into item-level evidence;
- it dropped hedges and notes;
- it kept values the recode made invalid.

The matrix's headline counts therefore overstate how much usable evidence there is. On direction, the review recommends three things:
- don't freeze v4;
- don't run the yield audit;
- correct the evidence map, strengthen the paper's literature-based argument, and treat any narrower test as a separate decision.

Muse and Codex took nearby positions after Round 7. All three read the same record and RESULTS.md, so their agreement counts for less than three independent views. The direction is Brett's.

## Verification

**Confirmed against the files:**
- **The 13-column counts.**
  - 168 cells: 128 Y only, 37 N only, 3 with both, and 61 resting on Wiktionary alone.
  - 197 of the 365 cells fall outside these columns.
  - 81 class records bear on these columns.
  - Four cells on the general controls have an unhedged, non-secondary entry from a source other than Wiktionary; the regional extension rows have none.
  - All three P12S positives (BASTARD_SUPP, YES, NO) rest on CGEL alone.
- **A.** `build_long.py` ignores the input scope field. 106 Wiktionary records are scoped to the page (103 `page`, 2 `page (headword)`, 1 `page (hell, neighbour)`), and all of them become item-level rows. BASTARD_SUPP/P06's note was lost: "This is the argument (subject) use, not the supplementary epithet … Use it for nothing positional" (`rows-wiktionary.tsv` line 183).
- **B.** Ljung's FUCKING_PRENOM/P08 entry ("N (one token)", with the note "Treat as mixed evidence") reached the matrix as an unhedged N, which makes a false Y/N conflict.
- **C.** `properties-v4.csv` makes P10S x wherever P10A = N for a pattern. Gutzmann's distributed-recurrence examples for OUCH and OOPS show a pattern that isn't available, yet the matrix records them as P10S = N.
- **D.** Of the 25 P13 N cells, 20 rest on Wiktionary pronunciations alone and 5 on secondary Ljung statements. FREEZE-v4 line 756 says the cell must "distinguish a permitted variant's existence from evidence excluding all such variants"; the review cites line 754.
- **E.** In `build_matrix.py`, the OH/Gutzmann hedges are keyed on P07, but the lookup runs after P07 is converted to P07D, so they're lost. Class records keep only six fields, dropping the hedge and the secondary flag.
- **Quotation checks.** `check_quotes.py` accepts the pieces of an ellipsis-joined quotation in any order. FREEZE-v4 line 504 says ellipsis-joined text isn't a quotation.
- **Every FREEZE-v4 line the review cites** says what it claims: 123, 251, 268, 483, 504, 529, 779, 791, 796, 893, 903.
- **Harness.**
  - With all memberships at 0.5, M0 smooths as (s+1)/(n+2) and M2 as (s+2)/(n+4).
  - The attenuation example's 0.4136/0.5864 reproduces by hand.
  - `resummarize()` pops a key (`harness_sha256`) that the saved metadata no longer has, and regenerates the true values under the current world.
  - The as-run testimony unit is `si * N + r`.
- **Shared targets.** `D_shared` favours INTJ on every informative shared target (P06, P12, P13; P09 is zero).
- **The paper.** Lines 482–483 list "strengthens rather than becoming redundant when repeated" among the expressive properties, and interjection membership among the category's properties of another kind.
- **The grammar reports.** The CGEL report's row 33 (p. 568) links the prenominal and degree uses of *bloody* and *damn* through the missing ·ly. The Quirk report lists §8.21 ("Such preparation for focus may be expletive") under "Found but not read".

**Taken on trust, not rechecked:**
- the 10⁻¹³ reproduction of the summaries;
- the values it quotes from `results-round7.json`;
- cap against split, 8/54 against 2/42;
- that the residual check runs only in the full-record fit;
- `normalize_grammar.py` lines 215 and 218.

**One count differs.** For cells with two or more families other than Wiktionary, I get 36 and the review gets 31: P02 7 against 5, P10S 2 against 1, P13 2 against 0. My count uses uppercase (primary) sources, excludes W and collapses H/S and Q/B/R. The review's definition isn't stated. I'm leaving the discrepancy unresolved.

## Punch list

### Fixed now (pipeline bugs)

- **A.** The input scope is respected. Rows scoped to a page, headword or sense, or recorded as an alternative match, enter the matrix hedged, with their note. That covers 126 entries, all from Wiktionary.
- **B.** The hedge detector catches "one token" and notes that say "mixed evidence". One entry is affected: FUCKING_PRENOM/P08, Ljung.
- **E.** Hedges are looked up under the column before conversion too, which restores OH/P07D's hedge. Class records keep their hedge and secondary flag: 15 of the 167 are hedged and 7 are secondary.

**Effect of the rebuild.**
- No cell is added or removed, and the long table changes only in its hedge field (127 rows).
- 240 cells now carry an unhedged primary entry, down from 326. The stats field `primary_unhedged` reads 237 (down from 324) because it also excludes entries flagged secondary; 3 cells are firm only through such entries.
- The page marks a cell hedged only when every entry in it is hedged, so a firm entry beside a hedged one still shows as firm.
- The other headline counts are unchanged: 365 cells, 356 with a primary entry, and 64 with two or more families. Hedged entries still count as primary, so the 64 includes cells where one family's only entry is hedged. Counting unhedged entries only, 53 cells have two or more families.
- **Fix A is a choice, not a closure.** Rows scoped to a page are kept as item-level entries, hedged. The alternative is to exclude them from cells and show them only as corroboration. That alternative would also stop BASTARD_SUPP/P06's Wiktionary entry counting as a second family. Brett's call.
- In the 13 principal columns, P13 drops from 20 to 4 cells with an unhedged entry, P03 from 15 to 14, and P07D from 19 to 18.
- No P13 N cell keeps an unhedged N, because all 20 Wiktionary-only P13 N cells came from rows scoped to the page.
- The Bearers by Perspective page was republished from the rebuilt matrix (Version 10).

### Proposed, for Brett's word (they change values, not just code)

- **C.** Recode OUCH and OOPS from P10S = N to P10A = N for the pattern "distributed recurrence", with P10S x for that pattern. This needs the pattern field the protocol requires, which the long table doesn't carry yet.
- **D.** Fix A already hedges the 20 Wiktionary-only P13 N cells, and the 5 Ljung cells were hedged before. What's left is whether to move the Wiktionary pronunciations to a separately scoped property ("ordinary variant documented"), so they stop sitting in P13 as hedged N.
- **Quotation checks.** Check the order of ellipsis pieces, or fail ellipsis-joined quotations outright as FREEZE-v4 line 504 says.

### The FINDINGS criterion: adopted, FINDINGS.md revised

The question FINDINGS.md asked came from my brief to the grammar readers: does a form property hold of the expressive uses as a group and fail for the controls and interjections? It conflicts with the paper and with Brett's commitments:
- The paper (line 483) puts interjection membership inside the expressive cluster.
- No single property needs to separate.

The question to ask is whether an expressive profile changes what you'd expect about a form property, compared with relevant alternatives. FINDINGS should also add CGEL's missing ·ly (p. 568) as a second cross-slot candidate, recorded once, as a relation between uses rather than copied into rows. Quirk §8.21 should be read before anything is designed on pre-focus placement.

### Deferred to Brett (protocol, harness, paper)

**Definitions in FREEZE-v4 §6 and §2:**
- **N/N/N.** The written definitions don't make it impossible (BLOODY_INFIX), and the harness generates without N/N/N while its likelihood still allows it.
- **P10.** There is a fourth state: P10A Y with P10S N and P10R N, where repetition only multiplies. FREEZE-v4 line 796 says there isn't one.
- **P07D with P11E.** They aren't one fact for mixed expressions, so pooling them as TRUTH_CONDITIONAL needs another justification.
- **"Never" against finite non-occurrence.** This is adapt, since part of it is already in the text: lines 530–531 record instances among opportunities and allow a rate beside the value. What's missing is a distinction at the level of the value between a categorical N and finite non-occurrence. Question-marked examples shouldn't become universal N.
- **Targets inside bearer identity.** DAMN_REACT, DAMN_NP and BLOODY_INFIX are identified by properties a target would then "predict".

**Thresholds.** The estimability checks (line 268: 10 rows, 5 jointly visible, 0.8, 0.3) are thresholds, which conflicts with Brett's 2026-11-04 rule. The review proposes continuous diagnostics plus an explicit statement of nonidentification.

**Round 7 interpretation:**
- **M2 attenuates the class contrast,** by fractional rate estimation followed by mixing. The review proposes a mixture-likelihood alternative.
- **M2 and M0 smooth differently,** so M2 needs a baseline with matched smoothing.
- **D is an end-to-end oracle comparison,** not recovery of one parameter.
- **Every informative shared target favours INTJ,** so no world tests a reversal.
- **Cap against split** wasn't a paired comparison.
- **Residual checks** run on a different fit from the scored predictions.
- **`resummarize()`** can't be rerun as it stands.

**Concealment.** One class generalization applied to ten rows is one assertion. Holding out a single cell doesn't hold out the proposition.

**The paper:**
- the scope of strengthening under repetition (line 482), given Gutzmann's material;
- whether the expressive "membership in the lexical category interjection" (line 483) stays as written once FINDINGS' criterion is corrected (it should).

**Direction.** The review's ranked options are in its §7. Its choice is a corrected evidence map and a literature-based paper, with a narrow test as a separate decision. It would reconsider a matrix study only for targets that:
- show informative contrasts;
- aren't part of how a bearer is identified;
- rest on observations distinct from the assignment evidence.

## The naive property list

Brett prompted a fresh GPT-Pro instance with no project context to list properties of the seven expressive bearers across subfields. Its uncited contrasts are, by its own statement, its judgments. Under the project's rules that's model introspection, not evidence. What it offers is a property frame from outside the project's categories, which FREEZE-v4 §13 item 11 lists as a missing fork.

**Already columns:**

| Its property | Column |
|---|---|
| internal expandability (*the selfish bastard*, *you poor bastard*) | P04 |
| number variation (*the bastards*, *you bastards*) | P06 (and P05) |
| morphological invariance (*bloody*, *damn*, *fucking*) | P05 N |
| attributive restriction (*fucking*) | predicative N |
| external detachment; independent utterancehood | P02; P01 |
| no blood, parentage or theological entailment | P07D N |
| independence from host polarity | P11E |
| distributed repeatability (*fucking*) | P10S, with the pattern recorded |
| perspective dependence | Potts's perspective column |
| *the hell* tight after the wh-word | after wh-word |

**Candidates the matrix lacks:**
- **Restricted substitutability in tmesis** (*abso-very-lutely*). This is the *very* test FINDINGS listed as missing, and it's a form contrast with a control. It's untested until a source states it.
- **Host selectivity of *the hell*** (interrogative *who*, not relative *who*), plus embedded questions (*I wonder what the hell …*), elliptical fragments (*Why the hell?*) and the qualified polarity and D-linking restrictions.
- **The adverb without ·ly** (*bloody*, *damn*), the same relation as CGEL p. 568.
- **Evaluative target resolution.** The structural host and the evaluated target can differ for *fucking*; the epithet is aimed at a person.
- **Intensification neutral to polarity** (*bloody marvellous* / *bloody awful*, *damn slow*).
- **Separate challengeability.** *No, he hasn't* against *Don't call him that*.
- **Prosodically conditioned insertion sites,** and whether the inserted item keeps its own stress.

**Its citations are leads, not checked.**
- Held locally: Ippolito 2022 (`literature/ippolito2022hell-questions`) and Ljung 2011.
- Not held, as the paste gives them:
  - McCarthy on prosodic structure and expletive infixation (*Language*);
  - Zingler on expletive insertion (*English Language and Linguistics*);
  - Zwicky, "Hey, whatsyourname!";
  - Lo Guercio and Orlando (SALT 32);
  - the *Journal of Linguistics* paper on the aggressively non-D-linked construction and ellipsis;
  - Palacios Martínez on taboo vocatives;
  - Reed on *bloody* as an Anglo-Norman intensifier;
  - the BNC 1994–2014 swearing comparison;
  - Pullum on slurs and obscenities;
  - the "culprit hypothesis" paper (*Language and Cognition*);
  - a 2025 *Theoretical Linguistics* paper on expressive intensification;
  - the Springer paper on perspective shifting.

McCarthy and Zingler bear directly on the review's point that pre-focus placement and metrical infixation aren't one measurement.
