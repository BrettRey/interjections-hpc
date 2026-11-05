# Source reading: shafto-etal-2011-crosscat
<!-- SUMMARY: subagent reading of shafto-etal-2011-crosscat for the inquiry-relative paper and the matrix-lesion study, saved verbatim by the parent session; key quotations spot-checked against the PDF · status: received · updated: 2026-11-04 -->

Saved verbatim by the parent Claude session from the subagent's hand-back. The parent spot-checked the key quotations against the PDF.

No RESPONSIBILITY NOTICE: I found nothing material.

**Source:** Patrick Shafto, Charles Kemp, Vikash Mansinghka & Joshua B. Tenenbaum, "A probabilistic model of cross-categorization", *Cognition* 120(1): 1–25 (2011), doi:10.1016/j.cognition.2011.02.010. I checked every quotation and page number against the PDF. pdftotext drops minus signs, so I read signs off the rendered pages (pp. 11, 12, 17). The paper never uses "view". Its terms are "system of categories" and "feature kinds".

**1. The model**

The base model, which they call the "single system model", is Anderson's rational model. It's a Dirichlet-process mixture over a binary object × feature matrix. Its prior is a Chinese Restaurant Process: "The CRP states that the probability of assigning the object to an existing category is proportional to the number of objects in that category, and the probability of assigning that object to a new category depends on a single parameter" α (p. 22, Eq. 3). Within each category, each feature gets a beta-Bernoulli likelihood (Eq. 4, p. 22).

CrossCat adds a second CRP, which partitions the features. It "extends the approach of the single system model by allowing there to be potentially many systems of categories, where each system categorizes the objects based on a subset of the features" (p. 6).
- **Posterior:** p(s,{w}|D,δ,α) ∝ p(s|α)p({w}|α)p(D|s,{w},δ) (Eq. 2, p. 7).
- **Parameters:** one α governs both CRPs (p. 7). All runs fix α = 0.5 and δ = 0.25 (fn. 4, p. 7).
- **Inference:** Gibbs moves of objects within a system alternate with Metropolis–Hastings moves of features between systems (p. 23).
- **Core claim:** "Our approach fixes neither the categories nor the feature kinds, and allows both to mutually constrain each other" (p. 3).

All the rival models are built on the same base:
- the single system model;
- two features-first models: subset attention (random feature subsets) and subset search (subsets of similar features) (p. 7);
- an objects-first model, repeated recategorization, which re-clusters the features the first solution explains poorly (p. 8).

**Experiment 1** used three artificial sets of "eight objects and six features" (p. 8) and 30 sorters (p. 10). Correlations with sort frequencies:
- 3/3 orthogonal set: CrossCat r = 0.91; rivals 0.16, 0.16, −0.76 and −0.88 (p. 11).
- 3/2 set: CrossCat 0.70; rivals −0.06 to −0.28 (p. 12).
- One-system set: a rough tie (p. 12).

**Experiment 2** used 22 animals × 106 features (p. 13; fn. 13, p. 21) and 13 instruments (p. 13), with 25 participants. The text never gives the number of instrument features. On pairwise co-membership CrossCat barely beat subset search: 0.71 vs 0.70 for animals and 0.86 vs 0.85 for instruments (p. 17). Its clearer wins were on the most divergent pairs and on how many categories people formed (pp. 17–18).

**2. Bearing on the paper**

The analogy holds in one place: "categories can be mutually exclusive (within a system of categories) or overlapping (across systems)" (p. 19). That matches the *damn* pattern, where standalone and prenominal uses fall together in one system and apart in another. Exclusivity within a system isn't a break, because Brett's groupings are also yes/no.

It breaks in four places:
- **(a) One feature, one system.** Each feature belongs to exactly one system. The authors call this "a simple starting point" (p. 6) that "will ultimately need to be relaxed" (p. 19). So CrossCat can't represent a classification that "counts properties of other kinds in its cluster" (the paper's abstract). The fix they propose, an Indian Buffet prior with noisy-AND, is untested (p. 20).
- **(b) Bottom-up versus top-down.** Systems are learned from co-variation alone. The authors grant that "Top-down information, such as intuitive theories and verbal statements, also plays a key role in cross-categorization" (p. 22). Brett's inquiries are top-down: "An inquiry identifies a question and a standard of success."
- **(c) Level.** CrossCat is a rational model of how lay people sort. It isn't an account of what warrants a category for an investigator.
- **(d) Causes.** The authors treat systems as distinct causal histories: "nature is composed of many different sets of joints, reflecting a complex of causal histories, and the problem is to infer the joints that separate these histories" (p. 21). In the working paper, categories "can share causal processes."

