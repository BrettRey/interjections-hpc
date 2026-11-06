# Quirk et al. 1985: extraction report (partial, delivered on request)

Saved verbatim by the parent session (Claude Opus 5.5) from the subagent's SubagentHandback report. Model output, not a source; every quotation is checked by the parent against the page-marked source text before use.

---

Partial report on Quirk et al. (1985), delivered early as you asked. Every quotation below is copied from the OCR file `/private/tmp/claude-502/-Users-brettreynolds-projects-LLM-CLI-projects-papers-queue-english-interjections/5a0b28ba-2821-445d-9ca6-f1e7abe03419/scratchpad/sources/quirk1985-paged.txt`, OCR errors included. The two columns of each spread share a physical line in that file, so a quotation that runs over more than one line is split with "...", and each piece is a contiguous substring of one line (the format `check_quotes.py` accepts). Each PDF page holds a two-page spread: the left column is the even printed page and the right column the odd one. I give PDF page and file line so the rows can be checked; `check_quotes.py` has no Quirk entry and the offset isn't constant, so the parent needs a per-row mapping. No responsibility notice is needed.

## 1. Table

Columns: item_id or CLASS | property | value | scope | "quotation" | printed page (§; PDF page; file lines) | note

**Interjections and formulae (§§11.53–11.55)**

- **CLASS:interjection** | P03 INTEGRATED | N | class
  - "Interjections are purely emotive words which do not enter into syntactic...relations. Some of them have phonological features which lie outside the"
  - p. 853 (§11.55; PDF 433; ll. 29394–95)
  - Members listed: Ah, Aha, Ahem, Boo, Eh, Hey, Mm, Oh, Oho, Ooh, Oops, Ouch, Ow, Pooh, Sh, Tut-tut, Ugh, Uh-huh, Uh-uh, Wow. Note [a] adds Yippee, Psst and Alas (archaic). Meaning ("purely emotive") is tied here to the form statement.
- **CLASS:interjection** | P04 DEPENDENTS | N | class
  - Same quotation, p. 853, §11.55
  - "do not enter into syntactic relations" covers dependents.
- **CLASS:interjection** | P13 PHONO_ANOM | Y | class
  - "regular system of the language. Whew, for instance, contains a bilabial"
  - p. 853 (§11.55; l. 29397)
- **TUTTUT** | P13 PHONO_ANOM | Y | item
  - "consists of a series of alveolar clicks"
  - p. 853 (§11.55; l. 29398)
  - The OCR prints the form as "rut-rut". Note [c] gives a spelling pronunciation "often with an...ironic tone". That is a permitted variant and doesn't overturn the Y.
- **SH, UGH** | P13 | U | item
  - "Sh [J]" and "Ugh [m]"
  - p. 853 (§11.55; ll. 29410, 29412)
  - The phonetic symbols are garbled and there is no explicit statement.
- **CLASS:interjection** | prosody (lengthening / wide pitch range) | Y | class
  - "many interjections may be associated with...nonsystematic features such as extra lengthening and wide pitch range."
  - p. 853 (§11.55; ll. 29401–02)
  - This is not P12S or P12I. It's a candidate prosodic form property.
- **OH, AH** | P02 SUPPLEMENT (and position: clause-initial) | Y | item
  - "Interjections are sometimes used to initiate utterances: Oh, what a nuisance;"
  - p. 853 (§11.55 Note [b]; l. 29418)
  - The OCR continues "Ah, that'spegfect."
- **CLASS:formula** | fixity of form | Y (little or no change) | class
  - "Most of the formulae allow for little or no change in their form."
  - p. 853 (§11.54 Note; l. 29382)
  - The starred examples given are for *How do you do* (*How did you do?), not *How are you*.
- **CLASS:formula** | P01 STANDALONE | Y (weak) | class
  - "Most formulae used for stereotyped communication situations are grammat...ically irregular."
  - p. 852 (§11.54; ll. 29392–93)
  - The formulae appear under the "Nonsentences" heading. All items below are listings without context sentences, so the parent may want to downgrade to U.
