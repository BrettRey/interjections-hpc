# Columns that look like complements: the determinatives codebook applied to properties-v4
<!-- SUMMARY: the determinatives-as-nouns codebook's polarity rules applied to properties-v4.csv, with further lessons from that project; the fixes were applied on 2026-11-05 (see DECISIONS) · status: applied, open items in FREEZE-v4 section 13 · updated: 2026-11-05 -->

Brett asked (2026-11-05) for a close look at how the determinative matrix in `papers/queue/determinatives-as-nouns` handles groups of columns that look like simple complements but aren't. Written by Claude Opus 5.5.

## What the determinatives codebook does

The source is `planning/codebook.md` §4 (Polarity) and §5, revised after an external logic review (`reviews/external-logic-20261024-135944/`). Its rules:

- **One polarity throughout.** "Every column states a possibility, ◇P. Then n means ¬◇P (never) everywhere, and the burden runs the same way in every column."
- **Universal columns are reversed.** "must be outranked by a coindexed element" becomes "may occur without a binder".
- **Definable columns are derived, not coded.** "does not inflect" is derived from the inflection columns. Coded separately, "it contradicted them for 17 forms".
- **Absence columns are added only where needed.** The absence column ◇¬P is added "only where P can be necessary".
- **Joint states.** A ◇P/◇¬P pair, or a pair like personal/non-personal, gives three states: must, must not, either. A form for which the property can't arise is x ("a status, not a value"), not "neither". The logic review rejected an earlier four-state reading.
- **Term negation** (Horn 1989). "May be non-personal" equals "may not be personal" only where non-personal covers the property's whole domain. Otherwise it is "a contrary with gaps", and the codebook states its extension.
- **Requires versus combines with.** For head selection, "requires" and "combines with" are derived from three possibility columns (§5).
- **Secondary uses are graded, not discarded.** Set-denoting secondary uses are graded in a frame rather than discarded as different words, since discarding them "would build *CGEL*'s analysis into the data" (§3).

## Applied to `analysis/matrix-lesion/properties-v4.csv`

### 1. The position trio P01, P02, P03

These read like a three-way partition: a use is standalone, supplement or integrated. They are actually three possibility claims over one domain, the positions in which the use occurs.

- **Joint states.** Seven combinations are admissible. N/N/N is impossible, because a use occurs somewhere.
- **P02 N is derived.** Its N standard ("always integrated or always standalone") is defined through the other two columns. So it's a derived value, and one source proposition then supplies two INTJ diagnostics.
- **"Standalone-only" is a joint state**, □P01, not a column. P11N's inapplicability turns on it.
- **Consequences for the harness.**
  - `world_cross` draws the three independently. Over 2,000 simulated inventories, 7.3% of rows (3.4 of 46 on average) have the impossible N/N/N state.
  - `applicability()` reads only P01 and P02, and 49% of the rows it marks INAPPLICABLE have P03 = Y.

### 2. P11N, NEGATION_SURVIVES

This looks like "survives / doesn't survive", but neither value is a "never".

- **Y needs one example** of the contribution outside negation's scope (◇wide).
- **N needs one report** of it cancelled or embedded (◇narrow).
- **Both can hold of one use**, so they don't contradict each other.

The property Potts treats as diagnostic is the universal one: the wide reading is forced. "The content of definite descriptions can also escape up through holes, plugs, and tense operators" (Potts 2007, p. 172), and "It is this invariance that accounts for much of what is special about expressive content" (p. 172). So a Y resting on one example doesn't record the expressive property. In possibility form the column becomes "may be interpreted inside the scope of host negation", and its n (never) is the expressive hallmark.

INAPPLICABLE is the codebook's x. FREEZE §6 already says so ("an explicit inapplicable state at the assertion layer for uses with no host environment; it is not the same as an unscored unknown"). But its domain isn't fixed by P01–P03.
- **The CSV allows a standalone use to have a host.** The P11N notes list "independent adjacent turn" as a host relation, so a use that only ever stands alone can still have one.
- **FREEZE line 262 assumes otherwise.** It equates standalone with no host ("standalone rows carry at most three EXPRESSIVE diagnostics").
- **The harness follows line 262.** Its ENTAILED rule (P11N entailed by P01–P03) rests on that equation.

### 3. P10S, REPETITION_STRENGTHENS

Its N standard, "redundant or unavailable", merges two different states:
- **Redundant is an n:** repetition is possible and adds nothing.
- **Unavailable is an x:** repetition isn't possible, so strengthening can't arise.

FREEZE §6 already asks for separate fields: "split the evidence into strengthening, event multiplication, redundancy, and unavailability. More than one may be supported." The CSV hasn't caught up.

The repetition pattern is a frame in the codebook's sense. Values can differ by pattern: Gutzmann 2013 (p. 47) tests only distributed recurrence for *ouch* and *oops*.

### 4. P12, PROSODY_HOSTED

- **Y:** one report of a separate intonation unit with a host.
- **N:** "characteristic intonational integration".

Both are possibilities, and N is a typical-case claim, not "never". A use can be phrased either way.

### 5. P07, NONPROP

P07 is a universal stated negatively, so the burden runs the opposite way from P01–P05:
- **Y** ("no contribution to descriptive or truth-conditional content") needs a generalization.
- **N** needs a single assignment of descriptive content.

