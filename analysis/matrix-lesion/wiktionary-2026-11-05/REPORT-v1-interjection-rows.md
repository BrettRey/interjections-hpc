# Wiktionary extraction v1: interjection rows (from the template-stripped sense text; see the responsibility notices)

Saved verbatim by the parent session (Claude Opus 5.5) from the subagent's SubagentHandback report. Model output, not a source; every quotation is checked by the parent against the page-marked source text before use.

---

## Read first: the extraction lost material, so much of the silence below is an artifact

1. **Templates were stripped from wiktionary-senses.txt.** Every IPA line is a bare `*`. Every EXAMPLE line is empty. Etymon forms are blank ("From , enm, from , ang"). Several definitions survive only as ".": W:sh:Interjection:1 @412, W:mm-hm:Interjection:1 @1095, every okay sense including W:okay:Interjection:1 @1305, W:yes:Verb:2 @1387 ("To say ."), and W:no:Verb:1 @1595. As a result, P13 is readable only where Pronunciation prose survived (ugh @417, lah @2628). HISTORICAL_SOURCE is readable only where the etymon was plain text.
2. **Block ids are not unique.** W:ah:Interjection:1 occurs at lines 15, 111 and 130. W:ah:Pronunciation:0 occurs at 6, 52 and 123. W:gee:Interjection:1 occurs at 577 (the bearer) and 621 (the horse command). The tut, bye and gee Noun/Verb ids also repeat under different etymologies. Every locator below is therefore given as block id @ line number.
3. **HABA has no blocks.** A case-insensitive grep for "haba" over *.txt, *.json and *.log matched nothing in wiktionary-senses.txt. It matched only raw/haba.json, raw/hello.json, raw/how_are_you.json and fetch-log.json:265-267. So the page was fetched but produced no blocks. Under the brief I didn't read those files.

All quotations were grep-checked against the file. They are delimited by « and », and everything between the guillemets is character-exact, including curly ’ “ ”, the literal `&mdash;` and `<u>…</u>`.

## 1. Table

