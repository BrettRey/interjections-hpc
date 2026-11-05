"""Draft the relatedness facts (roots and word form) for items-v4 by rule.

Brett, 2026-11-05: "what about the morphology columns, which include roots.
That would link bearers". After the determinatives-as-nouns codebook
(section 1): facts at the base level are the same for every row that shares
the base, take no m, are pooled by base, and the tests run with and without
them. String identity only: analytic decompositions (blood + -y,
heaven + -s, thank + -s) are not coded. Whether the uses of one form are
one lexeme is a question for the analysis, not a rule.
Output: morphology-facts-v4.csv, for Brett to approve.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
items = list(csv.DictReader(open(os.path.join(HERE, "items-v4.csv"), encoding="utf-8")))
BASES = ["damn", "bloody", "bastard", "bang", "the", "you"]
rows = []
for it in items:
    form = it["form"].lower()
    words = form.strip("-").replace("-", " ").split() if not form.startswith("-") else [form.strip("-")]
    facts = {f"MB_{b.upper()}": b in words for b in BASES}
    facts["MW_LY"] = any(w.endswith("ly") and len(w) > 3 for w in words)
    facts["MW_PHRASAL"] = " " in form
    halves = form.split("-")
    facts["MW_REDUP"] = len(halves) == 2 and halves[0] == halves[1] and halves[0] != ""
    facts["MW_SUBWORD"] = form.startswith("-") and form.endswith("-")
    for col, v in facts.items():
        rows.append({"item_id": it["item_id"], "form": it["form"], "column": col,
                     "level": "base" if col.startswith("MB") else "word",
                     "value": "Y" if v else "N", "status": "drafted by rule, for Brett to approve"})
with open(os.path.join(HERE, "morphology-facts-v4.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
ys = {}
for r in rows:
    if r["value"] == "Y":
        ys.setdefault(r["column"], []).append(r["item_id"])
for c, v in ys.items():
    print(c, v)