- **CLASS:expletive (formula)** | P01 | Y (weak) | class
  - "EXPLETIVES (familiar; likewise graded in order of increasing strength): My"
  - p. 852 (§11.54; l. 29430)
  - Members, in order: My Gosh, (By) Golly, (Good) Heavens, Doggone (it), Darn (it), Heck, Blast (it), Good Lord, (Good) God, Christ Almighty, Oh hell, Damn (it), Bugger (it), Shit, Fuck (it).
- **DAMN_REACT** | P01 | Y (weak) | item
  - "hell, Damn (it), Bugger (it) (esp BrE), Shit, Fuck (it)"
  - p. 852 (§11.54; l. 29434)
  - Bare *Damn* is this row. *Damn it* is closer to DAMN_NP.
- **HEAVENS** | P01 Y (weak); P04 Y | item
  - "Gosh, (By) Golly, (Good) Heavens, Doggone (it) (AmE), Darn (it),"
  - p. 852 (§11.54; l. 29431)
  - P04 rests on the optional modifier *Good*.
- **DAMN_NP** | P04 DEPENDENTS; P01 | Y | item
  - "Blast you (BrE), Damn you, Go to hell, Bugger off (BrE), Fuck off,"
  - p. 852 (§11.54; l. 29427)
  - Listed under "EXPRESSIONS OF ANGER OR DISMISSAL". *Damn you* takes an object.
- **CLASS:imprecation** | no negative form / no indefinite object | N | class
  - "Some imprecations are imperative in form, but they do not have the structural potentialities...of imperatives. For instance, there are no negative forms *Don't blast you, 'Don't bugger it, and...an indefinite object, such as some students, is not possible: *Blast some students!"
  - p. 853 (§11.54 Note; ll. 29388–90)
  - It says "Some imprecations", and the starred examples are for *blast* and *bugger*. Don't transfer the N to DAMN_NP without further warrant. It does supply a contrast with STOP (an ordinary imperative), but Quirk is silent on STOP.
- **YES, OKAY** | P01 | Y (weak) | item
  - "(a) assent, agreement: Yes, Yeah /jet; All right, OK (informal)"
  - p. 852 (§11.54 "REACTION SIGNALS"; l. 29405)
- **NO** | P01 | Y (weak) | item
  - "(b) denial, disagreement: No, Certainly not, Definitely not, Not at all,"
  - p. 852 (§11.54; l. 29407)
- **HELLO** | P01 | Y (weak) | item
  - "Hello; Hi (familiar)"
  - p. 852 (§11.54; l. 29398)
- **BYE** | P01 | Y (weak) | item
  - "Cheerio (BrE, familiar), See you (familiar), Bye(-bye) (familiar), So"
  - p. 852 (§11.54; l. 29400)
  - *Bye-bye* is a reduplicated variant.
- **THANKS** | P04 Y; P06 Y (determiner); P01 Y (weak) | item
  - "THANKS: Thank you (very much), Thanks (very much), Many thanks, Ta"
  - p. 852 (§11.54; l. 29409)
  - P04 rests on *Thanks (very much)*; P06 on *Many thanks*, a quantifying determinative with the plural.
- **SORRY** | P01 (weak) | Y | item
  - "APOLOGIES: (I'p) sorry, (I beg your) pardon (formal), My mistake"
  - p. 852 (§11.54; l. 29419)
  - "(I'p)" is OCR for "(I'm)". The bracketed *I'm* may indicate integrated use; I can't tell whether that's the same use.
- **HOWAREYOU** | P01 (weak) | Y | item
  - "INTRODUCTIONS: HOWdo you do? (formal), How are you?, Glad to meet"
  - p. 852 (§11.54; l. 29402)
- **YES, NO, OKAY** | P10A / P10S, pattern unspecified | Y | item
  - "expressions likeyes, no, ~vell,OK, allright are often repeated foremphasis"
  - p. 982 (§13.102 Note [b]; PDF 498; l. 33734)
  - This is very likely the "pattern-unspecified Quirk proposition" the audit refers to. It sits in a section on asyndetic repetition of identical items and cross-refers to §18.58, but it doesn't state a pattern.

