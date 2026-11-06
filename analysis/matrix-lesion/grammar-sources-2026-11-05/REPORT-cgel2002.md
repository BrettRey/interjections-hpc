# CGEL (Huddleston & Pullum 2002): extraction report

Saved verbatim by the parent session (Claude Opus 5.5) from the subagent's SubagentHandback report. Model output, not a source; every quotation is checked by the parent against the page-marked source text before use.

---

CGEL (Huddleston & Pullum 2002) extraction for the matrix-lesion v4 bearers

No RESPONSIBILITY NOTICE: I found no authorization or oversight risk. Two discrepancies with the project files go first.

**Discrepancies with items-v4.csv (flagged, nothing acted on)**
- **BLOODY_INTENS.** The rationale cites p. 584 for "adverbial modifiers of adjectives, not of verbs". In this text the "not of verbs" mark appears on `damn –v` and `very –v`, but `bloody` is unmarked (file line 29619: "bloody          damn –v"). CGEL states "not of verbs" for damn and very, not for bloody. An OCR drop of the mark is possible, so check the PDF (PDF page 604).
- **BASTARD_SUPP.** The rationale says the epithet forms its "own intonation unit". CGEL limits that to the epithet that comes before the clause ("when it precedes the clause nucleus", p. 1413). The item's own example puts it at the end ("He's taken my chair again, the bastard").
- **THE_HELL_WH.** "Immediately after an interrogative" is CGEL's wording on p. 916. P. 1087 says such phrases "can only occur initially". Both pages apply.
- **p. 1584.** In CGEL this page is about comparative inflection. The tmesis page 1584 belongs to Quirk et al. (App. I.75), as items-v4 already says for BLOODY_INFIX. CGEL has nothing on tmesis (see section 4).

Page conversion checked against running heads (printed = PDF − 20): PDF 573 = 553, 578 = 558, 588 = 568, 604 = 584, 605 = 585, 936 = 916, 1009 = 989, 1107 = 1087, 1381 = 1361, 1433 = 1413, 1604 = 1584, 1636 = 1616. "L." gives the line in cgel2002-paged.txt. Quotations that wrap across lines are joined with single spaces, so normalize newlines and indentation before string-checking. I reproduced ∗ (U+2217), curly apostrophes, ·ly and ∼ as the file has them.

## 1. Table

