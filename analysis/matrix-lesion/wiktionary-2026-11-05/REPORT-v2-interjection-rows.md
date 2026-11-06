# Wiktionary extraction v2 supplement: interjection rows (from the template-expanded text)

Saved verbatim by the parent session (Claude Opus 5.5) from the subagent's SubagentHandback report. Model output, not a source; every quotation is checked by the parent against the page-marked source text before use.

---

## Wiktionary W2: supplementary extraction for 25 interjection bearers (half B)

There's no responsibility notice; I found nothing at that threshold.

I read only `/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/wiktionary-2026-11-05/wiktionary-senses-v2.txt` (matched senses, Pronunciation, Etymology and Usage notes), the v1 interjection report, `items-v4.csv` and `properties-v4.csv`.

- Everything between « and » is copied character for character from v2, including curly quotes. I grep-checked the ones with special characters (IPA, tone letters, the click sign, CJK).
- Block ids are v2 ids, with E<k>.
- I agree with all of v1's sense matches.
- I coded no P13 N. Under the brief ("N needs an explicit statement"), a short IPA list isn't one. For P13's negative standard ("gives the conventional form(s) in full and all are within ordinary word phonology"), that's the parent's call, so the ordinary transcriptions are listed separately in 1b.

### 1. Table

item_id | property | value | scope | «quotation» | block id | note
---|---|---|---|---|---|---
AH | P02 | Y | item | «Ah, I understand now.» | W:ah:E1:Interjection:1 | EXAMPLE. This is a modern instance, so it should replace v1's P02 row, which rested on the c. 1175 Ormulum line. «Ah, the flowers of spring.» (same block) is ah plus a verbless NP, so it isn't P02.
AH | NEW:HISTORICAL_SOURCE | Y | page | «From Middle English ah, aa, a (“ah”), of imitative origin, or from Old English ēa, *eah (“oh, alas”), from Proto-West Germanic *a, *ah (“ah”).» | W:ah:E1:Etymology:0 | Two alternatives are given. The same block also has «Some propose that the Middle English is borrowed from Old French a (“ah!, oh!, hey!”)».
AH | NEW:ETYM_NATURAL_OR_IMITATIVE | Y | page | «of imitative origin» | W:ah:E1:Etymology:0 | This is one of the two alternatives.
HEY | P02 | Y | item | «Hey, look at this!» | W:hey:E1:Interjection:1 | EXAMPLE, with an imperative clause.
HEY | NEW:HISTORICAL_SOURCE | Y | page | «From Middle English hey, hei, also without h- in ey, from Old English *hē, ēa (interjection), attested as first element in hēlā, ēalā (“O!, alas!, oh!, lo!”).» | W:hey:E1:Etymology:0 | 
HEY | NEW:ETYM_NATURAL_OR_IMITATIVE | Y | page | «Probably a natural expression, as may be inferred from its presence with similar meaning in many other unrelated languages» | W:hey:E1:Etymology:0 | Fills the adjective v1 found stripped ("Probably a expression").
OH | P02 | Y | item | «Oh, so that's how it works.» | W:oh:E1:Interjection:3 | EXAMPLE from the primary match.
OH | NEW:HISTORICAL_SOURCE | Y | page | «Inherited from Middle English o.» | W:oh:E1:Etymology:0 | v1 found this block empty. The run-together tree before it reads «Latin ōOld French ohbor.Middle English o», that is Latin ō > Old French oh (borrowed) > Middle English o.
OOPS | P02 | Y | item | «Oops, I did it again» | W:oops:E1:Interjection:1 | QUOTATION: 2000, Max Martin, Rami Yacoub, “Oops!… I Did It Again”, performed by Britney Spears (a song lyric). The EXAMPLE in the block is a "!" case (see 1c).
OUCH | NEW:HISTORICAL_SOURCE | Y | page | «Some sources say the interjection is attested since 1838 (and specifically in American English) and derives ultimately from German autsch, perhaps specifically via Pennsylvania German outch (“cry of pain”)» | W:ouch:E1:Etymology:0 | The block opens «Uncertain.» Its tail is garbled (see 3).
OUCH | NEW:ETYM_NATURAL_OR_IMITATIVE | Y | page | «"natural" exclamation attested since the mid 1600s» | W:ouch:E1:Etymology:0 | A rival account in the same block. The sentence carrying it is broken, so who it's attributed to can't be read.
UGH | P13 | Y | page | «(lexically) IPA(key): /ʌɣ/, /ʌ(ɡ)/, /ʌx/, /əː/» | W:ugh:E0:Pronunciation:0 | /x/ and /ɣ/ (velar fricatives) aren't General English phonemes. /x/ does occur in Scottish English, but the page states no community. This is the IPA v1 couldn't read; it supports v1's P13 row, which rested on the prose line «(natural exclamation) Any low-back vowel…». /ʌ(ɡ)/ also allows a word-final /ʌ/ (see the HUH row).
UGH | P02 | Y | item | «Ugh, what a smell of Christian blood there is here» | W:ugh:E0:Interjection:1 | QUOTATION: 1886, Peter Christen Asbjørnsen, translated by H.L. Brækstad, Folk and Fairy Tales, page 57. The clause is an exclamative. Also 1855, Robert Browning, Childe Roland: «But, ugh! it sounded like a baby's shriek.», where ugh sits between a coordinator and its clause.
WOW | P02 | Y | item | «Wow, I sure was surprised!» | W:wow:E1:Interjection:1 | This is v1's secondary match. The primary match, Interjection:2, has only «Wow! How do they do that?», a "!" case.
WOW | NEW:HISTORICAL_SOURCE | Y | page | «Attested since the 16th century; borrowed from Scots wow; ultimately a natural exclamation.» | W:wow:E1:Etymology:0 | Fills the borrowing source v1 found stripped: Scots wow.
ALAS | P02 | Y | item | «I wanted to catch the last bus home, but alas, I was ten minutes late and had to take a taxi instead.» | W:alas:E1:Interjection:1 | EXAMPLE, with alas between a coordinator and its clause. There's also a clause-medial parenthetical in the 1920 quotation (Edward Carpenter, Pagan and Christian Creeds, page 188): «has alas! been reserved for», between the auxiliary and the participle.
ALAS | P10A | Y | item | «saying, Alas, alas, that great citie Babylon, that mighty citie» | W:alas:E1:Interjection:1 | Pattern: adjacent repetition. QUOTATION: 1611, King James Version, Revelation 18:10 (Early Modern English). Nothing bears on P10S or P10R.
ALAS | NEW:HISTORICAL_SOURCE | Y | page | «From Middle English alas, from Old French a las (French hélas), from a (“ah”) + las, from Latin lassus (“weary”).» | W:alas:E1:Etymology:0 | Fills v1's «from fro + fro».
AHA | NEW:HISTORICAL_SOURCE | Y | page | «From Middle English a ha, aha, natural expression. Equivalent to ah + ha!.» | W:aha:E1:Etymology:0 | The Middle English form, stripped in v1, is now readable.
AHA | NEW:ETYM_NATURAL_OR_IMITATIVE | Y | page | «natural expression» | W:aha:E1:Etymology:0 | 
GEE | P02 | Y | item | «Gee, I didn't know that!» | W:gee:E1:Interjection:1 | EXAMPLE. Also the 1935 screenplay for Roberta: «Gee, that's swell.»
TUTTUT | P13 | Y | page | «IPA(key): /tʌt/, [ǀ]» | W:tut:E1:Pronunciation:0 | [ǀ] is the dental click. The block also has «Audio (UK, click):(file)». /tʌt/ and Northern England /tʊt/ are the spelling pronunciation that items-v4 excludes. tut E1 governs Interjection:1, the matched sense. The tut-tut page itself has no Pronunciation block. The only community named is "UK", on the audio line.
HUH | P13 | Y | page | «(General American) IPA(key): /hʌ/, [hʌ̃], /hə/, [hə̃]» | W:huh:E1:Pronunciation:0 | A candidate; the parent may prefer U. The RP line is «(Received Pronunciation) IPA(key): /hʌ/, [hʌ̃]». There are two grounds, and neither is a non-English segment. (a) [hʌ̃] and [hə̃] have a nasalized vowel with no nasal consonant to cause it. (b) /hʌ/ ends a word with a stressed checked vowel. v1 treated ugh's «Note: may be nasalized.» as allophonic. If that stands, ground (a) falls here too and only (b), a phonotactic ground, remains.
YES | NEW:HISTORICAL_SOURCE | Y | page | «From Middle English yes, from Old English ġīese (“by all means, of course, yes”), derived from the same root as yea.» | W:yes:E1:Etymology:0 | Replaces v1's stripped row. A run-together tree precedes it.
YES | NEW:DELOCUTIVE_VERB | Y | page | «(colloquial, intransitive) To say “yes”.» | W:yes:E1:Verb:2 | v1 read this gloss as "To say ."
NO | P02 | Y | item | «No, you are mistaken.» | W:no:E2:Particle:1 | EXAMPLE. Also «No, you may not watch television now.»
NO | NEW:HISTORICAL_SOURCE | Y | page | «Inherited from Middle English no, na, from Old English nā, nō (“no, not, not ever, never”), from Proto-West Germanic *naiwō, from Proto-Germanic *naiwô (“never”), from *ne (“not”) + *aiwō (“ever”)» | W:no:E2:Etymology:0 | The E2 id now confirms that this etymology governs the Particle senses; v1 had only file order. The block ends «Doublet of nay.»
NO | NEW:DELOCUTIVE_VERB | Y | page | «(intransitive, colloquial) To say “no”.» | W:no:E2:Verb:1 | Fills v1's "To say ."
THANKS | P02 | Y | item | «Thanks, courteous wall: Jove shield thee well for this!» | W:thanks:E1:Interjection:1 | QUOTATION: c. 1595–1596 (date written), Shakespeare, A Midsommer Nights Dreame, First Folio 1623. It's weaker in the same way as v1's HEAVENS row: a vocative NP comes between, a colon separates, and it's Early Modern English. The parent may prefer U.
THANKS | NEW:HISTORICAL_SOURCE | Y | page | «From Middle English thanks, thankes, from Old English þancas (“thanks”), from Proto-Germanic *þankōs, nominative plural of *þankaz (“thought, gratitude”)» | W:thanks:E1:Etymology:0 | Replaces v1's stripped row. It also makes v1's FROZEN_PLURAL_SHAPE row readable: a Proto-Germanic nominative plural.
SORRY | P04 | Y | item | «Sorry about yesterday. — No worries.» | W:sorry:E1:Interjection:1 | EXAMPLE under the Interjection heading, with a PP complement. The same block has «Sorry I’m so late.», with a content-clause complement. There's a rival analysis. The Usage note calls the interjection «a clipping of I'm sorry» (W:sorry:E1:Usage notes:0), and the adjective takes the same complements («I am sorry I stepped on your toes.», W:sorry:E1:Adjective:1). So these may be elliptical adjective phrases. That's for the parent or Brett to decide.
SORRY | NEW:HISTORICAL_SOURCE | Y | page | «From Middle English sory, from Old English sāriġ (“feeling or expressing grief, sorry, grieved, sorrowful, sad, mournful, bitter”)» | W:sorry:E1:Etymology:0 | This is the adjective's etymology. For the interjection, v1's clipping row (from the Usage notes) is the governing source. This row only fills the forms v1 found stripped.
HELLO | NEW:HISTORICAL_SOURCE | Y | page | «Ultimately from a variant of Old English ēalā, such as hēlā, which was used colloquially at the time similarly to how hey and (in some dialects) hi are used nowadays.» | W:hello:E1:Etymology:0 | Adds the Old English source to v1's holla/hollo row. The same block also says (paraphrased) that it may have been influenced by Old Saxon halo, the imperative of halōn.
HEAVENS | P02 | Y | item | «Heavens, is that the time?» | W:heavens:E0:Interjection:1 | EXAMPLE. A complete interrogative clause follows directly, so this is a cleaner instance than v1's 1907 Chambers row.
LAH | P13 | Y | page | «Variant for senses 1–4: IPA(key): [lɑh˨]» | W:lah:E2:Pronunciation:0 | This is word-final [h], which is separate from v1's lexical-tone row. The community comes from the line above, «(Singapore, Malaysia) IPA(key): /lɑː/, [lä(ː)]*». Brett needs to decide whether ordinary word phonology in that community allows final [h].
LAH | NEW:HISTORICAL_SOURCE | Y | page | «From Malay lah, Hokkien 啦 (--la) and Cantonese 啦 (laa1).» | W:lah:E2:Etymology:0 | Lim (2007)'s third source, stripped in v1, is Hokkien: «Hokkien 啦 (--la), which indicates finality, completion and confirmation-seeking» (same block).

