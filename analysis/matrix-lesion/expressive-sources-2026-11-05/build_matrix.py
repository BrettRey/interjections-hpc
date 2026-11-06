"""Build the bearer-by-property matrix from long.csv.

Cells use item-level statements only. Class-level statements are kept
apart, because one class statement inherited across its members counts as
a single testimony unit (FREEZE-v4 section 4). Writes matrix.json (for the
page) and MATRIX.md.
"""
import csv
import json
from collections import defaultdict

P10_PATTERNS = ["adjacent", "recurring: separate events", "recurring: one event", "recurring", "pattern unrecorded"]
KINDS = [
    ("distribution", ["P01", "P02", "P03", "P04", "P06", "after wh-word", "insertion into word/phrase",
                      "degree modifier of adj/adv", "degree with gradable noun", "You X! frame",
                      "attributive", "predicative", "modifies verbs", "transitive", "catenative", "clausal form", "emphasis before non-NP", "combines into formula", "slot filler (Ljung)",
                      "host-class specialization", "creates epithet NP", "takes a modifier", "pro-form one",
                      "restricted hosts", "clause-medial position", "wh-phrase in situ", "before wh-word",
                      "wh-phrase alone", "imperative potential", "recurs at several points",
                      "modifier inside a standalone phrase"]),
    ("morphology", ["P05", "comparable", "count", "non-count", "frozen plural", "optative verb form",
                    "has homonym in other class", "delocutive noun", "delocutive verb", "no word class",
                    "historical source", "imitative or natural origin", "has ·ly adverb", "phonetically modified variants"]),
    ("meaning", ["P07D", "P08", "P09"] + [f"{b} · {pat}" for b in ("P10A", "P10S", "P10R") for pat in P10_PATTERNS] + ["repeated with and", "P11E", "Potts:independence", "Potts:nondisplaceability",
                 "Potts:perspective", "Potts:ineffability", "Potts:immediacy", "local scope", "scopeless (McCready)", "unbindable",
                 "denial-immune", "emphasis", "valence shift", "expressive strength",
                 "modifiable by expressives", "main expressive content", "takes an argument (Gutzmann)",
                 "resource-sensitive", "Gutzmann type", "attitude target", "multifunctional",
                 "utterance scope", "conative", "ironic use", "nonliteral"]),
    ("realization", ["P12S", "P12I", "P13", "P13D", "stress cue", "intonation specified", "lexical tone",
                     "stress tied to use", "host-stress conditioned", "placed before stress",
                     "lengthening, wide pitch range", "hosts a clitic"]),
    ("social and lexical", ["taboo load", "interchangeable swear word", "grammatically regular",
                            "glossed by its use", "fixed form", "formulaic"]),
]
COLKIND = {c: k for k, cs in KINDS for c in cs}
# Testimony families, counted once when the matrix counts independent sources:
# the Student's Introduction (S) abridges CGEL (H); Biber et al. 1999 (B) and
# 2021 (R) share Leech with Quirk et al. 1985 (Q) and borrow its "grammatical
# framework of concepts and terminology" "with few exceptions" (2021, p. xxxii).
FAMILY = {"S": "H", "B": "Q", "R": "Q"}  # C (COCA, hand-extracted) is its own family

# Hedges the parent added after reading the reports (reason shown on the page).
HEDGES = {
    ("DAMN_REACT", "P10S", "G"): "Potts's added tokens in (34) are all prenominal; DAMN_REACT is never repeated (Potts report).",
    ("DAMN_DEGREE", "emphasis before non-NP", "L"): "Said of damn(ed) as an emphasizer before verbs, a use not in the inventory.",
}
# AH, AHA, OH, OUCH, WOW P13 (Ljung pp. 76-77): Ljung's own statement that they are "phonologically
# regular"; no hedge since 2026-11-05 (decision call 3). Quirk 2.58 Note doesn't say it.
for c in ["P01", "P02", "P07", "P08", "takes an argument (Gutzmann)"]:
    HEDGES[("OH", c, "G")] = "Gutzmann glosses Oh! as surprise; the inventory's OH is the change-of-state or receipt use."