item_id | property | value | scope | «quotation» | block id @line | note
---|---|---|---|---|---|---
AH | P08 | Y | item | «An expression of relief, relaxation, comfort, confusion, understanding, wonder, awe, etc. according to uttered inflection.» | W:ah:Interjection:1 @16 (Etymology1) | POS Interjection. Relief, comfort, wonder and awe are affective.
AH | NEW:INTONATION_SPECIFIED | Y | item | «according to uttered inflection.» | W:ah:Interjection:1 @16 | The meaning varies with intonation; no fixed contour is given.
AH | P02 | Y | page | «Earliest recorded use is circa 1175 in the Ormulum: A, Maȝȝstre! icc wat tatt tu full wiss Arrt Godess Sune» | W:ah:Etymology1:0 @3 | Middle English attestation: A stands beside a vocative and a complete clause. It's admissible for the modern use only if the parent accepts a Middle English stage; otherwise drop it.
AH | NEW:DELOCUTIVE_NOUN | Y | page | «An instance of the interjection ah.» | W:ah:Noun:1 @32 | Separate Noun sense, {{en-noun}} @29. Its example "oohs and ahs at the fireworks" shows a plural and a determiner, but under conversion, so P06 is U in the primary record.
AH | NEW:DELOCUTIVE_VERB | Y | page | «To give a cry of "ah".» | W:ah:Verb:1 @39 | {{en-verb}} @36. Its inflection is derivational, so it isn't P05 evidence.
HEY | NEW:CONATIVE | Y | item | «An exclamation to get attention.» | W:hey:Interjection:1 @148 | POS Interjection. Register label informal ({{tlb|en|informal}} @145). There's no evaluative content, so no P08.
HEY | NEW:DELOCUTIVE_VERB | Y | page | «To greet with a "hey"» | W:hey:Verb:1 @180 | Built on the greeting sense (Interjection:4), not the attention sense.
OH | P08 | Y | item | «Expression of surprise.» | W:oh:Interjection:1 @224 | Applies only if the surprise sense counts as change of state. The primary match, Interjection:3, states cognitive content only.
OH | NEW:DELOCUTIVE_NOUN | Y | page | «An utterance of oh; a spoken expression of surprise, acknowledgement, etc.» | W:oh:Noun:1 @273 | Conversion, so P06 is U.
OH | NEW:DELOCUTIVE_VERB | Y | page | «(intransitive) To utter the interjection oh; to express surprise, etc.» | W:oh:Verb:1 @280 | Label intransitive.
OOPS | NEW:HISTORICAL_SOURCE | Y | page | «A shortening of whoops-a-daisy, whoopsie-daisy, or oops-a-daisy, which in turn is a mispronunciation of ups-a-daisy or upsy-daisy.» | W:oops:Etymology:0 @311 | Source: whoops-a-daisy (shortening). The same block also gives "Related to or a variation of whoops".
OOPS | NEW:ETYM_NATURAL_OR_IMITATIVE | Y | page | «A presumably 'natural' exclamation, attested in writing since 1921.» | W:oops:Etymology:0 @311 | This sits alongside the shortening account in the same block.
OUCH | P08 | Y | item | «An expression of one's own physical pain.» | W:ouch:Interjection:1 @365 | Pain is read as an affective state. The parent may class physical pain as sensory rather than affective.
OUCH | NEW:DELOCUTIVE_VERB | Y | page | «To exclaim "ouch!" in discomfort or pain.» | W:ouch:Verb:1 @396 | Label intransitive.
UGH | P08 | Y | item | «Used to express repugnance, disgust, or annoyance.» | W:ugh:Interjection:1 @425 | POS Interjection.
UGH | P13 | Y | page | «Any low-back vowel followed by a fricative articulated between the velum and the throat.» | W:ugh:Pronunciation:0 @417 | A fricative between velar and pharyngeal is outside general English word phonology. No speech community is stated. The block's IPA lines are stripped. The next line, «Note: may be nasalized.» @418, describes allophonic nasalization, which isn't P13.
WOW | P08 | Y | item | «An expression of amazement, awe, or admiration.» | W:wow:Interjection:2 @456 | Interjection:1 @451 (excitement, surprise, astonishment, pleasure) also matches.
WOW | NEW:ETYM_NATURAL_OR_IMITATIVE | Y | page | «Attested since the 16th century; borrowed from ; ultimately a natural exclamation.» | W:wow:Etymology1:0 @438 | The source of the borrowing is stripped.
WOW | NEW:DELOCUTIVE_NOUN | Y | page | «An utterance of "wow".» | W:wow:Noun:2 @490 | Label informal.
ALAS | P08 | Y | item | «Used to express sorrow, regret, compassion, grief, resignation, or disappointment.» | W:alas:Interjection:1 @520 | No "dated" label survives (the headword @517 is a bare {{en-intj}}).
ALAS | NEW:HISTORICAL_SOURCE | Y | page | «from fro + fro» | W:alas:Etymology1:0 @506 | The forms are stripped. Language code fro is Old French, so the source is a two-element Old French compound whose forms can't be read.
AHA | NEW:HISTORICAL_SOURCE | Y | page | «Equivalent to ah + ha.» | W:aha:Etymology:0 @548 | A compound of two interjections. The Middle English form is stripped.
GEE | P08 | Y | item | «(somewhat, dated) A general exclamation of surprise or frustration.» | W:gee:Interjection:1 @578 (Etymology1; not @621) | Labels somewhat, dated.
GEE | NEW:HISTORICAL_SOURCE | Y | page | «A shortening of Jesus, perhaps as in the oath by Jesus.» | W:gee:Etymology1:0 @568 | Source: Jesus (a shortened oath form).
GEE | NEW:IRONIC_USE | Y | page | «It is often used for ironic or sarcastic effect, with the speaker putting on an air of youthful innocence.» | W:gee:Usage notes:0 @586 | The same note's register statement is «Gee is generally considered somewhat dated or juvenile.» By file order it falls under Etymology1.
TUTTUT | P08 | Y | item | «An expression of annoyance or impatience.» | W:tut-tut:Interjection:1 @698 | POS Interjection.
TUTTUT | P08 | Y | item | «Tut tut; an expression of disapproval.» | W:tut:Interjection:1 @719 | Disapproval is evaluative.
TUTTUT | P10A | Y | item | «Tut tut; an expression of disapproval.» | W:tut:Interjection:1 @719 | Pattern: lexicalized reduplication (tut is glossed by its doubled form). Nothing bears on P10S.
TUTTUT | NEW:ETYM_NATURAL_OR_IMITATIVE | Y | page | «Imitative.» | W:tut:Etymology1:0 @707 | Not P09, since nothing says the use depicts.
TUTTUT | NEW:DELOCUTIVE_VERB | Y | page | «To express such a sound, especially as a mild reproof» | W:tut-tut:Verb:1 @704 | {{en-verb|++}} @701 doubles the final consonant, a derivational fact and not P05. Also «To make a tut tut sound of disapproval.» at W:tut:Verb:1 @728. "such a sound" treats the interjection as a sound.
HUH | NEW:INTONATION_SPECIFIED | Y | item | «(informal, with rising pitch) Used to indicate that one did not hear what was said.» | W:huh:Interjection:5 @1130 | A fixed rising contour; Interjection:1 @1113 is also "(with rising pitch)". The page separates huh's senses by rising versus falling pitch.
BYE | NEW:HISTORICAL_SOURCE | Y | page | «Shortened form of goodbye.» | W:bye:Etymology2:0 @1211 | A clipping of goodbye. By file order it governs the Interjection block @1213.
OKAY | NEW:HISTORICAL_SOURCE | Y | page | «A respelling of OK.» | W:okay:Etymology:0 @1262 | Source: OK.
YES | P02 | Y | item | «Are you busy? &mdash; Yes, I’m busy.» | W:yes:Particle:1 @1329 (quotation) | POS Particle. Yes stands beside the complete clause "I’m busy". P01 is not coded: whether a bare answer counts as standalone is Brett's call under P01's note on answer fragments.
YES | NEW:HISTORICAL_SOURCE | Y | page | «derived from the same root as yea» | W:yes:Etymology:0 @1309 | The etymon forms are stripped. Related historical note: «In Old and Middle English, yes was a more forceful affirmative than yea.» (W:yes:Usage notes:0 @1341).
YES | NEW:DELOCUTIVE_NOUN | Y | page | «An affirmative expression; an answer that shows agreement or acceptance.» | W:yes:Noun:1 @1364 | {{en-noun|+|yesses}} @1361 gives the plural yesses. It's a conversion, so P06 is U.
YES | NEW:DELOCUTIVE_VERB | Y | page | «We yessed simultaneously.» | W:yes:Verb:2 @1390 | The gloss @1387 is stripped ("To say ."). {{en-verb|~es,~ses}} @1378. Labels colloquial, intransitive. The inflection is derivational, not P05.
NO | NEW:HISTORICAL_SOURCE | Y | page | «from gem-pro + gem-pro, equivalent to .» | W:no:Etymology2:0 @1484 | The forms are stripped; it's a two-element Proto-Germanic compound. It governs the Particle senses by file order only.
NO | NEW:DELOCUTIVE_NOUN | Y | page | «A negating expression; an answer that shows disagreement, denial, refusal, or disapproval.» | W:no:Noun:1 @1584 | {{en-noun|es|s}} @1581. Conversion, so P06 is U.
NO | NEW:DELOCUTIVE_VERB | Y | page | «(intransitive, colloquial) To say .» | W:no:Verb:1 @1595 | The verb's object is stripped. {{en-verb|~es}} @1592.
THANKS | P08 | Y | item | «Used to express appreciation or gratitude.» | W:thanks:Interjection:1 @1644 | Gratitude is read as affective; the parent should check this.
THANKS | NEW:HISTORICAL_SOURCE | Y | page | «nominative plural of gem-pro, from . More at thank.» | W:thanks:Etymology:0 @1623 | Source: a plural related to thank; the forms are stripped.
THANKS | NEW:FROZEN_PLURAL_SHAPE | Y | page | «nominative plural of gem-pro, from . More at thank.» | W:thanks:Etymology:0 @1623 | The noun headword {{en-noun|p|sg=thank<l:obsolete>}} @1651 belongs to the noun use, not the interjection.
SORRY | P08 | Y | item | «Expresses regret, remorse, or sorrow.» | W:sorry:Interjection:1 @1725 | POS Interjection.
SORRY | NEW:HISTORICAL_SOURCE | Y | page | «The interjection is generally understood as a clipping of I'm sorry.» | W:sorry:Usage notes:0 @1755 | Source: I'm sorry. The Etymology adds «Unrelated to sorrow despite the similarity in form and meaning.» @1676; its etymon forms are stripped.
SORRY | NEW:IRONIC_USE | Y | page | «A typically sarcastic use slows down the rhythm and stresses the final syllable, as . This is often spelled as sorree or emphatically as something like sor-REE!! in print.» | W:sorry:Usage notes:0 @1756 | The IPA is stripped (" as ."). This isn't P13.
SORRY | NEW:STRESS_SHIFT | Y | page | (same quotation as the row above) | W:sorry:Usage notes:0 @1756 | Final stress marks the sarcastic use.
SORRY | NEW:DELOCUTIVE_NOUN | Y | page | «The act of saying sorry; an apology.» | W:sorry:Noun:1 @1762 | {{en-noun|+|s}} @1759. Conversion, so P06 is U.
HELLO | P02 | Y | item | «Hello. This is Marsha.» | W:hello:Interjection:2 @1831 (quotation) | Telephone-greeting sense. Hello stands beside a complete clause. The full stop raises a P01 question, which I leave to Brett.
HELLO | NEW:HISTORICAL_SOURCE | Y | page | «From holla, hollo (attested 1588).» | W:hello:Etymology:0 @1774 | Also «Thus, equivalent to a compound of hey and lo.» @1775; the block calls hello a variant of hallo.
HELLO | NEW:STRESS_SHIFT | Y | page | «word-initial stress is also heard in certain contexts, such as some uses of hello there, and even in isolation.» | W:hello:Usage notes:0 @1851 | "hello there" could be a P04 dependent; I haven't coded it. Register note: «The greeting hello is among the most universal and neutral in use.» @1850.
HELLO | NEW:DELOCUTIVE_NOUN | Y | page | «"Hello!" or an equivalent greeting.» | W:hello:Noun:1 @1857 | {{en-noun|s,es}} @1854. Conversion, so P06 is U.
HELLO | NEW:DELOCUTIVE_VERB | Y | page | «To greet (someone) with "hello".» | W:hello:Verb:1 @1866 | {{en-verb|+,~es}} @1863. Label transitive.
HEAVENS | P08 | Y | item | «(informal) An expression of surprise, contempt, outrage, disgust, boredom, or frustration.» | W:heavens:Interjection:1 @1991 | POS Interjection. Label informal.
HEAVENS | P02 | Y | item | «“Heavens!” exclaimed Nina, “the blue-stocking and the fogy!—and yours are pale blue, Eileen!» | W:heavens:Interjection:1 @1993 (quotation) | Weaker than the YES and HELLO rows: the unit right after Heavens! is a verbless NP, and the complete clause comes only after the dash. The parent may prefer U.
HEAVENS | NEW:FROZEN_PLURAL_SHAPE | Y | page | «The plural form "heavens" or "the heavens" has been typical in reference to the impersonal sky since the 17th century.» | W:heavens:Usage notes:0 @1984 | This is about the Noun senses ({{en-noun|p}} @1962). The page has no Etymology block linking the interjection to the plural, so the Y rests on the spelling being the same.
LAH | P01 | N | item | «clause-final [[w:Discourse marker|discourse particle]]» | W:lah:Particle:0 @2632 (headword label) | A position label of the "attributive" kind. Variety labels Manglish, Singlish. "Clause-final" isn't exceptionless: Particle:16 @2742 puts lah inside the clause («“Who lah that Panjali?» @2745). Every placement given is still within a host.
LAH | P02 | Y | item | «Don’t know lah this is very hard to say.» | W:lah:Particle:1 @2639 (quotation) | Gloss: «Placed at the end of a sentence to accentuate the mood or attitude of the speaker.» @2635. Whether a clause-final particle "enters the construction" is an analytic question for the parent.
LAH | P08 | Y | item | «(less common) Used to convey a slight sense of dissatisfaction or irritation.» | W:lah:Particle:14 @2732 | Particle:1's "mood or attitude of the speaker" @2635 points the same way.
LAH | P10A | Y | item | «He teach them how to cook lah, learn computer lah» | W:lah:Particle:15 @2738 (quotation) | Pattern: distributed recurrence (in the enumeration sense). Nothing bears on P10S.
LAH | P13 | Y | page | «The different senses of this word are distinguished by lexical tone.» | W:lah:Pronunciation:0 @2628 (Etymology2) | The feature is suprasegmental, not segmental. Brett needs to decide whether lexical tone counts as "sounds" for the Singapore/Malaysian community. The IPA is stripped. The identical line @54 is on the ah page under Etymology3 (Singlish ah), not the AH bearer.
LAH | NEW:LEXICAL_TONE | Y | page | (same quotation as the row above) | W:lah:Pronunciation:0 @2628 | 
LAH | NEW:INTONATION_SPECIFIED | Y | item | «Pitch contour: <u>falling</u>» | W:lah:Particle:6 @2680 | Every Particle sense states a contour (low-mid, mid-falling, falling, mid-rising, mid, high-mid).
LAH | NEW:HOST_STRESS_CONDITIONED | Y | page | «lah is more likely to occur after clauses ending in a lexically stressed syllable (e.g., No need, lah!) than after clauses ending in an unstressed syllable» | W:lah:Usage notes:0 @2753 | Relevant to P12I (rhythmic grouping with the host), but the note doesn't state intonational integration, so P12I isn't coded.
LAH | NEW:HISTORICAL_SOURCE | Y | page | «Bazaar Malay, for its use as a particle of emphasis» | W:lah:Etymology2:0 @2622 | Lim (2007) lists several sources: Bazaar Malay, Cantonese 啦 laa ({{zh-l|啦|tr=laa}} @2620, @2624), and a third whose form is stripped.
HOWAREYOU | NEW:NONLITERAL | Y | item | «(idiomatic) An informal greeting, not requiring a literal response. In form a question, and thus followed by a question mark.» | W:how are you:Phrase:1 @2591 | POS Phrase ({{en-head|phr|head=?}} @2588). Labels idiomatic, informal. This isn't a P07D statement either way.
HOWAREYOU | NEW:CLAUSAL_FORM | Y | item | (same quotation as the row above) | W:how are you:Phrase:1 @2591 | "In form a question" states interrogative clause form.