| item_id / CLASS | property | value | scope | "quotation" | p. | note |
|---|---|---|---|---|---|---|
| DAMN_PRENOM | predicative use (attributive-only) | N | item | "Thus we have that damn noise, but not ∗That noise is damn ;" | 553 | L.28099. Starred example. Damn is in list [1] of attributive-only adjectives (L.28094). Hedged by n. 10 ("normally"; see section 3). No P-row in v4. |
| DAMN_PRENOM | P03 INTEGRATED | Y | item | "that damn noise" | 553 | L.28099. Attributive modifier. |
| CLASS:attributive-only adjectives | definition | — | class | "Adjectives that do not normally occur except as (heads of) attributive modifiers include:" | 553 | L.28093. Members in [1] include damn, frigging, main, mere, utter, very (the adjective), own, sole. |
| CLASS:expressive attributives [15] (dear, poor, wretched; bleeding, bloody, fucking) | modifiability (P04 modifiers), pro-form *one*, subset | N (all three) | class | "These items are all semantically non-restrictive. They pass the entailment test, but fail the other three." | 558 | L.28334–28335. "The other three" are subset, modifiability and pro-form (defined p. 554, [3]). This is an unhedged failure statement. Complements aren't addressed, so P04 is N for modifiers only. |
| CLASS:attributive-only expletives | attributive-only + non-propositional | Y | class | "a quite large number of attributive- only expletives, items that make no contribution to the propositional meaning of the clause" | 558 | L.28335–28337. Hyphen break at "attributive-". Here meaning is tied to a form property (attributive-only). |
| CLASS:attributive-only expletives | membership / strength | — | class | "These expletives vary considerably in expressive strength, with damn(ed) at the low end of the scale and regarded as quite mild, fucking at the high end" | 558 | L.28338–28340. Places damn(ed) in this class, so the [15] class row applies to DAMN_PRENOM by membership. |
| BLOODY_PRENOM | P03 INTEGRATED | Y | item | "the bloody tax inspector" | 558 | L.28333. Also "You’re a bloody genius!" (L.28338). |
| BLOODY_PRENOM | P03 INTEGRATED | Y | item | "my bloody sales tax" | 36 | L.2435. This is the prenominal use, not BLOODY_INTENS. |
| BLOODY_PRENOM | P07D DESCRIPTIVE | N | item | "the truth conditions for [iiib] are exactly the same as those for [iiia]." | 37 | L.2467–2468. Meaning, with no form tie. Grouped with *but* and *even* (see section 3). |
| FUCKING_PRENOM | P03 INTEGRATED | Y | item | "a fucking investigation" | 558 | L.28333. The [15] class row applies. |
| CLASS:expletive adjective–adverb pairs [15iii] (bleeding, bloody, damn(ed), fucking) | no ·ly adverb | N (·ly form) | class | "Those in [iii] are representative of expletives which occur as attributive-only adjectives and systematically exclude the ·ly suffix, giving a bloody disgrace vs bloody disgraceful." | 568 | L.28841–28843. The heading of [15] is "Pairs where there is little if any difference in meaning" (L.28824). This links the PRENOM and DEGREE uses of damn and bloody as a same-form adjective–adverb pair. ·ly is derivation, not P05. |
| BLOODY_INTENS | degree modifier of an adjective | Y | item | "bloody disgraceful" | 568 | L.28843. |
| BLOODY_INTENS | modifies verbs (–v) | U | item | "bloody          damn –v" | 584 | L.29619. Bloody is listed but has no –v mark. Silence, not N. |
| BLOODY_INTENS | takes a modified phrase as head (submodification) | Y | item | "bloody nearly completely useless" | 585 | L.29688. Bloody modifies *nearly completely useless*. This is evidence of the degree use, not of bloody taking a dependent (not P04). |
| DAMN_DEGREE | modifies verbs (–v) | N | item | "But we do not find ∗I as enjoyed it as Kim, ∗I damn hated it, ∗They dead hit the target, etc." | 585 | L.29654. Starred. –v is defined at L.29640: "The items in [31] marked ‘–v’ do not occur with the same sense as modifiers of verbs." Example "damn rude" at L.29642. |
| DAMN_DEGREE (use uncertain) | clause-level *damn well* | Y | item? | "Damn and jolly combine with well to form clause-level modifiers with emphatic meaning: I damn/jolly well hope you’re right." | 585 | L.29660–29662. It's unclear whether *damn well* is DAMN_DEGREE or a separate use. |
| VERY_INTENS | modifies verbs (–v) | N | item | "∗They are very entertaining the prime minister and her husband." | 81 | L.4480. Also "very –v" (p. 584, L.29624) and "Since very cannot modify verbs" (p. 553, L.28073–28074). The same property as DAMN_DEGREE, held by a control. |
| VERY_INTENS | P10A REPEATABLE (adjacent) | Y | item | "very, very good" | 585 | L.29689. Also "The examples in [ii] illustrate the adverbs that iterate most readily" (L.29690). Nothing on iterating damn or bloody. |
| VERY (adjective, not VERY_INTENS) | homonymy | — | item | "The meaning of very in very kind is clearly different from that of the adjective in this very room or the very edge of the cliff" | 568 | L.28820–28821. Very in the p. 553 attributive-only list is this adjective. |
| CLASS:degree adverbs | no 'intensifier' category | — | class | "the number of –v items is very small in comparison with the total number of items that can function as degree modifier in the structure of AdjPs and" | 585 | n. 18, L.29696–29697. See section 3. |
| CLASS:degree adverbs dead, plain | restriction to particular hosts | Y | class | "Dead and plain combine with a quite narrow range of adjectives." | 585 | L.29664–29665. Host restriction in non-expressive degree adverbs. |
| CLASS:degree attributives ending in ·ing [8ii] (blithering, crashing, thumping) | restriction to particular hosts | Y | class | "attributive-only adjectives ending in the suffix ·ing belonging to informal style; they tend to combine with only one or two nouns as head" | 555 | L.28204–28205. Expletives aren't listed here; the hedge is "tend to". |
| MAIN_PRENOM | attributive-only | Y | item | "main" (list [1]) | 553 | L.28095. In the same list as damn. |
| MAIN_PRENOM | pro-form *one* | Y | item | "the main ones" | 555 | L.28183. Contrast "∗an utter one" (L.28184). |
| MAIN_PRENOM | P04 (modification) | N, hedged | class | "They allow the pro-form one (cf. the main one), but do not normally accept modification." | 558 | L.28329–28330 (particularising attributives). "Normally" isn't "never", so this is a questionable N under the brief. |
| PROBABLE_PRENOM | P03 INTEGRATED | Y | item | "the probable result" | 557 | L.28302 (modal attributives [13i]). |
| PROBABLE_PRENOM | P04 / pro-form | U | class | "They mostly fail the other tests, though a few allow modification (an absolutely certain winner) or accept one as head" | 558 | L.28319–28320. Says "mostly" and is silent on probable itself. Modal attributives are listed under types of attributive-only adjective, but nothing denies predicative *probable*, so predicative use is U. |
| QUICKLY | P05 INFLECTS (comparison) | N | class | "The majority of gradable adverbs have bases formed with ·ly, and the inflectional endings are never attached to bases of this kind" | 1584 | L.78940–78941. Grading is analytic: "Most gradable adverbs take analytic forms: softly ∼ more softly ∼ most softly." (L.78937). Quick ∼ quickly is at L.78953–78955. |
| CLASS:interjection | P03 INTEGRATED, P04 DEPENDENTS | N | class | "a category of words that do not combine with other words in integrated syntactic constructions, and have expressive rather than propositional meaning." | 1361 | L.68018–68020. Definitional. The stated exception is the n. 70 NP-complement case (DAMN_NP). |
| CLASS:interjection | members | — | class | "Central members of the interjection category in English are such words as ah, hey, oh, oops, ouch, sh, ugh, wow (or the now dated alas)" | 1361 | L.68020–68021. The p. 22 list adds damn, gosh, ooh, whoa (L.1707). |
| CLASS:interjection | P01 STANDALONE, P02 SUPPLEMENT | Y | class | "used as expressive exclamations, on their own, or as supplements with clausal anchors" | 1361 | L.68022–68023. Covers AH, HEY, OH, OOPS, OUCH, SH, UGH, WOW, ALAS. |
| AH | P02 SUPPLEMENT | Y | item | "Ah, so you were there after all!" | 1360 | L.68011. Printed p. 1360 (before the PDF 1381 marker). |
| ALAS | P02 SUPPLEMENT, inside the clause | Y | item | "but soon, alas!, the casualties began" | 1734 | L.86412. Alas sits inside the clause, not at its edge. |
| HEY | P02 SUPPLEMENT | Y | item | "Hey, did you hear the weird report on the evening news?" | 1388 | L.69284. Also "Hey, birdbrain!" with a vocative (p. 1652, L.82267). |
| DAMN_REACT | P02 SUPPLEMENT | Y | item | "Damn, we’ve missed the bus again!" | 1360 | L.68012. |
| DAMN_REACT | reanalysis | — | item | "a number of words such as blast, bugger, damn, fuck which are primarily verbs, but which in supplements like that in [ii] have lost their verbal meaning" | 1361 | L.68023–68025. P01 is Y through class membership (reanalysed as an interjection). |
| DAMN_NP | P04 DEPENDENTS (complement) | Y | item | "The verbal origin is more relevant in expressions like Damn these mosquitoes! or Fuck you!, where they have an NP complement." | 1361 | n. 70, L.68060–68061. Category: "It may be best to regard such words as exceptional interjections that combine with an NP complement to form an interjection phrase." (L.68063–68064). Also P01 Y. |
| BASTARD_SUPP | P02 SUPPLEMENT (end) | Y | item | "He’s taken my chair again, the bastard." | 1413 | L.70544. Front: "The bastard, he’s taken my chair again." (L.70543). |
| BASTARD_SUPP | occurs inside the clause (not edge-only) | Y | item | "Max, the bastard, has taken my chair again" | 1413 | L.70552. So "position at clause edges" fails as a restriction. |
| BASTARD_SUPP | P01 STANDALONE | Y? | item | "The bastard! Max has taken my chair again" | 1413 | L.70551. Given as "cf.", punctuated as a separate exclamation. Parent decides whether this counts as standalone. |
| BASTARD_SUPP | meaning tied to supplement function | — | item | "the bastard is a supplement (cf. Ch. 15, §5); it is not referential but is used to express the speaker’s attitude towards the person referred to by he." | 1413 | L.70548–70550. |
| BASTARD_SUPP | P12S PROSODY_SEPARATE | Y (prenuclear only) | item | "when it precedes the clause nucleus, the epithet is prosodically distinct from a left-dislocated NP in that it forms a separate intonational unit" | 1413 | L.70553–70555. Nothing is stated for the clause-final or medial positions. |
| BASTARD_SUPP | P06 NOMINAL_COMB | Y (determiner) | item | "the bastard" | 1413 | Determiner *the*. |
| CLASS:epithet | form tied to epithet use | Y | class | "Some is more natural than a with epithets" | 381 | L.19481. The definition is at p. 380, L.19474–19475: "the head noun idiot is what is known as an epithet, an emotive expression which serves to indicate annoyance with the individual concerned". The quotation stops at the page edge. |
| YOU_BASTARD | P03 INTEGRATED | N | item | "nor in the exclamatory construction You bastard! Such NPs can never occupy a complement position in ordinary clause structure: ∗You fool are late!" | 353 | n. 14, L.18113–18114. An explicit "never". "Such NPs" covers vocatives and the exclamatory construction. CGEL's "complement" includes the subject, so the starred example is a subject. |
| YOU_BASTARD | P01 STANDALONE | Y | item | "the exclamatory construction You bastard!" | 353 | L.18113. |
| YOU_BASTARD | P06 NOMINAL_COMB | Y (determiner *you*, singular head) | item | "The requirement for a plural head with you does not apply in vocative NPs" | 353 | L.18112. The same sentence continues with "nor in the exclamatory construction You bastard!" |
| YOU_BASTARD (vocative, not the exclamatory use) | P04 (modifier) | Y? | item? | "Derogatory terms are commonly accompanied by determinative you, as in you stupid bastard, etc." | 523 | L.26672–26673. This is vocative. Parent decides whether it transfers. |
| CLASS:vocative | P01, position | Y | class | "A vocative can stand alone without any sense of ellipsis" | 523 | L.26684. Position: "in front, central, or end position" (L.26686). Applies to the vocative use only. |
| THE_HELL_WH | P03 INTEGRATED (post-head modifier) | Y | item | "Interrogatives take else and emotive modifiers such as on earth, the hell" | 430 | L.21993. |
| THE_HELL_WH | position immediately after a wh-head | Y | class (emotive modifiers) | "These modifiers are constrained to occur immediately after an interrogative word in head, not dependent, function: ∗[What on earth reason] could they have for rejecting it?" | 916 | L.45907–45909. Examples: "[What the hell] is she trying to do?" (L.45899). |
| THE_HELL_WH | not in situ (initial only) | N | item | "contrast ∗And after that you went [where the hell]?" | 916 | L.45910. |
| THE_HELL_WH | not in situ (initial only) | N | class | "Interrogative phrases containing emotive modifiers such as on earth, the hell, ever, etc., however, can only occur initially, hence not in the position of the gap in [iv]: ∗And so you want what on earth?" | 1087 | L.54339–54341. |
| THE_HELL_WH | restriction to particular hosts (*which*) | N (hedged) | class | "with which, for this involves selection from an identifiable set" | 916 | L.45904. The preceding words are "hardly compatible" (L.45903), a hedge. |
| THE_HELL_WH | meaning tied to position | — | class | "They do not contribute to the propositional meaning, and we will refer to them as emotive modifiers." | 916 | L.45904–45905. Open-ended membership: "Variants of hell in [iia] are heck, blazes, deuce, dickens, fuck, etc." (L.45905–45906). |
| THE_HELL_WH | host restriction (subordinate clauses) | N outside question-orientation | class | "They are admissible in corresponding subordinates only in contexts of question-orientation." | 981 | L.49060–49061. Starred: "∗I recall how on earth you saved her." (L.49056). |
| THE_HELL_WH | host restriction (fused relatives) | N | item | "Fused relatives do not admit these expressions: ∗Whoever the hell said that was wrong." | 989 | L.49433. Exhaustive conditional is Y: "whatever the hell that means" (L.49431). |
| THE_HELL_WH | radical ellipsis (wh-phrase alone) | N except in stated frames | class | "Emotive modifiers such as on earth, the hell, ever are not permitted unless followed by a stranded preposition, else, or (in the case of why) not" | 1541 | L.76888–76889. "but not ∗Why ever?" (L.76890). This would exclude "What the hell?" as a reduced interrogative; I didn't check that against attestation. |
| THE_HELL_WH | clitic host | Y | item | "What the hell’s she doing?" | 1615 | L.80517. Class statement at L.80538–80539: "a monosyllabic interrogative word, alone or followed by one of the emotive modifiers the hell, on earth, ever, etc." |
| EXACTLY_WH | position before or after the wh-head | Y (both) | item | "The adverbs exactly and precisely may follow the head, as in [46iiib], or precede: Just exactly who do you think you are?" | 916 | L.45914–45915. Contrasts with the emotive modifiers' post-head-only position. |
| EXACTLY_WH | in situ | Y | item | "And so you want what, exactly?" | 1087 | L.54338–54339 (wraps). Directly contrasted with "∗And so you want what on earth?" |
| YES / NO | P01 STANDALONE | Y | item | "They may stand alone, or combine with a clause that expresses the answer more" | 847 | L.42495. |
| YES / NO | P03 INTEGRATED (polarity adjunct) | Y (candidate) | item | "the yes and no can be regarded as a special type of adjunct, a polarity adjunct, which agrees in polarity with the clause" | 848 | L.42536–42538. CGEL doesn't call them interjections. |
| YES / NO | restriction to particular hosts (polarity concord) | N for mismatched hosts | item | "Yes it isn’t and ∗No it is are thus ungrammatical as single clauses." | 848 | L.42536. The first ∗ is detached on L.42535. |
| YES / NO | P12S PROSODY_SEPARATE | Y | item | "The adjunct can also be placed at the end of the clause, with prosodic detachment: It is, yes and It isn’t, no." | 848 | L.42539–42540. Also "?Yes I will." (L.42561), a ?-marked use of yes to refuse a negative directive. |
| CLASS:supplements | P12S | Y | class | "Supplements are detached prosodically from the" | 66 | L.3880. The sentence crosses to p. 67. |
| CLASS:supplements (stated for PP/AdvP supplements) | P11E (negation) | N | class | "The supplements differ from the most central modifiers in that they do not fall within the scope of negatives in the anchor" | 1360 | L.68002–68003. Meaning tied to supplement function. Scope is uncertain because it is stated under (h) PPs and AdvPs. |

