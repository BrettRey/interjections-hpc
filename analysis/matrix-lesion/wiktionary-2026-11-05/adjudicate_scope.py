"""Judge whether each Wiktionary row scoped to a page, headword or sense applies to the
specified use (Brett, 2026-11-05: "you should be able to figure out which of these are
relevant"). Writes scope-adjudication.tsv, which build_long.py reads. Judged by Claude
Opus 5.5 from the Wiktionary block each row cites; OED facts are from ../oed-2026-11-05/OED-NOTES.md.

Verdicts:
  USE        the block is about this use (an interjection's own page, a usage note on the sense)
  WORD       the block is about the word, and nothing on the page or in the OED separates this use
  PRON       the pronunciation applies to this use; whether an ordinary pronunciation supports
             P13 = N is a separate question (decision call 3)
  ROUTE      the block gives the word's history, but this use has its own route (OED)
  OTHER_USE  the block is about a different use or sense; left out of this use's cell
  DUP        a v1 row whose text was garbled by template stripping, superseded by the v2 row
"""
import csv, json, sys
m = json.load(open("../expressive-sources-2026-11-05/matrix.json"))
rows = []
for r in m["rows"]:
    for col, c in r["cells"].items():
        for e in c["entries"]:
            if "scoped" in e["hedge"]:
                rows.append((r["id"], col, e["page"], e["q"]))
J = {}
def put(b, col, page, v, why):
    J[(b, col, page)] = (v, why)

INTJ_OWN = "the interjection's own page and etymology"
for b, col, page, q in rows:
    v1 = page.startswith("v1 ")
    if col == "P13":
        if b in ("HUH", "LAH", "TUTTUT", "UGH"):
            put(b, col, page, "USE", "the page is the interjection's (or particle's); the transcription is of this use")
        else:
            put(b, col, page, "PRON", "one documented pronunciation of the form, which this use shares; it doesn't exclude other variants (call 3)")
    elif col in ("delocutive noun", "delocutive verb"):
        put(b, col, page, "USE", "the derived sense is defined by reference to this use (an utterance of the interjection)")
    elif col in ("imitative or natural origin",):
        put(b, col, page, "USE", INTJ_OWN)
# Etymologies and the rest, item by item
E = {
 "AH": ("USE", INTJ_OWN), "AHA": ("USE", INTJ_OWN), "ALAS": ("USE", INTJ_OWN), "HEY": ("USE", INTJ_OWN),
 "OH": ("USE", INTJ_OWN), "OUCH": ("USE", INTJ_OWN), "WOW": ("USE", INTJ_OWN), "OOPS": ("USE", INTJ_OWN),
 "OKAY": ("USE", INTJ_OWN), "GEE": ("USE", "Etymology 1, the Jesus etymology, is the interjection's; the OED (gee int.2) agrees"),
 "BYE": ("USE", "Etymology 2 is the interjection's (shortened goodbye); the OED (bye int.) agrees"),
 "HELLO": ("USE", INTJ_OWN), "YES": ("USE", "the answer word's etymology"), "NO": ("USE", "Etymology 2, the answer particle's (E1 is the determiner)"),
 "LAH": ("USE", "Etymology 2, the particle's"),
 "THANKS": ("WORD", "the plural noun's etymology; the interjection is that noun used alone"),
 "SORRY": ("WORD", "the adjective's etymology; the interjection comes from it through I'm sorry (usage note)"),
 "BLACK": ("WORD", "the adjective control's own word history"), "COFFEE": ("WORD", "the noun control's own word history"),
 "MAIN": ("WORD", "the adjective's word history"), "MAIN_PRENOM": ("WORD", "the adjective's word history"),
 "PROBABLE_PRENOM": ("WORD", "the adjective's word history"), "QUICKLY": ("WORD", "the adverb's word history"),
 "STOP": ("WORD", "the verb's word history"), "EXACTLY_WH": ("WORD", "the adverb's word history"),
 "VERY_INTENS": ("WORD", "very's word history; its degree use developed from it"),
 "BANG_NOUN": ("WORD", "Wiktionary's one etymology for verb and noun; the noun use is ordinary"),
 "DAMN_REACT": ("WORD", "the verb's etymology; the OED derives damn int. from the verb by conversion"),
 "DAMN_NP": ("WORD", "the verb's etymology; the use is the verb or comes from it"),
 "FUCKING_PRENOM": ("WORD", "fuck + -ing; the OED (fucking adj. & adv.) agrees"),
 "DAMN_PRENOM": ("ROUTE", "the verb's etymology; the OED derives damn adj. & adv. by clipping damned adj."),
 "DAMN_DEGREE": ("ROUTE", "the verb's etymology; the OED derives damn adj. & adv. by clipping damned adj."),
 "BLOODY_PRENOM": ("ROUTE", "the adjective's etymology; the OED calls the origin of the intensifying use 'uncertain and disputed'"),
 "BLOODY_INTENS": ("ROUTE", "the adjective's etymology; the OED calls the origin of the intensifying use 'uncertain and disputed'"),
 "BASTARD_SUPP": ("ROUTE", "the word's etymology ('illegitimate child'); the abusive use's development is the OED's to date (not yet read)"),
 "YOU_BASTARD": ("ROUTE", "the word's etymology ('illegitimate child'); the abusive use's development is the OED's to date (not yet read)"),
 "THE_HELL_WH": ("ROUTE", "the noun hell's etymology; the hell as an intensifier after wh-words is a later development (OED not yet read)"),
 "BANG_DEPICT": ("ROUTE", "the verb's etymology; whether the depictive Bang! is imitative in its own right is the OED's (not yet read)"),
}
GARBLED_V1 = {("ALAS","from fro"), ("BASTARD_SUPP","Frankish"), ("YOU_BASTARD","Frankish"), ("NO","gem-pro"),
              ("VERY_INTENS","derived from la"), ("VERY_INTENS","intensified by ,"),
              ("VERY_INTENS","degree adverbs, and too"), ("NO","To say .")}
