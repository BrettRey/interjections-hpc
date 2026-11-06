"""Turn the Wiktionary extraction reports into TSV rows (source, item_id,
property, value, scope, quote, page, note) for checking and the matrix.
Handles straight-quoted and guillemet-quoted tables and locators written as
'block id @line' or with 'Lnnn' in the note."""
import csv, re, sys
w = csv.writer(sys.stdout, delimiter="\t")
w.writerow(["source", "item_id", "property", "value", "scope", "quote", "page", "note"])
for path in sys.argv[1:]:
    last = ""
    for line in open(path, encoding="utf-8"):
        if " | " not in line or re.match(r"^\|?\s*-{3}", line) or line.lower().startswith(("item_id", "| item_id")):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) < 6:
            continue
        item, prop, val, scope, quote, loc = cells[:6]
        note = " | ".join(cells[6:])
        qs = re.findall(r"«(.+?)»", quote) or re.findall(r'"(.+)"', quote)
        if not qs and "same quotation" in quote:
            qs = [last]
        if not qs:
            continue
        last = qs[0]
        bid = re.split(r"\s+@|\s+\(", loc.strip("`"))[0].strip()
        for q in qs:
            w.writerow(["wiktionary", item, prop, val, scope, q, bid, note])