**YOU_BASTARD and BASTARD_SUPP**

- **CLASS:exclamatory NP with *you*** (for YOU_BASTARD) | P01 Y; *you*-prefix | class
  - "If the phrase is directed at the person addressed, it may be prebced by...You idiot!"
  - p. 850 (§11.53(iv); PDF 432; ll. 29335–36)
  - Members: You angel!, You poor thing!, You idiot!
- **CLASS:exclamatory NP** | P06 (determiner) | articles often omitted | class
  - "Notice that articles are often omitted."
  - p. 850 (§11.53(iv); l. 29334)
- **CLASS:vocative epithet** (for YOU_BASTARD / BASTARD_SUPP) | *you*-prefix | Y | class
  - "(ii) unfavourable (also preceded by you in noun phrases); bastard,"
  - p. 774 (§10.53; PDF 394; l. 26789)
  - This is vocative function. I can't tell whether it is the same use as YOU_BASTARD.
- **CLASS:vocative epithet** | P04 | Y | class
  - "(d) my very dearest; my oldfriend; you silly bastard; youfilthy liar"
  - p. 774 (§10.53(h); l. 26816)
- **CLASS:vocative** | P06 | no determiner required | class
  - "same nouns in other functions in that they do not require a determiner."
  - p. 775 (§10.53; l. 26812)
- **CLASS:vocative epithet** | P08 STANCE | Y | class
  - "and bastard may also convey the...speaker's admiration for the addressee's ingenuity."
  - p. 775 (§10.53; ll. 26780–81)
- **CLASS:tag exclamation** (for BASTARD_SUPP) | P02 | Y | class
  - "be called 'tag exclamations', such as"
  - p. 1417 (§18.59 Note [a]; PDF 716; l. 48968)
  - The legible member is "the idiot" (the OCR has "the iclirrr"). It cross-refers to §17.68 Note [b], which I didn't read.
- **CLASS:tag exclamation** | clause edges (final or initial) | Y | class
  - "The exclamatory tag is furtller distinguished by being capable of (i) referring hack to a noun...and (ii) occurring initi;~llyas wcll ;ISlin;rlly:...Tllc idiot, he ran ;~w;!yfro111school."
  - p. 1418 (§18.59 Note [a]; PDF 717; ll. 48983, 48990, 48993)
  - Badly garbled OCR.
- **CLASS:tag exclamation** | P12I PROSODY_INTEGRATED | Y (garbled) | class
  - "preceding nucleus, instead of having llleir own (usually rising) nucleus."
  - p. 1417 (§18.59 Note [a]; l. 48973)
  - My reading: vocatives and tag exclamations "may form the 'tail' of a preceding nucleus". The "tail" wording itself is unquotable OCR. This conflicts with CGEL's own-intonation-unit claim for BASTARD_SUPP.

**THE_HELL_WH and EXACTLY_WH**

- **THE_HELL_WH** | P03 (postmodifier); host restricted to interrogative wh-words | Y | item
  - "In familiar style, the wh-words as interrogatives (cf 11.14 Note [a]) can be...postmodified by certain set prepositional phrases, eg:...(in) the hell (familiar)"
  - p. 451 (§7.64; PDF 232; ll. 15940–52)
  - The section number isn't legible in the OCR. I inferred §7.64 from the index entry "ever (intensifier) ... 7.64". Hosts listed: who, what, where. Also listed: on earth, (in) the heck.
- **THE_HELL_WH** | form variant (with or without *in*) | note | item
  - "Omission of the preposition in the last two examples is preferred by some...and obligatory for others."
  - p. 451 (§7.64; ll. 15954–55)
- **THE_HELL_WH** | after a wh-word | Y | item
  - "Various other ways exist of intensifying the emotive effect of a wh-question:...Who the hell are you? (casual)"
  - p. 817 (§11.14 Note [b]; PDF 415; ll. 28261–63)
  - This is §11.14, not §11.21 as the task guessed.