SUPERSEDED_V1 = {("AHA","Equivalent to ah + ha."), ("HELLO","From holla"), ("LAH","Bazaar Malay"), ("YES","derived from the same root"),
                 ("YES","We yessed")}
OTHER = {
 ("BASTARD_SUPP","P06"): "the example is the argument use (Some bastard stole my car), not the epithet",
 ("EXACTLY_WH","P03"): "the example is the focusing use (exactly to prove the point), not the modifier after a wh-word",
 ("BLOODY_PRENOM","P05"): "the headword line's bloodier/bloodiest belong to the descriptive adjective; CGEL treats expletive bloody as attributive-only",
 ("BLOODY_PRENOM","comparable"): "the headword template's comparison belongs to the descriptive adjective",
 ("DAMN_NP","P05"): "the verb's paradigm; it doesn't show this use (Damn these mosquitoes!) inflecting",
 ("HEAVENS","frozen plural"): "the note is about the plural noun for the sky, not the exclamation (OED heavens int. not yet read)",
}
USE_COL = {
 "glossed by its use": "the hell sense 'used as an intensifier' is this use",
 "host-stress conditioned": "usage note on the particle", "insertion into word/phrase": "the page is -bloody- itself",
 "placed before stress": "the page is -bloody- itself", "ironic use": "usage note on the interjection",
 "lexical tone": "the particle's pronunciation", "stress tied to use": "usage note on the interjection or greeting",
 "modifies verbs": "the note names the degree-adverb senses", "P10A": "the note names the degree use (very, very important)",
 "P10S": "the note names the degree use (very, very important)", "P04": "the verb use", "catenative": "the verb use",
 "P05": "usage note on the adverb quickly itself", "P06": "the noun's headword line, and the use is the noun",
 "comparable": "the adjective's headword line, and the use is the adjective",
 "frozen plural": "the plural noun's etymology; the interjection is that noun used alone",
}
for b, col, page, q in rows:
    v1 = page.startswith("v1 ")
    if v1 and any(b == gb and s in q for gb, s in GARBLED_V1):
        put(b, col, page, "DUP", "v1 text garbled by template stripping; the v2 row from the same revision has the full text"); continue
    if v1 and any(b == gb and q.startswith(s) for gb, s in SUPERSEDED_V1):
        put(b, col, page, "DUP", "v1 row superseded by the v2 row from the same revision"); continue
    if b == "THANKS" and v1:
        why = ("the plural noun's etymology; the interjection is that noun used alone. The v1 text is garbled by "
               "template stripping; the v2 etymology block from the same revision gives 'nominative plural'")
        put(b, col, page, "DUP" if col == "historical source" else "USE", why if col != "historical source"
            else "v1 text garbled by template stripping; the v2 row from the same revision has the full text"); continue
    if b == "WOW" and v1:
        put(b, col, page, "USE", INTJ_OWN + "; the v1 text lost a template, but 'ultimately a natural exclamation' is intact"); continue
    if (b, col) in OTHER:
        put(b, col, page, "OTHER_USE", OTHER[(b, col)]); continue
    if (b, col, page) in J:
        continue
    if col == "historical source":
        v, why = E[b]; put(b, col, page, v, why)
    elif col in USE_COL:
        put(b, col, page, "USE", USE_COL[col])
    else:
        put(b, col, page, "UNJUDGED", "")
w = csv.writer(open("scope-adjudication.tsv", "w"), delimiter="\t")
w.writerow(["bearer", "column", "page", "verdict", "reason", "quote"])
for b, col, page, q in rows:
    v, why = J[(b, col, page)]
    w.writerow([b, col, page, v, why, q[:120]])
from collections import Counter
print(Counter(J[(b, c, p)][0] for b, c, p, q in rows))
