# Independent read of the perspective-precision revision
<!-- SUMMARY: fresh-context Claude verifier (read-only) on inquiry-relative-categories.tex; lead finding: meaning-based assignment recycled the projected meaning; saved by the parent verbatim · status: record · updated: 2026-11-03 -->

Saved by the parent session (Claude Code, Opus 5.5) verbatim from the verifier's handback. Model output; findings were checked against CGEL pp. 31-32 before being applied.

---

Adversarial read of the perspective-precision revision to `inquiry-relative-categories.tex`

No RESPONSIBILITY NOTICE: these are review findings, with no coordination or authorization risk. I edited nothing.

Files read in full: the revised `/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/inquiry-relative-categories.tex` (1545 lines) and the pre-revision `/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/reviews/perspective-precision-2026-11-03/before/inquiry-relative-categories.tex`. I compared every changed passage. Sources checked: `/Users/brettreynolds/projects/LLM-CLI-projects/literature/huddlestonpullum2002.md`, `/Users/brettreynolds/projects/LLM-CLI-projects/literature/wilkins1992.md`, `/Users/brettreynolds/projects/LLM-CLI-projects/literature/ameka1992-interjections.md` and `/Users/brettreynolds/projects/LLM-CLI-projects/literature/Potts - 2007 - The expressive dimension.md`. Line numbers below refer to the revised .tex unless marked "md".

---

## Bottom line

The revision's first key move, "converging evidence about distribution and meaning" for assignment, is the one I'd reverse. It conflicts with the paper's own source–target rule, and it isn't what CGEL's §4.4, Wilkins or Ameka say about assignment. The damn-boundary fix overcorrects. The definition the revision now relies on already settles that an integrated modifier isn't an interjection. The phonology fix (conventional form vs productions) is clean. The CGEL p. 30 move is fine as a quotation, but the same section of CGEL undercuts the meaning-based assignment.

---

## A. Lead finding: assignment by meaning recycles the projected meaning (items 2 and 3)

**The lines:**
- 240–241: "Assigning a word to the category thus draws on evidence about distribution and about meaning together."
- 257–258: "An analyst who has assigned reaction \mention{ouch} to the category, from its reactive meaning and from independent uses..."
- 276–279: "Membership also supports more specific expectations about meaning than the definition's contrast between expressive and propositional meaning. Members characteristically express reactions..."
- 302–303: "Where an assignment has been made without using the target property, membership can guide expectations about that property."
- 834–837: "...\textit{CGEL}'s definition already joins the first two. What matters for each expectation is whether the projected property helped assign the case, not which field reported it."
- 1504–1506: "Assigning a sign-type to the category, on converging evidence about distribution and meaning, gives reason to expect a reactive, expressive, or conative use"
- 111–112: "A lexical category can thus guide inquiry well beyond the evidence used to assign its members."

**The internal problem (holds whatever CGEL says).**
- Under the rule at 302–303 and 836–837, an expectation about meaning has no projective force when meaning helped assign the case.
- For the paper's own worked case, ouch is assigned "from its reactive meaning" (258), and membership then projects that members "express reactions" (278–279).
- The conclusion (1504–1506) says outright that assignment on meaning gives reason to expect a reactive or expressive use.
- The "more specific" defence at 276–277 doesn't hold. Line 306–307 says CGEL's criterion is "broad enough to cover conative \mention{sh}", so the range at 278–280 is a partition of that criterion. Line 283–284 then concedes the category doesn't say which part ("the narrower groupings specify which one").
- So for meaning, membership adds nothing beyond the assignment evidence. And 111–112 is false as written, because meaning is among "the evidence used to assign its members".

**The source problem.**
1. **CGEL calls the quoted sentence a "general definition" (md 41530).** Its §4.4 (md 1003–1018) separates general definitions from language-particular ones:
   - "A language-particular deﬁnition will enable us to decide which expressions in the language concerned belong to the category."
   - "At the language-particular level, as we have argued, it is necessary to focus on form... At the general level it is quite legitimate to invoke meaning."
   - Membership is decided "by virtue of the distinctive grammatical properties speciﬁed in the language-particular deﬁnition", and "this category as a whole satisﬁes the general deﬁnition".

   So the quotation is accurate, but the "thus" draws an assignment procedure from a definition CGEL says isn't one. This is the same section the paper quotes at p. 30 (md 990). The paper cites the section for the category's place in the grammar and overrides its main point a page later.

   One complication cuts the other way. CGEL's own English description at 1361 does mention meaning: central members "in their sole or primary meaning are used as expressive exclamations", and damn-type verbs "have lost their verbal meaning". So CGEL's practice is mixed, and meaning enters most clearly as *loss* of verbal meaning in the reanalysis cases.