- **CLASS:wh-intensifier** (*ever*) | host restriction | Y | class
  - "Ever can be an intensifier. It normally occurs as a separate word and only...with interrogative wh-words, for example:"
  - p. 451 (§7.64; ll. 15956–58)
  - §11.14 Note [b] gives the same for *ever*, adding: "which emphasizes the bafllement or emotional involvement of the speaker" (l. 28256).
- **THE_HELL_WH** | grouped with emphasizer asseveratives | note | item
  - "Cf also the following, all very informal :...Why on earth did you alter the"
  - p. 585 (§8.100; PDF 299; ll. 20446, 20463)
  - The table lists the hell, the blazes, on earth, in heaven, in (the) hell, for pity's/goodness' sake, attached to who/what/why/how. On p. 584 (l. 20508): "with Group (a) that we should associate the asseveratives of very informal".
- **EXACTLY_WH** | after a wh-word; also before one | Y | item
  - "Exactly commonly focuses on lvh-items, and preciselydoes so too, but less commonly; this can...<What) exactiy gdo you mean)?"
  - p. 608 (§8.116ff, focusing-subjunct note [b], exact § not read; PDF 311; ll. 21331, 21334)
  - Also "Exactly <who) is asking for me?" (l. 21333).
- **EXACTLY_WH** | P04 (focused by *just*) | Y (weak) | item
  - "Just can also focus on exactly and precisely:"
  - p. 608 (l. 21341)
  - Example: "Just (exactly) what do you expect?"

**Emphasizer adverbs (§§8.102–8.103)**

- **CLASS:emphasizer (adverb)** | no premodification by however/how/so | N | class
  - "the focus of clause comparison or be premodified by however, how, or so."
  - p. 586 (§8.102; PDF 300; l. 20587)
  - Members (§8.100): actually, certainly, clearly, definitely, indeed, obviously, plainly, really, surely, for certain, for sure, of course; frankly, honestly, literally, simply, fairly, just. No bearer is listed.
- **CLASS:emphasizer (adverb)** | P04 | N (with exception) | class
  - "The emphasizers either cannot be modified or are unlikely to be modified;"
  - p. 588 (§8.103; PDF 301; l. 20611)
  - The exception given is *definitely*.

**Intensifying, emotive and other attributive-only adjectives (§§7.31–7.45)**

- **CLASS:emphasizer (adjective)** | may occur predicatively | N | class
  - "have a general heightening effect and are generally...attributive only, eg:"
  - p. 429 (§7.33; PDF 221; ll. 15070–71)
  - Starred examples on p. 430: "*The fabrication ispure." (l. 15154) and "*The h'ero is real." (l. 15163). Members: true, clear, pure, real, certain, definite, plain, simple, outright, sheer, sure.
- **CLASS:amplifier (noninherent)** | may occur predicatively | N | class
  - "On the other hand, when they are noninherent, amplifiers are attributive...*The fool is complete."
  - p. 429 (§7.33; ll. 15089–91)
  - Also "*The nonsense was total." (p. 430, l. 15107).
- **CLASS:emotive adjectives** | may occur predicatively | N | class
  - "A few adjectives with strongly emotive value which will not be further discussed are restricted...to attributive position, though the scope of the adjective clearly extends to the person referred to...by the noun,eg: youpoorman, my dearlady, that lvretchedwonzan.These all involve nonrestrictive"
  - p. 429 (§7.32 Note; ll. 15056–59)
  - Members: poor, dear, wretched. Quirk doesn't list damn, bloody or fucking here.
- **CLASS:intensifying adjective (attributive-only)** | restriction to particular hosts | Y | class
  - "adjectives which can be used as intensifiersand are restricted to attributive position have...severe restrictionson the nouns they modify."
  - p. 430 (§7.34 Note; ll. 15170–71)
  - Examples: a great/big baby, a big fool.
- **CLASS:intensifying adjective** | gradable (comparison or grading) | N | class
  - "Here, after the determinatives, is where peripheral, nongradable adjectives...are placed, in particular the intensifying adjectives (emphasizers, amplifiers,"
  - p. 437 (§7.45; PDF 225; ll. 15362–63)
  - Members: certain, definite, sheer, complete, slight.
