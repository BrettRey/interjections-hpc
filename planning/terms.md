# Terminology ledger
<!-- SUMMARY: Reader's vocabulary for the lexical-category framing; which specialist terms this venue's readers own (free) and which must be glossed (earned) · status: active · updated: 2026-07-24 -->

Reader assumed: a general theoretical-linguistics audience of the kind
*Journal of Linguistics* serves. Grammatical description is common ground;
the Boyd/HPC programme is not.

Built after Reviewer #2 at *Journal of Pragmatics* reported that several of
the paper's compounds were so unfamiliar they couldn't be guessed at, and
diagnosed "a referential void" behind them. Their specific hits are recorded
below with what was done. Verbatim report:
`notes/2026-07-23-jop-decision-letter-and-reviews.md`.

## Free — this reader owns it

| Term | Status | Why |
|---|---|---|
| interjection | free | The paper's object, and a household grammatical term. Flagged by `check-terms.py` only because it appears unglossed in the title, which is correct for this venue. |
| supplement, supplement function | free | CGEL's own term, and this reader knows CGEL. Definition still quoted at first use because the paper leans on its precise content. |
| routine formulae | free | Standard in the pragmatics of formulaic language, and glossed anyway via Coulmas. |
| projectibility | free | Glossed at first use in the abstract and again with Goodman in the introduction, per the house rule for this term. |
| interrogative, animacy | free | Ordinary descriptive vocabulary. |

## Earned — must be glossed at first use

| Term | Status |
|---|---|
| profile | **Glossed §1.** R2 asked "what profile? Is he talking about the Langackerian profile?" That name collision is the real problem: it isn't merely unglossed, it's owned by another framework. The gloss now defines it as the combination of cluster properties a form shows in a given environment, and disowns the figure-and-base sense explicitly. |
| licenses | **Glossed §1.** R2 asked why the verb "support" was doing this work. Replaced throughout with *licenses*, defined as a defeasible good default rather than an entailment. |
| projection target | **Glossed §1** as part of the evidential ladder. |
| stable profile | **Glossed §1**, ladder item: does the combination actually recur? |
| network order | **Glossed §1**, ladder item: are the properties linked, not merely co-occurring? |
| stabilizer | **Glossed §1**, ladder item: is something holding the combination together? Nine uses were previously unglossed and `check-terms.py` hard-flagged it. |
| corrective control | **Glossed §1**, ladder item, with the explicit note that only this would license calling the cluster homeostatic and that the paper doesn't claim it. |
| homeostatic | Cut from six uses to four. R2 asked why the term appears at all. Four of the six were disclaimers telling the reader it doesn't apply, which is what made the apparatus look unmotivated. The survivors are Boyd's lineage, the Boyd quotation, the ladder's corrective-control gloss, and the conclusion's substantive limit claim. |
| causal-pragmatic kind | Glossed at first use in §1. |
| property cluster | Glossed at first use ("descriptively for the empirical pattern of co-occurring features"). |
| token | **Footnoted at first use.** Two senses collide in this paper: the interactional-linguistic sense in *change-of-state token* and *response token*, and the paper's own unit of analysis, token as against lexeme. R1 read the first as a type/token error. |
| path dependence | Rewritten in §1 with a concrete *damn* vs *gee* contrast after R2 called the original paragraph meaningless. |
| conversational valence | Glossed at first use in §2.6, where Libert's single-property definition is engaged. Libert's term, not the paper's. |
| projective declaration | **Glossed §1.** Claim-side object from the history paper: what's observed, what's predicted, over which cases. Replaces the earlier *projection target*. |
| warrant | **Glossed §1.** Kept separate from the world-side objects, per the history paper's central revision. Table 2 carries it link by link. |
| profile / stability | **Glossed §1.** *Profile* is the worldly relation the declaration posits; *stability* is the separate claim that it recurs. Note this is the history paper's sense, narrower than the property-bundle sense the paper used before 2026-07-25. |
| grounds | **Glossed §1.** What explains the profile's obtaining or persisting. *Stabilizers* and *corrective control* are grounds of increasing strength. |

## Retired

| Was | Now | Why |
|---|---|---|
| syntactic supplementarity | supplement function | R2: the compound "is never used to describe interjections' syntactic behavior." It was a coinage sitting next to CGEL's established term, which the paper already used elsewhere. Five occurrences replaced. |
| supports inferences | licenses defeasible inferences | See *licenses* above. |
| four-stage trajectory (of Gehweiler's *gee* development) | three positions, two mechanisms | Not a terminology fix but an accuracy one: Gehweiler's thesis is that the two transitions work differently, the second abruptly and by hearer re-analysis. "Stage" implied the uniform ladder she argues against. |
| projection target | projective declaration | Superseded. The history paper divides the earlier broad *profile* notion into a claim-side declaration and a worldly profile. |
| diagnostic ladder, rungs | the four objects | Superseded, and misleading: a ladder implies an order, but stability and network order are independent. A combination can recur without revealing direction among its parts, and a directed dependence can hold without recurring. |

## Standing rule

`python3 ../../../.house-style/check-terms.py main.tex --follow-inputs --ledger planning/terms.md --gate`
must pass before submission anywhere. A term is cleared by glossing it or by
being marked free here with a reason. Softening a gloss to get past the gate
defeats the point.