Excluded uses (not these bearers):
- damn: *give a damn* (pp. 823, 838, 978), *damnedest* (p. 416), *a damn sight better* (p. 327 n. 1, an NP "specialised to the modifying functions", L.16792), "damned out of existence" (p. 1584 n. 14, authorial prose).
- hell: *Get the hell out of here* (p. 853, L.42742, a non-wh host) and *Like hell you will!* (p. 924, L.46288–46289, "an expletive + personal pronoun subject + auxiliary").
- heavens on p. 343 is the plural-only noun.
- bastard on p. 1246 (L.62232) is a predicative noun licensing a hollow infinitival.
- "the lucky bastard’s just won a million" (p. 1412, L.70512) is an epithet inside the clause that refers, not BASTARD_SUPP.

## 2. Form properties CGEL gives that hold of two or more expressive uses

None of them separates the expressive uses from every control and interjection.

- **Attributive-only.** Holds of DAMN_PRENOM (starred example), BLOODY_PRENOM and FUCKING_PRENOM (class). MAIN_PRENOM is in the same p. 553 list, so this fails against a control. PROBABLE_PRENOM is U. Interjections never occur in integrated constructions, so the property doesn't apply to them.
- **No modification.** Holds of BLOODY_PRENOM, FUCKING_PRENOM and DAMN_PRENOM (class, unhedged). MAIN_PRENOM also lacks it (hedged "normally"), and modal attributives "mostly" do. The interjection class also takes no dependents, except DAMN_NP. The bastard uses do take modifiers (*you stupid bastard*, vocative; *the lucky bastard*).
- **No pro-form *one*.** Holds of the expletive attributives. MAIN passes ("the main ones"), so this separates expressives from MAIN. But *utter*, a non-expressive degree attributive, fails it too (∗an utter one).
- **No ·ly adverb.** Holds of [15iii] bleeding, bloody, damn(ed), fucking, which ties BLOODY_PRENOM/BLOODY_INTENS and DAMN_PRENOM/DAMN_DEGREE together as same-form adjective–adverb pairs (p. 568). VERY_INTENS also has no ·ly form, and the [15v] items (fast, hard, late, ...) are listed without ·ly counterparts too. QUICKLY has one. CGEL says nothing about interjections here.
- **Not a modifier of verbs (–v).** Stated for DAMN_DEGREE only; BLOODY_INTENS is U. VERY_INTENS has the same property, so it doesn't discriminate.
- **Supplement function with prosodic detachment.** Holds of BASTARD_SUPP (the separate intonational unit is stated for the prenuclear position only), DAMN_REACT (supplement), and YOU_BASTARD (never in a complement position). It is equally stated for the interjection class, YES/NO ("prosodic detachment"), vocatives, and non-expressive PP and AdvP supplements (p. 1360). It is a property of the supplement function.
- **Restriction to clause edges.** Fails: CGEL gives medial BASTARD_SUPP ("Max, the bastard, has ...") and medial ALAS.
- **Position after a wh-word, initial only, no in-situ.** Holds of only one expressive bearer (THE_HELL_WH). It is still the one form property where CGEL gives an explicit expressive/control split: EXACTLY_WH may precede or follow the head and may occur in situ (p. 916; p. 1087). The class also includes *ever* and *on earth*, which aren't expletives, so the property belongs to emotive modifiers rather than to taboo words.
- **Insertion inside words or phrases.** CGEL has nothing on it (section 4).

