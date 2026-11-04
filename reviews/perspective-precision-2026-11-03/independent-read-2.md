# Independent read 2 (responsibility-verifier, claude-opus-5-5)
<!-- SUMMARY: second independent read of inquiry-relative-categories.tex, saved verbatim by the parent session · status: actioned in round 5 · updated: 2026-11-03 -->

Saved verbatim by the parent session from the subagent hand-back (agent a42ab42b6f5e0bf36); the harness's two-space indent removed. The subagent read the file while round 5's first half was being applied, as its report notes.

## Prompt

```
Thank you for this. I'd like a careful, independent read of a revised linguistics manuscript.

**File:** `/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/inquiry-relative-categories.tex`. Read all of it; it's about 10,400 words. The paper argues that linguistic categories are inquiry-relative, with English interjections as the worked case.

**The author's commitments are fixed. Work within them; don't argue against them.** Brett Reynolds's account of categories:
- A lexical category is what several fallible diagnostics converge on, not what any single criterion defines. For interjections the diagnostics are:
  - internal dependents (none, with the exceptional *damn* + NP);
  - external function or status (standalone use, or supplement to a clause);
  - morphology (no inflection);
  - meaning (expressive rather than propositional);
  - prosody and phonology.
- Membership is projectible: observing some of the cluster's properties in a case licenses expecting the others.
- The paper's source–target rule applies to each inference, not to the category. A property used to assign a particular case can't then count as confirming the expectation about it. Meaning can serve as a diagnostic in one case and a projection target in another.
- A previous reviewer recommended assigning by distribution alone. Brett rejected that as essentialist. Don't recommend it.

**What I need.**
1. **Errors within that framework.** Look for any claim that contradicts the converging-diagnostics account, slips back to a single-criterion assignment, or violates the per-inference source–target rule. Look also for claims that contradict each other across sections. Examples: category vs syntactic function vs constructional status (CGEL: independent utterance is a status, not a function); prenominal *damn* is outside the interjection category, with its actual category left open; "contribution" means only what a use contributes to interpretation, while "achievement" is the assessment slot.
2. **Perspective labels still used loosely.** "Grammatical", "semantic", "interactional", "phonological", "prosodic", "expressive", "syntactic": say for each what it should specify (object, question, classification, or inference).
3. **Source fidelity** for the CGEL quotations (p. 30 and p. 1361). CGEL is at `/Users/brettreynolds/projects/LLM-CLI-projects/literature/huddlestonpullum2002.md`; search "on the basis of their inflection" and "The general definition of interjection".
4. **Quality.** Where is the argument weakest, slackest, or least interesting? Brett asked for excellence, "Balance the need to be interesting with care. Don't bury everything in caveats." Flag:
   - caveat stacks;
   - sealed paragraph closers;
   - corrective negation without an opponent;
   - colon reveals;
   - restatement passed off as revelation;
   - any paragraph that doesn't advance the argument.

**For each finding:** quote the line, say what's wrong, give a minimal fix in the paper's voice, and rank it (critical, important, minor).

**Boundaries.** This is read-only: don't edit files. Put the full report in your final message. If something in the framework itself looks inconsistent with the text, say so plainly, but within Brett's account. Stop when you've read the whole manuscript; say "none" for any category with nothing to report.
```

## Report

## Review of the inquiry-relative categories manuscript

File: `/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/inquiry-relative-categories.tex`

**The manuscript changed while I was reading it.** Lines 252–262 were rewritten during my read, which pushed everything after them down five lines. They now say "CGEL reserves meaning for definitions of that general, cross-linguistic kind and decides which English words belong by their form (31–32)". All line numbers below come from my final grep of the current file.

DECISIONS.md (2026-11-03, rounds 3–4, line 1056) says the CGEL p. 31 "focus on form" quotation had been removed. A paraphrase citing pp. 31–32 is now back. That's a fact for Brett to note, not a verdict. No RESPONSIBILITY NOTICE: concurrent editing is normal here.

**What I checked directly:**
- CGEL in the PDF (PDF page = printed page + 20): pp. 30, 31, 32, 1350, 1360, 1361 and n. 70.
- Wilkins pp. 124–125: `/Users/brettreynolds/projects/LLM-CLI-projects/literature/wilkins1992.md`, line 33.
- main.tex's thesis: `main.tex` lines 90–93.
- DECISIONS.md lines 1053–1056.
- Every manuscript line quoted below.

