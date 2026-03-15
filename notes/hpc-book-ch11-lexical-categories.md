# Chapter 11: Lexical Categories and Their Maintenance -- Detailed Notes

**Source:** `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter11.tex`

---

## 1. How Lexical Categories Are Analysed as HPC Kinds

The chapter's central thesis is that lexical categories (word classes) are homeostatic property clusters maintained by converging mechanisms, not defined by necessary and sufficient conditions. The chapter opens by distinguishing **noun** (a syntactic HPC: heads NPs, takes determiners, inflects for number, fills argument slots, triggers agreement) from **name** (a semantic HPC: picks out individuals, resists descriptive modification, creates referential opacity, supports rigid reference). Key passage:

> "A syntactician and a semanticist can carve the same words differently without either being wrong -- because they're tracking different HPCs, maintained by different mechanisms, projectible for different purposes." (ll. 21)

The chapter identifies a **three-part typology** of word classes:

1. **Robust categories** (skeleton): Multiple mechanisms converge on thick, projectible clusters. Nouns and verbs are the paradigm cases. "The words that specialize in identification cluster together, and the words that specialize in predication cluster together, because the communicative demands are tight enough to keep the clustering going." (l. 65)

2. **Thin classes** (plumage): Real clustering but fewer, less tightly coupled mechanisms. Adjectives are the pivotal case -- a category in English with genuine distributional coherence but dramatically variable across languages. "The category doesn't shrink randomly; it shrinks from the periphery inward, losing less frequent and less communicatively essential members first. This is exactly what the maintenance view predicts." (l. 103)

3. **Fat labels** (wastebasket): A single term obscures multiple unrelated clusters. Adverb is the classic case -- "what Quirk called 'the dustbin of the parts of speech', a class with excellent storage capacity and terrible explanatory power -- a perfectly good drawer, provided you don't mistake it for a theory." (l. 42)

A fourth configuration emerges in the pronoun section:

4. **Braided categories**: Where multiple independent category types (lexical, semantic, operational) converge on the same items but are maintained by different mechanisms.

The chapter also proposes that **"lexical category" is itself an HPC**, one of whose maintained properties is a small category count (l. 165). This explains why grammars preserve a few high-level labels even when finer partitions would improve prediction.

---

## 2. Maintenance Mechanisms Identified for Lexical Categories

The chapter identifies **five core mechanisms** for nouns and verbs (the robust skeleton), then evaluates how many of these operate for thinner categories:

### For Nouns and Verbs (full convergence):

1. **Discourse frequency** -- Reference and predication are the backbone of every clause. Two sources of robustness: high *token* frequency (every clause needs them) and massive *type* frequency (thousands of items filling the same structural slots). "Token frequency entrenches individual forms (hence the irregular survival of *go*/*went*); type frequency builds the schematic category, because the more distinct items a learner encounters in a frame like *the ___*, the stronger the abstraction." (l. 70)

2. **Morphological agreement** -- "The system doesn't just *mark* the noun-verb distinction; it *enforces* it. Every new word entering the language must slot into a noun class or a verb paradigm, because the agreement morphology has no slot for anything else." (l. 71)

3. **Acquisition** -- Children learn nouns and verbs early, as categories (evidenced by overgeneralization). "What gets abstracted early gets entrenched early." (l. 72)

4. **Structural analogy** -- Novel words get slotted into pre-existing categories. "You encounter *shlep* for the first time and immediately know it inflects (*she shleps*, *they shlepped*), takes objects (*shlep the suitcase*), appears in verb-phrase constructions (*keep shlepping*). You don't need to be told; you *predict*." (l. 73) Crucially, analogy is **emergent, not primitive**: it "doesn't initiate the category but amplifies one that has begun consolidating through the other mechanisms." (l. 73)

5. **Semantic recruitment** -- "The world keeps producing entities that need to be referred to and events that need to be predicated -- and the naming role, the very thing the introduction distinguished from nounhood, is itself a feeder mechanism." (l. 74)

### For Adjectives (partial convergence):

- **Discourse task**: Real but shallow. Attribution is useful but dispensable -- "you can always build a reference without an adjective" (l. 108). "Shallow pressure produces shallow clustering."
- **Acquisition**: Later than nouns/verbs. "Later entry into the system means fewer cycles of entrenchment before the transmission bottleneck begins filtering." (l. 109)
- **Morphological glue**: Borrowed, not owned. "When the only morphological glue holding a category together is copied from another category, the bond is weaker -- because the morphology doesn't differentiate the adjective from the noun; it assimilates the adjective *to* the noun." (l. 110)

### For Manner Adverbs (comparable to adjectives, thinner than N/V):

- Productive `-ly` derivation keeps the class open
- Syntactic positioning independently maintained (e.g., *fast*, *well*, *hard* occupy VP-internal slots without `-ly`)
- Dependency-distance minimisation reinforces positional clustering
- Gradability connects to degree-modification system
- Three or four independent mechanisms -- "comparable to adjectives, thinner than nouns and verbs" (l. 145)

### For the Adverb Label (no convergence):

