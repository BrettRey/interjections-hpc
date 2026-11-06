# Wiktionary extraction v1: expressive and control rows (from the template-stripped sense text; see the responsibility notices)

Saved verbatim by the parent session (Claude Opus 5.5) from the subagent's SubagentHandback report. Model output, not a source; every quotation is checked by the parent against the page-marked source text before use.

---

RESPONSIBILITY NOTICE
Observation: wiktionary-senses.txt has lost template content on all 16 pages I read. Pronunciation blocks are bare bullets with no IPA (lines 801-815, 902-911, 1872-1879, 2007-2021, 3189-3199). Etymology chains have their source forms stripped ("From , from , from , from la." at 799; also 915, 1882, 2133, 2321, 2555, 3048, 3268, 3306, 3485). Nearly every EXAMPLE line and most QUOTATION lines are empty. Several glosses are cut where a template stood: 3100 "Used as an", 3027 "(mildly, vulgar) .", 3034 "(mildly, profane, slang, interrogative) .", 2371 "; evil", 2566 "; with speed", 2952 ", annoying or worthless.". Usage notes stop mid-word at a character cap (1919, 2453, 2530, 3071).
Possible consequence: P13 and NEW:HISTORICAL_SOURCE can't be read for any of my 21 bearers, and every Y that would come from an example sentence is missing (P06 for BANG_NOUN, P01 for DAMN_REACT, P03 for DAMN_PRENOM, among others). Anyone reading the merged table will take "no Wiktionary statement" to mean Wiktionary is silent, when the gap comes from the extractor. The other agent's half probably has the same defect.
Paused: nothing. I didn't read raw/*.json because the brief rules out other files, so this is inferred from the text pattern and not checked against the wikitext.
Needed from Brett: should the column be re-extracted from /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/wiktionary-2026-11-05/raw/*.json with templates expanded (IPA, etymology, ux/quote) before it's coded? Until then, treat what follows as evidence from glosses, labels and headwords only.

Second defect: block ids are not unique. The same id appears more than once in W:bang:Noun:0/1 (lines 922/925 and 1085/1088), W:stop:Noun:0/1 (2219, 2303, 2312), W:very:Usage notes:0 (3224 and 3264), W:main:Noun:0/1 (3385, 3447, 3476) and W:hell:Verb:0/1 (3148, 3165, 3175). Every row below gives the header line number (L) in its note, so a string check by id alone won't land on the wrong block.

File: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/wiktionary-2026-11-05/wiktionary-senses.txt

1. TABLE
Fields are separated by " | ". Quotations are in straight double quotes, and any pipe inside them belongs to the quoted text.

```
DAMN_REACT | P08 | Y | item | "Used to express anger, irritation, disappointment, annoyance, contempt or surprise, etc." | W:damn:Interjection:1 | L882. POS Interjection (headword {{en-intj}}, L879). Labels: slang, slightly, vulgar. EXAMPLE empty.
DAMN_REACT | NEW:USE_DESCRIPTION_GLOSS | Y | item | "Used to express anger, irritation, disappointment, annoyance, contempt or surprise, etc." | W:damn:Interjection:1 | L882.
DAMN_PRENOM | NEW:COMPARABLE | N | item | "{{en-adj|-}}" | W:damn:Adjective:0 | L854. Only one Adjective sense, so the headword is the matched sense's. No attributive/predicative label.
DAMN_PRENOM | NEW:USE_DESCRIPTION_GLOSS | Y | item | "Generic intensifier. Fucking; bloody." | W:damn:Adjective:1 | L857. POS Adjective. Labels: slang, slightly vulgar. Not P08 (intensifier names no evaluative content). Six EXAMPLE lines empty.
DAMN_DEGREE | NEW:COMPARABLE | N | item | "{{en-adv|-}}" | W:damn:Adverb:0 | L867. Only one Adverb sense.
DAMN_DEGREE | P07D | Y | item | "Very; extremely." | W:damn:Adverb:1 | L870. POS Adverb. Labels: slang, slightly vulgar. Synonym gloss giving degree content, coded the same as VERY_INTENS. If synonym glosses don't count, drop both.
BANG_NOUN | P07D | Y | item | "A sudden percussive noise." | W:bang:Noun:1 | L925 (first of two bang Noun:1 ids). POS Noun. Headword "{{en-noun}}" (L922) prints no plural, so P06 is uncoded. Gloss is almost the same as BANG_DEPICT's.
BLOODY_PRENOM | NEW:COMPARABLE | Y | item (headword) | "{{en-adj|er}}" | W:bloody:Adjective:0 | L1884. Applies to the whole headword. Nothing in the file ties it to Adjective:3; the only comparative forms in the file are "bloodier"/"bloodiest" in a search URL under Adjective:2 (bloodshed), L1899.
BLOODY_PRENOM | P03 | Y | item | "There seems to be something wrong with our bloody ships today." | W:bloody:Adjective:3 | L1902. 1916 Beatty quotation, prenominal after a genitive pronoun.
BLOODY_PRENOM | P03 | Y | item | "You bloody fool, I could′ve stabbed you in the heart" | W:bloody:Adjective:3 | L1902 (quotation at L1911, prime character as in file). Prenominal inside an exclamatory NP (compare YOU_BASTARD).
BLOODY_PRENOM | NEW:USE_DESCRIPTION_GLOSS | Y | item | "Used as an intensifier." | W:bloody:Adjective:3 | L1902. POS Adjective. Labels: informal, Britain, Ireland, Commonwealth, Hawaii, mildly vulgar. Not P08.
BLOODY_INTENS | P08 | Y | item | "Used to express anger, annoyance, or shock, or for emphasis." | W:bloody:Adverb:1 | L1924. POS Adverb. Labels: informal, Australia, Britain, India, Ireland, Newfoundland, NZ, South Africa, mildly vulgar. Quotations empty, so the adjective-modifying use isn't confirmed. Headword "{{en-adv}}" has no comparability parameter (not coded).
BLOODY_INTENS | NEW:USE_DESCRIPTION_GLOSS | Y | item | "Used to express anger, annoyance, or shock, or for emphasis." | W:bloody:Adverb:1 | L1924.
BLOODY_INFIX | NEW:INFIX | Y | item | "{{head|en|infix}}" | W:-bloody-:Infix:0 | L2989. POS Infix. Same fact as MW_SUBWORD (relatedness).
BLOODY_INFIX | NEW:INFIX | Y | page | "An example of tmesis." | W:-bloody-:Usage notes:0 | L2998.
BLOODY_INFIX | NEW:PRE_STRESS_PLACEMENT | Y | page | "Usually inserted before the stressed syllable." | W:-bloody-:Usage notes:0 | L2998. "Usually" marks the typical case, so no exclusivity.
BLOODY_INFIX | NEW:USE_DESCRIPTION_GLOSS | Y | item | "An intensifier." | W:-bloody-:Infix:1 | L2992. Labels: British, Australian, slang. The page has no Etymology or Pronunciation block.
FUCKING_PRENOM | NEW:COMPARABLE | N | item | "{{en-adj|-}}" | W:fucking:Adjective:0 | L2936.
FUCKING_PRENOM | NEW:ATTRIBUTIVE | Y | item | "{{lb|en|vulgar|attributive}}" | W:fucking:Adjective:0 | L2936. On the headword, so it covers Adjective:1 and :2.
FUCKING_PRENOM | NEW:PREDICATIVE | N | item | "{{lb|en|vulgar|attributive}}" | W:fucking:Adjective:0 | L2936. Per the brief, an "attributive" label means attributive only. This is the only attributive/predicative label on any headword I read.
FUCKING_PRENOM | P03 | Y | item | "the specific word it grammatically modifies" | W:fucking:Adjective:1 | L2939. States a modifier position.
FUCKING_PRENOM | NEW:UTTERANCE_SCOPE | Y | item | "often applying more to the whole utterance than to the specific word it grammatically modifies" | W:fucking:Adjective:1 | L2939. Not one of Potts's six by name. Adverb:1 (L2968) says the same of the adverb.
FUCKING_PRENOM | NEW:USE_DESCRIPTION_GLOSS | Y | item | "An intensifier, often applying more to the whole utterance" | W:fucking:Adjective:1 | L2939.
FUCKING_PRENOM | P08 | Y | item | ", annoying or worthless." | W:fucking:Adjective:2 | L2951. Holds only if Adjective:2 is matched (see section 2). First gloss word stripped.
BASTARD_SUPP | P08 | Y | item | "A contemptible, inconsiderate, overly or arrogantly rude or spiteful person." | W:bastard:Noun:3 | L2782. POS Noun (headword {{en-noun|~}}, L2771). Labels: vulgar, offensive, or, pejorative, usually, referring specifically to a man. No sense covers the supplementary construction.
BASTARD_SUPP | P07D | Y | item | "A contemptible, inconsiderate, overly or arrogantly rude or spiteful person." | W:bastard:Noun:3 | L2782. Mixed: descriptive ("person", man) plus evaluative. The properties note says mixed = Y.
YOU_BASTARD | P08 | Y | item | "A contemptible, inconsiderate, overly or arrogantly rude or spiteful person." | W:bastard:Noun:3 | L2782.
YOU_BASTARD | P07D | Y | item | "A contemptible, inconsiderate, overly or arrogantly rude or spiteful person." | W:bastard:Noun:3 | L2782. Mixed, as above.
YOU_BASTARD | P06 | Y (plural) | item | "“Oh my God, they killed Kenny!” “You bastards!”" | W:bastard:Noun:3 | L2782 (quotation L2790, 1997 South Park). The only instance of this use in the file. P01 left uncoded: the line is its own turn, but P01's note says a solitary occurrence alone doesn't support Y.
BASTARD_SUPP; YOU_BASTARD | NEW:HISTORICAL_SOURCE | Y | page | "Frankish *bāst derives from a North Sea Germanic variety of" | W:bastard:Etymology:0 | L2755. Word-level etymology; the chain itself is stripped ("Likely from + , fro."). Nothing connects the epithet sense to the "born out of wedlock" sense.
THE_HELL_WH | NEW:COMPARABLE | N | item | "{{en-adv|-}}" | W:the hell:Adverb:0 | L3006.
THE_HELL_WH | NEW:POST_WH | Y | item | "typically after an interrogative term or relative pronoun" | W:the hell:Adverb:2 | L3015. "Typically", so no N for other positions. Wider than CGEL's interrogative-only, since relative pronouns are included. P03 left uncoded (the gloss gives a position, not a function).
THE_HELL_WH | NEW:USE_DESCRIPTION_GLOSS | Y | item | "Expletive used for emphasis" | W:the hell:Adverb:2 | L3015. Labels: sometimes, vulgar. Not P08 (expletive/emphasis alone). "the hell" has no Etymology block.
VERY_INTENS | NEW:COMPARABLE | N | item | "{{en-adv|-}}" | W:very:Adverb:0 | L3201.
VERY_INTENS | P07D | Y | item | "To a great extent or degree." | W:very:Adverb:1 | L3204. Paraphrase giving degree content, coded the same as DAMN_DEGREE.
VERY_INTENS | P10A | Y (adjacent repetition) | page | "Commonly intensified by , as in very, very important person." | W:very:Usage notes:0 | L3224 (the block after the Adverb senses). The word after "by" is stripped.
VERY_INTENS | P10S | Y (adjacent repetition) | page | "Commonly intensified by , as in very, very important person." | W:very:Usage notes:0 | L3224. "Intensified" states strengthening. This is as close as my pages come to Potts's repeatability, and it's stated for a control.
VERY_INTENS | NEW:VERB_MODIFIER | N | page | "When used in their senses as degree adverbs, and too never modify verbs (except in some dialects influenced by Chinese: see citations)." | W:very:Usage notes:0 | L3224 (line 3226). The subject word before "and too" is stripped. There's a stated dialect exception, so the N holds for general varieties only.
VERY_INTENS | NEW:HISTORICAL_SOURCE | Y | page | "derived from la" | W:very:Etymology:0 | L3183. Latin source form stripped. Same block: "Over time displaced the use of a number of Germanic words or prefixes to convey the sense 'very'" (history of the intensifier sense, not a source).
EXACTLY_WH | P07D | Y | item | "Of a focus, precisely, used to provide emphasis." | W:exactly:Adverb:2 | L3285. Mixed: synonym plus use description. Headword "{{en-adv}}" has no comparability parameter. Nothing about the post-wh position (contrast THE_HELL_WH).
EXACTLY_WH | NEW:USE_DESCRIPTION_GLOSS | Y | item | "used to provide emphasis" | W:exactly:Adverb:2 | L3285. A control with a use-description gloss, so this property doesn't separate cleanly.
MAIN_PRENOM | NEW:COMPARABLE | N | item | "{{en-adj|-}}" | W:main:Adjective:0 | L3309. Applies to the whole headword, but Adjective:5 (Appalachia) quotes "main-est" (section 4).
MAIN_PRENOM | P07D | Y | item | "Of chief or leading importance; prime, principal." | W:main:Adjective:1 | L3312. No attributive/predicative label.
PROBABLE_PRENOM | P07D | Y | item | "Likely or most likely to be true." | W:probable:Adjective:1 | L3496. Headword "{{en-adj}}" (L3493) has no comparability parameter. No attributive label.
PROBABLE_PRENOM | P07D | Y | item | "Likely to happen." | W:probable:Adjective:2 | L3502.
COFFEE | P07D | Y | item | "A beverage made by infusing the beans of the coffee plant in hot water." | W:coffee:Noun:1 | L2026. Headword "{{en-noun|~}}" (L2023). No answer-use or interjection sense on the page.
COFFEE | NEW:NONCOUNT | Y | item | "(uncountable)" | W:coffee:Noun:1 | L2026.
COFFEE | NEW:COUNT | Y | item | "(countable) A serving of this beverage." | W:coffee:Noun:2 | L2035.
COFFEE | P06 | Y | item | "(countable) A serving of this beverage." | W:coffee:Noun:2 | L2035. Based on a label, not an attested combination. Downgrade if labels don't count for P06.
STOP | P07D | Y | item | "(intransitive) To cease moving." | W:stop:Verb:1 | L2140. Headword "{{en-verb}}" prints no forms. The page has no Interjection section.
STOP | NEW:TRANSITIVE | Y | item | "(transitive) To cause (something) to cease moving or progressing." | W:stop:Verb:3 | L2150. Matches "Stop the car!".
STOP | P04 | Y | item | "(transitive) To cause (something) to cease moving or progressing." | W:stop:Verb:3 | L2150. Direct object, from the label.
STOP | NEW:CATENATIVE | Y | page | "This is a catenative verb that takes the gerund -ing to indicate the ending action (stop thinking), or the to infinitive to indicate the purpose of the interruption (stop to think)." | W:stop:Usage notes:0 | L2215. About the lemma.
STOP | P04 | Y | page | "This is a catenative verb that takes the gerund -ing to indicate the ending action (stop thinking), or the to infinitive to indicate the purpose of the interruption (stop to think)." | W:stop:Usage notes:0 | L2215.
STOP | P05 | Y | item | "the surpliced group stopped to say the last prayer" | W:stop:Verb:2 | L2144. A past form of the sense in a declarative quotation, not an inflected imperative.
BLACK | NEW:COMPARABLE | Y | item (headword) | "{{en-adj|er,more}}" | W:black:Adjective:0 | L2335. Applies to the whole headword; the file doesn't say which sense licenses it.
BLACK | P07D | Y | item | "(of an object) Absorbing all light and reflecting none; dark and hueless." | W:black:Adjective:1 | L2338. "(of an object)" is a selectional label, not attributive/predicative. No answer-use statement.
QUICKLY | NEW:COMPARABLE | Y | item | "{{en-adv|er,more}}" | W:quickly:Adverb:0 | L2562.
QUICKLY | P05 | Y | page | "Although the comparative (quicklier) and superlative (quickliest) one-word forms exist and are and have been in limited use, the two-word forms (more quickly and most quickly) are much more common." | W:quickly:Usage notes:0 | L2577. Inflected comparative and superlative.
QUICKLY | P07D | Y | item | "; with speed; fast; with expedition." | W:quickly:Adverb:1 | L2565. First gloss word stripped.
```

2. MATCHED SENSES
- DAMN_REACT: W:damn:Interjection:1 (Interjection).
- DAMN_NP: no matching sense. The closest is W:damn:Verb:5 "(slang, slightly <<vulgar>>) To curse; put a curse upon." (L843), which doesn't describe the exclamatory complement-taking use and has no transitivity label. I didn't derive P04 from the implied object.
- DAMN_PRENOM: W:damn:Adjective:1 (Adjective).
- DAMN_DEGREE: W:damn:Adverb:1 (Adverb).
- BANG_DEPICT: W:bang:Interjection:1 (Interjection), "A sudden percussive sound, such as made by the firing of a gun, slamming of a door, etc." (L1077). No rows. The wording doesn't support P09 (no resemblance or imitation), and the gloss is a nominal paraphrase nearly identical to Noun:1. Its four quotations are empty.
- BANG_NOUN: W:bang:Noun:1 at L925 (Noun, Etymology1). Noun:2 "A heavy strike..." is a neighbour.
- BLOODY_PRENOM: W:bloody:Adjective:3 (Adjective).
- BLOODY_INTENS: W:bloody:Adverb:1 (Adverb). I chose it over Adjective:3 because Adjective:3's quotations are prenominal and Wiktionary puts adjective-modifying uses under Adverb. The brief's comparability example assumed the adjective headword.
- BLOODY_INFIX: W:-bloody-:Infix:1 (Infix).
- FUCKING_PRENOM: W:fucking:Adjective:1 (intensifier), with Adjective:2 (", annoying or worthless.") also possible. Both sit under the headword with the "attributive" label. P08 Y depends on including :2.
- BASTARD_SUPP: W:bastard:Noun:3 (Noun). No sense covers the supplementary construction.
- YOU_BASTARD: W:bastard:Noun:3, through the quotation at L2789-2790 only; the use has no sense of its own. W:bastard:Interjection:1 (L2894, "Exclamation of strong dismay or strong sense of being upset", rare) has no addressee and isn't this use.
- THE_HELL_WH: W:the hell:Adverb:2 (Adverb).
- VERY_INTENS: W:very:Adverb:1 (Adverb).
- EXACTLY_WH: W:exactly:Adverb:2 (focus), with Adverb:1 (manner) as the alternative. Examples are stripped, so the wh position can't be confirmed.
- MAIN_PRENOM: W:main:Adjective:1 (Adjective). Adjective:2 is a neighbour.
- PROBABLE_PRENOM: W:probable:Adjective:1 and :2 (Adjective).
- COFFEE: W:coffee:Noun:1 and :2 (Noun).
- STOP: W:stop:Verb:1 and :3 (the two use_gloss examples), plus :2 (Verb).
- BLACK: W:black:Adjective:1 (Adjective). :12 "(of coffee or tea) Without any cream, milk or creamer." would fit a different answer use, but the use_gloss says colour.
- QUICKLY: W:quickly:Adverb:1 (Adverb).

3. NEW PROPERTIES
- NEW:COMPARABLE: the {{en-adj}}/{{en-adv}} headword marks the item comparable (Y: er or more) or not comparable (N: -). It applies to the whole headword, not to one sense.
- NEW:ATTRIBUTIVE: may occur in attributive function (from a label).
- NEW:PREDICATIVE: may occur in predicative function (N from an "attributive" label).
- NEW:TRANSITIVE: may take a direct object (from a "(transitive)" sense label).
- NEW:CATENATIVE: may take a non-finite clause complement (gerund-participial or to-infinitival).
- NEW:COUNT / NEW:NONCOUNT: sense labelled "(countable)" / "(uncountable)".
- NEW:INFIX: inserted inside a host word (Infix heading or tmesis note). Duplicates MW_SUBWORD, recorded here as source evidence.
- NEW:PRE_STRESS_PLACEMENT: may be placed immediately before the host's stressed syllable.
- NEW:VERB_MODIFIER: may modify a verb.
- NEW:UTTERANCE_SCOPE: the contribution may apply to the whole utterance rather than the word it grammatically modifies.
- NEW:POST_WH: may occur immediately after an interrogative word or relative pronoun.
- NEW:HISTORICAL_SOURCE: the source form the Etymology block gives (in the note).
- NEW:USE_DESCRIPTION_GLOSS: Wiktionary defines the matched sense by describing its use ("Used to...", "An intensifier", "Expletive used for...") rather than paraphrasing its content. This is a fact about the dictionary record, not a possibility of the use, so I coded Y only. Senses with paraphrase glosses only: DAMN_DEGREE, BANG_NOUN, BANG_DEPICT, BASTARD Noun:3, VERY, MAIN, PROBABLE, COFFEE, STOP, BLACK, QUICKLY. EXACTLY_WH is a control and still gets Y, so the property leaks.

4. WHAT I COULDN'T MATCH OR READ, AND NEIGHBOURING EVIDENCE
- P13 is unreadable for all 21 bearers (no IPA anywhere). HISTORICAL_SOURCE is unreadable except the bastard and very rows: the chains are stripped for damn (799), bang (915), bloody (1882, which says only "See Wikipedia for thoughts on sense evolution."), coffee (2004), stop (2133), black (2321), quickly (2555), hell (3048), exactly ("From .", 3268), main (3306) and probable (3485). The fucking Etymology block is empty (2907-2909). -bloody- and "the hell" have no Etymology block.
- Unreadable glosses that may matter:
  - hell Noun:4 (L3099) "(mildly, vulgar) Used as an" is truncated and may be the "what the hell" intensifier.
  - the hell Interjection:1 (L3026) and Pronoun:1 (L3033) are blank. Pronoun:1 is labelled interrogative and may bear on THE_HELL_WH.
  - The second bang Noun section (L1085-1089) has headword "{{en-noun|-}}", gloss ".", and no Etymology2 header.
  - bastard Adjective:6 and :8 are bare "*".
  - The bastard Interjection headword reads literally "{{en-intj|head=!}}" (L2892).
- Headwords with no comparability parameter, left uncoded: bloody Adverb:0 "{{en-adv}}", exactly Adverb:0 "{{en-adv}}", probable Adjective:0 "{{en-adj}}", bastard Adjective:0 "{{en-adj}}". Noun and verb templates print no forms, so BANG_NOUN has no P06 evidence, even though its use_gloss is defined by plurals.
- Attributive/predicative labels, evidenced negative. I checked the headword and matched sense lines W:damn:Adjective:0/1, W:bloody:Adjective:0/3, W:main:Adjective:0/1, W:probable:Adjective:0/1/2, W:black:Adjective:0/1 and W:very:Adverb:0/1. None carries an attributive or predicative label; only fucking's headword does. very's "Exclusively used attributively and never predicatively." (second W:very:Usage notes:0, L3264) follows the Adjective senses (the "true, same" very), not VERY_INTENS.
- Neighbouring-sense facts, not values for the bearer:
  - main Adjective:5 (Appalachia, L3336) quotes "Goose grease is the main-est thing for waterproofing shoes." under a "{{en-adj|-}}" headword.
  - main Adjective:2's Milton quotation "Beleivſt ſo main to our ſucceſs" (L3325) is predicative and degree-modified.
- Potts: none of the six is stated by name on my pages. The nearest statements are very's repetition note (coded P10A/P10S) and fucking's whole-utterance scope (NEW:UTTERANCE_SCOPE).
- Register fields, notes only:
  - bloody Usage notes (L1918): "As an intensifier in Commonwealth usage, bloody is sometimes considered a swear word, and it was formerly considered one of the strongest profanities in British English (approximately between 1750 and 1920)."
  - bastard Usage notes (L2843): endearment use in Australian English, which belongs to Noun:4 and isn't a bearer.
- For the comparison Brett wants (based on what this file shows):
  - Comparability doesn't separate expressive uses from same-slot controls. damn (adv), the hell and very are all "-". damn (adj), fucking and main are all "-". probable has no parameter, and bloody's "er" covers its whole headword.
  - Only fucking carries "attributive".
  - P08 splits inside one form: bloody's Adverb sense states affect, but its Adjective intensifier sense doesn't.
  - The one repetition-strengthening statement belongs to the control very.
  - The post-wh slot is recorded for "the hell" but not for exactly.