- **CLASS:adverb-related noninherent** (for PROBABLE_PRENOM) | may occur predicatively | N | class
  - "Some noninherent adjectives that are attributive only can be related to...apossible friend...['possibly a friend']"
  - p. 431 (§7.36; PDF 222; ll. 15137, 15150, 15153)
  - *probable* itself wasn't found. *possible* is the nearest member. Others: former, old, past, present, occasional.

**Controls (VERY_INTENS, MAIN_PRENOM, BLACK, QUICKLY)**

- **MAIN_PRENOM** | P03 | Y | item
  - "Some restrictive adjectives can be related to restrictive adverbs (cf 8.1 18):...It is the main reason."
  - p. 431 (§7.35; ll. 15111, 15116)
  - Quirk places it under the "Attributive only" heading, but I didn't find a starred predicative for *main*. Predicative status is U.
- **VERY_INTENS** | P03 | Y | item
  - "Gradability is also manifested through modification by intensifiers, ie adverbs...which convey the degree of intensity of the adjective:"
  - p. 435 (§7.42; PDF 224; ll. 15287–88)
- **VERY_INTENS** | P10A, P10S (adjacent repetition) | Y | item
  - "Some intensifiers can be repeated for emphasis:...very very good ['extremely good']"
  - p. 473 (§7.89; PDF 243; ll. 16757–59)
- **VERY_INTENS** | P10A (syndetic repetition) | N | item
  - "Repetition of intensifiers is a type of coordination that is always asyndetic...(cf 13.102) : *very and very good."
  - p. 473 (§7.89; ll. 16778–79)
  - Also "*very much much" (l. 16776).
- **CLASS:attributive adjectives + degree intensifiers** | P10S (adjacent, asyndetic) | Y | class
  - "Somewhat similar to these last examples is the intensifying effect of repetition...of attributive adjectives and of degree istensifiers:...very, very, very good [= 'extremely good']"
  - p. 981 (§13.102; PDF 497; ll. 33695–99)
  - Also "an old, old man".
- **BLACK** | P03 | Y | item
  - "Gradable adjectives are either inherent, as in a blackcoat, or noninherent, as"
  - p. 436 (§7.44; PDF 225; l. 15367)
- **QUICKLY** | P04 | Y | item
  - "A: How quickly does he do"
  - p. 471 (§7.88; PDF 242; l. 16689)

**Expressive degree and attributive uses, expletive placement, tmesis**

- **DAMN_DEGREE** | P03 | Y | item
  - "They damn near killed themselves in that accident."
  - p. 601 (§8.112; PDF 307; l. 21029)
  - *damn* modifies the approximator *near*; Quirk labels it "more widespread informal use".
