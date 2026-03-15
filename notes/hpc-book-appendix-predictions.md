# Notes on Appendix: Predictions (HPC Book)

**Source file:** `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/appendix_predictions.tex`

---

## 1. Overall Structure and Purpose

The appendix is explicitly framed around **accountability and testability**. The opening paragraph states:

> "This appendix collects the empirical predictions that the HPC framework generates across the book's case studies. The point is accountability: if the framework is to be preferred over essentialism and prototype theory on grounds of testability, the predictions should be findable in one place, each with a source chapter and a defeat condition that says what would count as disconfirmation."

### Prediction Format

Each prediction uses a custom LaTeX macro `\prediction{ID}{Title}{Description}{Source}{Defeat}` with five fields:

1. **ID** (e.g., P1, P2, ... P30, D1, D2)
2. **Title** (a short label, e.g., "Asymmetric fraying")
3. **Description** (the substantive prediction, typically 2-4 sentences)
4. **Source** (chapter reference)
5. **Defeat condition** (what would count as disconfirmation)

This is a rigorous format: every prediction has a named falsification condition. The appendix explicitly acknowledges variation in sharpness:

> "Predictions vary in sharpness. Some are quantitative (P28 specifies that conditioned models outperform pooled baselines on a measurable metric); some are directional (P1 predicts that tight diagnostics erode before loose ones, without specifying rates); some are consistency checks (P20 predicts within-family correlation without specifying its magnitude). All are defeasible."

---

## 2. Taxonomy of Predictions

The predictions are organized into two tiers:

### Tier 1: Framework Predictions (P1-P11)
These "follow from the HPC architecture itself: any maintained category, in any domain, should exhibit them." These are the most relevant for the interjections paper because they apply to *any* HPC category.

### Tier 2: Case-Study Predictions (P12-P30)
These are specific to domains examined in the book: countability, definiteness/deitality, grammaticality, pro-form gender, social stabilization, cross-domain extension.

### Framework-Breaking Defeat Conditions (D1-D2)
Two findings that would "break the framework, not just a single prediction within it."

---

## 3. Complete List of Framework Predictions (P1-P11) with Verbatim Quotes

**P1. Asymmetric fraying.**
> "When stabilizers weaken, tight diagnostics should erode before loose ones. Decay is patterned, keyed to which mechanism weakened first, not spreading uniformly across the cluster."
> *Defeat:* "Diagnostics move as unstructured noise; no stable variance structure across replications."

**P2. Sticky-lock drift.**
> "Usage and semantic properties shift before morphosyntactic frames do; when frames finally fail, they fail in bursts rather than gradually. The asymmetry reflects the difference between frequency-sensitive and structurally entrenched maintenance."
> *Defeat:* "Frame loss is gradual and proportional to frequency decline, with no burst signature."

**P3. Phase transition in genesis.**
> "Grammaticalization should show nonlinear cluster formation -- a point at which co-occurring properties snap into a self-sustaining equilibrium -- rather than the continuous clines assumed by standard accounts."
> *Defeat:* "Historical data shows smooth, monotonic co-change with no identifiable inflection point."

**P4. Cross-domain extension tracks mechanism density.**
> "Metaphor productivity correlates with shared maintenance structure between source and target domains, not with surface similarity alone."
> *Defeat:* "Productivity correlates with surface overlap and shows no residual effect of mechanism sharing."

**P5. Conditioning recovers structure.**
> "Apparent gradience in category membership decomposes under social conditioning (dialect, register, community). If conditioning produces no gain in prediction, the maintenance claim is unsupported."
> *Defeat:* "Conditioned and pooled models perform identically; variation is irreducible noise."

**P6. Conventionalization requires mechanism support.**
> "Frequency alone doesn't conventionalize a metaphor; the target domain must supply maintenance mechanisms that sustain the transferred cluster. High-frequency metaphors without target-domain support should decay."
> *Defeat:* "Frequency fully predicts conventionalization with no residual role for mechanism structure."

**P7. Failure modes predict metaphor quality.**
> "A fat source domain yields ambiguous metaphor (too many properties compete for relevance); a thin source yields shallow metaphor (too few properties to anchor); a negative source yields nothing usable."
> *Defeat:* "Metaphor quality is independent of source-domain cluster structure."

**P8. Developmental cluster tightening.**
> "Children's diagnostics should become more correlated over time, not merely more accurate individually. The signature of maintenance is increasing covariance among properties, not just improving performance on each one."
> *Defeat:* "Diagnostic accuracy improves but inter-diagnostic correlations remain flat or decrease."

