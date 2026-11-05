# Source reading: gries-divjak-2009
<!-- SUMMARY: subagent reading of gries-divjak-2009 for the inquiry-relative paper and the matrix-lesion study, saved verbatim by the parent session; key quotations spot-checked against the PDF · status: received · updated: 2026-11-04 -->

Saved verbatim by the parent Claude session from the subagent's hand-back. The parent spot-checked the key quotations against the PDF.

No RESPONSIBILITY NOTICE.

Source: Stefan Th. Gries and Dagmar Divjak (as printed, p. 57), pp. 57–75. The .md misnumbers footnotes by one; cite them from the PDF.

**Headline.** The method bears constructively on the occurrence-level design and Tier B, and on the Tier A matrix mainly as criticism: its stated advantages include that "judgments are not gathered in an introspective way that relies on implicit knowledge" (p. 60), so Tier A cells resting on grammarians' introspection are the evidence it argues against. And it takes membership as given.

**1. Method**

Atkins's ID tag: "all the collocations/colligations correlating (probabilistically or perfectly) with a particular sense are referred to as an ID tag" (p. 59). The authors use it for any coded variable ("87 variables, i.e. our ID tags", p. 66), discriminating or not. They extend Hanks's profile to "a comprehensive inventory of elements co-occurring with a word within the confines of a simple clause or sentence in actual speech and writing" (p. 61).

Steps (p. 61): sample a lemma's tokens; "a (so far largely) manual analysis of many properties of the word forms (i.e. the annotation of the ID tags)"; tabulate; evaluate. "each row contains one citation of the word in question, each column contains an ID tag and each cell contains the level of the ID tag for this citation" (p. 62). Counts per sense become within-tag percentages: "each sense of a word or each near synonym within a semantic domain is characterized by one co-occurrence vector of within-ID tag relative frequencies" (p. 63).

Evaluation: token frequency, type frequency divided by token frequency, pairwise correlation or cosine (pp. 64–65); then hierarchical agglomerative clustering with per-cluster t-values and within-cluster z-scores (pp. 66–67).

Cases: polysemous *run*, 815 citations, 252 ID tags, "many of the ID tags in this study code the presence/absence of particular collocates" (p. 67). Nine Russian 'try' verbs (near-synonymy), 1,585 sentences, 87 ID tags, "similarity metric: Canberra; amalgamation strategy: Ward" (p. 69), three clusters; per-verb N from 53 to 260 (Table 5, p. 69).

Validation: robustness checks only. Cosine "yielded the same conclusions" (n. 9, p. 69); a phylogenetic algorithm gave results "for all practical purposes identical" (n. 10, p. 70). A search of the PDF text for `experiment` finds only Sandra and Rice's methods (p. 58), "experimentally-induced biases" (p. 60) and the Russian data (p. 72). Psycholinguistic follow-up is only cited, for "the mental reality of radial categories (cf. Divjak and Gries 2008)" (p. 73): Dagmar Divjak & Stefan Th. Gries, "Clusters in the mind? Converging evidence from near synonymy in Russian", *The Mental Lexicon* 3(2): 188–212 (reference list, p. 74; no DOI given). I haven't read it.

**2. What Brett could adopt**

- Table 2 as the occurrence-level schema: one CABNC token per row, every feature with explicit levels (absent and inapplicable included) plus a per-property opportunity flag. Tier B's counts, and its Y/N/U by the K rule, then come from that table.
- Within-feature percentages (p. 63) for mechanism questions; nothing here argues for dropping K in the lesion matrix.
- Sample size: no floor is stated. Table 3's 'lack' sense has 14 tokens (p. 63).
- Stratified sampling for rare items, "keeping the genre constant" (p. 69). v4's COCA/BNC top-up mixes variety and genre with CABNC; record source per token.
- Feature range: Table 1 (p. 62) is clause-internal verb grammar, with pragmatics and prosody only possibilities ("others such as phonology or pragmatics", n. 3, p. 61), so P01, P02 and P12 lack precedent.
- Reliability: nothing to adopt. Searching the PDF text for `reliab|agree|kappa|coder|annotator|inter-rater|intercoder|validat` finds no agreement statistic; the reliability hit is "At present there is no reliable way for assigning (many) ID tags automatically" (p. 73).

**3. Absences and limits**

Zeros enter at full weight, with no opportunity standard, and identify "those cases where the co-occurrences of senses/words and particular ID tags seem impossible" (pp. 64–65). For the two 'escape' senses the chapter concedes the gap ("although both unattested combinations are conceivable", p. 68) and uses it: "While the results of a corpus-based application of the criterion of disjoint distribution are certainly dependent on sample sizes, they indicate – in the absence of evidence to the contrary – that the two ‘escape’ senses should not be lumped together" (p. 68). A zero from 53 tokens weighs what one from 260 does, and records non-occurrence among all tokens, not opportunity environments; v4's N is stricter.

Acknowledged: "the choice of ID tags to be included in the analysis and the subsequent interpretation of the results contain elements of subjectivity – as does, if to a lesser degree, the annotation/coding of the dataset" (p. 73); measure choice, since "it is impossible to recommend any one specific measure" (p. 66); collocates swamping the vector, hence a rerun "omitting collocation-based ID tags lest individual collocates distort the picture" (p. 68).

Unacknowledged: feature dependence. Composite tags ("present tense with a perfective infinitive", p. 71) overlap their components, and the distance sums over columns, so redundancy multiplies evidence; v4's "entailed" state and testimony units address this.

**4. Against Brett's commitments**

- Membership is an input: each citation "was coded for the senses they instantiate" (p. 67) before profiling, and the nine verbs were chosen in advance. Profiles compare and cluster a fixed set; they don't decide who belongs to it.
- The t-value step finds "ID tags that have a positive t-value in one cluster and negative values in all other clusters" (p. 66) from the features that built the clusters, the circularity v4's concealment avoids.
- Disjoint distribution is a single-criterion split: the 'escape' decision rests on one PP contrast (p. 68), against "no single property decides".
- Agreement: the *run* prototype argument converges seven criteria on 'fast pedestrian motion' (p. 67), and clustering uses all features at once.
- Level: the warrant is "that distributional similarity reflects, or is indicative of, functional similarity" (p. 59). A profile of interjections is corpus-distributional and can't supply EXPRESSIVE's meaning anchor (P08 has no corpus standard).

Files: /Users/brettreynolds/projects/LLM-CLI-projects/literature/gries_divjak_2009_behavioral-profiles.pdf (PDF page N = printed page N+55); /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/FREEZE-v4.md (sections 2, 4–7 read).