# Gutzmann 2013 quotations are checked against an OCR text. These were
# checked against the printed page image (p. 5, example 3) on 2026-11-05.
EX3 = "I hear your {∅ / blasted / bloody / damn / fucking} dog barking. [example (3), read from the page image]"
PAGE_CHECKED = {("BLOODY_PRENOM", "P03", "G", "5"): EX3, ("FUCKING_PRENOM", "P03", "G", "5"): EX3}
items = {r["item_id"]: r for r in csv.DictReader(open("../items-v4.csv"))}
# Every column in long.csv must have a kind, or its cells would vanish from the page.
_missing = {r["column"] for r in csv.DictReader(open("long.csv"))} - set(COLKIND) - {"P07", "P11N", "P12"}
assert not _missing, f"columns with no kind: {_missing}"
long = list(csv.DictReader(open("long.csv")))
# Convert the superseded columns to the 2026-11-05 schema (FREEZE-v4 section 6).
dropped_p11 = 0
for r in long:
    r["conv"], r["orig_column"] = "", r["column"]
    if r["column"] == "P07" and r["value"] in ("Y", "N"):
        r["column"], r["value"], r["conv"] = "P07D", {"Y": "N", "N": "Y"}[r["value"]], "converted from P07, value reversed"
    elif r["column"] == "P11N":
        if r["value"] == "N":
            r["column"], r["value"], r["conv"] = "P11E", "Y", "converted from P11N N (embedding reported)"
        else:
            r["scope"] = "dropped"
            dropped_p11 += 1
    elif r["column"] == "P12" and r["value"] in ("Y", "N"):
        r["column"], r["value"], r["conv"] = ("P12S", "Y", "converted from P12 Y") if r["value"] == "Y" else ("P12I", "Y", "converted from P12 N")
cells = defaultdict(list)
classes = []
for r in long:
    if r["scope"] == "item":
        # HEDGES may be keyed on the column before conversion (P07 for P07D): look up both.
        hedge = (HEDGES.get((r["bearer"], r["column"], r["source"])) or HEDGES.get((r["bearer"], r["orig_column"], r["source"]))
                 or HEDGES.get((r["bearer"], r["column"].split(" · ")[0], r["source"])))
        if r["hedge"] and not hedge:
            hedge = r["hedge"] if r["hedge"] != "hedged" else "Use match uncertain or evidence weak in the source report."
        q, ocr = r["quote"], r["source"] in ("G", "Q", "B")  # quotations checked against OCR text
        if (r["bearer"], r["column"], r["source"], r["page"]) in PAGE_CHECKED:
            q, ocr = PAGE_CHECKED[(r["bearer"], r["column"], r["source"], r["page"])], False
        cells[(r["bearer"], r["column"])].append(
            {"v": r["value"], "src": r["source"], "page": r["page"], "q": q, "hedge": hedge or "",
             "secondary": r["secondary"], "ocr": ocr, "conv": r["conv"], "basis": r.get("basis", "")})
    elif r["scope"] == "class":
        classes.append({"cls": r["bearer"].split("CLASS:")[-1].strip(), "col": r["column"], "v": r["value"],
                        "src": r["source"], "page": r["page"], "q": r["quote"],
                        "hedge": ("Use match uncertain or evidence weak in the source report." if r["hedge"] == "hedged" else r["hedge"]),
                        "secondary": r["secondary"], "conv": r["conv"]})

bearers = sorted({b for b, _ in cells})
for extra in ["EXACTLY_WH", "MAIN_PRENOM", "PROBABLE_PRENOM"]:
    if extra not in bearers:
        bearers.append(extra)
tier_order = {"expr-core": 0, "expr-control": 1, "core": 2, "boundary": 3, "control": 4, "extension": 5}
bearers.sort(key=lambda b: (tier_order.get(items[b]["analyst_tier"], 9), b))
cols = [c for _, cs in KINDS for c in cs if any(k[1] == c for k in cells)]

def summary(entries):
    vals = {e["v"] for e in entries}
    yn = vals & {"Y", "N"}
    v = "Y/N" if yn == {"Y", "N"} else (yn.pop() if yn else "; ".join(sorted(vals)))
    prim = sorted({e["src"] for e in entries if not e["secondary"]})
    fams = {FAMILY.get(s, s) for s in prim}
    sec = sorted({e["src"] for e in entries if e["secondary"]} - set(prim))
    srcs = prim + [s.lower() for s in sec]
    return {"v": v, "srcs": srcs, "primary": len(fams), "hedged": all(e["hedge"] for e in entries), "n": len(entries)}

