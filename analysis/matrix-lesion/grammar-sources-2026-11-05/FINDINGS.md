# What the reference grammars add on form
<!-- SUMMARY: five grammars (CGEL, Student's Introduction, Quirk 1985, Biber 1999 ch. 14, Biber 2021 chs 7 and 14) read for form properties of the expressive uses; none states one for the uses as a group; the properties stated hold within one slot or of classes with non-expressive members; two candidates cross slots (CGEL's missing ·ly, Quirk's pre-focus placement with tmesis) · status: development data, for Brett · updated: 2026-11-05 -->

Development data under FREEZE-v4 §9, not study data. Every quotation was string-checked against page-marked text (`quote-checks/RESULTS.txt`); every report row was mapped to a matrix column by hand, with polarity and hedges (`normalize_grammar.py`; dropped rows and reasons in `quote-checks/DROPPED.txt`). Testimony families: H with S; Q with B and R.

The question is whether an expressive profile changes what you'd expect about a form property, compared with the controls and the other rows. No single property has to hold of every member and fail for every nonmember, and the expressive uses overlap the interjections by design (the paper counts interjection membership among the expressive category's properties). **No grammar states a form property for the expressive uses as a group.** The properties they state hold within one slot, or of a class that also has non-expressive members. Two candidates cross slots (below). The reading was targeted, so this is a claim about the passages searched. Each `REPORT-*.md` §4 gives the search strings and the sections not reached. The notable gaps:
- CGEL: AdjP modification, Ch. 6 §3.2, pp. 547–550.
- Quirk: §7.56ff, and the body of §§8.104–8.111.
- SIEG: nearly everything outside ch. 6 §§1.3–2.2.
- Biber 2021: §14.4.1.1, on where vocatives (and so insulting NPs) occur.
- Biber 1999: only ch. 14 is in hand.

Insertion is stated Y for one bearer (BLOODY_INFIX) and stated N for none, so it stays untested.

**The splits the grammars do give are within one slot, and each class that carries the property also contains non-expressive members.**
- Prenominal. Attributive-only holds of *damn* (CGEL p. 553, "∗That noise is damn") but MAIN is in the same list (CGEL p. 553; SIEG p. 120). The pro-form test separates them: the expressive attributives fail it (CGEL p. 558), *main* passes ("the main ones", p. 555). *Utter*, which isn't expressive, fails it too (∗an utter one, p. 555).
- After wh-words. THE_HELL_WH occurs only right after the wh-word and never in situ; EXACTLY_WH also precedes the wh-word and occurs in situ (CGEL pp. 916, 1087; Quirk p. 608). The class CGEL states it for, "emotive modifiers", includes *ever* and *on earth*.
- Degree. *damn* and *very* both fail to modify verbs (CGEL pp. 584–585; SIEG p. 116); *bloody* is unmarked. Biber 2021 lists *bloody* and *damn* with *really* and *terribly* as informal amplifiers (p. 560).

**Biber 1999 and 2021 split the expressive uses by form on purpose.** *Damn!*, *gee* and *heavens* are inserts. Prenominal and degree *bloody* and *fucking* "can combine with other words in the normal clausal syntax of English" (2021 p. 1089). *You bastard* is an exclamatory NP, excluded from expletives because insults "refer to people" (2021 p. 1089).

**Two candidates cross slots.**

*The missing ·ly (CGEL).* CGEL (p. 568) says expletives such as *bleeding*, *bloody*, *damn(ed)* and *fucking* "occur as attributive-only adjectives and systematically exclude the ·ly suffix, giving a bloody disgrace vs bloody disgraceful". That relates the prenominal and degree uses of one form, so it belongs on the relation between the uses, recorded once rather than copied into each row as corroboration. Its comparison is ordinary adjective–adverb pairs, flat adverbs such as *fast* included.

*Pre-focus placement (Quirk).* Quirk §18.59 Note [b] (p. 1418, read from the page image because the OCR lost it) says expletives provide "a rhetorical transition between theme and an emotionally coloured focus". Its examples are *silly idiot*, *darned way*, *bloody awful* and *darned well listen*. The note compares tmesis, where the inserted amplification comes "just prior to the point of main emphasis" (App I.76 Note [c], p. 1584). That puts word-internal insertion (BLOODY_INFIX) and clause-level expletive placement under one description. Its limits:
- Quirk's class is "expletives (in the broadest sense)" and includes *silly*.
- Neither the controls nor *very* are tested against it.
- A rhetorical transition to an emotionally coloured focus and placement just before the main stress aren't the same measurement.
- §8.21 ("Such preparation for focus may be expletive") was found but not read.
- BLOODY_INFIX is identified by insertion, so predicting insertion for it recovers an identifying fact. A test would need uses identified independently.

CGEL, SIEG and both Biber grammars say nothing about insertion.

**Discrepancies the readers found in project files:**
- **items-v4 BLOODY_INTENS cites "not of verbs" for *bloody* (CGEL p. 584).** In the text the –v mark is on *damn* and *very* only. Check the PDF (PDF 604).
- **items-v4 BLOODY_INFIX cites Quirk "App. I.75".** Quirk's own cross-reference is App I.76 Note [c].
- **QUICKLY P05 conflict.** Wiktionary's usage note (Y) and SIEG's "neither ∗quicklier nor ∗quickerly" (N) disagree. The question is whether *quicker* belongs to the lexeme *quickly* or to adverbial *quick*.
- **Biber 2021 treats *hell* in *What the hell* as a noun use** (Table 14.10 note, p. 1092). The matrix row follows CGEL's emotive modifier.
