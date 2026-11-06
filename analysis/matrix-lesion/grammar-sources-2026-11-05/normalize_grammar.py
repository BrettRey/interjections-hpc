"""Map the grammar agents' free-text rows onto the matrix's columns.

Input rows-<src>.tsv (parse_tables.py / parse_bullets.py output, quotations
checked with check_quotes_g.py). Output norm-<src>.tsv in the same format,
with property labels build_long.py understands, values Y/N, and hedges as
"Y (hedged: reason)". Every row is mapped by hand below (parent's reading of
each report row, 2026-11-05); dropped rows give their reason. Polarity is
handled here: "attributive-only" is predicative N; "no ·ly adverb" is
has-ly-adverb N; a host restriction is restricted-hosts Y.
"""
import csv, sys

D = "DROP"
H = lambda why: ("hedged", why)
MAP = {
 "cgel2002": {
  0: ("DAMN_PRENOM", "NEW:PREDICATIVE", "N", None),  # starred *That noise is damn
  1: ("DAMN_PRENOM", "P03", "Y", None),
  2: D, 5: ("CLASS:attributive-only expletives", "NEW:EXPRESSIVE_STRENGTH", "Y", None),
  3: ("CLASS:expressive attributives (dear, poor, wretched; bleeding, bloody, fucking)", "NEW:TAKES_MODIFIER / NEW:PRO_ONE", "N", None),
  4: ("CLASS:attributive-only expletives", "NEW:PREDICATIVE; P07D", "N", None),
  6: ("BLOODY_PRENOM", "P03", "Y", None), 7: ("BLOODY_PRENOM", "P03", "Y", None),
  8: ("BLOODY_PRENOM", "P07D", "N", None), 9: ("FUCKING_PRENOM", "P03", "Y", None),
  10: ("CLASS:expletive adjective-adverb pairs (bleeding, bloody, damn(ed), fucking)", "NEW:LY_ADVERB", "N", None),
  11: ("BLOODY_INTENS", "NEW:DEGREE", "Y", None), 12: "DROP: U (no -v mark is silence)",
  13: ("BLOODY_INTENS", "NEW:DEGREE", "Y", None),
  14: ("DAMN_DEGREE", "NEW:VERB_MODIFIER", "N", None),
  15: "DROP: damn well is a clause-level use not in the inventory",
  16: ("VERY_INTENS", "NEW:VERB_MODIFIER", "N", None), 17: ("VERY_INTENS", "P10A", "Y", None),
  18: "DROP: the adjective very, not VERY_INTENS", 19: "DROP: warning, kept in the report",
  20: ("CLASS:degree adverbs dead, plain", "NEW:RESTRICTED_HOSTS", "Y", None),
  21: ("CLASS:informal attributives in -ing (blithering, crashing, thumping)", "NEW:RESTRICTED_HOSTS", "Y", H("'tend to'")),
  22: ("MAIN_PRENOM", "NEW:PREDICATIVE", "N", H("list of adjectives that 'do not normally occur' predicatively; no starred example")),
  23: ("MAIN_PRENOM", "NEW:PRO_ONE", "Y", None),
  24: ("CLASS:particularising attributives (main, ...)", "NEW:TAKES_MODIFIER", "N", H("'do not normally accept modification'")),
  25: ("PROBABLE_PRENOM", "P03", "Y", None), 26: "DROP: U",
  27: ("CLASS:gradable adverbs in -ly (quickly, ...)", "P05", "N", None),
  28: ("CLASS:interjection", "P03; P04", "N", None), 29: D,
  30: ("CLASS:interjection", "P01; P02", "Y", None),
  31: ("AH", "P02", "Y", None), 32: ("ALAS", "P02; NEW:CLAUSE_MEDIAL", "Y", None),
  33: ("HEY", "P02", "Y", None), 34: ("DAMN_REACT", "P02", "Y", None), 35: D,
  36: ("DAMN_NP", "P04", "Y", None),
  37: ("BASTARD_SUPP", "P02", "Y", None), 38: ("BASTARD_SUPP", "NEW:CLAUSE_MEDIAL", "Y", None),
  39: ("BASTARD_SUPP", "P01", "Y", H("given as 'cf.', punctuated as a separate exclamation")),
  40: D, 41: ("BASTARD_SUPP", "P12S", "Y", None), 42: ("BASTARD_SUPP", "P06", "Y", None),
  43: "DROP: a preference for some over a, not a possibility claim",
  44: ("YOU_BASTARD", "P03", "N", H("CGEL says never in a complement position; modifier position not addressed")),
  45: ("YOU_BASTARD", "P01", "Y", None), 46: ("YOU_BASTARD", "P06", "Y", None),
  47: ("CLASS:derogatory vocatives with you (you stupid bastard)", "P04", "Y", None),
  48: ("CLASS:vocative", "P01", "Y", None),
  49: ("THE_HELL_WH", "P03", "Y", None), 50: ("THE_HELL_WH", "NEW:POST_WH", "Y", None),
  51: ("THE_HELL_WH", "NEW:IN_SITU", "N", None),
  52: ("CLASS:emotive modifiers (on earth, the hell, ever)", "NEW:IN_SITU", "N", None),
  53: ("CLASS:emotive modifiers (on earth, the hell, ever)", "NEW:RESTRICTED_HOSTS", "Y", H("'hardly compatible' with which")),
  54: ("CLASS:emotive modifiers (on earth, the hell, ever)", "P07D", "N", None),
  55: ("CLASS:emotive modifiers (on earth, the hell, ever)", "NEW:RESTRICTED_HOSTS", "Y", None),
  56: ("THE_HELL_WH", "NEW:RESTRICTED_HOSTS", "Y", None),
  57: ("CLASS:emotive modifiers (on earth, the hell, ever)", "NEW:WH_ALONE", "N", H("except before a stranded preposition, else, or not")),
  58: ("THE_HELL_WH", "NEW:CLITIC_HOST", "Y", None),
  59: ("EXACTLY_WH", "NEW:POST_WH; NEW:PRE_WH", "Y", None), 60: ("EXACTLY_WH", "NEW:IN_SITU", "Y", None),
  61: ("YES NO", "P01", "Y", None),
  62: ("YES NO", "P03", "Y", H("CGEL: 'can be regarded as' a polarity adjunct")),
  63: ("YES NO", "NEW:RESTRICTED_HOSTS", "Y", None), 64: ("YES NO", "P12S", "Y", None),
  65: ("CLASS:supplements", "P12S", "Y", None),
  66: ("CLASS:supplements (PP and AdvP)", "P11E", "N", None),
 },
 "quirk1985": {
  0: ("CLASS:interjection", "P03", "N", None), 1: ("CLASS:interjection", "P04", "N", None),
  2: ("CLASS:interjection", "P13", "Y", None), 3: ("TUTTUT", "P13", "Y", None),
  4: "DROP: U", 5: "DROP: U",
  6: ("CLASS:interjection", "NEW:LENGTHENING", "Y", None),
  7: ("OH AH", "P02", "Y", None),
  8: ("CLASS:formula", "NEW:FIXED_FORM", "Y", None),
  9: ("CLASS:formula", "P01", "Y", H("listed under Nonsentences, without context")),
  10: ("CLASS:expletive formulae (My Gosh ... Fuck (it))", "P01", "Y", H("listed under Nonsentences, without context")),
  11: ("DAMN_REACT", "P01", "Y", H("a listing without context")),
  12: [("HEAVENS", "P01", "Y", H("a listing without context")), ("HEAVENS", "P04", "Y", None)],
  13: ("DAMN_NP", "P04; P01", "Y", None),
  14: ("CLASS:imprecations (some)", "NEW:IMPERATIVE_POTENTIAL", "N", None),
  15: ("YES OKAY", "P01", "Y", H("a listing without context")),
  16: ("NO", "P01", "Y", H("a listing without context")), 17: ("HELLO", "P01", "Y", H("a listing without context")),
  18: ("BYE", "P01", "Y", H("a listing without context")),
  19: [("THANKS", "P04", "Y", None), ("THANKS", "P06", "Y", None), ("THANKS", "P01", "Y", H("a listing without context"))],
  20: ("SORRY", "P01", "Y", H("a listing without context")), 21: ("HOWAREYOU", "P01", "Y", H("a listing without context")),
  22: ("YES NO OKAY", "P10S", "Y", H("'often repeated for emphasis'; pattern unspecified")),
  23: "DROP: a frequency statement, not a possibility claim",
  24: ("CLASS:vocative epithets", "P04", "Y", None), 25: "DROP: no determiner required is not a possibility claim",
  26: ("CLASS:vocative epithets", "P08", "Y", None),
  27: ("CLASS:tag exclamations (the idiot)", "P02", "Y", None),
  28: ("CLASS:tag exclamations (the idiot)", "P12I", "Y", H("OCR garbled; the 'tail' wording is unreadable")),
  29: ("THE_HELL_WH", "P03; NEW:POST_WH", "Y", None), 30: D,
  31: ("THE_HELL_WH", "NEW:POST_WH", "Y", None), 32: D,
  33: ("EXACTLY_WH", "NEW:POST_WH; NEW:PRE_WH", "Y", None),
  34: ("EXACTLY_WH", "P04", "Y", H("focused by just; the agent marked it weak")),
  35: ("CLASS:emphasizer adverbs", "NEW:TAKES_MODIFIER", "N", H("'cannot be modified or are unlikely to be'; definitely excepted")),
  36: "DROP: same claim as row 35",
  37: ("CLASS:emphasizer adjectives (pure, real, sheer, ...)", "NEW:PREDICATIVE", "N", None),
  38: ("CLASS:noninherent amplifiers (complete, total, ...)", "NEW:PREDICATIVE", "N", None),
  39: ("CLASS:emotive adjectives (poor, dear, wretched)", "NEW:PREDICATIVE", "N", None),
  40: ("CLASS:attributive-only intensifying adjectives", "NEW:RESTRICTED_HOSTS", "Y", None),
  41: ("CLASS:intensifying adjectives", "NEW:COMPARABILITY", "N", None),
  42: ("MAIN_PRENOM", "P03", "Y", None), 43: ("VERY_INTENS", "P03", "Y", None),
  44: ("VERY_INTENS", "P10A; P10S", "Y", None),
  45: ("VERY_INTENS", "NEW:SYNDETIC_REPEAT", "N", None),
  46: ("CLASS:attributive adjectives and degree intensifiers", "P10S", "Y", None),
  47: ("BLACK", "P03", "Y", None), 48: ("QUICKLY", "P04", "Y", None),
  49: ("DAMN_DEGREE", "P03", "Y", None),
  50: "DROP: a damn sight is an NP idiom (CGEL p. 327 n. 1), not DAMN_PRENOM",
  51: ("BLOODY_INTENS", "P03", "Y", None),
  52: ("CLASS:expletives in a clause", "NEW:PRE_STRESS", "Y", None),
  53: D, 54: ("CLASS:expletives in a clause", "NEW:SPREADS", "Y", None), 55: D,
  56: ("BLOODY_INFIX", "NEW:INSERTION", "Y", None), 57: ("BLOODY_INFIX", "NEW:PRE_STRESS", "Y", None),
  58: D,
 },
}

