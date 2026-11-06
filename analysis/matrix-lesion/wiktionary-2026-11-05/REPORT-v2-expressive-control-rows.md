# Wiktionary extraction v2 supplement: expressive and control rows (from the template-expanded text)

Saved verbatim by the parent session (Claude Opus 5.5) from the subagent's SubagentHandback report. Model output, not a source; every quotation is checked by the parent against the page-marked source text before use.

---

W2 supplementary extraction: expressive and control bearers (21), from wiktionary-senses-v2.txt

There's no RESPONSIBILITY NOTICE. Three coding decisions are flagged at the top of section 3 for you to settle before merging: comparability now shows Wiktionary's template default, P01 is now coded from EXAMPLE lines, and the P13 N values rest on the community clause.

Source file: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/wiktionary-2026-11-05/wiktionary-senses-v2.txt
Line numbers (L) are from v2. Every quotation in the table was grep-checked against that file. Many citation headers carry invisible U+200E marks, so each quotation stays inside the example or quotation sentence. The file also has an invisible character after "+" in "exact + -ly" and "blood + -y" (a plain-"+" grep fails), so I quoted only up to the "+" in those cases.

1. TABLE
Fields are separated by " | ".

```
DAMN_REACT; DAMN_NP; DAMN_PRENOM; DAMN_DEGREE | P13 | N | page | "/ˈdæm/, [ˈdæm] ~ [ˈdam]" | W:damn:E1:Pronunciation:0 | L1088. Every variety line (RP, SSB, N England, US with and without /æ/ raising, Australia, NZ /ˈdɛm/) is ordinary English word phonology. N holds only if you accept a page-level block as giving the conventional forms in full. Nothing is specific to the interjection use.
DAMN_REACT; DAMN_NP; DAMN_PRENOM; DAMN_DEGREE | NEW:HISTORICAL_SOURCE | Y | page | "From Middle English dampnen, from Old French damner, from Latin damnāre (“to condemn, inflict loss upon”), from damnum (“loss”)." | W:damn:E1:Etymology:0 | L1085. The page has one etymology, and it governs every damn sense. No path to the expressive uses is stated.
DAMN_NP | P04 | Y | item | "That man stole my wallet. Damn him!" | W:damn:E1:Verb:5 | L1132. Constructed EXAMPLE line; object "him". This confirms the first pass's closest match ("To curse; put a curse upon."). Wiktionary files the use under Verb, which bears on the "category unresolved" rationale. Labels: slang, slightly vulgar.
DAMN_NP | P01 | Y | item | "That man stole my wallet. Damn him!" | W:damn:E1:Verb:5 | L1132. "Damn him!" is its own sentence in an editor-constructed example. This departs from the first pass, which declined P01 for a quotation (see section 3, flag 2).
DAMN_NP | P05 | Y | page (headword) | "damn (third-person singular simple present damns, present participle damning, simple past and past participle damned)" | W:damn:E1:Verb:0 | L1104. Verb headword, which covers all six Verb senses. Verb:5 itself shows no inflected form; the inflected examples are under Verb:1 and Verb:3 ("will be damned", "I'll be damned as a troublemaker"). Drop this row if headword scope doesn't count for this use.
DAMN_PRENOM | P03 | Y | item | "Shut the damn door!" | W:damn:E1:Adjective:1 | L1146. Prenominal, after a determiner.
DAMN_PRENOM | P03 | Y | item | "The whole damn building came down!" | W:damn:E1:Adjective:1 | L1149. Prenominal, after another modifier. Also 2005 Shadow the Hedgehog quotation "Where's that damn FOURTH Chaos Emerald" (L1151).
DAMN_DEGREE | P03 | Y | item | "That car was going damn fast!" | W:damn:E1:Adverb:1 | L1159. Modifier of an adverb. See section 2 for the other Adverb:1 lines.
BANG_DEPICT; BANG_NOUN | P13 | N | page | "/ˈbeɪ̯ŋ/, [ˈbeɪ̯ŋ], [ˈbɛ̃ŋ]" | W:bang:E0:Pronunciation:0 | L213 (US, Canada, /æ/ raising). The nasalized vowel is an allophone under raising. Other lines: /ˈbæŋ/, /ˈbaŋ/, /ˈbaŋɡ/ (without ng-coalescence), /ˈbæːŋ/. All ordinary. Pronunciation sits at E0, so it covers both etymologies.
BANG_DEPICT; BANG_NOUN | NEW:HISTORICAL_SOURCE | Y | page | "From Middle English *bangen, from Old English *bangian or borrowed from Old Norse banga (“to pound, hammer”)" | W:bang:E1:Etymology:0 | L221. Governs both Noun:1 and Interjection:1, which sit under E1. The source is a Germanic verb "to beat, pound". The block doesn't call the word imitative; compare ah's "of imitative origin" (L16).
BANG_NOUN | P06 | Y (plural) | item (headword) | "bang (plural bangs)" | W:bang:E1:Noun:0 | L228. Covers the E1 Noun senses. Replaces v1's empty "{{en-noun}}".
BANG_NOUN | P06 | Y (determiner) | item | "When he struck it with a hammer, there was a loud bang." | W:bang:E1:Noun:1 | L233.
BANG_NOUN | P04 | Y | item | "When he struck it with a hammer, there was a loud bang." | W:bang:E1:Noun:1 | L233. Modifier "loud".
BANG_DEPICT | P01 | Y | item | "He pointed his finger at her like a gun and said, “Bang!”" | W:bang:E1:Interjection:1 | L384. Constructed EXAMPLE line; the use is a whole quoted utterance. Same rule as DAMN_NP and YOU_BASTARD (flag 2).
BANG_DEPICT | P01 | Y | item | "Bang! Away he goes with a mighty bound. Leo has missed him. Bang! right under him again." | W:bang:E1:Interjection:1 | L385. Haggard, She, 1886–1887 (published 1887), as given. Bang! is its own sentence in narrative.
BANG_DEPICT | P10A | Y (adjacent repetition) | item | "Bang, bang, bang." | W:bang:E1:Interjection:1 | L388. Burgess, Time for a Tiger, 1956 (published 1972), p. 17. The line shows the repetition but not its effect, so P10S and P10M stay uncoded.
BANG_DEPICT | P10A | Y (distributed recurrence) | item | "Bang! Away he goes with a mighty bound. Leo has missed him. Bang! right under him again." | W:bang:E1:Interjection:1 | L385. Haggard as above; two tokens across one passage.
BASTARD_SUPP; YOU_BASTARD | P13 | N | page | "/ˈbɑːs.təd/" | W:bastard:E1:Pronunciation:0 | L403 (RP). Also Northumbria /ˈbæs.tæd/ and GA /ˈbæs.tɚd/. All ordinary.
BASTARD_SUPP; YOU_BASTARD | NEW:HISTORICAL_SOURCE | Y | page | "from Old English bastard (used as an epithet), from Anglo-Norman bastard, Old French bastart (“illegitimate child”)" | W:bastard:E1:Etymology:0 | L397. The v1 chain was stripped; this is it. It says the Old English word was already "used as an epithet". The Frankish *bāst line (v1 row) is the next paragraph, L398.
BASTARD_SUPP | P06 | Y (determiner) | item (sense) | "Some bastard stole my car while I was helping an injured person." | W:bastard:E1:Noun:3 | L424. Sense-level only. This is the argument (subject) use, not the supplementary epithet, and no Noun:3 line shows the supplement. Use it for nothing positional. Headword "bastard (countable and uncountable, plural bastards)" (L411) also gives the plural.
YOU_BASTARD | P01 | Y | item | "You sick bastard!" | W:bastard:E1:Noun:3 | L425. Constructed EXAMPLE line; the exclamatory NP is its own utterance. Flag 2: v1 declined P01 for the South Park "You bastards!".
YOU_BASTARD | P04 | Y | item | "You sick bastard!" | W:bastard:E1:Noun:3 | L425. Modifier "sick" inside the exclamatory NP.
BLOODY_PRENOM; BLOODY_INTENS | P13 | N | page | "/ˈblɜ.ɖiː/" | W:bloody:E0:Pronunciation:0 | L783 (India). The retroflex [ɖ] is ordinary for the labelled community. Main line /ˈblʌ.di/ (L782); Northumbria /ˈblɪ.diː/. Doesn't cover -bloody-, which is a separate page.
BLOODY_PRENOM; BLOODY_INTENS | NEW:HISTORICAL_SOURCE | Y | page | "From Middle English blody, blodi, from Old English blōdiġ, blōdeġ (“bloody”)" | W:bloody:E1:Etymology:0 | L791. The block goes on "equivalent to blood + -y" and "See Wikipedia for thoughts on sense evolution." So this is the lemma's source, and no path to the intensifier is stated.
BLOODY_PRENOM | P10A | Y (distributed recurrence) | item | "Try to keep those bloody women's bloody heads on their bloody shoulders" | W:bloody:E1:Adjective:3 | L817. Robert Jordan, Lord of Chaos, 1994, p. 519. Three prenominal tokens in one clause; the effect isn't shown.
BLOODY_PRENOM | P05 | Y | page (headword) | "bloody (comparative bloodier, superlative bloodiest)" | W:bloody:E1:Adjective:0 | L794. Headword-level only. The only inflected form in a sense is "bloodiest" under Adjective:2 (bloodshed), L808. Nothing ties an inflected form to Adjective:3. I'd drop this row if headword scope is ruled out for P05.
BLOODY_INTENS | P03 | Y | item | "Walk! Not bloody likely." | W:bloody:E1:Adverb:1 | L836. Shaw, Pygmalion, 1912 (date written), published 1916, Act III, p. 153. Modifier of an adjective. This confirms the position v1 couldn't.
BLOODY_INTENS | P03 | Y | item | "Dice are no bloody good" | W:bloody:E1:Adverb:1 | L837. Robert Jordan, Lord of Chaos, 1994, p. 109.
BLOODY_INTENS | NEW:COMPARABLE | Y | item (headword) | "bloody (comparative more bloody, superlative most bloody)" | W:bloody:E1:Adverb:0 | L831. Template default (flag 1): v1 showed a bare "{{en-adv}}", so no editor parameter asserts this.
FUCKING_PRENOM | P13 | N | page | "/ˈfʌkɪŋ/, [ˈfɐkɪŋ]" | W:fucking:E1:Pronunciation:0 | L1223. Also /ˈfʌkiŋ/, g-dropping /ˈfʌkɪn/, N England /ˈfʊkɪŋ/. All ordinary.
FUCKING_PRENOM | NEW:HISTORICAL_SOURCE | Y | page | "From fuck + -ing." | W:fucking:E1:Etymology:0 | L1219. The next line (L1220) is a module error message ("Etymology link to -ing is ambiguous…"), not content.
FUCKING_PRENOM | P03 | Y | item | "Give me the fucking key!" | W:fucking:E1:Adjective:1 | L1256. Attested prenominal instance; v1's P03 came from gloss wording.
FUCKING_PRENOM | P08 | Y | item | "Offensive, annoying or worthless." | W:fucking:E1:Adjective:2 | L1264. Full gloss; replaces v1's ", annoying or worthless.". Still holds only if Adjective:2 is matched.
FUCKING_PRENOM | P07D | Y | item | "Offensive, annoying or worthless." | W:fucking:E1:Adjective:2 | L1264. Conditional on the Adjective:2 match. Consistency flag: v1 coded P07D Y for DAMN_DEGREE and VERY_INTENS from paraphrase glosses ("Very; extremely."), and this is a paraphrase gloss too. Whether evaluative-only content counts as descriptive is your call. Not a use-description gloss.
FUCKING_PRENOM | P10A | Y (distributed recurrence) | item | "a fucking balloon with a fucking Weetabix crushed on top" | W:fucking:E1:Adjective:2 | L1269. 2024 August 28, Raven Smith, Vogue, quoting Liam Gallagher. Conditional on the Adjective:2 match.
THE_HELL_WH | P13 | N | page | "/ðəˈhɛl/" | W:the hell:E0:Pronunciation:0 | L3072. Single transcription.
THE_HELL_WH | NEW:HISTORICAL_SOURCE | Y | page (hell, neighbour) | "From Middle English hel, hell, helle, hælle, from Old English hel, hell, from Proto-West Germanic *hallju, from Proto-Germanic *haljō (“hell, netherworld”)" | W:hell:E1:Etymology:0 | L1481. The "the hell" page has no Etymology block. This is the hell page's E1, which governs hell Noun:4 (below). It's the base noun's source, not a source for the phrase.
THE_HELL_WH | NEW:POST_WH | Y | item | "What the hell was that?" | W:the hell:E0:Adverb:2 | L3087. Attested example; v1's Y came from the gloss. Also post-wh: "Whoever the hell is running the place now" (2009 February 19, Gareth Lewis, Southern Daily Echo; L3090).
THE_HELL_WH | P03 | Y | item | "What the hell was that?" | W:the hell:E0:Adverb:2 | L3087. Holds only if the post-wh position is read as modifier of the interrogative word (CGEL p. 1087, per items-v4). v1 left P03 uncoded ("a position, not a function"); your call.
THE_HELL_WH | NEW:USE_DESCRIPTION_GLOSS | Y | item (alternative match) | "Used as an intensifier in phrases grammatically requiring a noun." | W:hell:E1:Noun:4 | L1532. The stripped v1 gloss "Used as an…", now readable. Its EXAMPLE is "What the hell is wrong with you?!" (L1535). Use only if you adopt hell Noun:4 as a match. Not P08. See section 3 on the category disagreement.
VERY_INTENS | P13 | N | page | "/ˈvɛɾe/" | W:very:E1:Pronunciation:0 | L3245 (Scotland). The tap is ordinary there. Main line /ˈvɛɹi/ (L3239); also /ˈvɛəɹi/, /ˈveɹi/, Wales /ˈvɛɾi/.
VERY_INTENS | NEW:HISTORICAL_SOURCE | Y | page | "From Middle English verray, from Old French verai (“true”), from Early Medieval Latin vērāgus" | W:very:E1:Etymology:0 | L3235. Replaces v1's "derived from la". The source sense is "true".
VERY_INTENS | P10A | Y (adjacent repetition) | page | "Commonly intensified by reduplication, as in very, very important person." | W:very:E1:Usage notes:0 | L3274. Update to the v1 row: the stripped word is "reduplication".
VERY_INTENS | P10S | Y (adjacent repetition) | page | "Commonly intensified by reduplication, as in very, very important person." | W:very:E1:Usage notes:0 | L3274. Update to the v1 row.
VERY_INTENS | NEW:VERB_MODIFIER | N | page | "very and too never modify verbs (except in some dialects influenced by Chinese: see citations)" | W:very:E1:Usage notes:0 | L3275. Update to the v1 row: the stripped subject is "very". The dialect exception stands, so N holds for general varieties only.
VERY_INTENS | P03 | Y | item | "and was very clean" | W:very:E1:Adverb:1 | L3261. 1913, Marie Belloc Lowndes, The Lodger, ch. II. Modifier of a predicative adjective.
VERY_INTENS | P04 | Y | item | "She's so very similar to her mother." | W:very:E1:Adverb:1 | L3258. Holds only if "so" attaches to "very" and not to "very similar"; that's an analyst's call. Same pattern in "didn't turn out so very expensive" (L3260).
EXACTLY_WH | P13 | N | page | "/ɪɡˈzæk(t).li/" | W:exactly:E1:Pronunciation:0 | L1192.
EXACTLY_WH | NEW:HISTORICAL_SOURCE | Y | page | "From exact" | W:exactly:E1:Etymology:0 | L1189. The line reads "From exact + -ly." with an invisible character after "+", so I quoted only to "exact". Replaces v1's "From .".
EXACTLY_WH | P03 | Y | item (sense) | "He did it that way exactly to prove the point." | W:exactly:E1:Adverb:2 | L1208. Focus sense as a modifier, but not after a wh-word. See section 2 for the evidenced negative on POST_WH.
EXACTLY_WH | NEW:COMPARABLE | Y | item (headword) | "exactly (comparative more exactly, superlative most exactly)" | W:exactly:E1:Adverb:0 | L1196. Template default (flag 1): v1 showed bare "{{en-adv}}". Covers both Adverb senses.
MAIN_PRENOM | P13 | N | page | "/meɪn/" | W:main:E0:Pronunciation:0 | L2013.
MAIN_PRENOM | NEW:HISTORICAL_SOURCE | Y | page | "From Middle English mayn, main, maine, mæin, meyn, from main (noun) (see further at etymology 2)" | W:main:E1:Etymology:0 | L2020. Same block: "compare Old English mæġen (“strong, main, principal”)".
MAIN_PRENOM | NEW:ATTRIBUTIVE | Y | item | "The main office is actually one of the smaller rooms." | W:main:E1:Adjective:1 | L2028. Evidence is an example, not a label (v1's ATTRIBUTIVE row was label-based, for fucking).
MAIN_PRENOM | P03 | Y | item | "The main office is actually one of the smaller rooms." | W:main:E1:Adjective:1 | L2028.
PROBABLE_PRENOM | P13 | N | page | "/ˈpɹɒbəbl̩/" | W:probable:E1:Pronunciation:0 | L2653. The syllabic /l̩/ is an ordinary English syllabic lateral, not a syllabic fricative. GA /ˈpɹɑbəbl̩/.
PROBABLE_PRENOM | NEW:HISTORICAL_SOURCE | Y | page | "From Middle English probable, from Old French probable, from Latin probābilis (“that may be proved, credible”)" | W:probable:E1:Etymology:0 | L2650.
PROBABLE_PRENOM | NEW:ATTRIBUTIVE | Y | item | "The probable source of the failure was the mass of feathers in the intake manifold." | W:probable:E1:Adjective:1 | L2664.
PROBABLE_PRENOM | P03 | Y | item | "The probable source of the failure was the mass of feathers in the intake manifold." | W:probable:E1:Adjective:1 | L2664.
PROBABLE_PRENOM | NEW:PREDICATIVE | Y | item | "It's probable that it will rain tomorrow" | W:probable:E1:Adjective:1 | L2663. The content clause is extraposed (CGEL treats it as extraposed subject), so this is not P04.
PROBABLE_PRENOM | NEW:PREDICATIVE | Y | item | "success is looking probable" | W:probable:E1:Adjective:2 | L2669.
PROBABLE_PRENOM | P04 | Y | item | "the most probable reason is that it never had any quantity of funds worth embezzling" | W:probable:E1:Adjective:1 | L2665. 1959 October, Michael Robbins, Railway Magazine, p. 721. Degree modifier "most", attributive. Analytic, so not P05.
PROBABLE_PRENOM | NEW:COMPARABLE | Y | item (headword) | "probable (comparative more probable, superlative most probable)" | W:probable:E1:Adjective:0 | L2659. Template default (flag 1): v1 showed bare "{{en-adj}}".
COFFEE | P13 | N | page | "/ˈkɒfi/" | W:coffee:E1:Pronunciation:0 | L975 (RP). Also SSB /ˈkɔfɪj/, US /ˈkɔfi/, /ˈkɑfi/, NZ [ˈkɔ̟fi], Scotland /ˈkɔfe/. All ordinary.
COFFEE | NEW:HISTORICAL_SOURCE | Y | page | "Borrowed from Dutch koffie, from Italian caffè, from Ottoman Turkish" | W:coffee:E1:Etymology:0 | L972. The chain continues to Ottoman Turkish kahve and Arabic qahwa. I trimmed before the Arabic script for string safety.
COFFEE | P06 | Y (determiner) | item | "As I sip a coffee at Brasserie Balzar" | W:coffee:E1:Noun:2 | L1004. 2008 April 12, Agnes Poirier, The Guardian. Attested; upgrades v1's label-based P06.
COFFEE | P06 | Y (plural) | item (headword) | "coffee (countable and uncountable, plural coffees)" | W:coffee:E1:Noun:0 | L991.
COFFEE | P03 | Y | item | "He and his friends used to order coffee whenever they went out." | W:coffee:E1:Noun:1 | L995. Object position.
STOP | P13 | N | page | "/(ɪ)sʈɔp/" | W:stop:E0:Pronunciation:0 | L2830 (South Asia). The retroflex [ʈ] and optional prothetic vowel are ordinary for the labelled community. Other lines: /stɒp/, /stɔp/, /stɑp/.
STOP | NEW:HISTORICAL_SOURCE | Y | page | "From Middle English stoppen, stoppien, from Old English stoppian (“to stop, close”)" | W:stop:E1:Etymology:0 | L2834.
STOP | P04 | Y | item | "The sight of the armed men stopped him in his tracks." | W:stop:E1:Verb:3 | L2853. Attested object; upgrades v1's label-based row. Also "I need to stop the cheque I wrote him." (L2854).
BLACK | P13 | N | page | "/blæk/" | W:black:E1:Pronunciation:0 | L554. Also /blak/, NZ /blɛk/.
BLACK | NEW:HISTORICAL_SOURCE | Y | page | "From Middle English blak, black, blake, from Old English blæc" | W:black:E1:Etymology:0 | L548. The chain continues to Proto-Germanic *blakaz ("burnt").
BLACK | NEW:PREDICATIVE | Y | item | "The items around him were black in colour." | W:black:E1:Adjective:1 | L567.
BLACK | P04 | Y | item | "The items around him were black in colour." | W:black:E1:Adjective:1 | L567. PP dependent "in colour".
BLACK | NEW:ATTRIBUTIVE | Y | item | "a drop of the blackest tincture wears away and vanishes" | W:black:E1:Adjective:1 | L570. 1712 October 22, Addison, The Spectator, no. 507.
BLACK | P05 | Y | item | "a drop of the blackest tincture wears away and vanishes" | W:black:E1:Adjective:1 | L570. Inflected superlative of the matched sense. Headword "black (comparative blacker or more black, superlative blackest or most black)" (L563).
QUICKLY | P13 | N | page | "/ˈkwɪk.li/" | W:quickly:E1:Pronunciation:0 | L2693.
QUICKLY | NEW:HISTORICAL_SOURCE | Y | page | "From Middle English quykly, quikliche, quicliche, cwikliche, cwickliche, from Old English cwiculīċe." | W:quickly:E1:Etymology:0 | L2690. The block continues "By surface analysis, quick + -ly."
QUICKLY | P07D | Y | item | "Rapidly; with speed; fast; with expedition." | W:quickly:E1:Adverb:1 | L2701. Full gloss; replaces v1's "; with speed; ...".
QUICKLY | P03 | Y | item | "Luckily, the error was quickly corrected." | W:quickly:E1:Adverb:1 | L2703.
QUICKLY | NEW:VERB_MODIFIER | Y | item | "Luckily, the error was quickly corrected." | W:quickly:E1:Adverb:1 | L2703. Contrast VERY_INTENS's N.
```