## 2. Matches per bearer

There are three kinds of negative: no blocks at all, a heading whose gloss was stripped, and readable senses of which none matches.

- **AH**: W:ah:Interjection:1 @16 (Etymology1). The other two ids with this name (@111, @130) are Singlish ah and the "Yuck" sense; neither is the bearer.
- **HEY**: W:hey:Interjection:1 @148.
- **OH**: W:oh:Interjection:3 @232 (understanding, recognition, realization), with Interjection:1 @224 (surprise) as a secondary match.
- **OOPS**: W:oops:Interjection:1 @328. Interjection:2 @334 ("mild surprise or shock") is possible. The noun ("A minor mistake…", {{en-noun|+|*}}) and verb ("To make a mistake") are semantic conversions, not delocutive ones.
- **OUCH**: W:ouch:Interjection:1 @365.
- **SH**: heading present, gloss stripped. W:sh:Interjection:1 @412 is ".". The page has no Pronunciation or Etymology block.
- **UGH**: W:ugh:Interjection:1 @425.
- **WOW**: W:wow:Interjection:2 @456, plus Interjection:1 @451.
- **ALAS**: W:alas:Interjection:1 @520.
- **AHA**: W:aha:Interjection:1 @560. Interjection:2 @564 (surprise, exaltation, contempt) is a different sense.
- **GEE**: W:gee:Interjection:1 @578. The @621 block is the horse command and isn't the bearer.
- **TUTTUT**: W:tut-tut:Interjection:1 @698 and W:tut:Interjection:1 @719. W:tut:Interjection:2 @722 ("Hush; be silent.") isn't the bearer.
- **MMHM**: heading present, gloss stripped. W:mm-hm:Interjection:1 @1095 is ".". There's no Pronunciation or Etymology block.
- **HUH**: W:huh:Interjection:5 @1130, plus Interjection:1 @1113.
- **BYE**: W:bye:Interjection:1 @1217 ("(colloquial) Goodbye.", a synonym gloss with no properties). The "bye" in the Interjection:2 @1220 quotation is the AAVE dismissal sense, not the bearer.
- **OKAY**: heading present, gloss stripped. W:okay:Interjection:1 @1305 is ".", and so is every other okay sense.
- **YES**: W:yes:Particle:1 @1324, and Particle:2 @1332 for the affirmative answer to a negative question. The Usage notes @1342 illustrate that answer: «the questions "You don’t want it, do you?" and "Don’t you want it?" are answered by "yes" if the respondent does want the item». It's the bare-answer case, so I left P01 for Brett.
- **NO**: W:no:Particle:1 @1536, and Particle:5 @1559 (agreement with a negative question).
- **THANKS**: W:thanks:Interjection:1 @1644.
- **SORRY**: W:sorry:Interjection:1 @1725 and Interjection:2 @1732.
- **HELLO**: W:hello:Interjection:1 @1822 and Interjection:2 @1828.
- **HEAVENS**: W:heavens:Interjection:1 @1991.
- **LAH**: W:lah:Particle:1–17 @2634–2751 (Etymology2), with the headword at @2632.
- **HOWAREYOU**: W:how are you:Phrase:1 @2591. Phrase:2 @2595 (Irish derision) isn't the bearer.
- **HABA**: the page has no blocks in wiktionary-senses.txt (see item 3 at the top).