- "No shared proper purpose, no converging mechanisms, no cluster of properties that travel together across the class." (l. 139)
- "Knowing that something is 'an adverb' tells you it isn't a noun, a verb, or an adjective -- and almost nothing else." (l. 139)

### Summary Table (from chapter, Table 11.2):

| Mechanism | N/V | Adjective | Manner adv. | "Adverb" |
|-----------|-----|-----------|-------------|----------|
| Dedicated morphology | Yes | Partial | Partial | No |
| Agreement ecosystem | Yes | Partial | No | No |
| Exclusive syntactic slot | Yes | Partial | Partial | No |
| Early acquisition | Yes | No | No | No |
| Early predictive commitments | Yes | Yes | Yes | No |
| Diachronic stability | Yes | Partial | Partial | No |

---

## 3. Synchronic Maintenance vs. Diachronic Recruitment

The chapter distinguishes these implicitly rather than with a dedicated section. Key points:

**Synchronic maintenance** is handled by the five mechanisms above operating continuously: agreement enforcing categories, analogy extending them to new members, entrenchment preserving them against change, acquisition transmitting them across generations.

**Diachronic recruitment** is discussed through:

- **Semantic recruitment as a feeder mechanism**: "Name and noun are distinct HPCs, but the semantic pressure of the first continuously recruits members into the second." (l. 74) The world keeps producing new entities to refer to and new events to predicate, keeping the categories open.

- **Structural analogy maintaining from the open end**: "Structural analogy extends the category to new members, maintaining the cluster from the open end." (l. 73) But this is emergent -- "the verb-island data just described show that two-year-olds don't analogize across verbs; the leap requires a critical mass of exemplars. Once reached, it's self-reinforcing." (l. 73)

- **The `-ly` morphology feeding two categories**: The derivational process produces forms that land in different clusters (manner adverb vs. speech-act modifier) "because the other mechanisms pulling on them diverge." (l. 149) One mechanism recruiting items, but the other mechanisms sorting them into different HPCs after recruitment.

- **The pronoun territory** shows diachronic recruitment explicitly: personal pronouns descend from demonstrative stock; interrogative *who* has entirely separate PIE ancestry; relative *who* developed through Middle English grammaticalization. "Two diachronic lineages, one synchronic territory." (l. 187)

- The **counterfactual template** at l. 77 is diagnostic: "Consider what would happen if only one mechanism were operating." Each alone would produce partial, fragile, variable clusters. "Partial clusters invite drift; drift invites reanalysis; reanalysis invites new partitions."

---

## 4. Category vs. Function Distinction

The chapter consistently maintains the CGEL distinction between category (word class) and function, though the terminology foregrounds category more than function:

- **Pronoun** is treated as a subcategory of noun (following CGEL): "CGEL formalizes the syntactic profile: pronouns are a subcategory of nouns." (l. 179)

- The **name/noun** distinction maps to the category/function architecture: name is semantic (a cluster about reference-tracking), noun is syntactic (a cluster about distributional behaviour). They overlap in extension but are distinct HPCs with distinct maintenance profiles.

- The **pronoun/pro-form** distinction parallels name/noun: "Pronoun names a syntactic cluster: heads NPs, case-marked, closed category. Pro-form names a semantic one: referentially dependent, light in descriptive content, taking its value from context." (l. 181)

- **IRE words** (interrogative, relative, exclamative) form an **operational category** that cross-cuts lexical categories: "*who* is a pronoun, *which* a determinative, *where* and *when* prepositions, *how* an adverb." (l. 204)

- The chapter notes that "The traditional taxonomy, which has only one axis -- lexical category -- can't represent this overlap. It has to decide whether *who* is 'really' a pronoun or 'really' an IRE word. The HPC framework doesn't face the dilemma." (l. 253)

**Importantly, "supplement" as a function is not discussed in this chapter.** The word "supplement" does not appear. This is relevant for the interjections paper, where interjections characteristically function as supplements.

---

## 5. Peripheral/Marginal Categories Like Interjections

**Interjections are not discussed in this chapter at all.** There is no mention of interjections, exclamatives-as-interjections, or the word "interjection" anywhere in the text.

However, the chapter's framework provides tools directly applicable to interjections:

- The **thin-class analysis** (adjective model) could apply: interjections may have a real but thin cluster, with fewer mechanisms than nouns/verbs.

- The **fat-label risk** is relevant: is "interjection" a genuine category with converging mechanisms, or a wastebasket like "adverb"?

- The **braided-category model** (pronoun territory) might be relevant if interjections operate at the intersection of lexical, pragmatic, and prosodic planes with independent maintenance regimes.

- The **mechanism-density diagnostic** is directly applicable: "What varies across word classes isn't importance but mechanism density -- and mechanism density is what the coupling continuum measures." (l. 49)

- The chapter's typology (skeleton / plumage / wastebasket / braid) invites the question: **where do interjections sit?** The interjections paper could argue they are a genuine thin HPC (not a wastebasket), maintained by specific mechanisms (prosodic isolation, semantic bleaching pathways, pragmatic conventionalization).

