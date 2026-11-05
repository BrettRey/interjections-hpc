"""Check that each quotation appears in its source, on or near the cited page.

Input: a TSV with columns source, item_id, property, value, scope, quote, page.
Sources map to page-marked texts and printed-page offsets
(printed = pdf + offset). Prints one line per row: OK, PAGE (found on
another page) or MISSING.
"""
import csv
import re
import sys
import unicodedata

HERE = sys.argv[1]
SRC = {
    "ljung2011": ("ljung2011-paged.txt", -13),
    "potts2007": ("potts2007-paged.txt", 164),
    "mccready2010": ("mccready2010-paged.txt", 0),
    "gutzmann2013": ("gutzmann2013-paged.txt", -1),
}


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("­", "")
    s = re.sub(r"[‘’‚′`´]", "'", s)
    s = re.sub(r"[“”„″]", '"', s)
    s = re.sub(r"[–—−]", "-", s)
    s = re.sub(r"-\s*\n\s*", "", s)          # line-break hyphenation
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"(\w)- (\w)", r"\1\2", s)
    return s.lower().strip()


def pages(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    parts = re.split(r"\n=== PDF page (\d+) ===\n", text)
    out = {}
    for i in range(1, len(parts) - 1, 2):
        out[int(parts[i])] = norm(parts[i + 1])
    return out


cache = {k: pages(f"{HERE}/{v[0]}") for k, v in SRC.items()}
rows = list(csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t"))
counts = {"OK": 0, "PAGE": 0, "MISSING": 0}
for r in rows:
    src, off = r["source"], SRC[r["source"]][1]
    q = norm(r["quote"].strip().strip('"'))
    # allow an ellipsis inside the quotation: every piece must be present
    pieces = [p.strip() for p in re.split(r"\.\.\.|\[\.\.\.\]|…", q) if p.strip()]
    try:
        cited = int(re.match(r"\d+", r["page"]).group()) - off
    except (AttributeError, TypeError):
        cited = None
    found = [p for p, t in cache[src].items() if all(x in t for x in pieces)]
    if not found and len(pieces) == 1:  # quotation may run across a page break
        for p in cache[src]:
            if q in (cache[src].get(p, "") + " " + cache[src].get(p + 1, "")):
                found = [p]
                break
    if cited in found or (cited is not None and cited - 1 in found and len(pieces) == 1):
        status = "OK"
    elif found:
        status = "PAGE"
    else:
        status = "MISSING"
    counts[status] += 1
    if status != "OK":
        where = ",".join(str(p + off) for p in found[:3])
        print(f"{status}\t{src}\t{r['item_id']}\t{r['property']}\tcited {r['page']}\tfound {where}\t{r['quote'][:70]}")
print(counts)