2. **Wilkins (1992: 124, md 33) states the paper's source–target rule as his method.** Defining by one type of criterion "allows the investigator to examine the set of elements thus defined to see whether it also manifests other regular features describable in terms of the other two domains (i.e. the domains which did not supply the criteria...)". He adds (p. 125, md 53): "I have clearly avoided any mention of the semantic or pragmatic functions of interjections." The paper cites exactly this at 251–254, one paragraph after adopting the opposite procedure.
3. **Ameka (1992: 105–106, md 206–208):** primary interjections are defined "in terms of their distribution". Meaning enters only for secondary interjections ("refer to mental acts", md 201–205).

So the abstract's "Established descriptions identify core members... from converging evidence about distribution and meaning" (66–69) misdescribes two of its three sources. The abstract's colon gloss also gives only the distributional half.

**Fix (a), recommended: assign the core on distribution and project meaning.** It takes few edits, it matches the cited sources, and it makes the paper's rule hold for meaning. It doesn't bring back the partition by discipline you diagnosed, because the evidence is named by its object (distribution), not by the field that reports it.
- 237–242 → "Its general definition adds a semantic clause: interjections \enquote{do not combine with other words in integrated syntactic constructions, and have expressive rather than propositional meaning} \citep[1361]{HuddlestonPullum2002}. \textit{CGEL} uses such definitions to characterize a category as a whole, and decides which English words belong by their form \citep[30--31]{HuddlestonPullum2002}. I assign the core by distribution, as \textcite[124]{wilkins1992} does, so its characteristic meanings remain available as expectations." (Check the 30–31 page range against the PDF; see "Inferred" below.)
- 258: delete "from its reactive meaning and".
- 66–70 abstract: "...including \mention{ouch}, \mention{oops}, \mention{hey}, and \mention{sh}, by their distribution: in their conventional uses these words stand alone or supplement a clause without entering integrated constructions. Membership also supports expectations about characteristic meanings..."
- 276–277: "Membership also supports expectations about meaning."
- 834–836: end the sentence at "distribution, meaning, and sound." Delete "\textit{CGEL}'s definition already joins the first two", which puts an admission rule among the warranting observations.
- 1504–1506: "Assigning a sign-type to the category from its distribution gives reason to expect an affective or cognitive reaction or an attempt to direct attention or action, often..."
- 589: "these converging descriptions" → "these descriptions".
- 386–388 can stay ("Their distribution and that change in meaning link them to the core"). That's CGEL's own use of meaning loss for reanalysed verbs.

**Fix (b), if you want to keep converging evidence.**
- Assignment may use only the negative criterion: the use contributes no proposition that could be denied or questioned.
- 258 becomes "from its non-propositional meaning".
- Every projected meaning claim must name something finer than "expressive", and the paper must say what the projected range excludes among non-propositional meanings. Otherwise the expectation adds nothing.
- 1506 has to change either way.
- The abstract would have to attribute converging assignment to CGEL alone, not to "established descriptions".

**What would reverse this:** if you hold that English assignment legitimately uses meaning (as CGEL does for reanalysed verbs), the conflict with §4.4 weakens. The recycling at 258/278/1506 stays an inconsistency under the paper's own stated rule, so you'd still need (b) at minimum.

---

## B. Prenominal damn: the imported definition settles what the revision leaves open (item 2)

- 238–239 quote CGEL: interjections "do not combine with other words in integrated syntactic constructions".
- 391–392 and 887–889: prenominal damn is "an integrated modifier inside the noun phrase".
- 403–405: "Whether the difference also crosses the boundary of the lexical category interjection would need an analysis of that use's category, which the expressive grouping doesn't require."

By the definition the paper now relies on, an integrated modifier isn't an interjection. CGEL's one exception (n. 70) is for heads taking an NP complement, not for modifiers. What's open is which category prenominal damn belongs to, not whether it's an interjection. The hedge also costs an argument. At 429–432, "come apart" now rests on sh alone, because "whatever its category" withdraws the second direction.

Minimal fix: replace 400–405 with one sentence. "Calling prenominal \mention{damn} a modifier specifies its function; that integrated position falls outside the interjection category as defined, and I leave open which category it does belong to." Then:
- cut "whatever its category" (432);
- cut "including one whose lexical category is left open" (162–163);
- keep "Left open here" in Table 1 (648).