---

## 6. Prototype Theory vs. HPC for Lexical Categories

The chapter does not engage with prototype theory directly -- the word "prototype" appears once in passing ("most prototypical nouns do name things," l. 21), but there is no sustained comparison of prototype and HPC approaches.

However, the chapter's framework implicitly contrasts with prototype theory:

- **Graded membership** is shared with prototype theory: "gradient membership, exactly as HPC predicts" (l. 199 re: *who*). But the HPC account grounds gradedness in **mechanism convergence**, not in distance from a prototype.

- The **essentialist alternative** is the main foil, not prototype theory. The chapter's contrasts are with definitional/essentialist accounts: "A definitional account predicts relatively sharp, context-invariant boundaries once the definition is met; limited sensitivity to the ecological supports that surround a category; and relatively uniform acquisition once the defining cues are available." (l. 282)

- The **maintenance view** differs from prototypes by asking **why** items cluster, not just observing **that** they do. The mechanisms provide causal explanations for clustering; prototypes provide descriptive generalizations about typicality.

- The explicit HPC vs. essentialism diagnostic (l. 282): "The maintenance view predicts graded membership where supports are partial; measurable plasticity in thin regions under short-term distributional perturbation (register shifts, contact, instruction); and super-additive gains in generalisation when multiple supports converge."

---

## 7. Feedback Loops and Mutual Reinforcement Between Properties

The chapter identifies several feedback/reinforcement dynamics:

### Self-reinforcing analogy:
"Once reached, it's self-reinforcing -- analogy doesn't initiate the category but amplifies one that has begun consolidating through the other mechanisms." (l. 73) This is a clear positive feedback loop: once enough items are in a category, analogy pulls new items in, which makes the category more robust, which strengthens the analogical pull.

### Morphological lock-in:
Agreement systems create bidirectional lock-in: "The morphological lock-in stabilizes the category boundary from both sides: nouns are the things that control agreement; verbs are the things that show it." (l. 71) This is mutual reinforcement: the agreement system needs categories, and the categories are reinforced by the agreement system.

### Convergence as resilience:
"In many well-documented systems, weakening one strand doesn't collapse the category because the others compensate. This is the signature of a robust HPC -- not a single causal thread but a cable of independent strands." (l. 79) The independence of mechanisms provides fault tolerance.

### The braid architecture:
In the pronoun territory, "The three types of category feed each other: the lexicon's paradigms stabilize distributions, which in turn enable the operations that reshape discourse -- and discourse recruits new lexical items back into the cycle." (l. 223) This is an explicit feedback cycle: paradigms -> distributions -> operations -> discourse -> recruitment -> paradigms.

### Recruitment-maintenance cycle for N/V:
Semantic recruitment (name -> noun) is itself a feeder mechanism. The communicative need for reference recruits words into nounhood, which strengthens the category's distributional coherence, which makes it easier for new recruits to slot in via analogy.

### Entrenchment-acquisition loop:
"What gets abstracted early gets entrenched early" (l. 72). Early acquisition leads to deep entrenchment, which makes the category more resistant to change, which makes it more available as a template for acquisition by the next generation.

---

## Additional Notes Relevant to the Interjections Paper

### The counterfactual template (diagnostic tool)
"Consider what would happen if only one mechanism were operating." (l. 77) The interjections paper could apply this: what if only prosodic isolation operated? Only semantic bleaching? Only pragmatic conventionalization? Each alone would produce some clustering, but the convergence is what makes interjections a genuine (if thin) category.

### Mechanism density as a continuum
"Section 8 introduced a continuum from hard coupling (phonemes) through loose coupling (grammatical categories) to composite coupling (constructions). Here that continuum earns its keep within a single level of description." (l. 49) Interjections could be placed on this continuum.

### Fat labels survive because they're cheap
"The fat label survives not because it's accurate but because it's cheap, and because the sociology of grammar teaching entrenches it." (l. 171) The interjections paper could argue the opposite: interjection is NOT a fat label; it has genuine mechanism convergence.

### Field-relative projectibility
"Because naturalness is discipline-relative, the same expressions may form one natural category for semantics and another for morphosyntax (Boyd 1999: 147)." (l. 31) For interjections, projectibility is primarily pragmatic rather than truth-conditional -- this is what makes them distinctive and what the paper should foreground.

### The category/class distinction
The chapter consistently distinguishes **category** (an HPC kind with converging mechanisms) from **class** (a grouping that may or may not reflect genuine clustering). This is critical for the interjections paper: the argument should be that interjections are a genuine *category*, not merely a *class*.

### Communicative situations affecting category thickness
"Even within a single language, the thickness of the cluster varies across communicative situations." (l. 125) This could apply to interjections: their clustering may be thicker in spoken/informal registers and thinner in formal written language.

### Disconfirmation conditions
The chapter models how to state falsifiers: "If a language showed no such asymmetries -- truly symmetrical distribution, no processing cost for function-switching, no acquisitional priority -- the convergence story would need qualification." (l. 85) The interjections paper should similarly state what would falsify the interjection-as-HPC claim.