**Not checked:**
- **Potts 2007:** the cited paper isn't held. `literature/potts2007dimensions.md` is a different text with no *damn* in it.
- **Wharton 2016:** not held. Only `wharton2000` is in `literature/`.
- **Other sources:** Ameka, Quirk, Gehweiler, Dingemanse, and the GloWbE figures.

---

## 1. Errors within the framework

### Critical

**1.1 Standalone *Damn!* doesn't differ from supplementary *damn* in integration (l. 400–402).**
> "Supplementary \mention{damn} and the prenominal modifier differ in function, and standalone \mention{Damn!} differs from both in integration"

- **What's wrong:** CGEL p. 1350 defines supplements as "elements which occupy a position in linear sequence without being integrated into the syntactic structure of the sentence". So supplementary *damn* isn't integrated either. Standalone and supplementary *damn* differ in status (no anchor versus an anchor). Only the prenominal use is integrated. This is the status/function/integration slip at the paper's central example.
- **Fix:** "Supplementary *damn* and the prenominal modifier differ in function and integration. Standalone *Damn!* shares the supplement's lack of integration but has no anchor: it's an independent utterance. The expressive analysis groups all three."

**1.2 Prenominal *damn* is excluded "as defined", which is a single-criterion exclusion (l. 403–405).**
> "Calling prenominal \mention{damn} a modifier specifies its function; that integrated position falls outside the interjection category as defined"

- **What's wrong, part 1:** "As defined" rests the exclusion on the integration clause of CGEL's general definition. On the converging account, prenominal *damn* shares three diagnostics with the core: no inflection, no dependents, and expressive meaning. The text never says why integration outweighs them.
- **What's wrong, part 2:** "a position falls outside the category" also runs function and category together.
- **What's wrong, part 3:** In §3.3 (l. 881–894) the investigator is told that prenominal *damn*'s "inconvenient distribution isn't by itself a reason to remove it". A reader will see the paper doing that very thing in §2.3, unless the difference is stated.
- **Fix in §2.3:** "In that position *damn* is integrated into the noun phrase and isn't set off prosodically. Those diagnostics converge against membership. Its lack of inflection and dependents doesn't outweigh them, because many words outside the category share both (compare l. 816–818). I leave open which category it belongs to."
- **Fix in §3.3, after l. 886:** "The lexical category differs here: integration is one of its diagnostics, so prenominal *damn*'s position counts against its membership, not against a projection."

**1.3 The text splits source and target at the level of the category, and prosody and phonology are never named as diagnostics.**
- **Abstract, l. 80:** "A category's basis of identification doesn't confine the domain of its useful predictions". This gives the category one fixed identifying basis, which is the category-level reading Brett excludes.
- **l. 836–838:** "The category's place in the grammar rests on general statements about its members' constructions, morphology, and meaning; membership also supplies expectations about conversational use and realization". Realization is placed on the projected side only.
- **§2.1:** It lists inflection, dependents, function/status and meaning as diagnostics. Prosody and phonology appear only under "The expectations extend to realization" (l. 301).
- **The contradiction:** DECISIONS.md line 1056 says rounds 3–4 added "prosody/phonology" as diagnostics. The text doesn't deliver that. Only l. 844 ("If that boundary helped identify the case") and l. 1001–1006 (unusual phonology "as defeasible evidence") imply it.
- **Fix, abstract:** "The properties used to assign a case don't confine what membership lets an investigator expect about it."
- **Fix, end of l. 312:** "Like meaning, these properties can also help assign a case, provided the same observation isn't then counted as confirming the expectation."
- **Fix, l. 836–838:** "...general statements about its members' constructions, morphology, meaning, and realization. Any of these can be the source of one inference and the target of another."

**1.4 Wilkins is cited as the motive for the per-inference rule, but his actual reason argues against combining criteria (l. 318–320).**
> "\textcite[124--125]{wilkins1992} defines the class formally for this reason"

- **What Wilkins says (p. 124):** "The advantage of using only one type of criteria ... rather than using a combination of criteria, is that such a procedure allows the investigator to examine the set of elements thus defined to see whether it also manifests other regular features describable in terms of the other two domains".
- **What's wrong:** That is a category-level partition, and an argument against convergence. "For this reason" makes it the source of Brett's per-inference rule.
- **Fix:** "Wilkins (1992: 124) secures the same separation for the whole class, defining it by formal criteria alone so that its semantic and pragmatic regularities stay open to test. Applying the rule to each inference instead lets meaning help assign one case and be predicted for another."