**What would reverse this:** an analysis in which prenominal damn isn't integrated (an expletive-insertion analysis, say). If that's what you have in view, name it. Then "integrated modifier" at 391–392, 889 and in Table 1 is the claim that needs hedging, not the category.

---

## C. "Difference in function" with standalone Damn! contradicts the paper's status/function rule (item 2, introduced by the revision)

Lines 375–376 and the Table 1 caption (630–631) stipulate that independent utterance "is a status, not a syntactic function". Yet the revision uses "differ in function" for the standalone/prenominal pair at:
- 162;
- the §2.3 heading (380);
- 396 ("A functional analysis separates the two uses, one an independent utterance and the other a modifier");
- 426, 688, 783 (Table 2), 858, 1413–1414 and 1514 ("connects standalone and prenominal \mention{damn} across their difference in function").

A functional analysis assigns no function to standalone Damn!. Fix: wherever function is the claim, compare *supplementary* damn (a supplement) with the prenominal modifier, which is a genuine difference of function. For example:
- 396: "A functional analysis separates supplementary \mention{damn} from the prenominal modifier; the expressive analysis groups them."
- 1514: "connects supplementary and prenominal \mention{damn} across their difference in function".

Where the standalone use has to stay, write "difference in integration".

---

## D. Other errors, overclaims and new imprecision (item 2)

1. **"Contribution" now has two senses, and the revision caused it.** The term `\term{contribution}` (740), and the Table 2 row "Contribution", mean what a grouping accomplishes. The revision replaced "semantic" with "contribution" in the other sense, what a use contributes to interpretation: 78, 416 ("The grouping by contribution"), 787 ("relations of contribution", in the same table as the "Contribution" row), 857, 1264, 1284, 1331, 1417, and the Table 1 caption.

   Fix: rename the assessment slot `\term{achievement}` at 697–699 and 740, and in the Table 2 row. The paper already says "These achievements can accumulate" (746–747). Table 2, 787: "Compare which differences in contribution each preserves".
2. **The disciplinary partition is back at 315–317:** "The category's value to other inquiries comes from the further associations of membership with meaning, use, and realization." That gives grammar the constructional statements and gives "other inquiries" meaning and realization. But the paper says a syntactician needs prosodic detachment (351–357, 1498), and CGEL, a grammar, describes supplement intonation (1350). Fix: "Membership is informative beyond those statements through its associations with meaning, use, and realization."
3. **Ambiguous referent, 686–688:** "Expressive classification extends some of those expectations to a use with a different function". Read as written, "those" picks up the expectations of the category or of supplement function, and neither extends to prenominal damn. Fix: "Expressive classification supports its own expectations, about perspective and repetition, for uses that differ in function".
4. **1180–1182:** "could cross the present boundary between the verbal and interjectional analyses". A classification doesn't cross a boundary between analyses. Fix: "A classification by independently established verbal ancestry would include the head whichever present analysis is right."
5. **583–585, "a classification by function" for Ameka's phatic class.** This collides with the paper's syntactic sense of *function* (CGEL p. 23, line 325–331). Fix: "a classification by communicative function".
6. **1015–1018, Bang!:** "Choosing between nominal and interjectional analyses needs distributional and constructional evidence". Under the revision's converging-evidence view, this should also ask whether depiction counts as "expressive rather than propositional" meaning, and the paper doesn't say. Under fix (a), 1015–1018 is already consistent. That's another reason to prefer (a).
7. **313–316:** the "general statements" listed for interjections are the definition's distributional half restated. In §3.2's terms (794–798) that's an admission rule, not category standing. Optional fix to link the two: "...and characteristically lack inflection. Within syntax, membership licenses the inference from one environment to the other."
8. **1407:** "That variation leaves other groupings useful." Its referent is two paragraphs back, across the syntax paragraph (pre-existing, but now harder to follow). Fix: "Variation in the associated properties leaves other groupings useful."

---

## E. Does the source–target rule hold elsewhere? (item 2b)