The codebook would reverse it: "may contribute descriptive content". Because absences weigh, an N on P07 and an N on P01 are different kinds of evidence as the schema stands. Gutzmann's mixed items (intensifier *fucking*, p. 10) fit once the column is reversed.

### 6. P09, DEPICTIVE

- **Y:** "depicting through resemblance".
- **N:** "non-iconic".

These are contraries with a gap: an iconic use that doesn't depict gets neither. The codebook would state N's extension.

### 7. P06, NOMINAL_COMB

- **Y is a disjunction** (a determiner, or plural form).
- **N includes "a conversion analysis".** That is the move the determinatives codebook refused for secondary uses: it would build the analysis into the data.

P04, P05 and P06 were made disjoint in v4. Disjoint isn't complementary, and that's fine.

## What would follow (all FREEZE or CSV text changes, Brett's call)

- **One polarity.** State every column in possibility form with n = never, or at least mark for each whether Y or N is the generalization. Otherwise an absence weighs differently from column to column.
- **The position trio as one family.**
  - Treat P01–P03 as one family with the N/N/N exclusion.
  - Derive "standalone-only", and P11N's x, from it.
  - Keep derived states out of the membership fit (codebook §9: "derived columns excluded so that nothing leaks").
  - This settles the open entailed-concealment question by construction.
- **Split three columns.**
  - P11N into ◇narrow, with "never" as its n.
  - P10S into FREEZE §6's four fields.
  - P12 into ◇separate and ◇integrated.
- **In the harness**, draw positions jointly with N/N/N excluded, and compute applicability from the joint state and host relation.

## Other lessons from the determinatives project

From `planning/codebook.md` §§5–9 and `notes/2026-10-24-codebook-and-pilot.md`. The application to this study is Claude's.

1. **Merge only on logical entailment, and pool correlated properties in families.**
   - The rule (§6): "Two columns merge only if one follows logically from the other, in the same frame." Distinct properties stay, "however strongly they correlate", and "the family structure (section 9) keeps one mechanism from counting as several".
   - Application: P07 and P11N don't entail each other as coded, since a source can support P07 = Y and P11N = N for one use. So Gutzmann's point that they rest on one fact calls for one super-column that the analysis pools over, not a merged column. This revises the merge suggested earlier in this session.
2. **The column set, not the sample, decides the test.**
   - The determinatives result (§9, tree-recovery simulation): 11 of 77 columns were properties only pronouns and determinatives can have, and none was a property only nouns can have. That was because the 2021 search looked there. The test then picked the nested tree whatever generated the data.
   - Their remedy: a column frame drawn from a source no rival chose, balanced across categories; the test run on the columns every category can have; the rest reported separately.
   - Application: the v4 properties came mostly from the interjection literature, and EXPRESSIVE got four diagnostics. Round 7's bonds result was also partly built in by construction. The expressive-source matrix of 2026-11-05 is a start on balancing the column set.
3. **Hold out the group, not the form.**
   - The determinatives point (§9): "The rivals differ only above the subcategory level, so holding out one form tests nothing that separates them."
   - Possible application, a conjecture for testing: our one-cell lesion is predicted from the row's own visible diagnostics whatever the grouping. That may be why M2 never beat the plain convergence score in Round 7. The analogue would hold out whole rows or form families.
4. **Frames proposed blind and frozen before judging.**
   - The rule (§5): "The frame list is frozen before Brett judges any cell." That way proposals come from coders blind to the point, which answers the worry that features become data-dependent. A frame "must be justified by a contrast within one word", and a property is split by frame "only where some form's value changes across frames".
   - Application: this is a working answer to the severity question raised today. Freeze the feature proposals, then code. P10S patterns, P11 operators and P12's hosted environment are frame questions.
5. **Blind coding with plain labels, several model families, and calibration against Brett's own cells.**
   - The rule (§7): coders see forms "described in plain words", "never the matrix's category-bearing names", and never the hypothesis.
   - Application: our item ids (DAMN_REACT, BASTARD_SUPP) and tiers (expr-core) carry analysis.
   - The pilot found that a definition, not coder error, explained most mismatches: gender defined by pro-form selection against gender fixed in the word. So pilot each definition against judged cells before a wave.
6. **Copies of a form must not change the verdict.**
   - The rule (§9): "duplicate the noun rows tenfold and confirm the verdict doesn't move."
   - Application: the inventory has four *damn* uses, three *bloody* uses, and two each of *bang* and *bastard*. Facts about a whole form family should be pooled by family, the way the determinatives codebook pools lexeme and base facts (§1). Examples are Ljung's "it is impossible to use damn(ed) in such a way" (p. 151) and Gutzmann's multifunctional *damn* (p. 10).
7. **An "accepted" status audited by a gold sample.**
   - The proposal (§11, fork 7): cells where all model families agree are accepted subject to Brett's judgment of a stratified random sample. The design is borrowed from `papers/development/diagnostic-validity`: a seeded gold sample with corrections in the manner of prediction-powered inference.
   - Application: this is a far cheaper route to coded evidence than the 552-packet sealed audit, and it bears on the open yield-audit decision.
8. **Smaller rules worth adopting.**
   - x is distinct from U everywhere, not just for P11N.
   - m is kept for degraded acceptability only.
   - Register and variety are a field, not a value.
   - Every n carries the strongest counterexample the coder considered.