### Important

**1.5 New inconsistency created by the live edit (l. 294–297).**
> "\textit{CGEL}'s semantic criterion is broad enough to cover all three, so \mention{sh} is a secure member"

- **What's wrong:** Line 255–257 now says CGEL decides membership by form. This sentence then draws a membership conclusion from CGEL's general definition.
- **Fix:** "CGEL's general definition is broad enough to cover all three, and *sh*'s conative meaning counts toward its membership even without the evaluative or affective stance that defines the narrower expressive grouping."

**1.6 The conclusion contradicts §2.1 and §4.1 (l. 1498–1500).**
> "Assigning a sign-type to the category on whichever of these diagnostics have been observed gives reason to expect the rest"

- **What's wrong:** Line 264 says "No one diagnostic decides membership". §4.1 accepts Ameka's point that unusual phonology isn't sufficient.
- **Fix:** "...once enough of these diagnostics converge..."

**1.7 *Bang!*: the list of evidence that can settle its category is incomplete (l. 1012–1015).**
> "Choosing between nominal and interjectional analyses needs distributional and constructional evidence ... or an independently warranted association connecting the observed phonology"

- **What's wrong:** It leaves out morphology, which the paper itself offers at l. 673–674 (*two bangs*). It also says nothing about why meaning is set aside.
- **Fix:** "...needs converging evidence about the selected use, such as number contrast and nominal dependents, or a warranted association with its phonology. Its depictive meaning doesn't discriminate here, because both analyses allow it."

**1.8 The intro treats independent utterance as a function (l. 100–101).**
> "analyses of function and lexical category distinguish them"

- **What's wrong:** The first *damn* use has a status, not a function, by the paper's own rule (l. 378–379).
- **Fix:** "analyses of function, constructional status, and lexical category distinguish them".

**1.9 "Characteristic functions", plural (l. 370–371 and l. 1401).**
- **What's wrong:** Interjections have one function (supplement) and one status.
- **Fix:** "through its supplement function".

**1.10 The case for *mm-hm* and *huh?* is thinner than presented (l. 580–588).**
> "Neither takes dependents or inflects"

- **What's wrong:** By the paper's own relevant-opportunity test (l. 910–912), absence of inflection and dependents in standalone responses says little, because the competing analyses wouldn't show them either. The assignment therefore rests on the non-elliptical analysis. Two diagnostics go unused: meaning, and phonology (*mm-hm* lacks a vowel, like *sh*).
- **Fix:** "Absence of inflection and dependents is weak evidence in standalone responses (Section 3.3). The assignment rests on the non-elliptical analysis, on non-propositional meaning, and, for *mm-hm*, on a vowelless form like *sh*'s."

**1.11 The grouping-basis slot assumes one basis per grouping (l. 720–726, Table 2).**
- **What's wrong:** That fits the expressive grouping, which has one relation, conveyed stance. It doesn't fit the lexical category as Brett defines it.
- **Fix:** add to l. 720: "For the lexical category, the basis is the convergence of several fallible diagnostics; for the expressive grouping, it's a single relation, conveyed stance."

**1.12 Supplementation is identified "from the completeness of the anchor" (l. 356–358).**
- **What's wrong:** Completeness doesn't separate supplements from clause-level modifiers. CGEL p. 1360 says "there is little difference between supplements with a clause as anchor and modifiers". What separates them there is that supplements fall outside negative scope and can't be the focus of an *it*-cleft.
- **Fix:** "...from the completeness of the anchor, and from the expression's exclusion from negative scope and *it*-cleft focus (CGEL 1360)..."

**1.13 "Contribution" appears in the assessment slot.**
- **The uses:**
  - l. 1220 "descriptive and explanatory contributions"
  - l. 1402 "what each classification contributes"
  - l. 983 "These possibilities contribute to the interjection profile"
  - l. 1213 "whether ancestry contributes anything further"
- **The table:** Table 1's caption (l. 627) says "contribution", but the column is "Meaning or action" and holds action classes ("Continuation resource", "Closing resource").
- **Fix:**
  - l. 1220: "achievements"
  - l. 1402: "what each classification achieves"
  - l. 983: "belong to the interjection profile"
  - l. 1213: "adds any further information"
  - caption: "...and meaning or sequential action"

