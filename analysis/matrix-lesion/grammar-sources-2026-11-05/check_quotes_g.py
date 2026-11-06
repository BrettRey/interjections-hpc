"""Check grammar-report quotations against page-marked source text.

Usage: python3 check_quotes_g.py SOURCES_DIR rows.tsv
rows.tsv columns: source, item_id, property, value, scope, quote, page, note.
Sources with a fixed offset (printed = pdf + offset) are checked against the
cited page. Quirk 1985 and the Biber 1999 OCR have no fixed offset, so for
them a quotation passes when the cited printed page number appears in the
first or last lines (the running heads) of a page that contains it.
Prints OK / PAGE / MISSING per row and a count.

Since 2026-11-05 (decision call 4): pieces must appear in order, a quotation
joined with an ellipsis fails (ELLIPSIS; FREEZE-v4 line 504), several spans are
allowed only when marked "[span N, role]", a trailing "[...]" basis note is
stripped before checking, and a quotation read from the page image is reported
as IMAGE (checked by eye, not by string). Quirk is checked against single-page
crops of its two-page spreads (quirk1985-split.txt), because the spread OCR
interleaves the facing page's lines.
"""
import csv, re, sys, unicodedata

D = sys.argv[1]
LIT = "/Users/brettreynolds/projects/LLM-CLI-projects/literature"
SRC = {
    "cgel2002": (f"{D}/cgel2002-paged.txt", r"\n=== PDF page (\d+) ===\n", -20),
    "quirk1985": (f"{D}/quirk1985-split.txt", r"\n=== PDF page (\d+ (?:left|right)) ===\n", None),
    "sie2005": (f"{D}/sie2005-paged.txt", r"\n=== PDF page (\d+) ===\n", -8),
    "biber1999": (f"{LIT}/biber1999-lgswe-inserts-ocr.txt", r"\n?===== PDF page (\d+) \(two-page spread\) =====\n", None),
    "biber2021c07": (f"{D}/biber2021-c07-paged.txt", r"\n=== PDF page (\d+) ===\n", 499),
    "biber2021c14": (f"{D}/biber2021-c14-paged.txt", r"\n=== PDF page (\d+) ===\n", 1029),
}

def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("­", "")
    s = re.sub(r"[‘’‚′`´]", "'", s)
    s = re.sub(r"[“”„″]", '"', s)
    s = re.sub(r"[–—−]", "-", s)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"(\w)- (\w)", r"\1\2", s)
    return s.lower().strip()

cache, heads = {}, {}
def load(src):
    if src in cache:
        return
    path, marker, _ = SRC[src]
    parts = re.split(marker, "\n" + open(path, encoding="utf-8", errors="replace").read())
    cache[src], heads[src] = {}, {}
    for i in range(1, len(parts) - 1, 2):
        k = parts[i].split()
        p = (int(k[0]), k[1]) if len(k) == 2 else int(k[0])
        body = parts[i + 1]
        cache[src][p] = norm(body)
        lines = [l for l in body.splitlines() if l.strip()]
        heads[src][p] = set(re.findall(r"\b(\d{1,4})\b", " ".join(lines[:4] + lines[-3:])))

def nxt(p):
    if isinstance(p, tuple):
        return (p[0], "right") if p[1] == "left" else (p[0] + 1, "left")
    return p + 1

def in_order(t, pieces):
    pos = 0
    for x in pieces:
        j = t.find(x, pos)
        if j < 0:
            return False
        pos = j + len(x)
    return True

rows = list(csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t"))
counts = {"OK": 0, "PAGE": 0, "MISSING": 0, "ELLIPSIS": 0, "IMAGE": 0}
for r in rows:
    src = r["source"]
    load(src)
    off = SRC[src][2]
    raw = r["quote"].strip().strip('"')
    basis = re.search(r"\[(single-page OCR crop|page image|read from the page image).*\]\s*$", raw)
    raw = raw[:basis.start()].strip() if basis else raw
    if re.search(r"\.\.\.|\[\.\.\.\]|…|\. \. \.", raw):
        counts["ELLIPSIS"] += 1
        print(f"ELLIPSIS\t{src}\t{r['item_id']}\t{r['property']}\tcited {r['page']}\t{raw[:80]}")
        continue
    if basis and "image" in basis.group(1):
        counts["IMAGE"] += 1
        continue
    q = norm(raw)
    pieces = [x.strip(" .") for x in re.split(r"\[span \d+[^\]]*\]", q) if x.strip(" .")]
    m = re.search(r"\d+", r["page"] or "")
    cited = int(m.group()) if m else None
    found = [p for p, t in cache[src].items() if in_order(t, pieces)]
    if not found and len(pieces) == 1:
        for p in cache[src]:
            if q in cache[src][p] + " " + cache[src].get(nxt(p), ""):
                found = [p]
                break
    if off is not None:
        ok = cited is not None and (cited - off in found or (cited - off - 1 in found))
        where = ",".join(str(p + off) for p in found[:3])
    else:
        ok = cited is not None and any(str(cited) in heads[src][p] or str(cited - 1) in heads[src][p] for p in found)
        where = ",".join(f"pdf{p}(heads {'/'.join(sorted(heads[src][p]))[:30]})" for p in found[:2])
        if not ok and isinstance(found[0] if found else None, tuple):  # a half page may carry no running head
            ok = any(str(cited) in heads[src].get(q2, set()) or str(cited - 1) in heads[src].get(q2, set())
                     for p in found for q2 in (p, (p[0], "left"), (p[0], "right")))
    status = "OK" if ok else "PAGE" if found else "MISSING"
    counts[status] += 1
    if status != "OK":
        print(f"{status}\t{src}\t{r['item_id']}\t{r['property']}\tcited {r['page']}\tfound {where}\t{r['quote'][:80]}")
print(counts)
