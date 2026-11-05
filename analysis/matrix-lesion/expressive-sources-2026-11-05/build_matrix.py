"""Build the bearer-by-property matrix from long.csv.

Cells use item-level statements only. Class-level statements are kept
apart, because one class statement inherited across its members counts as
a single testimony unit (FREEZE-v4 section 4). Writes matrix.json (for the
page) and MATRIX.md.
"""
import csv
import json
from collections import defaultdict

KINDS = [
    ("distribution", ["P01", "P02", "P03", "P04", "after wh-word", "insertion into word/phrase",
                      "degree modifier of adj/adv", "degree with gradable noun", "You X! frame",
                      "emphasis before non-NP", "combines into formula", "slot filler (Ljung)",
                      "host-class specialization", "creates epithet NP"]),
    ("morphology", ["optative verb form", "has homonym in other class", "no word class"]),
    ("meaning", ["P07", "P08", "P10S", "P11N", "Potts:independence", "Potts:nondisplaceability",
                 "Potts:perspective", "Potts:ineffability", "scopeless (McCready)", "unbindable",
                 "denial-immune", "emphasis", "valence shift", "expressive strength",
                 "modifiable by expressives", "main expressive content", "takes an argument (Gutzmann)",
                 "resource-sensitive", "Gutzmann type", "attitude target", "multifunctional"]),
    ("realization", ["P13", "stress cue"]),
    ("social and lexical", ["taboo load", "interchangeable swear word", "grammatically regular"]),
]
COLKIND = {c: k for k, cs in KINDS for c in cs}

# Hedges the parent added after reading the reports (reason shown on the page).
HEDGES = {
    ("DAMN_REACT", "P10S", "G"): "Potts's added tokens in (34) are all prenominal; DAMN_REACT is never repeated (Potts report).",
    ("DAMN_DEGREE", "emphasis before non-NP", "L"): "Said of damn(ed) as an emphasizer before verbs, a use not in the inventory.",
}
for b in ["AH", "AHA", "OH", "OUCH", "WOW"]:
    HEDGES[(b, "P13", "L")] = "Ljung reporting Quirk et al.; no forms transcribed, so P13's N standard may not be met."
for c in ["P01", "P02", "P07", "P08", "takes an argument (Gutzmann)"]:
    HEDGES[("OH", c, "G")] = "Gutzmann glosses Oh! as surprise; the inventory's OH is the change-of-state or receipt use."

# Gutzmann 2013 quotations are checked against an OCR text. These were
# checked against the printed page image (p. 5, example 3) on 2026-11-05.
EX3 = "I hear your {∅ / blasted / bloody / damn / fucking} dog barking. [example (3), read from the page image]"
PAGE_CHECKED = {("BLOODY_PRENOM", "P03", "G", "5"): EX3, ("FUCKING_PRENOM", "P03", "G", "5"): EX3}
items = {r["item_id"]: r for r in csv.DictReader(open("../items-v4.csv"))}
long = list(csv.DictReader(open("long.csv")))
cells = defaultdict(list)
classes = []
for r in long:
    if r["scope"] == "item":
        hedge = HEDGES.get((r["bearer"], r["column"], r["source"]))
        if r["hedge"] and not hedge:
            hedge = "Use match uncertain or evidence weak in the source report."
        q, ocr = r["quote"], r["source"] == "G"
        if (r["bearer"], r["column"], r["source"], r["page"]) in PAGE_CHECKED:
            q, ocr = PAGE_CHECKED[(r["bearer"], r["column"], r["source"], r["page"])], False
        cells[(r["bearer"], r["column"])].append(
            {"v": r["value"], "src": r["source"], "page": r["page"], "q": q, "hedge": hedge or "",
             "secondary": r["secondary"], "ocr": ocr})
    elif r["scope"] == "class":
        classes.append({"cls": r["bearer"].split("CLASS:")[-1].strip(), "col": r["column"], "v": r["value"],
                        "src": r["source"], "page": r["page"], "q": r["quote"]})

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
    sec = sorted({e["src"] for e in entries if e["secondary"]} - set(prim))
    srcs = prim + [s.lower() for s in sec]
    return {"v": v, "srcs": srcs, "primary": len(prim), "hedged": all(e["hedge"] for e in entries), "n": len(entries)}

out = {
    "sources": {"L": "Ljung 2011, Swearing (Palgrave)", "P": "Potts 2007, Theoretical Linguistics 33(2)",
                "M": "McCready 2010, Semantics & Pragmatics 3(8)", "G": "Gutzmann 2013, in Beyond Expressives (Brill)"},
    "columns": [{"id": c, "kind": COLKIND[c]} for c in cols],
    "rows": [{"id": b, "form": items[b]["form"], "gloss": items[b]["use_gloss"], "tier": items[b]["analyst_tier"],
              "cells": {c: dict(summary(cells[(b, c)]), entries=cells[(b, c)]) for c in cols if (b, c) in cells}}
             for b in bearers],
    "classes": classes,
}
json.dump(out, open("matrix.json", "w"), ensure_ascii=False, indent=1)

with open("MATRIX.md", "w") as fh:
    fh.write("# Expressive bearers by property, from four sources\n")
    fh.write("<!-- SUMMARY: what Ljung 2011, Potts 2007, McCready 2010 and Gutzmann 2013 state of particular bearers in items-v4, item-level statements only, every quotation string-checked; development data, not study data · status: for Brett to inspect · updated: 2026-11-05 -->\n\n")
    fh.write("Item-level statements only; class-level statements are in matrix.json and on the page. Cell: value, then sources (L Ljung, P Potts, M McCready, G Gutzmann); a lowercase letter means that source only reports another work there. `?` = hedged. Development data under FREEZE-v4 §9: not study data.\n\n")
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
out["stats"] = stats
json.dump(out, open("matrix.json", "w"), ensure_ascii=False, indent=1)
print(len(bearers), "bearers;", len(cols), "columns;", len(classes), "class statements;", stats)