**P9. Category comorbidity.**
> "Categories that share maintenance mechanisms should co-occur typologically more often than chance predicts. Shared stabilizers create non-accidental dependencies between categories across languages."
> *Defeat:* "Typological co-occurrence is fully predicted by genealogical and areal confounds with no residual mechanism effect."

**P10. Hub-node asymmetry.**
> "For each category, one property's removal should destabilize the cluster more than others. The hub property is the one most densely connected to maintenance mechanisms, identifiable by targeted perturbation."
> *Defeat:* "All properties contribute equally to cluster stability; no perturbation asymmetry is detectable."

**P11. Competitive exclusion.**
> "When two forms grammaticalize into the same functional niche, the outcome tracks mechanism overlap: the form with greater access to existing maintenance infrastructure survives."
> *Defeat:* "Outcome is random with respect to mechanism overlap and tracks only frequency or prestige."

---

## 4. Predictions Most Relevant to Interjections

### Directly applicable framework predictions:

**P1 (Asymmetric fraying)** -- If interjections lose category properties, the loss should be patterned. For interjections: which diagnostics would erode first? Prosodic isolation is arguably "loose" (many things can be prosodically isolated); non-inflection is "tight" (few things are non-inflecting AND syntactically free). The interjections paper could test whether items leaving the interjection category lose properties in a predictable order.

**P2 (Sticky-lock drift)** -- Semantic/pragmatic properties of interjections (emotive force, discourse function) should shift before morphosyntactic frames (syntactic non-integration, non-inflection). This is testable diachronically: *God* > *gee* involves semantic bleaching first, with syntactic independence following. When interjections DO get syntactically integrated (e.g., *oh God, I forgot*), the burst prediction could be tested.

**P3 (Phase transition in genesis)** -- Grammaticalization into interjections should show a tipping point, not a smooth cline. Gehweiler (2008) on *gee* might provide evidence here: is there a historical moment where the properties "snap" into place? This is directly relevant to the JHP angle.

**P5 (Conditioning recovers structure)** -- Apparent gradience in interjection membership (are fillers interjections? are routine formulae?) should decompose once you condition on dialect, register, or community. Regional interjections (*lah*, *yaar*) provide natural conditioning variables.

**P8 (Developmental cluster tightening)** -- Children acquiring interjections should show increasing correlation among interjection properties over time, not just increasing use of individual interjections. This is a genuinely non-obvious prediction.

**P9 (Category comorbidity)** -- Languages with rich interjection inventories should share other structural features (e.g., prosodic flexibility, morphological simplicity in certain domains). This is testable typologically.

**P10 (Hub-node asymmetry)** -- One interjection property should be more central than others. Candidate: prosodic isolation or non-referentiality? If you remove prosodic isolation (integrate an interjection syntactically), does the cluster destabilize faster than if you add referential content? This could distinguish between "prosodic isolation is the hub" vs. "non-referentiality is the hub."

**P11 (Competitive exclusion)** -- When two forms compete for the same interjection niche (e.g., *nay* > *yeah*; *gee* vs. *jeez*), the survivor should be the one with greater access to existing maintenance infrastructure.

### Case-study predictions with interjection parallels:

**P12 (Implicational hierarchy)** -- Countability has a tight/loose hierarchy. Does interjection membership have an analogous hierarchy? E.g., no item should be prosodically integrated AND non-inflecting AND non-referential AND emotively laden without also being syntactically supplemental. The triangular distribution prediction could apply.

**P21 (Three-register dissociation, from Grammaticality)** -- The dissociation between qualitative jolt, reactive resistance, and normative correction could apply to interjection categorization judgments. When people say *hello* isn't an interjection, are they experiencing a qualitative jolt (it doesn't feel like one), reactive resistance (their grammar resists calling it one), or normative correction (they've been told it isn't one)?

**P24 (Basin stability at boundaries)** -- Gradient judgments about interjection membership at boundaries (fillers, routine formulae, vocatives) should be sharp within individual speakers but variable across speakers, with the variance structured by social conditioning.

---

## 5. Framework-Breaking Defeat Conditions (D1-D2)

**D1. Projection without maintenance.**
> "A robust, cross-linguistically stable category that projects strongly -- supporting reliable inductive generalizations across novel instances -- with no identifiable causal structure sustaining the cluster. This would show that the maintenance leg of the HPC triad is dispensable."