## 3. Warnings against using these properties as diagnostics

- **n. 18, p. 585.** CGEL refuses a lexical category 'intensifier': "the number of –v items is very small in comparison with the total number of items that can function as degree modifier".
- **n. 10, p. 553.** Attributive-only means "normally": "It excludes nonce-uses, as when one says, in jocular vein, His ignorance could only be described as utter." (L.28117–28118). The predicative N for DAMN_PRENOM rests on "no established non-attributive use".
- **p. 555, heterogeneity.** "Attributive-only adjectives are too numerous and semantically heterogeneous to permit a simple and exhaustive classification." (L.28186–28187). On the pro-form test they "give mixed results" (L.28182).
- **p. 37, meaning.** The non-propositional meaning of bloody is grouped with *but* and *even*: "We will handle the non-propositional meaning conveyed by items such as but, even, and bloody in these examples in terms of the concept of conventional implicature." (L.2469–2470). Non-propositional meaning is the property CGEL ties to form most often (p. 558 attributive-only; p. 916 position; p. 1361 non-combination; p. 1413 non-referential supplement). Even so, it doesn't separate expressives from connectives or focus words.
- **p. 564, residue category.** "With fairly small- scale exceptions (including interjections), all other words are assigned to the adverb category." (L.28623–28625). CGEL treats a category defined by residue as incoherent.
- **p. 1361, reanalysis.** The interjection class's "no integrated combination" has a stated exception (n. 70, DAMN_NP). Damn, blast, bugger and fuck are "primarily verbs", so the category is assigned per use.
- **p. 916, open membership.** The class is open-ended: heck, blazes, deuce, dickens, fuck, etc.
- **Homonymy.** Very in the attributive-only list is the adjective, not VERY_INTENS (p. 568).
- **Hedges.** "Do not normally" (MAIN), "mostly" (modal attributives), "hardly compatible" (*which*) and "tend to" (·ing attributives) are not "never". Under the brief's rule they shouldn't count as N.
- **Supplement properties.** Prosodic detachment and staying outside the scope of negation are properties of supplements in general (p. 66; p. 1360). They hold for *probably*, *frankly* and *in my opinion* as much as for the expressives.