### Minor

**1.14 "Modification" for repetition (l. 458–459).**
> "The distinction changes the interpretation of a possible modification."

"Modification" is a CGEL function term. Fix: "...changes how repetition is interpreted."

**1.15 Core uses picked out by membership (l. 238).**
> "conventional interjectional uses"

This selects the core by the label it's meant to establish. Fix: "in the uses CGEL describes, as exclamations on their own or as supplements".

**1.16 A verbal analysis with no proponent (l. 411–412).**
> "A verbal analysis remains a substantive alternative."

No proponent or evidence is given, and CGEL n. 70 argues against an understood-subject version. Fix: name the evidence (the NP complement; the historical *God* subject in n. 70) or see 4.4.

**1.17 Potts: "an attitude toward its referent" (l. 397), unverified.**
Potts 2007 isn't held. Check whether he requires the attitude to target the noun's referent before keeping the phrase.

---

## 2. Perspective labels used loosely

**"Expressive": the strongest problem.** The word carries four senses:
- **CGEL's broad sense:** non-propositional meaning, covering *hey* and *sh*. CGEL p. 1361 calls the central members "used as expressive exclamations". Used at abstract l. 69–70, l. 254, l. 294.
- **Ameka's sense:** one of three functions (l. 293).
- **The paper's narrow sense:** Potts-style stance, adopted "from here on" at l. 416–418.
- **The ideophone tradition's sense** (l. 453).

The abstract uses the broad sense (l. 69–70) and the narrow sense (l. 75) in consecutive sentences. After the narrowing, l. 442–443 ("groups both as expressive interjections") uses the broad sense for the opponent.

What each should specify: the diagnostic is a criterion on meaning (non-propositional); the grouping is a classification of stance-conveying uses. Fix: write "non-propositional meaning" wherever the diagnostic is meant (abstract, §2.1), and "one exclamatory class" at l. 442–443.

**"Grammatical": none in visible prose.** The `sec:grammatical-core` label key is invisible. "Place in the grammar" (l. 274, 836, 1388, 1503) should specify the general statements the category allows; see 1.3.

**"Semantic":**
- l. 294 should be "CGEL's general definition" (a criterion).
- l. 434 "a semantic membership condition" should specify the condition on meaning for the expressive grouping.
- l. 492 "the semantic perspective" names a field. Fix: "no single category answers the questions about what a use contributes".
- l. 1372 "semantic residue" is undefined for this reader.

**"Interactional":** The heading at l. 540, "Interactional resource classes", names a field. Fix: "Classes of sequential action".

**"Phonological":**
- l. 1092 "The two phonological inquiries" includes prosodic classes of realizations, against §4's own split (phonological = sign-type sound shape; prosodic = realizations). Fix: "The two sound-based inquiries".
- l. 706 "A phonologist can classify the individual productions" should be "A phonetician" (the object is productions).
- l. 312 "the phonological and prosodic relations" is vague.
- l. 1047 "phonological interjection" has no named user.

**"Prosodic":** Mostly specified (l. 1052 is exemplary). "Separate intonational packaging" is predicated of sign-types (l. 111, 301) and of realizations. §4.2 separates them, so this is minor.

**"Syntactic":**
- l. 1088 "syntactic independence" should specify non-integration (supplement or independent status).
- l. 115 "Syntax itself requires more than lexical classification" names an inquiry. That's acceptable, but see 4.9.