2. PER BEARER
- DAMN_REACT: P13 and HISTORICAL_SOURCE only. Interjection:1 (L1168–1170) still has no example or quotation, only "EXAMPLE: Synonyms: see" and "See also dammit". Nothing new for P01. Neighbour: Noun:1 "He said a few damns and left." (L1177) puts the curse word in the plural with a quantifier. It's filed as its own sense, so it's a P06 candidate for you to judge, not a value for this bearer.
- DAMN_NP: P04 Y and P01 Y from Verb:5 "Damn him!". P05 is headword-level only. Other object-taking lines are other senses: Verb:1 "I damn you eternally, fiend!" (L1110) and Verb:2 "look, with a spot I damn him" (L1115).
- DAMN_PRENOM: P03 Y twice from examples. The headword "damn (not comparable)" matches v1.
- DAMN_DEGREE: P03 Y. Other Adverb:1 lines: "How are you damn quick?" (damn modifies quick; this isn't the post-wh slot), "You must be so damn rapid." (it's unclear what "so" attaches to, so I left P04 uncoded), "I damn well hope you never come back." (damn modifies well, not the verb; relevant to CGEL's *I damn hated it) and 1989 Gay Community News "damn near down on our knees".
- BANG_DEPICT: P01 Y twice, P10A Y in two patterns, HISTORICAL_SOURCE and P13. P09 is not coded. "pointed his finger at her like a gun and said, “Bang!”" supports depiction, but the brief's example clause covers P01–P06 and P12 only, and P09 needs the source to characterize the use as resemblance-based, which the gloss still doesn't. No P02: no line puts Bang beside a clause inside one sentence.
- BANG_NOUN: P06 Y (plural headword; determiner), P04 Y, HISTORICAL_SOURCE and P13.
- BLOODY_PRENOM: P10A Y (Jordan), HISTORICAL_SOURCE, P13 and a headword-scope P05. The only predicative bloody on the page ("I was bloody to him", L825) is Adjective:4 (dated, "Badly behaved; unpleasant; beastly."), not the intensifier.
- BLOODY_INTENS: P03 Y twice (adjective-modifying use confirmed), COMPARABLE as template default, HISTORICAL_SOURCE and P13.
- BLOODY_INFIX: nothing new. The examples attest the infix ("Absobloodylutely!" L7, Wyndham 1951 "Piccabloodydilly Circus" L8, Guardian 2010 "a-bloody-gain" L9), but NEW:INFIX is already Y. Reading PRE_STRESS_PLACEMENT off them would need stress facts the file doesn't give. The page has no Pronunciation or Etymology block (all its blocks are Infix:0, Infix:1 and Usage notes:0), so P13 and HISTORICAL_SOURCE have no value. That's an absence in the page, not an extractor fault.
- FUCKING_PRENOM: full Adjective:2 gloss (P08), conditional P07D and P10A, an example-based P03, HISTORICAL_SOURCE and P13. Two lines filed under Adjective:1 aren't prenominal: "I was fucking high" (L1258) modifies an adjective, and "three o’fucking clock" (L1260) is tmesis. Wiktionary's Adjective heading is broader than the bearer's use. NEW:PREDICATIVE N (label) is unchanged, and every prenominal example is consistent with it.
- BASTARD_SUPP: readable HISTORICAL_SOURCE ("used as an epithet"), P13 and a sense-level P06. Still no line shows the supplementary construction.
- YOU_BASTARD: P01 Y and P04 Y from "You sick bastard!". Neighbour: Noun:4 (endearing) has "Get over here, you old bastard!" (L435). Interjection:1 (L534, "Exclamation of strong dismay...") is not this use, as v1 said.
- THE_HELL_WH: example-based POST_WH, a P03 for your call, P13 and a neighbour etymology. The Adverb:2 quotations also show the sense outside the slot: "I sure wish the hell I stayed in the closet" (1971, Allan Oxside, Body Politic, no. 1, p. 3; L3088) and "all-the-hell-over-the-place" (1989, Wittke, Gay Community News; L3089). So "typically" isn't exclusive, and the matched sense is wider than the bearer's CGEL use.
- VERY_INTENS: completed quotations for the three v1 rows, HISTORICAL_SOURCE, P13, P03, and a P04 that depends on attachment. Not coded: "‘Is she busy?’ ― ‘Not very.’" (L3259) is an answer fragment, which the P01 note excludes. "That dress is very you." (L3256) modifies a pronoun; I noted it but didn't code it.
- EXACTLY_WH: evidenced negative for POST_WH. A case-insensitive grep of the whole v2 file for `\b(what|who|where|why|how|when|which) exactly\b` found nothing. I read Adverb:1, Adverb:2 and Interjection:1 in full (L1198–1216). The only wh-adjacent line has exactly before the wh-word: "exactly when to change" (1976 Stevie Wonder, Adverb:1, L1204). Neighbour: Interjection:1 "Signifies agreement or recognition." (L1215), with "Yes, exactly!".
- MAIN_PRENOM: ATTRIBUTIVE Y and P03 Y from an example, HISTORICAL_SOURCE and P13. Evidenced negative for predicative under Adjective:1: all five lines (L2028–2031) are attributive. The only predicative main is Milton under Adjective:2, as v1 noted.
- PROBABLE_PRENOM: ATTRIBUTIVE Y, PREDICATIVE Y twice, P03, P04, COMPARABLE as template default, HISTORICAL_SOURCE and P13.
- COFFEE: P06 attested (determiner) and headword plural, P03, HISTORICAL_SOURCE and P13. No answer-use example: Noun:1 and Noun:2 read in full (L993–1004).
- STOP: attested P04, HISTORICAL_SOURCE and P13. "I stopped at the traffic lights." (Verb:1, L2843) also gives P05 on a use_gloss sense; P05 is already Y in v1, so I didn't add a row. There's no bare imperative "Stop!" on the stop page. A grep for `^(EXAMPLE|QUOTATION):.*\bStop\b` over the whole file finds imperatives only on other pages: "Stop banging on the door." (W:bang:E1:Verb:4, L311), "Hey! Stop that!" (W:hey:E1:Interjection:2, L1735) and a "Stop complaining, lah" quotation (L1899). Those are neighbours, not rows.
- BLACK: PREDICATIVE, ATTRIBUTIVE, P04, P05 (sense-level), HISTORICAL_SOURCE and P13. No answer-use line in Adjective:1 (L565–571). Adjective:12 "Jim drinks his coffee black" (L623) is the neighbour v1 mentioned.
- QUICKLY: full gloss (P07D), P03, VERB_MODIFIER Y, HISTORICAL_SOURCE and P13.

3. FLAGS, NEIGHBOURS NOW READABLE, AND WHAT'S STILL UNREADABLE

Three flags to settle before merging:
1. Comparability is now Wiktionary's template default. In v1, bare "{{en-adv}}"/"{{en-adj}}" headwords were left uncoded. In v2 the same headwords print "more X, most X": bloody Adverb:0 (L831), exactly Adverb:0 (L1196), probable Adjective:0 (L2659), and bastard Adjective:0 "bastard (comparative more bastard, superlative most bastard)" (L487, not a bearer). That's the template's output when no editor parameter is given. Coding these Y would reverse v1's finding that comparability doesn't separate expressive uses from controls, and it would do so on default rather than asserted evidence. I've coded them Y with a "template default" note so you can filter them.
2. P01 from EXAMPLE lines. I coded P01 Y for DAMN_NP, BANG_DEPICT and YOU_BASTARD from editor-constructed examples. Those lines exemplify the use as conventional, which is the positive standard, so I read the P01 note's solitary-occurrence exclusion as aimed at single corpus tokens. This departs from v1's abstention on "You bastards!". Apply it to all three or to none.
3. P13 N at page scope depends on the community clause. Several transcriptions contain symbols a reader may question: [ɖ] in bloody (India), [ʈ] and the prothetic (ɪ) in stop (South Asia), syllabic /l̩/ in probable, [ɛ̃] in bang, the tap in Scottish very. Each is ordinary for its labelled community, and /l̩/ is a lateral, not a fricative. No page in my half has a click, a vowelless form, a nasal-only form or a syllabic fricative. All P13 values are page-level, not use-specific.

Neighbour senses now readable (not values for my bearers):
- W:the hell:E0:Interjection:1 (L3096): "Ellipsis of what the hell, an exclamation indicating surprise or dismay." If it were matched, P08 would be Y ("surprise or dismay"). Quotation "“The hell!” exclaimed Crane." (2013, Latimer, L3097). It's not THE_HELL_WH's use.
- W:the hell:E0:Pronoun:1 (L3103): "Ellipsis of what the hell (“what”)." with "The hell is that?" (L3104). Here the form is the interrogative itself, not a modifier after one.
- Category disagreement inside one source: the string in THE_HELL_WH's use is an Adverb on the "the hell" page ("What the hell was that?", Adverb:2) and a Noun on the hell page ("What the hell is wrong with you?!", Noun:4, glossed "in phrases grammatically requiring a noun"). This bears on the bearer's category, so I'm flagging it rather than resolving it.
- W:bang:E2:Noun:1 (L394): "Archaic spelling of bhang.", headword "bang (uncountable)". Irrelevant.
- W:bang:E1:Adverb:4 (L375): "(informal) Used as a general intensifier." ("I'm bang up for it!"). Not a bearer; noted because it's another use-description intensifier gloss.

Still unreadable or absent:
- bastard Adjective:6 (L507) and :8 (L513) have no gloss line. Each block holds only a quotation (Barrow a. 1678 "that bastard self-love"; Haggard "a bastard Arabic"). They look like quotations split off from :5 and :7, not senses. Not bearers.
- fucking Etymology L1220 is a module error message, not content.
- -bloody- has no Pronunciation or Etymology block, so BLOODY_INFIX gets no P13 or HISTORICAL_SOURCE.
- "the hell" has no Etymology block; the hell-page etymology above is a neighbour only.
- bloody's etymology hands sense evolution off to Wikipedia, so no path from the lemma to the expressive uses is stated.
- P12S/P12I: no matched sense in my half describes prosody. The -bloody- note "Usually inserted before the stressed syllable." (L12) is about placement, not intonation.
- Not reached: none. All 21 bearers covered.