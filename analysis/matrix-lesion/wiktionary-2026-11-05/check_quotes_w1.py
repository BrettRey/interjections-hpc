"""Check v1 rows against wiktionary-senses-v1.txt; ids can repeat, so every
block with the cited id is searched."""
import csv, re, sys, unicodedata
from collections import defaultdict
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[‘’′`´]", "'", s); s = re.sub(r"[“”″]", '"', s)
    return re.sub(r"\s+", " ", s).lower().strip()
text = open(sys.argv[1], encoding="utf-8").read()
parts = re.split(r"\n=== (W:[^=]+?) ===[^\n]*\n", text)
blocks = defaultdict(list)
for i in range(1, len(parts) - 1, 2):
    blocks[parts[i]].append(norm(parts[i + 1]))
c = {"OK": 0, "OTHER_BLOCK": 0, "MISSING": 0}
for r in csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t"):
    q = norm(r["quote"])
    if any(q in t for t in blocks.get(r["page"], [])):
        c["OK"] += 1; continue
    hit = [b for b, ts in blocks.items() if any(q in t for t in ts)]
    st = "OTHER_BLOCK" if hit else "MISSING"; c[st] += 1
    print(st, r["item_id"], r["property"], r["page"], "->", hit[:2], "|", r["quote"][:60])
print(c)