## 3. New properties

- **NEW:HISTORICAL_SOURCE**: the Etymology or Usage notes name what the use derives from; the source form goes in the note.
- **NEW:ETYM_NATURAL_OR_IMITATIVE**: the Etymology calls the form imitative or a natural exclamation rather than deriving it from a source word.
- **NEW:DELOCUTIVE_NOUN**: the page has a same-form noun sense meaning an utterance or instance of the expression. Plurals and determiners there are conversion evidence, so P06 is U in the primary record.
- **NEW:DELOCUTIVE_VERB**: the page has a same-form verb sense meaning to say the expression. Its inflections are derivational, not P05 evidence.
- **NEW:INTONATION_SPECIFIED**: the sense's gloss or label states a pitch contour, or says the meaning varies with intonation.
- **NEW:LEXICAL_TONE**: the Pronunciation says the senses are distinguished by lexical tone.
- **NEW:CONATIVE**: the gloss says the use is aimed at getting the addressee's attention or action.
- **NEW:IRONIC_USE**: the source says the use occurs ironically or sarcastically.
- **NEW:STRESS_SHIFT**: the source ties a stress placement to a sense or use.
- **NEW:FROZEN_PLURAL_SHAPE**: the source says the form is, or comes from, a plural.
- **NEW:HOST_STRESS_CONDITIONED**: the source says whether the use occurs depends on the host's stress pattern.
- **NEW:NONLITERAL**: the gloss says the use doesn't call for a literal response or interpretation.
- **NEW:CLAUSAL_FORM**: the gloss says the expression has clause form (for example, interrogative).