**1b. P13 readings I didn't code.** All of these fall within English word phonology; N versus U is the parent's call.

- AH: «IPA(key): /ɑː/, /aː/» (W:ah:E1:Pronunciation:0)
- HEY: «enPR: hā, IPA(key): /heɪ/» (W:hey:E0:Pronunciation:0)
- OH: «(Received Pronunciation) IPA(key): /əʊ/», plus «(Yorkshire) IPA(key): [ö̞]» (W:oh:E0:Pronunciation:0)
- OOPS: «(Received Pronunciation) IPA(key): /uːps/, /ʊps/» (W:oops:E1:Pronunciation:0)
- OUCH: «IPA(key): /aʊt͡ʃ/» (W:ouch:E1:Pronunciation:0)
- WOW: «IPA(key): /waʊ/, Rhymes: -aʊ», plus the South Asian «(interjection): IPA(key): /ʋɑʋ/». The second is a variety transcription; I noted it but didn't code it. (W:wow:E1:Pronunciation:0)
- ALAS: «(Received Pronunciation) IPA(key): /əˈlæs/, /əˈlɑːs/»
- AHA: «(Received Pronunciation) IPA(key): /ɑːhɑː/»
- GEE: «IPA(key): /d͡ʒiː/» (W:gee:E1:Pronunciation:0)
- BYE: «IPA(key): /baɪ/, Rhymes: -aɪ» (W:bye:E0:Pronunciation:0)
- OKAY: «(General American, stressed form) IPA(key): /ˌoʊˈkeɪ/» and «(unstressed form) IPA(key): /əˈkeɪ/». The reduced form isn't tied to a sense, so it isn't STRESS_SHIFT.
- YES: «(Received Pronunciation, General American, Canada) IPA(key): /jɛs/»
- NO: «(General American, Canada) IPA(key): /noʊ/»
- THANKS: «IPA(key): /ˈθæŋks/». Its [ˈθɛ̃ŋks] has nasalization before /ŋ/, which is ordinary.
- SORRY: «(Received Pronunciation) IPA(key): /ˈsɒɹi/». The sarcastic use has «/ˌsɒˈɹiːː/», an extra-long vowel. That use isn't the apology use; it might be a P10A lengthening for that use, but I didn't code it.
- HELLO: «(General American) IPA(key): /hɛˈloʊ/, /hə-/, /ˈhɛloʊ/»
- HEAVENS: «IPA(key): /ˈhɛvənz/, [ˈhɛvn̩z]». A syllabic nasal is ordinary in English.
- HOWAREYOU: «(General American) IPA(key): /haʊ ˈɑɹ ju/»

