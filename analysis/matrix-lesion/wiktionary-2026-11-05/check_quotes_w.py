"""String-check Wiktionary quotations against the block they cite in
wiktionary-senses.txt. Input TSV: source, item_id, property, value, scope,
quote, page (the block id). Prints non-OK rows and a tally."""
import csv, re, sys, unicodedata
HERE = sys.argv[1]

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[‘’′`´]", "'", s); s = re.sub(r"[“”″]", '"', s)
    s = re.sub(r"[–—−]", "-", s)
    return re.sub(r"\s+", " ", s).lower().strip()

text = open(sys.argv[3] if len(sys.argv) > 3 else f"{HERE}/wiktionary-senses-v2.txt", encoding="utf-8").read()
parts = re.split(r"\n=== (W:[^=]+?) ===[^\n]*\n", text)
blocks = {parts[i]: norm(parts[i + 1]) for i in range(1, len(parts) - 1, 2)}
counts = {"OK": 0, "OTHER_BLOCK": 0, "MISSING": 0}
for r in csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t"):
    q = norm(r["quote"].strip().strip('"'))
    pieces = [p.strip() for p in re.split(r"\.\.\.|…", q) if p.strip()]
    bid = r["page"].strip().strip("`")
    ok = bid in blocks and all(p in blocks[bid] for p in pieces)
    if ok:
        counts["OK"] += 1; continue
    found = [b for b, t in blocks.items() if all(p in t for p in pieces)]
    st = "OTHER_BLOCK" if found else "MISSING"
    counts[st] += 1
    print(f"{st}\t{r['item_id']}\t{r['property']}\tcited {bid}\tfound {','.join(found[:2])}\t{r['quote'][:70]}")
print(counts)
