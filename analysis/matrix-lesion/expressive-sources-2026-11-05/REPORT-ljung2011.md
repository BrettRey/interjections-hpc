# Extraction report: Ljung 2011 (partial, delivered on request after the agent's turn limit)

Saved verbatim by the parent session (Claude Opus 5.5) from the subagent's SubagentHandback report. Model output, not a source; every quotation is checked by the parent against the page-marked source text before use.

---

Ljung 2011 extraction report for *Swearing: A Cross-Cultural Linguistic Study* (Palgrave Macmillan, 2011)

Source file: /private/tmp/claude-502/-Users-brettreynolds-projects-LLM-CLI-projects-papers-queue-english-interjections/5a0b28ba-2821-445d-9ca6-f1e7abe03419/scratchpad/sources/ljung2011-paged.txt. The page offset (printed = PDF − 13) matches the running heads throughout, e.g. "=== PDF page 35 ===" is headed "22 Swearing". This is a partial report, delivered on request. All the assigned sections were read; the gaps are listed in section 4.

**How to read the quotations.** Line breaks are joined with one space. I avoided quotations that cross a hyphenated line break; where a sentence needed one, I cut the quotation before the break and say so in the note. The source's curly apostrophes and quote marks (’ ‘) and its en-dashes (–) are kept as they appear.

**One flag on the item file (not a responsibility notice).** In items-v4.csv, BASTARD_SUPP's rationale cites "Ljung 2011 p. 34 (epithets)". Page 34 describes the *anaphoric* epithet ("Tell the bastard/motherfucker to mind his own business!"), where the epithet sits in an argument position. That is a different use. Ljung's nearest match to the supplementary epithet is the third-party exclamation on pp. 127–128, and even there his example is a separate response turn, not a supplement to a host clause (row 50).

## 1. Table