## 4. Searches, negatives, and what I didn't reach

Search strings (regex, on cgel2002-paged.txt):
- `\b(damn|bloody|fucking|bastard|bugger|blasted|bleeding|frigging|goddam)` (-i)
- `[Ii]nterjection`
- `\b(ouch|wow|gee|gosh|tut|oops|ugh|alas|aha|hey|heavens|mm-hm|huh)\b` (-i)
- `the hell|on earth|the devil|in God|the heck|the fuck|in heaven|in the world`
- `earth`
- `[Ee]pithet`
- `tmesis|infix|abso-|expletive insertion|[Ee]xpletive`
- `insert(ed|ion)? (in|into|inside|within)|within (a|the) word|word-internal|inside (a|the) word|fan-|absobloody|kanga` (-i)
- `\b[Yy]es and no\b|answers? yes|...`
- a prosodic-detachment pattern (`set off intonationally|prosodically detached|separate intonation unit`, etc.)

Evidenced negatives:
- **Tmesis or infixation.** No CGEL statement on expletive insertion inside words; none of the tmesis/infix/insertion strings matched it. BLOODY_INFIX has no CGEL row.
- **Interjection forms.** No hits for gee, tut, aha, huh or mm-hm. Oops, ouch, ugh, wow and sh appear only in the p. 1361 list and the index; gosh only in the p. 22 list.
- **Index pages for *on earth*.** The index gives pp. 1259 and 1261, but those pages (PDF 1279–1281, L.62843–62990) contain no "earth" string. Possibly OCR loss; unread.
- **Bearers not searched:** BANG, OKAY, BYE, THANKS, SORRY, HELLO, HOWAREYOU, LAH, HABA, COFFEE, BLACK, STOP. QUICKLY was covered only through the ·ly comparison statement.

Sections not reached:
- AdjP modification (Ch. 6 §3.2, pp. 547–550)
- the exclamatives section of Ch. 10 beyond the imprecative retort
- the *give a damn* passages (pp. 823, 838, 978; excluded use)
- p. 983, L.49144 (*know* / *not know* with *on earth*), seen only in the grep line
- a footnote at L.53571 (around p. 1073) on *what ever*, unchecked

Files used:
- /private/tmp/claude-502/-Users-brettreynolds-projects-LLM-CLI-projects-papers-queue-english-interjections/5a0b28ba-2821-445d-9ca6-f1e7abe03419/scratchpad/sources/cgel2002-paged.txt
- /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/items-v4.csv
- /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/properties-v4.csv