**"Pragmatic":** none (l. 319 is Wilkins's term).

---

## 3. Source fidelity (CGEL)

- **Both quotations are verbatim, on the cited pages.**
  - p. 30: "on the basis of their inflection, the kinds of dependent they take and the function in larger constructions of the phrases they head" and "make general statements about words".
  - p. 1361: "The general definition of interjection ... do not combine with other words in integrated syntactic constructions, and have expressive rather than propositional meaning"; "primarily verbs"; "have lost their verbal meaning, and are best regarded as having been reanalysed as interjections".
  - p. 1361 n. 70: "It may be best to regard such words as exceptional interjections that combine with an NP complement to form an interjection phrase". The paper's "tentatively" is faithful.
  - "Ah, so you were there after all!" is [31i] on p. 1360, within the cited range.
- **The new paraphrase at l. 255–257 is faithful.** p. 31: "At the language-particular level ... it is necessary to focus on form ... At the general level it is quite legitimate to invoke meaning". p. 32: the category "as a whole satisfies the general definition".
- **"As CGEL's own treatment of *damn* ... does in practice" (l. 261–262) is defensible.** CGEL grounds the reanalysis in lost verbal meaning, and n. 70 rejects an understood subject because it "doesn't match their normal interpretation now".
- **Remaining problem:** l. 294 (item 1.5).
- **Unused support:**
  - n. 70 says "Historically, the blast and damn constructions were understood with God as subject". Cite it at l. 1165–1171, where the verbal route is called "partly reconstructive".
  - p. 1350 supports 1.1; p. 1360 supports 1.12.

---

## 4. Quality

### Important

**4.1 The same point is restated about eight times.** That conative *sh* lacks stance and prenominal *damn* shares it from outside the category appears at roughly l. 294–299, 429–435, 665–667, 684–686, 855–861, 1404–1410, 1445–1449 and 1508–1512. The *Dr Brown* subject/supplement contrast appears four times (l. 363–368, 616–620, 712–716, 1398–1400). Fix: cut §2.7's and §3.1's *Dr Brown* passages and l. 855–861, and compress §7's opening.

**4.2 The prosodic projection is screened off on the paper's own account.** "Separate intonational packaging" is listed as a projection of category membership (l. 72, 111, 301–303, 1390, 1501–1502). But l. 370–375 and l. 1065–1067 concede that supplement function predicts the boundary. Ameka's "including when they accompany another utterance" is the supplement case, and independent utterances are trivially their own units. Fix: give an interjection-specific prosodic expectation, or demote prosody in the abstract and conclusion. Then promote the sharper lexical projection buried at l. 876–878, resistance to determiners with conversion as the defeat condition (*a loud ouch*), into §2.1.

**4.3 The paper's one demonstrated competition is hypothetical (l. 517–523).**
> "These are hypothetical rivals, not summaries of Potts and Wharton."

Wharton 2016 (*Lingua* 175–176: 20–35) isn't held, so I can't say whether it argues against Potts. Check it. If it does, the real pair is the stronger case. Otherwise, use a real dispute the paper already has: Ameka versus Wilkins on routines (l. 590–597), or the category of the head in *damn* + NP.

**4.4 *Damn* + NP is a missed payoff (l. 407–414).** Here the diagnostics diverge:
- the NP complement looks verbal;
- independent status looks interjectional;
- CGEL n. 70 says the verbal meaning is gone;
- inflection is uninformative in a plain-form environment.

The converging account predicts an unresolved case, so say that instead of just calling it unresolved. Fix: "Here the diagnostics diverge: the complement looks verbal, the detachment and the lost verbal meaning look interjectional, and the plain form gives inflection no opportunity to show. On a converging account an unresolved assignment is the expected result."

**4.5 *Bye* is "Left open here" (l. 652) without applying the diagnostics** to the Ameka/Wilkins dispute (l. 590–597). At least say which diagnostic the two disagree about.

**4.6 Revision residue that the end-reader never saw.**
- l. 184–186 and l. 1370–1374: "Their confirmatory claims are withdrawn." Withdrawn from what? Fix: "The supplement also reports two analyses that can't bear confirmatory weight (Sections B–C)." Explain "derivatives" and "semantic residue" in the supplement only.
- l. 1413–1415: "a fixed arrangement with one category for grammar, another for semantics, and a third for interaction". The opponent is main.tex's own thesis (`main.tex` l. 90–93), not anything in this manuscript.
- l. 750 and l. 811: "differently named property".
- l. 852–853: "without a new experiment in this paper".
- l. 1262–1263: "beyond a frequency difference between geographical collections".

Cut each, or rewrite it in fresh terms.

**4.7 The "not which field owns it" frame recurs with no one cited as holding that view** (l. 728, 764, 847, 1480–1485, 1522). Keep l. 594 and l. 1434, where a real disagreement is at stake. Cut the rest, or name a holder.

**4.8 Caveat density.** "needn't / alone doesn't / by itself / doesn't itself / doesn't automatically" occurs 30 times in about 10,400 words.
- The worst stack is l. 823–829: four sentences of non-claims ("Projective warrant doesn't require..."; "support for a subtype doesn't automatically extend..."). Keep the last clause and cut the rest.
- Also trim the closing caveats at l. 283–285, l. 310–312 and l. 1132–1136.

**4.9 Sealed closers and restatement presented as revelation.**
- l. 472–478 "The descriptive comparison has a definite result. Separate expressive and depictive groupings preserve a difference in contribution that the undifferentiated alternative omits." The result is that drawing the distinction preserves it. Lead with the repetition contrast instead, and merge l. 464–470 with l. 480–486, since Potts on repetition is cited twice in a row.
- l. 896–902 restates l. 889–894 and l. 865–867. Cut l. 896–902.
- Other closers to cut:
  - l. 374–375 "These are connected inferences."
  - l. 461–462 "Repetition can thus transform the contribution in different ways."
  - l. 536–538 (a rule-of-three ending on an abstraction)
  - l. 576–578 "Thus the admission rule concerns..."
  - l. 1451–1453 "Their value lies both in ... and in ..."
  - l. 1097 "extend the family" ("family" is undefined)
- Corrective negation with no opponent: l. 115 "Syntax itself requires more than lexical classification"; l. 668 "A single ordering from less to more interjectional" (name the gradient accounts or cut); l. 1301–1302 (*um* and the grammar of *kick the bucket*).
- Colon reveals (minor): l. 159–160 "The division of labour here is different:" and l. 1421 "add a practical requirement:".

**4.10 Paragraphs that don't advance the argument.**
- Hill 1965 (l. 945–951): Gehweiler already supplies the temporal order.
- *Ouch* / *Aha* (l. 525–538) is misplaced in the encoding section. Move it to §2.3 as a third case where the category and the expressive grouping come apart.
- l. 993–999 treats phonological evidence as concerning a different subject from category membership. That undercuts the converging account, and l. 1001–1006 then corrects it. Keep only the depiction-versus-anomaly sentence.
- l. 1017–1024 "The strongest alternative ... that sufficient test" is obscure. Fix: "A broad class of phonologically unusual forms, with lexical category recorded separately, loses nothing for known cases. It fails only if membership in it is treated as sufficient for interjection status."
- l. 904–908 "A quoted token ..." has no clear antecedent.
- §6.1 and §6.3 are hypotheticals that each end "would need evidence". Compress them to one paragraph.

**4.11 The path-dependence argument is thin (l. 1125–1131).** What's explained is the form's relation to its source, which is etymology. The more interesting residue is left dangling at l. 1123: "The source invocation already permits peripheral packaging." Develop that with Gehweiler (pp. 84–85, per DECISIONS 2026-11-02; I didn't check the pages), or drop "path dependence" from the keywords.

**4.12 The contribution relative to Dupré and Khalidi is undersold (l. 1421–1427).** "Specify which relation ... and which objects" is modest. Name the paper's own tools: the per-inference source–target rule, and the identification-rule discipline of §3.3. Don't claim novelty without checking Khalidi 2013.

### Minor

**4.13 "The working class collects" (l. 560)** invites the social-class reading. Fix: "This working grouping".

**4.14 The `\href{inquiry-relative-evidence-supplement.pdf}` link (l. 1376)** won't resolve in a submitted PDF.

**4.15 "Gehweiler's primary *gee*" (l. 1142)** is unchecked against Gehweiler.

---

## Cross-document flags (corpus awareness)

- **Thesis:** main.tex argues for three classifications: grammar-facing, semantics-facing and interaction-facing (`main.tex` l. 90–93). This draft rejects that arrangement (l. 1413–1415).
- ***Bang!*:** main.tex places *Bang!* as a grammar-facing member (DECISIONS.md, 2026-11-02 entry at line 1053). This draft leaves its category unresolved (Table 1, l. 654).

If this draft supersedes main.tex, record both points in DECISIONS.md as deliberate distinctions.

## What would change these findings

- If Brett intends prosody and phonology as projection targets only, 1.3 is wrong, and so are DECISIONS.md line 1056 and the brief.
- If the pp. 31–32 paraphrase comes out again, 1.5 shrinks, but l. 294 would still misdescribe CGEL.
- If Wharton 2016 doesn't oppose Potts, 4.3 reduces to "use the Ameka/Wilkins dispute".
- Further concurrent edits may already have addressed some items.