- **Potts's immediacy recycles the expressive admission rule.** The admission rule is "conventional uses whose deployment conveys an evaluative or affective stance, rather than merely describing that stance" (416–418). Potts's immediacy (md 37) is that expressives "achieve their intended act simply by being uttered; they do not offer content so much as inflict it". The paper's gloss, "whether the utterance displays that attitude on the occasion of speaking" (424–425), is closer still to nondisplaceability ("Expressives predicate something of the utterance situation", md 28). Either way the projected property re-describes the admission criterion. Fix at 421–425: "Potts's account supplies expectations about perspective dependence and intensifying repetition \citep[166--167]{potts2007}. For \mention{damn}, these ask whose attitude is conveyed and whether repeating the form strengthens it." Perspective dependence and repetition are distinct from admission and are fine.
- **Supplements are partly identified by prosody.** CGEL's wording at 1350 (md 41213) is "In speech, supplements are marked as such by the prosody: they are intonationally separate". So for spoken data, detachment is part of how supplement status is identified. "An independently established supplementary analysis" (353) needs a stated non-prosodic route, or the functional grouping's prosodic expectation (also in the abstract, 74) is partly definitional. Fix at 353: "An analysis established without prosody, from the anchor's completeness as in (\ref{ex:core-distribution}), gives reason to expect that packaging..." CGEL also gives scope as a non-prosodic test: supplements "do not fall within the scope of negatives in the anchor" (md 41523, about p. 1360, said of PP and AdvP supplements).
- **mm-hm:** it's assigned partly through Ameka's phatic classification (583–584), and then membership "can orient expectations toward... interaction-managing uses" (555–556). Under fix (a), base the assignment on the non-elliptical analysis (587–588) and cite Ameka as corroboration of its job.
- **Checked and fine:** 256–263 under fix (a), 729–733, 844–849, 876–881, 1072–1078, 1183–1184 and 1199–1201.

---

## F. Remaining loose perspective labels (item 1)

| Line | Text | Should specify | Minimal fix |
|---|---|---|---|
| 97 | "differ in their grammatical organization" | constructional status and function | "differ in how they combine with other words" |
| 101–102 | "grammatical analysis distinguishes their constructional possibilities and asks which belong to..." | analyses of function and lexical category | "while analyses of function and lexical category distinguish them and ask which belong to the category interjection" |
| 161 | "including expressive and conative contributions" | Ameka's sense, next to the stance sense in the following sentence | "including reactions and attempts to direct attention or action" |
| 239/282/306–310/416/1506 | "expressive" | CGEL's definitional sense (non-propositional, covers sh), Ameka's functional sense (vs conative, phatic), the paper's stance sense (Potts) | at 416 add: "I use \term{expressive} in this narrower sense from here on." At 1506, "reactive, expressive, or conative" can't be read as a partition (reactive is a kind of Ameka-expressive), so use the fix in A |
| 640 vs 1408–1409 | ouch: "Pain or mishap reaction" in Table 1, but "its affective contribution" at 1409 | whether ouch is an expressive sign under 416 | decide; if it is, the Table 1 cell becomes "Affective reaction (expressive)" |
| 604 | "the combination of grammatical, semantic, interactional, and other properties" | the objects of the properties | "the properties attributed to it: the constructions its occurrences enter, its contribution to interpretation, its sequential uses, its conventional sound shape" |
| 735–736 | "needn't belong to the same domain" | kind of property | "needn't be the same kind of property" |
| 957 | "informative about sound as well as distribution" | conventional form vs the packaging of realizations | "about conventional sound shape and the packaging of its realizations, as well as distribution" |
| 1042–1044 | "assign every occurrence resembling \mention{huh}" to a class of signs | sign-type, not occurrence | "every form resembling \mention{huh}" |
| 1499 | "is as grammatical as an interest in lexical membership" | asserts something about the label; 1403 already makes the point | cut, or "Both belong to syntax." |
| 450 | "their grammatical organization varies across languages" | probably morphosyntactic integration | I didn't check Dingemanse 2018: 2–3. Check before changing. |

The internal label `sec:grammatical-core` is cosmetic and invisible to readers.

---

## G. CGEL support (item 3)

**Verified verbatim:**
- 1361 definition (md 41530). Accurate, but CGEL calls it the "general definition" (see A).
- Central-member list, "on their own, or as supplements with clausal anchors", and "(or the now dated alas)" (md 41530).
- n. 70, "It may be best to regard such words as exceptional interjections that combine with an NP complement to form an interjection phrase" (md 41548). "Tentatively" (410) is fair.
- p. 30, "make general statements about words" (md 990).
- p. 23, category vs function (md 822, 827).
- p. 1350, supplements "intonationally separate" (md 41213). The full wording "marked as such by the prosody" matters for E.
- The examples in (ex:supplements) appear verbatim at md 41528, 41412 and 41435.