**1c. Cases punctuated as their own sentence ("!" or "?") that I flagged rather than coded.** It's ambiguous whether these are P01 or P02. They stand on the same footing as v1's HELLO row «Hello. This is Marsha.»

- OUCH: «Ouch! You stepped on my toe! That hurt!» (W:ouch:E1:Interjection:1). This is the matched sense's only example.
- AHA: «Aha! That will work.» (W:aha:E1:Interjection:1)
- SORRY: «Sorry! I didn't see that you were on the phone.» (W:sorry:E1:Interjection:1) and «Oops! Sorry!» (Interjection:2)
- HUH: «Huh? Could you speak up?» (W:huh:E1:Interjection:5) and «Huh? Where did they go?» (Interjection:1)
- Answer fragments, recorded for P01 notes only: THANKS «Would you like some potatoes? — Thanks. —How many?» (W:thanks:E1:Interjection:1); NO «"Don’t you like milk?" "No." (i.e., "No, I don’t like milk.")» (W:no:E2:Particle:5)
- SH, standalone under a reporting clause: «"Sh!" said Josella, holding up a finger, and turning her ear to the wind.» (W:sh:E0:Interjection:1; 1951, John Wyndham, The Day of the Triffids)

**1d. Near misses I didn't code**

- NO: «Why is it when I say 'no', you both hear 'yes'?» (W:no:E2:Particle:1; 2000, Midsomer Murders). The words sit in a complement position but are marked as quotation (mention), so I didn't code P03.
- Vocative NPs aren't P04 dependents: «David, no!» (W:no:E2:Particle:1), «Yes, sir, we have your package right here.» (W:yes:E1:Particle:1), «Hello, everyone.» (W:hello:E1:Interjection:1).
- Audio, but no description: HELLO's Pronunciation table gives separate audio for each sense (W:hello:E1:Pronunciation:0). HUH has «Audio (Southern England, rising pitch):(file)» and a falling-pitch file. Neither is P12 evidence.
- Nothing in any matched sense supports P03, P05, P06, P12S or P12I. The newly readable glosses (SH, MMHM, OKAY) are all cross-references, so they give no P07D or P08.