out = {
    "sources": {"L": "Ljung 2011, Swearing (Palgrave)", "P": "Potts 2007, Theoretical Linguistics 33(2)",
                "M": "McCready 2010, Semantics & Pragmatics 3(8)", "G": "Gutzmann 2013, in Beyond Expressives (Brill)",
                "W": "English Wiktionary (CC BY-SA), fetched 2026-11-05",
                "H": "Huddleston & Pullum 2002, Cambridge Grammar of the English Language",
                "Q": "Quirk et al. 1985, A Comprehensive Grammar of the English Language",
                "S": "Huddleston & Pullum 2005, A Student's Introduction to English Grammar (same family as H)",
                "B": "Biber et al. 1999, Longman Grammar of Spoken and Written English, ch. 14 (OCR; same family as Q)",
                "R": "Biber et al. 2021, Grammar of Spoken and Written English, chs 7 and 14 (same family as Q)",
                "C": "COCA, lines hand-extracted by Brett 2026-11-05 (Tier B corpus attestation; analysis/hand-extracted/ouch-oops-*.md)"},
    "columns": [{"id": c, "kind": COLKIND[c]} for c in cols],
    "rows": [{"id": b, "form": items[b]["form"], "gloss": items[b]["use_gloss"], "tier": items[b]["analyst_tier"],
              "cells": {c: dict(summary(cells[(b, c)]), entries=cells[(b, c)]) for c in cols if (b, c) in cells}}
             for b in bearers],
    "classes": classes,
}
json.dump(out, open("matrix.json", "w"), ensure_ascii=False, indent=1)

with open("MATRIX.md", "w") as fh:
    fh.write("# Bearers by property, from the expressive literature, Wiktionary and five reference grammars\n")
    fh.write("<!-- SUMMARY: what Ljung 2011, Potts 2007, McCready 2010, Gutzmann 2013, English Wiktionary and five reference grammars (CGEL 2002, Student's Introduction 2005, Quirk et al. 1985, Biber et al. 1999 ch. 14, Biber et al. 2021 chs 7 and 14), plus COCA lines for repetition, state of particular bearers in items-v4, item-level statements only, every quotation string-checked; development data, not study data · status: for Brett to inspect · updated: 2026-11-05 -->\n\n")
    fh.write("Item-level statements only; class-level statements are in matrix.json and on the page. Cell: value, then sources (L Ljung, P Potts, M McCready, G Gutzmann, W Wiktionary, H CGEL, S Student's Introduction, Q Quirk et al., B Biber et al. 1999, R Biber et al. 2021, C COCA lines; H with S, and Q with B and R, each count as one testimony family); a lowercase letter means that source only reports another work there. `?` = hedged. Development data under FREEZE-v4 §9: not study data.\n\n")
    for kind, cs in KINDS:
        cs = [c for c in cs if c in cols]
        if not cs:
            continue
        fh.write(f"## {kind}\n\n| bearer | " + " | ".join(cs) + " |\n|" + "---|" * (len(cs) + 1) + "\n")
        for b in bearers:
            row = []
            for c in cs:
                if (b, c) in cells:
                    s = summary(cells[(b, c)])
                    row.append(f"{s['v']}{'?' if s['hedged'] else ''} {''.join(s['srcs'])}")
                else:
                    row.append("")
            if any(row):
                fh.write(f"| {b} | " + " | ".join(row) + " |\n")
        fh.write("\n")
allc = [summary(cells[k]) for k in cells]
stats = {"cells": len(allc), "with_primary": sum(1 for s in allc if s["primary"] >= 1),
         "with_two_primary": sum(1 for s in allc if s["primary"] >= 2),
         "primary_unhedged": sum(1 for k in cells if any(not e["secondary"] and not e["hedge"] for e in cells[k]))}
stats["dropped_old_P11N_Y"] = dropped_p11
out["stats"] = stats
json.dump(out, open("matrix.json", "w"), ensure_ascii=False, indent=1)
print(len(bearers), "bearers;", len(cols), "columns;", len(classes), "class statements;", stats)