item_id | property | value | scope | "quotation" | printed page | note
---|---|---|---|---|---|---
DAMN_REACT | P01 STANDALONE | Y | item | "it may take the form of interjections like English Damn!" | 54 | Also p. 74 ("exclamations like Fuck!, Shit! Damn!, Bugger!, Bloody hell!, Fucking hell!") and p. 83 ("developed into a formula exactly parallel to single-word interjections like Damn!, Fuck! and Shit!")
DAMN_REACT | P02 SUPPLEMENT | Y | item | "in supplements like . . . Damn, we’ve missed the bus again . . . are best regarded as having been reanalysed as interjections." | 77 | Secondary: Ljung is quoting Huddleston & Pullum 2002: 1361
DAMN_REACT | P01 (corpus count) | Y | item | "REACT: Reactive interjection, GF: gap filler, BC: before clause" | 94 | Table 4.5, Damn row: REACT 0, GF 1 (25%), BC 2 (50%), BW 1 (25%), total 4. A gap filler is a complete turn. Note 4 (p. 171, "DAMN: Damn it 2, Damn 2 = 4") shows half the tokens are *Damn it*, so the DAMN_REACT/DAMN_NP split is unknown. Zero reactive tokens. Ljung warns that low-N rows are "rather uninteresting" (p. 93)
DAMN_REACT | P02 (corpus count) | Y | item | "the most common position is before a clause over which they have scope." | 87 | Table 4.5 gives Damn 2 "before clause" slot-filler tokens. This is the supplement-like position. The same *Damn it* caveat applies
DAMN_REACT | NEW:COMBINES | Y (2 of 4) | item | "DAMN: Damn it 2, Damn 2 = 4" | 171 | Table 4.3 (p. 81): Damn single 2 (50%), combined 2 (50%). The combinations are all *Damn it*
DAMN_REACT; DAMN_NP | NEW:INTERCHANGEABLE | Y | item | "despite the clearly different literal meanings of fuck, damn and sod, these words are freely" | 13 | The sentence continues across a hyphen break: "...interchangeable in curses like Fuck you!, Damn you! and Sod you! and in interjections like Fuck!, Damn! and Sod it!"
DAMN_REACT or DAMN_NP | P01 | Y | item | "All that has happened is that Oh damn it! has changed roles." | 91 | (25) *Oh damn it.* starts as a reactive interjection and becomes the first turn once the hearer replies *What?*. The form *damn it* can't be assigned to one use
CLASS:expletive interjections | P08 STANCE | Y | class | "exclamations of irritation, pain or surprise containing expletives" | 74 | Members named include Damn! (DAMN_REACT), Fuck!, Shit!, Bugger!, Bloody hell!, God!, Gosh!, Crikey!
CLASS:interjections (swearing) | P08 | Y | class | "Interjections generally express surprise, pain, fear, anger," | 22 | Continues "disappointment and even joy". Members: God!, Shit!, Fuck!, Damn!, Hell!, Bloody hell!
CLASS:reactive expletive interjections | P07 NONPROP | Y | class | "reactive interjections do not have meanings in the established sense of the term." | 86 | Examples: Oh my god, Shit!, Oh bloody hell! Damn has no reactive tokens in Table 4.5
CLASS:pragmatic (non-reactive) expletive interjections | P07 | Y | class | "they have little or no propositional meaning" | 87 | Ljung applies Brinton's (1996) pragmatic-marker criteria. Per Table 4.5, all 4 Damn tokens are in this class
CLASS:pragmatic expletive interjections | P02 | Y | class | "It appears that the non-reactive expletive interjections meet all of these criteria" | 86 | One of those criteria is Brinton's (6): "occur either outside the syntactic structure or are attached to it". The usual position is before a clause (p. 87). Examples: Cor that was a proper macho man!; bloody hell look at that old codger
CLASS:interjections (Huddleston & Pullum, quoted) | P03 INTEGRATED | N | class | "do not combine with other words in integrated syntactic constructions, and have expressive rather than propositional meaning" | 77 | Secondary source. Also supports P07 Y. Central members named: ah, hey, oops, ouch, sh, wow
CLASS:interjections (Huddleston & Pullum, quoted) | P01; P02 | Y | class | "used as expressive exclamations, on their own, or as supplements with clausal anchors" | 77 | Secondary source. Members as in the row above
CLASS:interjections (Carter & McCarthy, quoted) | P08 | Y | class | "positive or negative emotional reactions to what is being or has just been said or to something in the situation" | 78 | Secondary (Carter & McCarthy 2006: 224). Members named include damn, heavens, ouch, ugh, wow. **This is the only mention of HEAVENS in the book**
SH; UGH; TUTTUT | P13 PHONO_ANOM | Y | item | "deviant forms some of which exhibit peculiarities in the relation between spelling and pronunciation, for instance tsktsk, tut-tut, sh and ugh" | 76 | Ljung reporting Quirk et al. 1985 §2.58 Note ("quasi-linguistic noises"). No phonetic forms are given. For TUTTUT, the brief excludes the spelling pronunciation
AH; AHA; OH; OUCH; WOW | P13 | N | item | "forms like Ah!, Aha!, Mm!, Oh!, Ouch! and Wow!" | 77 | Preceded on p. 76 by "the class as such also includes phonologically regular". Reported from Quirk et al. No forms are transcribed, so this may fall short of P13's "given in full" negative standard
GEE | NEW:HOMONYM | N | item | "the examples Crikey!, gee! and gosh! have no homonyms" | 79 | Gehweiler 2008 as reported. Figure 4.1 (p. 80) puts Gee! among the primary (−homonym) "moderated expletives". p. 78: gee evolved via Jesus!
GEE | P03 | N | item | "Outside of the interjectional context, God and Jesus may never be replaced by Gosh and Gee" | 11 | Starred example: *Gee died on the cross. This shows gee has no argument (noun) use. It doesn't restrict the interjection use itself
CLASS:WH-emphasizers (the hell, the heck, the devil, the fuck) | NEW:POST_WH_SLOT | Y | class | "are used as pure emphasizers after interrogative WH-words" | 22 | THE_HELL_WH is a member. "Pure emphasizers": no named feeling is assigned, so no P08 claim
THE_HELL_WH | NEW:INTERCHANGEABLE | Y | item | "The function of hell in who the hell is clearly just emphatic and the word can be replaced with the Devil, the fuck, etc." | 16 | Who the hell... counts as swearing (no literal or metaphorical meaning left)
THE_HELL_WH | NEW:WH_SLOT_SUBSTITUTION | Y | item | "In such constructions the taboo words may be replaced by the prepositional phrases like on earth, in the whole world, in God’s name, in the name of God" | 12 | The non-taboo substitutes are PPs. *exactly* is never mentioned
THE_HELL_WH | P03 | Y | item | "Where the fuck/the hell/the Devil/ did you put it?" | 12 | Exemplified inside the interrogative clause. Ljung calls it an emphasizer in the "emphatic slot", never a modifier
THE_HELL_WH | NEW:POST_WH_POSITION | Y | item | "placing certain swear words immediately after an interrogative pronoun or adverb" | 34 | Listed under the emphasis function of slot fillers
THE_HELL_WH; BLOODY_INFIX | NEW:SLOT_FILLER | Y | item | "involve placing a ‘swear word’ in the right slot in a given string, as for instance in What the hell do you mean? and absobloodylutely." | 30 | This is the basis for the class P01 N row below
CLASS:wh-the-X strings | NEW:FORMULAIC | Y | class | "resist semantic and syntactic analysis and have to be learnt as wholes." | 19 | The example is What the fuck do you mean?. Same page: "Anomalous syntax/usage is also common in swearing" (what/where/who the devil/fuck, absofuckinglutely, Henry the bloody Eighth)
BLOODY_INTENS; DAMN_DEGREE | NEW:DEGREE | Y | item | "A very common slot-filler function is that of intensifier expressing a high degree of the following adjective or adverb" | 33 | Examples on the same page: It's bloody marvellous; They drove damn fast. These are the glosses' own examples
BLOODY_INTENS | NEW:DEGREE | Y | item | "(1) as degree adverbs, for instance in bloody impressive, goddamn quickly" | 22 |
BLOODY_INTENS; DAMN_DEGREE | P03 | Y | item | "In (1) and (3) the degree adverbs damn and bloody indicate a high degree of the following adverbs well and quickly, and in (2) and (4) the same degree adverbs modify the adjectives sure and hard in the same way." | 147 | damn well, bloody quickly, damn sure, bloody hard work
BLOODY_INTENS; DAMN_DEGREE | NEW:AMPLIFIER | Y | item | "The adverbs considered here obviously belong to the first category, that is, they are amplifiers" | 148 | Quirk's amplifier/downtoner split
BLOODY_INTENS; DAMN_DEGREE | NEW:TABOO_LOAD | Y | item | "they function in the same way as very, highly or extremely, with the difference that these three words lack the taboo load" | 147 | Same function as *very*; taboo load is the only difference stated
VERY_INTENS | NEW:TABOO_LOAD | N | item | (same quotation) | 147 | Control
VERY_INTENS; BLOODY_INTENS | NEW:GRAMMATICALLY_REGULAR | Y | item | "From a grammatical point of view, there is no difference between the two examples above and examples like He’s so very lazy" | 19 | The two examples are He's so fucking/bloody/goddamned lazy and The fucking/bloody/goddamned postman hasn't been yet (vs The useless/no-good postman). Ljung exempts these uses from formulaicity
CLASS:intensifying uses of bloody, damn | P03; NEW:LOCAL_SCOPE | Y | class | "they are modifiers, viz. their scope is local, extending no further than the nearest element to the right." | 149 | Members: BLOODY_INTENS, DAMN_DEGREE, and the intensifying-adjective tokens of BLOODY_PRENOM/DAMN_PRENOM
CLASS:intensifying uses of bloody, damn | P07 | N (weak) | class | "they have clearly defined meanings" | 149 | My judgement call. Ljung assigns a high-degree meaning parallel to *very* and contrasts it with the hard-to-specify non-intensifying uses. He never says "truth-conditional". Code U if P07's N standard needs explicit descriptive content
DAMN_DEGREE | NEW:ADV_VS_ADJ_SPECIALIZATION | N | item | "as an intensifier of adverbs than of adjectives, while damn does not show similar tendencies towards specialization." | 173 | Ch. 7 note 5. The same note says degree *bloody* is "much less common" with adverbs, so BLOODY_INTENS = Y (prefers adjectives)
DAMN_DEGREE | P03 | Y | item | "intensifiers or adjectives of dislike as in English She is damn(ed) clever! and The damn(ed) car wouldn’t start!" | 54 | *damn(ed) clever* is DAMN_DEGREE
DAMN_PRENOM | P08 | Y | item | (same quotation) | 54 | *The damn(ed) car* is an "adjective of dislike"
damn(ed) [use not in the 46; nearest DAMN_DEGREE] | NEW:PRE_NONNP_EMPHASIS | N | item | "both bloody and fucking are found as emphasizers before all sorts of clause constituents. Note that it is impossible to use damn(ed) in such a way." | 151 | bloody and fucking = Y: I wish they'd all bloody leave me alone; You fucking stink; We're always fucking late. Parallels CGEL's *I damn hated it
DAMN_PRENOM; BLOODY_PRENOM | NEW:GRADABLE_NOUN_INTENSIFIER | Y | item | "A strong case can be made for including bloody, damn and their equivalents among the intensifying adjectives when they are used to indicate degree with regard to a following gradable noun" | 148 | Examples: Bye you damn fools; You bloody idiot!; a bloody nightmare; too much damn pain. p. 33 has It's a bloody miracle
DAMN_PRENOM; BLOODY_PRENOM | P08 | Y | item | "Obviously there is also an element of dislike however." | 148 | Said of the intensifying-adjective tokens
DAMN_PRENOM; BLOODY_PRENOM | P08 (Ljung's DISLIKE) | Y | item | "DISLIKE constructions in which bloody, damn, etc. serve to express the speaker’s dislike of the referent(s) of a following noun" | 149 | Examples: That damn Paul... (before a proper noun); (10) Damn heater!; that bloody pencil sharpener thing. *Damn heater!* is classed as adjective + noun, not as a curse. Ljung gives no criterion separating it from DAMN_NP
BLOODY_PRENOM | P08 | Y | item | "as adjectives of dislike as in I can’t stand that bloody cashier." | 22 |
CLASS:adjectives of dislike | P08 | Y | class | "Another slot-filler function for swear words is to indicate that the speaker dislikes the referent of the following noun." | 34 | bloody is the named member
BLOODY_PRENOM; FUCKING_PRENOM; DAMN_PRENOM | P08 | Y | item | "using alternately bloody, fucking, damned, goddamned, flipping to express negative attitude or simply emphasis" | 14 | Example: I can't open the damned/fucking/bloody... door. The form here is *damned*, not *damn*. "or simply emphasis" makes stance optional
BLOODY_PRENOM; FUCKING_PRENOM | P03 | Y | item | "the use of fucking, bloody, goddamned, etc. as intensifiers and as adjectival attributes" | 19 | Example: The fucking/bloody/goddamned postman hasn't been yet
BLOODY_PRENOM; DAMN_PRENOM; FUCKING_PRENOM | NEW:EMPHASIS (on a following NP) | Y | item | "There are also cases which undoubtedly express dislike on the part of the speaker, but whose main function seems to be to place emphasis on a certain noun" | 149 | Examples: in the bloody book; go to a damn doctor; (p. 150) the fucking underwear department; (p. 34) not a bloody bathtub
FUCKING_PRENOM | P08 | N (one token) | item | "In (14) there may be an additional element of dislike but not in (15)." | 150 | (15) is *in the fucking underwear department*. Ljung excludes dislike for this token only; the same page says emphasis plus dislike seems "to be the rule rather than the exception". Treat as mixed evidence
FUCKING_PRENOM | P08 | Y | item | "fucking which serves both as emphatic and/or derogatory adjective and as adverb of degree" | 40 |
BLOODY_PRENOM; DAMN_PRENOM | NEW:RETROACTIVE_EMPHASIS | Y | item | "By placing damn and bloody immediately after worst, every, 30 and no, the speaker emphasizes these elements, which are also no doubt pronounced with heavy stress." | 152 | Examples: the worst damn place; Every damn call; 30 damn years; no bloody money. The stress claim concerns the preceding word, so it isn't P12
BLOODY_PRENOM | NEW:BOOSTER | Y | item | "these words often occur in what looks like typical NP modifier positions and that when they are used in this position it is difficult to free oneself from the impulse to regard them as modifiers" | 151 | Example: It's not her bloody husband ≈ He's not her husband, for God's sake. This is a warning against reading P03 off position
BLOODY_PRENOM | NEW:CREATES_EPITHET_NP; P08 | Y | item | "the speaker actually creates a kind of epithet NP by including bloody before a normally non-epithet noun" | 127 | Example: You bloody/stupid teacher(s)!. bloody is grouped with *stupid* as "disparaging or negative adjectives"
BLOODY_PRENOM; DAMN_PRENOM | NEW:STRESS_CUE | Y | item | "Heavy stress on book and doctor would have supported the second interpretation." | 150 | Stress on the following noun would favour emphasis over dislike. Ljung couldn't check (no phonological annotation in BNC). Not P12
CLASS:expletive slot fillers (bloody, damn, damned, goddamn(ed), fucking) | P01 | N | class | "By definition, the expletive slot fillers are all used inside larger units." | 143 | Also "swear words that are not themselves independent utterances" (p. 143). Caution: ch. 4 also calls clause-initial interjections "slot fillers" (p. 87), and *Bloody fool!* / *Damn heater!* place these words inside standalone NPs
CLASS:expletive slot fillers | NEW:NONLITERAL | Y | class | "they are intended as swearing: their meanings are taboo, they are not used with their literal meanings" | 147 | bloody, damn(d), fucking. Under 1% of BNC *bloody* tokens are literal "blood-stained" (p. 144)
CLASS:slot fillers inside NPs and words | P08; P07 | Y | class | "the main – or perhaps even the only – function of the swearing expressions is to express the speaker’s attitudes and feelings." | 143 | Members: Henry the bloody Eighth, absofuckinglutely, kanga-bloodyroo (BLOODY_INFIX)
BLOODY_INFIX | NEW:INFIXATION; NEW:EMPHASIS | Y | item | "Emphasis may also take the form of infixation in a word as in Absobloodylutely, Infuckingcredible, Kangabloodyroo" | 34 | Phrase-level insertion also listed: Henry the fucking Eighth
CLASS:insertion emphasis | NEW:INSERTION | Y | class | "insertion of the expletive element into linguistic units normally considered to be impenetrable, viz. words and phrases" | 153 | Applies to "certain but not all" emphasizers. Examples mix phrase-level (into bloody perspective, at bloody home, Abu bleeding Dabi) and word-level (Unfuckingconscious). Table 7.2 (p. 155): bloody insertion 26/318, fucking 8/191; both levels counted together
infixed fucking (use not in the 46; bears on BLOODY_INFIX) | NEW:NO_WORD_CLASS | Y | item | "uses of fuck that can no longer be accounted for in terms of traditional word classes, as when it is used ‘intrusively’" | 40 | Said of fucking, not bloody
YOU_BASTARD | P01 | Y | item | "(10) You bastard/son of a bitch/dickhead!/Bastard!/Son of a bitch!" | 128 | Direct-address name-calling. Bare *Bastard!* is also given
CLASS:direct-address name-calling | P08 | Y | class | "exclamations with or without an initial You used to express the speaker’s negative attitude towards the addressee." | 126 | Members: traitor, idiot, snob, bastard, son of a bitch, dickhead
YOU_BASTARD | NEW:YOU_X_FRAME | Y | item | "By testing different nouns in such utterances we can conclude that the nouns traitor, idiot and snob, for example, are all epithets" | 126 | *You teacher! fails (p. 127); bastard passes (p. 128). Ljung's own epithet diagnostic
CLASS:name-calling nouns | P08 | Y | class | "The nouns used in these constructions are all evaluative: they are used to express the speaker’s – negative or positive – opinion of" | 33 |
CLASS:expletive epithets | P07; P08 | Y | class | "present-day uses/meanings of the words which are non-denotative and merely express the speaker’s negative opinion" | 129 | Table 6.3 members include bastard ("Contemptible person 16C+"; "Man, person, fellow 1910s UK")
CLASS:expletive epithets | NEW:THREE_NAMECALLING_FRAMES | Y | class | "it must have taboo meaning, it must have non-literal meaning which is not metaphorically linked to its literal meaning, and it must be able to appear in all three types of name-calling" | 33 | bastard qualifies (pp. 125, 128)
CLASS:name-calling | Potts nondisplaceability/immediacy | Y | class | "The standard insults, the unfriendly suggestions and name-calling express the speaker’s feelings towards the addressee at the moment of speech." | 114 | Contrasted with curses, which wish evil in the future. Ljung's wording, not Potts's terms
BASTARD_SUPP (nearest match) | P01; P08 | Y | item | "the exclamation The fool/idiot! must be a response to information provided by an interlocutor." | 127 | Example (11), p. 128: John refuses to pay for the meal. – The bastard/son of a bitch!. It is a separate response turn, so it gives **no P02 evidence**; the supplement use itself is never exemplified
DAMN_NP | NEW:OPTATIVE_VERB | Y | item | "where Damn, Fuck and Sod are examples of optative subjunctives of the same kind as live in Long live the Queen!" | 31 | Example: Damn you!. Ch. 5 note 3 (p. 172): "the ‘simple verb form’ lacks agreement with third person subjects and is in fact a subjunctive". Relevant to P05 opportunities; not an invariance claim
DAMN_NP | P04 DEPENDENTS; P01 | Y | item | "curses like Damn you!, Damn this place! with the basic meanings ‘May you/this place be damned!’" | 54 | p. 55: "the word God is understood"
DAMN_NP | P02 | Y | item | "(21) . . . they’re not doing a bad job, damn them. (BNC KGX 139)" | 108 | The curse follows a complete clause
CLASS:non-serious (expletive) curses | P08 | Y | class | "expressing the speaker’s dislike of something or somebody and meeting the requirements that neither God nor the Devil are used referentially" | 108 | Members: the devil take…, God damn America, damn them (DAMN_NP), Fucking fuck the pair of you!
DAMN_NP or DAMN_PRENOM | P04 | Y (ambiguous) | item | "(21) Damn paint and stuff, cor strewth. (KBR 531)" | 89 | Ljung: "exclaims Damn paint and stuff!" (pp. 89–90). Could be curse + NP, or dislike adjective + noun like *Damn heater!*. I can't tell which
CLASS:expletive expressions | Potts descriptive ineffability | Y (approx.) | class | "what we can do, more or less adequately, is to describe the range of ‘meanings’ that may be assigned to such" | 22 | p. 23: "even the speakers themselves may be uncertain about the exact nature of the feelings that triggered their use of swearing." Ljung's claim is that the particular feeling is underdetermined, which is not quite Potts's ineffability
CLASS:emotive language (swearing criterion 4) | Potts perspective dependence | Y (weak) | class | "aims a direct expression of the speaker’s attitude toward what he is speaking about" | 21 | Jakobson, quoted. The attitude is anchored to the speaker; Ljung never discusses any other perspective

**Searches with no statements found.**
- **EXACTLY_WH:** "exactly" returns 2 hits, both ordinary prose.
- **HEAVENS:** "heavens" returns 1 hit (p. 78, row above). *for heaven's sake* is a different item.
- **No statements for the 46 bearers** on P06, P09, P10S, P11N, P12, Potts independence or Potts repeatability, within what I read. I didn't grep "repeat" or "repetition".

**Uses of these forms that aren't among the 46:**
- **bastard, anaphoric:** "the bastard never told me" (p. 128); "Tell the bastard…" (p. 34, "In English this usage seems to be limited to persons"). This is P03 Y for that use.
- **bastard, predicative:** "You are a (real) bastard" (p. 128). P03 Y and P06 Y for that use.
- **bastard, noun support:** "a clever bastard" (p. 128): "In (14) the expletive epithets have lost their negative meaning and have become neutral words corresponding to fellow, chap, person, sort." That is P08 N for that use. Speakers hesitate to use bastard/bugger about women (p. 129).
- **bloody/fucking:** emphasizers before verbs, and modal adverbials (bloody well; "bloody don't think") (pp. 34, 151–152).
- **Bloody hell! / Fucking hell!:** formulaic interjections, left out of the Table 7.2 function counts.
- **damn:** self-curses (*Damn me if she isn't right!*, p. 112; *I'll be damned*, pp. 83, 112).
- **hell:** *The hell it is!* as a denial (p. 32); postposed *like hell* / *as hell*, which ch. 7 leaves out (note 1, p. 172).

**Non-46 bearers Ljung uses to establish properties:** Fuck!, Shit!, Cor, Gosh, Oh God, Hell, Bugger, Christ, Jesus, goddamn(ed), bleeding, son of a bitch, motherfucker, and many non-English items.

**Corpus figures.**
- **Table 7.1 (p. 145), expletive slot-filler tokens / total tokens:** bloody 3509/3519, fucking 2157/2162, damn 276/348, damned 23/27.
- **Two arithmetic slips in the source.**
  - Table 7.2 gives fucking "Emphasis on following NP" as 42 (19.9%), but 42/191 = 22.0%.
  - Table 4.3 gives Hell 1 single of 145, but the p. 81 text says "one of its 121".

## 2. NEW: properties

- **NEW:STAND_ALONE**: "instances of swearing that are independent utterances" (p. 143; p. 30 says they "function as utterances of their own"). Maps to P01.
- **NEW:SLOT_FILLER**: "swear words that are not themselves independent utterances but are used inside larger units, viz. as what earlier we have called slot fillers." (p. 143). Ch. 4 uses the same word for interjections placed before or after a clause (p. 87); see warning 8.
- **NEW:GAP_FILLER**: "Gap fillers operate vertically or interactively: in conversations they make up entire turns of their own, viz. they are themselves complete utterances." (p. 90)
- **NEW:REACTIVE**: "These outbursts often take the form of interjections which will be referred to here as ‘reactive (expletive) interjections’." (p. 83). They are "used merely to signal often involuntary speaker reactions to stimuli of various kinds" (p. 95).
- **NEW:PRAGMATIC_INTERJECTION**: "unless they are used as reactive interjections, there is every reason to regard expletive interjections as pragmatic markers." (p. 95). Introduced as "which will be called pragmatic (expletive) interjections." (p. 84)
- **NEW:SLOT_POSITION**: "can be made between five different slot filler positions for the expletive pragmatic markers in the turns where they occur." (p. 90). The five: before a clause, after a clause, inside a clause, before a word or phrase, after a word or phrase. Table 4.4 counts: 226, 40, 2, 30, 7.
- **NEW:SCOPE**: "the most common position is before a clause over which they have scope. (Strictly speaking, they have scope over the proposition underlying the clause.)" (p. 87)
- **NEW:COMBINES**: "the overwhelming majority of the taboo words prefer to be in the company of other words when used as interjectional utterances." (p. 82)
- **NEW:HOMONYM**: "The primary or prototypical interjections have no homonyms in other word classes while the secondary interjections do." (p. 78, reporting Gehweiler)
- **NEW:INTERCHANGEABLE**: non-literal swear words substitute for each other regardless of literal meaning (pp. 13, 16).
- **NEW:FORMULAIC**: "Formulaic sequences have been found to possess special characteristics, for example lack of compositionality, fixedness and a resistance to the insertion of pauses and hesitation forms" (p. 19)
- **NEW:ANOMALOUS_SYNTAX**: "Anomalous syntax/usage is also common in swearing" (p. 19)
- **NEW:GRAMMATICALLY_REGULAR**: intensifier and attributive uses are grammatically like *so very lazy* and *the useless postman* (p. 19).
- **NEW:DEGREE / NEW:AMPLIFIER**: "intensifier expressing a high degree of the following adjective or adverb" (p. 33). The adverbs "are amplifiers" (p. 148).
- **NEW:GRADABLE_NOUN_INTENSIFIER**: "to indicate degree with regard to a following gradable noun" (p. 148)
- **NEW:LOCAL_SCOPE**: "their scope is local, extending no further than the nearest element to the right." (p. 149)
- **NEW:EMPHASIS**: Ljung's −intensifying branch. Figure 7.1 (p. 153) splits it into emphasis "On constituent" (before / after / insertion) and "On speech act". Table 7.2 adds emphasis on a following NP, on a following non-NP, and on a preceding element.
- **NEW:RETROACTIVE_EMPHASIS**: an expletive placed after worst/every/30/no emphasizes those words (p. 152).
- **NEW:BOOSTER**: Stenström's term, "where it is called a booster and defined as ‘the speaker’s assessment of what s/he says’" (p. 151).
- **NEW:PRE_NONNP_EMPHASIS**: emphasizer use before verbs, infinitives, gerunds and numerals. bloody/fucking Y; damn(ed) N (p. 151).
- **NEW:INSERTION / NEW:INFIXATION**: insertion "into linguistic units normally considered to be impenetrable, viz. words and phrases" (p. 153; p. 34).
- **NEW:TABOO_LOAD**: the only stated difference between *very* and *bloody/damn* (p. 147).
- **NEW:POST_WH_SLOT / NEW:WH_SLOT_SUBSTITUTION**: the expletive sits immediately after an interrogative word (p. 34) and can be replaced by *on earth*, *in God’s name*, etc. (p. 12).
- **NEW:STRESS_CUE**: stress on the following noun would favour the emphasis reading over dislike (p. 150).
- **NEW:YOU_X_FRAME**: an epithet is a noun that succeeds in *You X!* or bare *X!* (pp. 126–127).
- **NEW:THREE_NAMECALLING_FRAMES**: an expletive epithet must appear in direct address, third-party reference and description (p. 33).
- **NEW:NEUTRALIZATION**: epithets used as noun supports lose their negative meaning (pp. 128, 131).
- **NEW:OPTATIVE_VERB**: damn in curses is an optative subjunctive (p. 31; note p. 172).
- **NEW:NONLITERAL**: Ljung's criterion 2, "not used with their literal meanings" (p. 147).
- **NEW:ADV_VS_ADJ_SPECIALIZATION**: bloody prefers adjective hosts; damn doesn't (p. 173).
- **NEW:NO_WORD_CLASS**: intrusive fucking can't be assigned to a traditional word class (p. 40).
- **NEW:PREDICATIVE (weak)**: "Unlike what was the case in the Germanic languages, Spanish can also place the superlative form of the expletive word in predicate complement position" (p. 158). This implies Germanic slot fillers lack the predicative use, but English is not named.

## 3. Warnings against using properties as diagnostics

1. **Feelings are underdetermined.** "the actual choice between, say, anger, surprise and joy can only be made in the individual speech situation" (pp. 22–23). And "most of the individual interjections are not linked to particular feelings but may be used to express all of them." (p. 86). Item-specific P08 content isn't reliable.
2. **"Exclamation" is a delivery category.** "What matters is obviously not the syntactic or other nature of the utterances, but merely the manner in which they are delivered" (p. 76)
3. **Intensifier and emphasizer blur.** "It is frequently impossible to distinguish clearly between expletives used as intensifiers and the same expletives used as emphasizers" (p. 33)
4. **Figure 7.1's categories overlap.** "the categories in the figure frequently overlap" (p. 153), and "It is frequently hard if not impossible in many cases to distinguish between certain of the categories in the tree diagram, in particular those of emphasis and dislike" (p. 153)
5. **Readings of the BNC data are uncertain without prosody.** "especially when the corpus providing the data lacks phonological annotation, as is the case with the BNC." (p. 149)
6. **Position isn't function (P03).** Booster *bloody* "often occur[s] in what looks like typical NP modifier positions" (p. 151). Also "the label ‘adjective’ is a misnomer" (p. 147) and "the term ‘adjective’ for bloody is a misnomer." (p. 144)
7. **Categories classify uses, not words.** "what the diagram describes is really the different uses of words. Words are not always or even normally members of only a single category." (p. 125). This supports coding at the level of uses.
8. **"Slot filler" means two different things.** In ch. 4 it covers interjections in supplement-like positions ("all obviously slot fillers as they were defined in Chapter 2", p. 87); in ch. 2 and 7 it covers phrase-internal modifiers. It maps onto neither P02 nor P03 by itself.
9. **The *Damn it* boundary.** X it! forms "are in most cases idiomatic units used as interjections, but which may also be curses containing the pronouns it as a direct object." (p. 110). Ljung also gives no criterion separating *Damn heater!* (adjective, p. 149) from *Damn this place!* (curse, p. 54).
10. **The You-X test can be gamed.** "the insertion test becomes less reliable above if we insert disparaging or negative adjectives like for example bloody or stupid in front of a noun" (p. 127)
11. **Reactive coding is shaky.** "more difficult to determine than for the other functions these findings should be taken with a certain amount of scepticism." (p. 95)
12. **Low counts mean little.** "the total number of occurrences is very low, this information is rather uninteresting." (p. 93). Damn has only 4 tokens.
13. **Reactive vs gap-filler depends on hearer uptake** and speaker intention (p. 91, *Oh damn it!*).
14. **Formulaic strings shouldn't be parsed internally.** "Oh my God! and Bloody hell! are no longer compositional syntactic units" (p. 80). Ljung concludes the field should "withdraw from the claim that the interjections are a word class" (p. 81).
15. **"Infixation" is a misleading label.** It is "a somewhat misleading term suggesting a kind of usage parallel with prefixation and suffixation." (p. 40)

## 4. What I did not read

**Not read:**
- The Introduction, apart from roughly lines 185–210 (unpaged; I used none of it).
- §§1.0–1.2.1.
- Chapter 3, apart from §3.3.2 and §3.7.
- §§5.0–5.1 (oaths, emphatic denials).
- §§6.1, 6.2 and 6.5 (politeness, ritual insults, unfriendly suggestions).
- Chapter 8, apart from the opening of §8.0.
- The notes to chapters 1–3 and 8.
- Most of §2.2 (themes).

**Searches.**
- **Greps run across the whole book:** damn(ed), bloody, fucking, bastard, "the hell|the heck|the devil|the fuck", and "heavens|very|exactly|on earth".
- **Not grepped outside the sections I read:** the other bearer forms (ah, oh, wow, ouch, ugh, oops, sh, hey, alas, aha, huh, mm-hm, bye, okay, yes, no, thanks, sorry, hello, lah, haba, bang, main, probable, coffee, stop, black, quickly, how are you), and "repeat|repetition". Mentions of those forms elsewhere in the book are unchecked.

**One page number is inferred:** p. 11 (the GEE row) comes from neighbouring page markers, not a marker read directly.