### 2. One line per bearer

- **AH**: a modern P02, the Middle English and Old English source, imitative etymology, and P13 ordinary.
- **HEY**: P02, the source, natural-expression etymology, and P13 ordinary.
- **OH**: P02 (Interjection:3), the source (Middle English o; the tree goes back to Latin ō via Old French), and P13 ordinary.
- **OOPS**: P02 (from the 2000 quotation) and P13 ordinary. The etymology is unchanged from v1.
- **OUCH**: the source (German autsch via Pennsylvania German outch), the natural-exclamation alternative, and P13 ordinary. P02 is flagged only ("!").
- **SH**: the gloss now reads «Alternative spelling of shh.», a redirect to the shh page, which wasn't fetched. The 1951 quotation is standalone. The page has no Pronunciation or Etymology block, so P13 is unreadable, not N.
- **UGH**: a new P13 row from the IPA (/ʌx/, /ʌɣ/) and P02 (1886). There's no Etymology block.
- **WOW**: P02 (Interjection:1) and the source (Scots wow). P13 is ordinary; the South Asian /ʋɑʋ/ is noted.
- **ALAS**: P02, P10A (adjacent repetition, 1611), the source (Old French a las, from Latin lassus), and P13 ordinary.
- **AHA**: the source (Middle English a ha) and natural-expression etymology. P02 is flagged only, and P13 is ordinary.
- **GEE**: P02 and P13 ordinary. The etymology is unchanged from v1.
- **TUTTUT**: P13 Y (the click [ǀ] on the tut page). The tut-tut and tut senses have no examples or quotations.
- **MMHM**: the gloss now reads «Alternative spelling of mhm.», a redirect to the mhm page, which wasn't fetched. There's no Pronunciation, Etymology or example, so nothing else is readable.
- **HUH**: a candidate P13 Y ([hʌ̃], and /hʌ/ ending a word on a checked vowel). The Etymology names no source. P02 is flagged only.
- **BYE**: P13 ordinary. The plain etymology sentence is unchanged from v1. The run-together tree adds the chain «English goodinflu.English goodbyeclip.English bye».
- **OKAY**: every sense, Interjection:1 included, reads «Alternative spelling of OK.» The OK page wasn't fetched. Beyond that, only the stressed and unstressed pronunciations are new.
- **YES**: the source (Old English ġīese) and the DELOCUTIVE_VERB gloss «(colloquial, intransitive) To say “yes”.» P13 is ordinary.
- **NO**: P02, the source (Old English nā, nō, from *ne + *aiwō, under E2), and the gloss «To say “no”». P13 is ordinary.
- **THANKS**: a weak P02 (Shakespeare) and the source (Proto-Germanic nominative plural). P13 is ordinary.
- **SORRY**: a candidate P04 (complements), the adjective's etymology, and the sarcastic /ˌsɒˈɹiːː/ (not coded). P02 is flagged only.
- **HELLO**: the Old English source (ēalā, hēlā). P13 is ordinary.
- **HEAVENS**: a clean P02. P13 is ordinary, and there's no Etymology block.
- **LAH**: P13 Y for final [h] ([lɑh˨]), and the full source, including Hokkien 啦 (--la).
- **HOWAREYOU**: nothing new. P13 is ordinary.
- **HABA**: skipped, as briefed; it's a confirmed negative.