**Not supported or misstated:**
- 240–241, the "thus": see A.
- 385, "\textit{CGEL} treats these uses as verbs that have \enquote{lost their verbal meaning}". CGEL treats the *words* as "primarily verbs" and these *uses* as reanalysed interjections, and its sentence concerns supplements; standalone Damn! is the paper's extension. Fix: "\textit{CGEL} counts \mention{damn} among words that are \enquote{primarily verbs} but in supplements like this one \enquote{have lost their verbal meaning, and are best regarded as having been reanalysed as interjections}."
- 311, "lets the grammar \enquote{make general statements about words}". CGEL's agent is "us", the grammarians. Fix: "lets a grammarian \enquote{make...}".
- 315–316, "characteristically lack inflection", is presented as one of CGEL's general statements, but it isn't on p. 1361. Cite Ameka 105–106 (md 253: "do not normally take inflections or derivations").

**Not checked:** pp. 22, 66, 944, and the exact page numbers 1356–1357 and 1360 (the examples exist; the page markers weren't read).

**Synergy:** CGEL's general/language-particular split is close kin to Haspelmath's comparative concepts and descriptive categories, which the paper cites at 154–156. Using CGEL's general definition as an English assignment test is the confusion both warn against. One sentence at 154–158 could connect them.

---

## H. Prose tics (item 4)

1. **The "rather than the field" frame appears six times:** 763–764, 836–837, 848–849, 1008–1009, 1489–1490, 1527–1528. The 836–837 instance ("not which field reported it") was added by the revision, duplicates 848–849, and answers the old draft rather than the reader. Cut it. Keep 848–849 and 1527–1528, and trim the rest.
2. **Corrective negation with no named opponent:**
   - 125–126, "would do nothing to resolve those questions": nobody is cited as assigning stance to semantics and depiction to semiotics. Cite someone or cut the sentence.
   - 402, "What the comparison establishes is a difference of function and integration": a pseudo-cleft written for the corrector. Goes with the fix in B.
   - 589–590, "rather than deductions from punctuation": cut.
   - 1410–1412, "needs no intermediate degree of interjection membership": name the gradient account or cut.
   - 1521–1522, "it doesn't reconcile them": repeats "unresolved"; cut.
3. **Caveat stack.** Disclaimers that examples are constructed or illustrative: 264–265, 461–462, 529, 579–580, 616, 891, 1210. One sentence at the first example would replace most of them (after 218): "Examples are constructed unless a source is cited, and the tables record analytical judgments." Keep 522 ("hypothetical rivals, not summaries of Potts and Wharton"), which protects attribution. The openness of prenominal damn's category is stated four times (162–163, 400–405, 432, 648); once in §2.3 plus the table is enough.
4. **Sealed closers.**
   - One formula appears four times: "each preserves... / either alone would lose" at 377–378, 397–398, 1414–1415 and 1457–1458. Cut 397–398 and 1414–1415.
   - Other restating closers to cut: 143–144 ("These achievements need separate assessment."), 702, 930 ("Whether it does is a comparative question."), 1517–1518 ("An apparent anomaly can thus reveal..."; which anomaly isn't named).
   - 111–112 is a sealed closer and, after the revision, false (see A).
   - Keep 274, 1050–1051 and 1447–1448, which state consequences.
5. **Colon reveals:**
   - 68–70 (abstract): announces two kinds of evidence and delivers one.
   - 308–310, "which concerns evaluative or affective stance: \mention{sh} is a secure member...". Use "; \mention{sh}" or "and \mention{sh}".
   - 1412–1414 is borderline.
6. **"Not X but Y":** 477–478 ("requires the distinction; it doesn't require a particular taxonomic rank") is a restating closer, so cut its second half. 243–244 and 1146–1148 have real targets; keep them.

---

## Verified, inferred, and what would reverse it

- **Verified directly** (quoted above with md lines): the CGEL passages, Wilkins pp. 124–125, Ameka pp. 105–106, and Potts's property list. I also confirmed that 258, 278–280, 302–303, 836–837 and 1504–1506 conflict as described.
- **Inferred:** the CGEL page numbers for §4.4. The md shows running heads for p. 27 at line 923 and p. 33 at line 1024, so "make general statements" on p. 30 and the general/language-particular passage on pp. 30–31 are plausible but weren't read off a page marker. Check against the PDF before citing pp. 30–31.
- **What would reverse the findings:**
  - A: see the note at the end of A; at least fix (b) is needed regardless.
  - B: an analysis of prenominal damn as non-integrated (also noted at the end of B).
  - C doesn't depend on any source; it follows from the paper's own stipulation at 375–376.