- **DAMN_PRENOM?** | P03 | Y (can't tell which use) | item
  - "Other intensifiers (and intensifying noun phrases) that are common with...a damn sight...better (very familiar)"
  - p. 473 (§7.89; ll. 16727, 16754)
  - This is the only prenominal *damn* I found. It's an idiom, and the NP modifies a comparative.
- **BLOODY_INTENS** | P03 | Y | item
  - "His lwork is'bloody iwl'ull"
  - p. 1418 (§18.59 Note [b]; l. 49005)
  - OCR for "His work is 'bloody 'awful". The stress mark falls on *bloody*.
- **CLASS:expletive (in a clause)** | placed just before the point of main emphasis | Y | class
  - "Compare tniesis (App 1.76 Note [c]) where the inserted amplific;~tionis usui~llymadc just prior...to the point of main emphasis:"
  - p. 1418 (§18.59 Note [b]; ll. 49007–10)
  - The OCR has lost the opening of Note [b], which presumably states the clause-level generalization. The legible examples are silly, darned (prenominal), bloody and darned well.
- **CLASS:expletive** | position doesn't match scope | note | class
  - "it is not of course thc final noun phrase as such that calls for...expletive comment. The whole utterance is emotion;~llycoloured, and in extreme cases such"
  - p. 1418 (§18.59 Note [b]; ll. 49012–13)
  - The example is "She lost her darned way", with *darned*, not *damned*.
- **CLASS:expletive** | P10A, distributed recurrence of different expletives | Y | class
  - "colouring (especially in exasperation) is expressed at addition;ll points in the sentence structure:"
  - p. 1418 (§18.59 Note [b]; l. 49014)
  - The garbled example reads as "These blasted people have darned well lost their stupid way!" These are different words, not one form repeated.
- **CLASS:expletive** | prosody as an alternative to the word | note | class
  - "Alternatively the 'scope' of the colouring as well as the colouring itself can be expressed by"
  - p. 1418 (l. 49016)
- **BLOODY_INFIX** | inserted inside a word | Y | item
  - "[c] It is a kind of blending that produces (especially in BrE) the very informal and usually...scatological 'tmesis' or use of infixes in"
  - p. 1584 (App I.76 Note [c]; PDF 800; ll. 55087–89)
  - The example forms are illegible (",obso,bloo,ly'..."; "...,ruddy'migl~ly").
- **BLOODY_INFIX** | stress: placed immediately before the most emphasized syllable | Y | item
  - "the indicated stressing shows, there is a common essential prosodic pattern such that the infixed...intensifier comes immediately before the most emphasized syllable"
  - p. 1584 (App I.76 Note [c]; ll. 55093–94)
  - Cross-refers to 18.59 Note [b].
- **CLASS:emotive emphasis** | class membership | note | class
  - "provides means of giving a unit purely emotive emphasis....interjections (cf 11.55), expletives and intensifiers (cf7.87fl; 8.104ff1,"
  - p. 1414 (§18.55; PDF 715; ll. 48906, 48910)
  - The page is inferred: PDF 715's running head isn't legible, and PDF 716 is pp. 1416/1417.

## 2. Form properties holding of two or more expressive uses

- **Placed immediately before the point of main emphasis.** This holds of BLOODY_INFIX explicitly (App I.76 Note [c]). Through the comparison in §18.59 Note [b], it also holds of BLOODY_INTENS (*bloody awful*) and of the expletives *darned* and *darned well*. DAMN_PRENOM is supported only through *darned*. The clause-level generalization itself is lost in the OCR. For interjections Quirk gives different prosody (extra lengthening, wide pitch range). For the controls Quirk says nothing; I didn't check whether *very* is positioned the same way.
- **Position doesn't match scope, and expletives recur at several points in one utterance** (§18.59 Note [b]). This is stated for expletives as a class. Bearers are covered only through BLOODY_INTENS and the *darned* examples. Quirk says nothing about it for the interjections or the controls.
- **Attributive only, nongradable, restricted to particular nouns** (§§7.32 Note, 7.33, 7.34 Note, 7.45). Quirk states these for emphasizer adjectives, noninherent amplifiers, and the emotive adjectives *poor*, *dear*, *wretched*. It doesn't place *damn*, *bloody* or *fucking* in any of these classes, so DAMN_PRENOM, BLOODY_PRENOM and FUCKING_PRENOM inherit nothing without an extra assumption. The controls also fall into attributive-only classes: *possible* is explicitly attributive-only (§7.36), and *main* is placed under the same heading.
- **Exclamatory or vocative NP preceded by *you*** (§11.53(iv), §10.53). This holds of YOU_BASTARD, and of *bastard* listed as a vocative epithet. It doesn't apply to the interjections or controls.
- **Clause edges.** Tag exclamations occur finally or initially (BASTARD_SUPP, by class), and interjections "initiate utterances" (OH, AH). Only one expr-core bearer (BASTARD_SUPP) is covered; nothing is said about the controls.
- **After a wh-word** (§§7.64, 11.14 Note [b], 8.100). Among the bearers this holds only of THE_HELL_WH. The control EXACTLY_WH has the same property (§8.116ff Note [b]).

## 3. Warnings against using a property as a diagnostic

- **After a wh-word doesn't separate THE_HELL_WH from EXACTLY_WH.** Quirk shows *What exactly do you mean?* The one difference shown is that *exactly* can also precede the wh-word (*Exactly who is asking for me?*). Quirk never says *the hell* can't precede, so that is silence, not N.
- **Repetition for emphasis holds of the control *very*** (§7.89, §13.102: *very very good* glossed 'extremely good'), and of *yes*, *no*, *OK*. Repetition strengthening isn't expressive-specific in Quirk.
- **Attributive-only is shared by restrictive and adverb-related adjectives** (*main*, *possible*). §7.31 also warns: "restrictions are not always absolute, and sometimes vary with individual" (p. 428, l. 15076).
- **Quirk assigns *the hell* to two classes.** §7.64 treats it as a PP postmodifying the wh-word; §8.100 groups it with emphasizer asseveratives. The emphasizer properties in §§8.102–8.103 (no modification) shouldn't be transferred to it.
- **The §18.59 Note [b] examples use *darned*, not *damned*.** Prenominal *damn* is attested only in the idiom *a damn sight*.
- **The imprecation N** (no negative form, no indefinite object) is for "Some imprecations", with *blast* and *bugger* as the starred examples, not *damn*.
- **OCR damage** is severe in §§18.55–18.59 and in the App I.76 examples. The opening of §18.59 Note [b] is missing entirely.
- **Citation discrepancy.** `items-v4.csv` (BLOODY_INFIX) cites "App. I.75" for tmesis. Quirk's own cross-reference ("App 1.76 Note [c]", l. 49007) and the section layout put it at App I.76 Note [c], p. 1584.
- **Section guesses in the task.** Interjections are §11.55 (the expletive list is in §11.54, Formulae), and the wh-intensifiers are at §11.14 Note [b], not §11.21.

## 4. Searches, and what I didn't reach

**Search strings (Grep on the Quirk file):**
- `expletive`
- `\b(damn|damned|bloody|fucking|bastard|bugger)\b`
- `on earth|the hell|the devil|in God's name|the heck|the blazes|ever\b.*wh` (noisy)
- `on earth|the hell\b|the devil|God's name|the heck|the blazes|ever \(|whoever|-ever`
- `tmesis|infix|reduplicat|repetition`
- `^\s*8\.10[4-9]|^\s*8\.11[0-6]|boosters|maximizers|amplifiers|downtoners`
- `\bprobable\b|\bmain (reason|objection|point)|...`
- `^\s*8\.21\b|^\s*8\.20\b|^\s*8\.22\b|darned|darn\b|jolly|awfully|terribly`
- `^\s*7\.8[7-9]\b|...`
- `^\s*I?1\.7[56]\b|Blends`

**No hits:**
- *fucking*: no hits for the participial form; only *Fuck off*, *Fuck you*, *Fuck (it)*.
- *the devil* in wh-questions: none; *the devil* occurs only in "The devil take you. (archaic)", l. 28994.
- *probable* as an attributive adjective: none.
- *bloody*: no other occurrences beyond l. 49005 and the tmesis passage.

**Found but not read:**
- l. 11349 "She's an absolute bastard, this truck." (context and page unknown)
- l. 27255 "I don't care a damn whether we win or lose. (familiar)"
- l. 37462 "damned ... apologize" (garbled)
- l. 9394 "What on earth are you doing?"
- l. 16101 "the main reason - The reason was mainly that"
- §8.21 (l. 17555, "Such preparation for focus may be expletive"; the index lists expletive at 8.21)
- §17.68 Note [b] (tag exclamations)
- the index's other expletive references (18.13?)

**Sections not reached:**
- §§7.56ff (adverbs premodifying adjectives: *awfully*, *terribly*, ll. 15703–15805)
- §§8.104–8.111 body (amplifier and booster lists; my grep found no *damn* or *bloody* there)
- Table 7.44
- §18.58 beyond its first lines

**Not searched individually:** gee, wow and the other interjection forms (covered only through the §11.55 list), "epithet", "stress"/"nucleus" in general, STOP, COFFEE.