**D2. Structure without lift.**
> "Usage variation that, once sampling noise is properly controlled, proves to be a random walk with no recoverable structure. This would show that the projection leg is illusory -- that the apparent patterns licensing induction are artifacts of insufficient statistical control."

These are relevant to the interjections paper because:
- D1 is the challenge interjections pose: if interjection membership projects (you can make inductive inferences about novel interjections), there must be identifiable maintenance mechanisms. The paper needs to identify these mechanisms, not just list co-occurring properties.
- D2 is what the "marginal and anomalous" view implicitly claims: interjection variation is noise, not structure. The paper should show recoverable structure in the variation.

---

## 6. Genuinely Non-Obvious Predictions (Beyond Restating Cluster Properties)

Several predictions go well beyond restating that categories are clusters:

1. **P1 (Asymmetric fraying)**: Predicts a specific *order* of property loss. Not just "properties can be lost" but "tight before loose."

2. **P2 (Sticky-lock drift)**: Predicts *burst dynamics* in frame loss. Not just "things change" but "they change in a specific temporal pattern."

3. **P3 (Phase transition)**: Predicts *nonlinearity* in category genesis. Directly contradicts the standard grammaticalization assumption of continuous clines. This is a strong, falsifiable prediction.

4. **P5 (Conditioning recovers structure)**: Predicts that social conditioning *decomposes* apparent gradience. This is a methodological prediction: it tells you what to do (condition on social variables) and what should happen (gradience resolves into discrete clusters). If it doesn't, the maintenance claim fails.

5. **P8 (Developmental cluster tightening)**: Predicts *increasing covariance*, not just increasing accuracy. This is a statistical signature that distinguishes HPC from independent acquisition.

6. **P10 (Hub-node asymmetry)**: Predicts *asymmetric destabilization* under perturbation. Not all properties are equal; one is the hub. This is testable and non-obvious.

7. **P25 (Chain coherence costs)**: Predicts processing costs from disrupted maintenance, *beyond* referent ambiguity. This distinguishes HPC from simple ambiguity accounts.

8. **P29 (LLM indiscriminate extension)**: Predicts that LLMs *without goals* extend categories indiscriminately. This is a novel prediction about artificial systems that follows from the theory.

---

## 7. Implications for the Interjections Paper

### What the interjections paper needs to do (based on this appendix):

1. **Identify maintenance mechanisms**, not just co-occurring properties. The appendix is clear: listing properties is description, not HPC analysis. The paper needs to explain *why* the properties cluster (semantic bleaching, prosodic isolation reinforcing syntactic independence, pragmatic conventionalization).

2. **Make predictions with defeat conditions.** The appendix format (prediction + defeat) should be adopted at least informally. The interjections paper should be able to say: "If interjections are an HPC, then X; if X is false, the HPC claim is weakened."

3. **Address the hub-node question.** Which interjection property is the hub? This could be the paper's most distinctive contribution.

4. **Exploit the diachronic angle.** P3 (phase transition) is directly testable with the bleaching data (Gehweiler 2008). Does *God* > *gee* show a tipping point? This is the JHP angle.

5. **Use P5 (conditioning recovers structure)** to handle the boundary disputes. The gradience at interjection boundaries (fillers, routine formulae) isn't a problem for HPC; it's a prediction. But the paper should show that conditioning on register/dialect/community decomposes the gradience.

6. **Address D1 directly.** Interjections project (you can infer prosodic behavior, syntactic non-integration, emotive force from categorizing something as an interjection). The paper must show that this projection has identifiable maintenance, not just co-occurrence.

### Key distinction the appendix enforces:

The difference between **describing a cluster** (interjections are non-referential, non-inflecting, prosodically isolated, etc.) and **explaining a cluster** (semantic bleaching creates non-referentiality AND prosodic isolation simultaneously, which reinforces syntactic independence, which enables free coinage). The HPC framework's advantage over prototype theory is precisely that it demands the second step.

---

## 8. Structural Observations

- 30 numbered predictions (P1-P30) plus 2 framework-breaking defeat conditions (D1-D2)
- Framework predictions are domain-general; case-study predictions are domain-specific
- Every prediction has a named defeat condition (specific to that prediction)
- The appendix explicitly references Chapter "what-changes" for the full defeat-condition architecture
- Predictions are cross-referenced to source chapters
- The format is designed for accountability: "findable in one place"
- No predictions are specifically about interjections (the book doesn't have an interjection case study), but the 11 framework predictions all apply to interjections as an HPC candidate
