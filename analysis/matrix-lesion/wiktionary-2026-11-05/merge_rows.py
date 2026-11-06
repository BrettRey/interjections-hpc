"""Merge the checked Wiktionary rows (v1 against the v1 text, v2 against the
template-expanded v2 text) into one rows-wiktionary.tsv for the matrix,
applying the parent's settlements of the agents' flags (2026-11-05):
- comparability rows that rest only on the template's default output are
  dropped (no editor asserted them);
- v1's Middle English P02 row for AH is dropped (v2 gives a modern example);
- rows the agents marked conditional, candidate, weaker, neighbour or for
  Brett's call are hedged, with the reason kept in the note;
- P01 from editor-constructed examples is hedged (P01's note excludes
  solitary occurrences; whether a constructed example counts is Brett's).
"""
import csv, re, sys
HEDGE = re.compile(r"your call|Holds only if|holds only if|Conditional|conditional|candidate|rival|[Ww]eaker|Applies only if|"
                   r"Drop this row if|I'd drop|neighbour|alternative match|Brett needs to decide|Constructed EXAMPLE|prefer U|"
                   r"admissible for the modern use only")
out = csv.writer(sys.stdout, delimiter="\t")
out.writerow(["source", "item_id", "property", "value", "scope", "quote", "page", "note"])
dropped = 0
for path, tag in [(sys.argv[1], "v1"), (sys.argv[2], "v2"), (sys.argv[3], "v2")]:
    for r in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"):
        note = r["note"]
        if "Template default" in note or (r["item_id"] == "AH" and r["quote"].startswith("Earliest recorded use")):
            dropped += 1
            continue
        v = r["value"]
        if HEDGE.search(note + " " + r["scope"]) and "hedged" not in v:
            v = v + " (hedged)"
        out.writerow(["wiktionary", r["item_id"], r["property"], v, r["scope"], r["quote"],
                      ("" if tag == "v2" else "v1 ") + r["page"], note])
print("dropped", dropped, file=sys.stderr)