MAP["sie2005"] = {
  0: "DROP: SIEG's silence on interjections is stated policy",
  1: ("CLASS:attributive-only adjectives ([25]: damn, eventual, former, main, mere, sole, utter, ...)", "NEW:PREDICATIVE", "N", None),
  2: D, 3: D,
  4: ("CLASS:degree adverbs very, pretty, too", "NEW:VERB_MODIFIER", "N", None),
  5: "DROP: 'independent of clause type' covers Get the hell out, a use not in the inventory",
  6: ("CLASS:supplements", "P12S", "Y", None),
  7: ("DAMN_PRENOM", "P03", "Y", None),
  8: ("DAMN_PRENOM", "NEW:PREDICATIVE", "N", H("list membership; the starred example is for utter")),
  9: ("THE_HELL_WH", "P03; NEW:POST_WH", "Y", None),
  10: ("VERY_INTENS", "P03", "Y", None), 11: ("VERY_INTENS", "NEW:VERB_MODIFIER", "N", None),
  12: ("MAIN_PRENOM", "P03", "Y", None),
  13: ("MAIN_PRENOM", "NEW:PREDICATIVE", "N", H("list membership; the starred example is for utter")),
  14: ("QUICKLY", "P05", "N", None), 15: ("BLACK", "P03", "Y", None), 16: ("YES NO", "P02", "Y", None),
}
MAP["biber1999"] = {
  0: ("CLASS:inserts (central members)", "P01", "Y", None), 1: ("CLASS:inserts", "P12I", "Y", None),
  2: ("CLASS:inserts", "NEW:CLAUSE_MEDIAL", "Y", H("'rarely occur medially'")),
  3: "DROP: 'in general' inability; not N", 4: ("CLASS:inserts", "P04", "Y", None), 5: D,
  6: ("CLASS:inserts", "P07D", "N", None),
  7: ("CLASS:inserts (interjections, response forms, hesitators)", "P13", "Y", None), 8: D,
  9: "DROP: N only for the combinations shown (*thank you a lot)", 10: D,
  11: ("CLASS:expletives (God, damn, shit, bloody hell, fuck; gosh, gee, heavens, heck, ...)", "P01", "Y", None),
  12: ("CLASS:expletives (God, damn, shit, bloody hell, fuck; gosh, gee, heavens, heck, ...)", "NEW:CLAUSE_MEDIAL", "Y", H("'very rare'")),
  13: ("CLASS:expletives (God, damn, shit, bloody hell, fuck; gosh, gee, heavens, heck, ...)", "P12I", "Y", None),
  14: ("CLASS:expletives (God, damn, shit, bloody hell, fuck; gosh, gee, heavens, heck, ...)", "P02", "Y", None),
  15: "DROP: scope of the class (bloody, fucking excluded); kept in the report", 16: ("CLASS:moderated expletives (gosh, gawd, goodness, ...)", "NEW:PHONETIC_MOD", "Y", None),
  17: D, 18: D,
  19: ("CLASS:exclamatory NPs, addressee type (you little devil, you silly cow; you bastard)", "P02", "Y", None),
  20: ("CLASS:exclamatory NPs, addressee type (you little devil, you silly cow; you bastard)", "P04", "Y", None),
  21: ("CLASS:exclamatory NPs, third-person type (the dirty bugger)", "P06", "Y", None),
  22: ("CLASS:expletive formulae (damn you, bugger me, fuck that)", "NEW:IMPERATIVE_POTENTIAL", "N", None),
  23: D, 24: D, 25: "DROP: prosody of huh uh, unh unh, not inventory bearers",
  26: ("CLASS:polite formulae (thank you, thanks, sorry, please, ...)", "P05", "N", None),
  27: D, 28: D,
  29: ("DAMN_REACT", "P01", "Y", None), 30: ("DAMN_NP", "P04", "Y", None),
  31: ("BLOODY_PRENOM", "P03", "Y", None),
  32: ("BLOODY_INTENS", "P03", "Y", H("stated for 'adjectives or adverbs bloody'; the only example is prenominal")),
  33: ("FUCKING_PRENOM", "P03", "Y", None), 34: ("YOU_BASTARD", "P01", "Y", None),
  35: ("THE_HELL_WH", "P03; NEW:POST_WH", "Y", None), 36: D,
  37: ("VERY_INTENS", "P10A", "Y", None), 38: ("STOP", "P04", "Y", None),
  39: ("OH", "P01", "Y", None), 40: ("OH", "P02", "Y", None), 41: ("AH", "P01", "Y", None), 42: ("AH", "P02", "Y", None),
  43: ("WOW", "P01; P02", "Y", None), 44: ("AHA", "P02", "Y", None), 45: ("OOPS", "P02", "Y", None),
  46: ("OOPS", "P10A", "Y", None), 47: ("OUCH", "P02", "Y", None), 48: ("UGH", "P01", "Y", None),
  49: ("UGH", "P02", "Y", None), 50: ("UGH", "P13", "Y", H("OCR 'ugit', presumably ugh")),
  51: ("TUTTUT", "P13; P10A", "Y", None), 52: ("TUTTUT", "P02", "Y", None), 53: ("GEE", "P02", "Y", None),
  54: ("HEAVENS", "P01", "Y", None), 55: ("HEY", "P02", "Y", None), 56: ("YES", "P01", "Y", None),
  57: ("NO", "P02", "Y", H("the preceding question isn't shown")), 58: D, 59: ("OKAY", "P01", "Y", None),
  60: ("MMHM", "P01", "Y", None), 61: ("MMHM", "P13", "Y", None), 62: ("HUH", "P01", "Y", None),
  63: ("HELLO", "P02", "Y", None), 64: [("BYE", "P01", "Y", None), ("BYE", "P10A", "Y", H("bye bye is a lexicalized reduplication"))],
  65: ("THANKS", "P02", "Y", None), 66: ("THANKS", "P04", "Y", None), 67: ("SORRY", "P01", "Y", None),
  68: ("SORRY", "P02", "Y", None), 69: ("SORRY", "P04", "Y", None),
}