### 3. Still unreadable, and v1 quotations that won't string-match v2

- **Unreadable:** SH and MMHM have no Pronunciation or Etymology, and their glosses send you to the shh and mhm pages, which weren't fetched. OKAY sends every sense to OK, which wasn't fetched. The second sentence of OUCH's Etymology is broken: «…from Pennsylvania. or "natural" exclamation…». HUH's Etymology names no source («Attested from circa 1600. Compare Dutch hè (“huh”).»). HABA has no page content.
- **v1 quotations that won't match v2 now that templates are restored:**
  - AHA: «Equivalent to ah + ha.» now reads «Equivalent to ah + ha!.»
  - LAH: «Pitch contour: <u>falling</u>» now reads «Pitch contour: falling [lɑ(ː)˦˨]» (W:lah:E2:Particle:6). The tone letters, for example «Pitch contour: low-mid [lɑ(ː)˨], mid-falling [lɑː˧˨]» (W:lah:E2:Particle:1), are now the readable evidence for v1's LEXICAL_TONE and INTONATION_SPECIFIED rows.
  - SORRY: «…stresses the final syllable, as .» now ends «as /ˌsɒˈɹiːː/.»
  - WOW: «borrowed from ;» now reads «borrowed from Scots wow;»
  - The stripped quotations in v1's ALAS, NO and THANKS etymology rows and in the YES and NO "To say ." rows are replaced by the rows above.
- **Year and source for v1's quotation rows:** YES «Are you busy? — Yes, I’m busy.» and HELLO «Hello. This is Marsha.» both sit under «2016, VOA Learning English (public domain)» (W:yes:E1:Particle:1; W:hello:E1:Interjection:2). HEAVENS's «“Heavens!” exclaimed Nina…» is from 1907 August, Robert W. Chambers, The Younger Set, page 359.
- **Locators:** v1's line numbers point into the old text file. v2 ids carry E<k> and should be used instead.