So CrossCat is a formal analogue of crosscutting classification, not of inquiry-relativity. It's useful as precedent and as contrast.

**Suggested sentences** (the citation key is a placeholder):

\textcite{shafto2011} model crosscutting classification as joint inference over several systems of categories, exclusive within each system and overlapping across them, so that one object can be grouped with different objects for different features \citep[6, 19]{shafto2011}. Their model gives each feature to one system, an assumption they expect \enquote{will ultimately need to be relaxed} \citep[19]{shafto2011}. The classifications here differ in counting properties of other kinds in their clusters, and in being fixed by a question rather than learned from co-occurrence.

**3. Bearing on the study**

In the paper's terms, FREEZE-v4 is features-first: "constraining features first, then inferring the best system of categories to explain those features" (p. 7). But the paper argues against random or similarity-chosen subsets as models of human sorting. It says nothing against theory-chosen anchors for an inquiry. Within a single system, CrossCat generalizes the FREEZE-v4 model in two ways:
- the number of classes is learned, not fixed at 2;
- δ = 0.25 pushes feature rates toward 0 and 1, whereas Beta(2,2) pulls them toward 0.5.

**CrossCat could test the design but shouldn't replace it.** Fit it to the diagnostic columns, or enumerate two-system solutions as they did (p. 11). Then check whether the learned feature partition reproduces INTJ {P01–P05, P07} against EXPRESSIVE {P07, P08, P10, P11}.
- P07 can sit on only one side, so the one shared diagnostic is exactly what this check can't test.
- If the partitions agree, the theory-chosen anchors are also where the co-occurrence splits.
- If they disagree, either the question draws a line that co-occurrence doesn't, or the data are too thin. The fit alone can't tell which.

**The Round 7 candidate isn't CrossCat.** It fixes two binary systems and lets a target load on both, which CrossCat forbids. That puts it closer to the authors' Indian Buffet extension (p. 20).

**Estimability.** In their real-world sets, features far outnumber objects. CrossCat learns feature partitions across features, so the study's binding constraint is about 12 features, not 46 rows. If P10 and P11 stay thin, EXPRESSIVE may have only two informative columns. CrossCat sends weak columns to a catch-all system: "the features in this system have little discriminative ability, and therefore should not be attended to" (p. 13). The paper gives no criterion for estimability.
- My judgement: it would run, but return a diffuse, α-sensitive posterior over feature partitions.
- Only the Round 7 harness, with knownness patterned on the yield audit, can settle this. If it doesn't recover planted two-system structure there, drop it.

**Missing data.** The paper runs "MCMC over the complete data set" (p. 7) on complete binary matrices. The instrument data were thresholded at two of four raters (fn. 8, p. 13). I searched the full text for "missing", "unobserved", "sparse" and "incomplete" and found nothing.
- Eq. 4 counts only observed values, so leaving unknown cells out is a routine extension if missingness is ignorable. The paper never shows this.
- The study's missingness isn't ignorable anyway. P11 is inapplicable without a host, and whether a cell is documented depends on which literatures discuss the item.

**4. Conflicts with Brett's commitments**
- **Converging diagnostics, no single property decides:** compatible within a system, since no feature is weighted by hand. But CrossCat also decides which diagnostics belong to which grouping, and it can send one to the catch-all system.
- **Absences count:** compatible. Eq. 4 treats presence and absence counts alike, and "values are symmetric" (fn. 7, p. 10). But their 0 means "judged to be false" (Fig. 1 caption, p. 2). Nothing separates a documented absence from an undocumented cell.
- **One anchor, with other kinds in the cluster:** a direct conflict, because each feature can belong to only one system. Systems also come out unlabelled, so a post-fit check like FREEZE-v4's (d) would be needed to say which learned system is which.