EXCL = "CLASS:expletives (God, damn, hell, shit, fuck; gosh, gee, heavens, ...)"
MAP["biber2021"] = {
  0: ("DAMN_REACT", "P01", "Y", None), 1: D, 2: "DROP: frequency", 3: "DROP: frequency",
  4: ("DAMN_NP", "P04", "Y", None), 5: ("DAMN_PRENOM", "P03", "Y", None), 6: "DROP: register",
  7: ("DAMN_DEGREE", "P03; NEW:DEGREE", "Y", None), 8: "DROP: frequency", 9: "DROP: frequency",
  10: ("BLOODY_INTENS", "P03; NEW:DEGREE", "Y", None), 11: "DROP: register",
  12: ("BLOODY_INTENS", "NEW:IN_STANDALONE_PHRASE", "Y", None),
  13: ("BLOODY_PRENOM", "P03", "Y", None), 14: ("BLOODY_PRENOM", "NEW:IN_STANDALONE_PHRASE", "Y", None),
  15: "DROP: classification (outside expletives); kept in the report",
  16: "DROP: use can't be matched (probably literal bloody)", 17: ("FUCKING_PRENOM", "P03", "Y", None),
  18: "DROP: degree fucking, not in the inventory", 19: "DROP: classification and meaning; kept in the report",
  20: ("YOU_BASTARD", "P01", "Y", None),
  21: ("CLASS:exclamatory NPs, addressee type (you little devil, you silly cow; you bastard)", "P02", "Y", None),
  22: ("CLASS:exclamatory NPs, third-person type (the dirty bugger)", "P06", "Y", None),
  23: ("THE_HELL_WH", "P03; NEW:POST_WH", "Y", None), 24: "DROP: classification (hell as a noun); kept in the report",
  25: "DROP: not an inventory bearer", 26: "DROP: not an inventory bearer", 27: D,
  28: ("OH", "P01", "Y", None), 29: ("OH", "P02", "Y", None),
  30: ("OH", "NEW:CLAUSE_MEDIAL", "Y", H("inside a restart")), 31: "DROP: frequency",
  32: ("AH", "P01", "Y", H("Biber's footnote on ah's 'core use' is not in the file")),
  33: [("AH", "P02", "Y", None), ("AH", "P12I", "Y", H("read from the transcription, not audio"))],
  34: "DROP: frequency", 35: ("WOW", "P01", "Y", None), 36: [("WOW", "P01", "Y", None), ("WOW", "P02", "Y", None)],
  37: ("OOPS", "P02", "Y", None), 38: ("OOPS", "P10A", "Y", None),
  39: [("OUCH", "P02", "Y", None), ("OUCH", "P12I", "Y", H("read from the transcription, not audio"))],
  40: ("UGH", "P01", "Y", None), 41: ("UGH", "P02", "Y", None),
  42: ("CLASS:inserts (interjections such as ugh, ooh; response forms; hesitators)", "P13", "Y", None),
  43: ("TUTTUT", "P13; P10A", "Y", None), 44: ("AHA", "P02", "Y", None),
  45: ("GEE", "P02", "Y", None), 46: ("GEE", "P08", "Y", None), 47: ("HEAVENS", "P01", "Y", None),
  48: ("HEY", "P02", "Y", None), 49: ("HEY", "NEW:CLAUSE_MEDIAL", "Y", H("inside a restart")),
  50: [("HEY", "P10A", "Y", None), ("HEY", "P10S", "Y", H("'for intensifying or attention-getting purposes'"))],
  51: ("MMHM", "P01", "Y", None), 52: ("MMHM", "P13", "Y", None), 53: ("HUH", "P01", "Y", None),
  54: ("OKAY", "P01", "Y", None), 55: ("OKAY", "P02", "Y", None), 56: "DROP: position frequencies",
  57: ("YES", "P01", "Y", None), 58: ("YES", "P02", "Y", None),
  59: ("NO", "P01", "Y", H("the preceding question isn't shown")), 60: ("NO", "P02", "Y", H("the preceding question isn't shown")),
  61: ("HELLO", "P01", "Y", None), 62: ("HELLO", "P02", "Y", None), 63: ("BYE", "P01", "Y", None),
  64: ("THANKS", "P04", "Y", None), 65: ("SORRY", "P01", "Y", None), 66: ("SORRY", "P02", "Y", None),
  67: ("SORRY", "P04", "Y", None), 68: ("STOP", "P04", "Y", None), 69: "DROP: a different string from HOWAREYOU",
  70: ("CLASS:amplifiers of gradable adjectives (more, very, so, too, extremely)", "NEW:DEGREE", "Y", None),
  71: ("VERY_INTENS", "P10A", "Y", None),
  72: ("VERY_INTENS", "NEW:IN_STANDALONE_PHRASE", "Y", None), 73: ("VERY_INTENS", "NEW:IN_STANDALONE_PHRASE", "Y", None),
  74: "DROP: classifier list; 'generally non-gradable' is a tendency",
  75: ("CLASS:central adjectives (black, big, new)", "NEW:PREDICATIVE; NEW:ATTRIBUTIVE; P05; NEW:COMPARABILITY", "Y", None),
  76: ("QUICKLY", "P04", "Y", None), 77: "DROP: 'not Y' is not a statement", 78: "DROP: frequency",
  79: ("CLASS:else (wh-postmodifier)", "NEW:POST_WH", "Y", None),
  80: ("CLASS:inserts (central members)", "P01", "Y", None), 81: ("CLASS:inserts", "P12I", "Y", None),
  82: ("CLASS:inserts", "NEW:CLAUSE_MEDIAL", "Y", H("'rarely occur medially'")), 83: "DROP: 'in general'; not N",
  84: ("CLASS:inserts", "P04", "Y", None), 85: D, 86: "DROP: criterion (5), noted in the report",
  87: ("CLASS:inserts", "P07D", "N", None), 88: ("CLASS:inserts", "P13", "Y", None),
  89: "DROP: N only for the combinations shown", 90: D,
  91: [(EXCL, "P01; P02", "Y", None), (EXCL, "NEW:CLAUSE_MEDIAL", "Y", H("'very rare'"))],
  92: (EXCL, "P12I", "Y", None), 93: D,
  94: ("CLASS:informal amplifiers (bloody, damn, incredibly, terribly, real, really)", "NEW:DEGREE", "Y", None),
  95: ("CLASS:attributive-only adjectives (mere)", "NEW:PREDICATIVE", "N", None), 96: D,
  97: ("CLASS:classifier adjectives (previous, motionless, continuous, dental)", "NEW:COMPARABILITY", "N", None),
  98: ("CLASS:adverbs", "P01", "Y", None),
  99: ("CLASS:adjectives as exclamations (Great!, Good!, Sorry!, Bloody brilliant!)", "P01", "Y", None),
  100: "DROP: category change, noted in the report", 101: ("CLASS:hesitators", "NEW:CLAUSE_MEDIAL", "Y", None), 102: D,
}
# Quotations read from the page image where the OCR text is unusable (parent, 2026-11-05).
QUOTE_OVERRIDE = {
  ("quirk1985", 52): "Expletives (in the broadest sense) provide a common mode of amplification in extremely informal speech, serving as a rhetorical transition between theme and an emotionally coloured focus [read from the page image, PDF 717; §18.59 Note [b]]",
}
src = sys.argv[1]
# Quirk's ellipsis-joined quotations, settled against the printed page (decision call 4, 2026-11-05):
# the OCR reads across two-page spreads, so most ellipses only bridged the facing page.
if src == "quirk1985":
    for a in csv.DictReader(open("quirk-ellipsis-resolved.tsv", encoding="utf-8"), delimiter="\t"):
        QUOTE_OVERRIDE.setdefault(("quirk1985", int(a["row"])), a["resolved_quote"] + f" [{a['basis']}]")
rows = list(csv.DictReader(open(f"rows-{src}.tsv", encoding="utf-8"), delimiter="\t"))
for r in rows:
    r["source"] = src  # biber2021c07/c14 were the checker's chapter split
w = csv.writer(sys.stdout, delimiter="\t")
w.writerow(["source", "item_id", "property", "value", "scope", "quote", "page", "note"])
assert len(rows) == len(MAP[src]), (len(rows), len(MAP[src]))
dropped = 0
for i, r in enumerate(rows):
    m = MAP[src][i]
    if isinstance(m, str):
        dropped += 1
        print(f"{src}\t{i}\t{r['item_id']}\t{r['property']}\t{m}", file=sys.stderr)
        continue
    for item, label, v, hedge in (m if isinstance(m, list) else [m]):
        value = f"{v} (hedged: {hedge[1]})" if hedge else v
        scope = "class" if item.startswith("CLASS:") else "item"
        w.writerow([src, item, label, value, scope, QUOTE_OVERRIDE.get((src, i), r["quote"]), r["page"], f"[report row {i}: {r['item_id']} | {r['property']} | {r['value']}] {r['note']}"[:500]])
print(f"{src}: {len(rows)} rows, {dropped} dropped", file=sys.stderr)