## 4. What I couldn't match or read

- **HABA**: no blocks (see the top).
- **SH, MMHM, OKAY**: the interjection glosses are stripped to ".".
- **P13 can't be read** for any bearer except UGH and LAH, because every IPA line is a bare `*`. That includes TUTTUT's click (tut Pronunciation @709–713), SH's vowelless form, MMHM, and HUH. Silence on P13 for these is an extraction artifact, not evidence.
- **Etymon forms are stripped**, so HISTORICAL_SOURCE can't be read for AH (@3: only the codes enm, ang and gmw-pro survive), HEY (@142: "Probably a expression, as may be inferred from its presence with similar meaning in many other unrelated languages", where the adjective before "expression" is gone), OH (empty block @218), OUCH (@354, which also cuts off mid-sentence) and HUH (@1098: "Attested from . Compare ."). WOW's borrowing source and the forms in ALAS, NO, YES, THANKS, SORRY and AHA are also missing; their rows record only what survives.
- **Potts's six properties (searched negative).** I read every block for my 24 pages: lines 2–199, 200–566, 567–796, 1091–1306, 1307–1620, 1621–1871, 1955–2000 and 2580–2754. No gloss or note states independence, nondisplaceability, perspective dependence, descriptive ineffability or immediacy. Repeatability appears only as the P10A rows (TUTTUT, LAH), and nothing supports P10S. One near miss: OUCH's "one's own physical pain" (@365, against Interjection:2 "in sympathy at another's pain" @369) concerns who has the pain, not Potts's perspective dependence, so I didn't code it.
- **Comparability doesn't apply to any matched sense.** The matched senses sit under {{en-intj}}, {{en-head|pcl}} or {{en-head|phr}}, none of which carries comparability. The comparability templates on these pages belong to other headwords: sorry {{en-adj|er}} @1694, okay {{en-adj|more,er}} @1289 (its senses are stripped), bye {{en-adj}} @1195, and no {{en-adv|-}} @1487 and @1610.
- **Near misses I didn't code:** "hello there" as a possible P04 dependent (@1851); the LAH usage note as possible P12I evidence (@2753); "not requiring a literal response" as possible P07D (@2591). NO's Particle senses sit under Etymology2 by file order only.