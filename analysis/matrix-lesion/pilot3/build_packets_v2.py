"""Build relevance-ranked P02 packet v2 for the same pilot items.

Changes from pilot 1/2 packets:
- candidate windows are generated around both item forms and
  distributional-behaviour expressions, then relevance-ranked rather
  than accepted in source order;
- overlapping windows from one source are merged, removing repeated
  copies of the same passage;
- bibliography-like windows are penalized;
- selection round-robins across sources;
- excerpts are split into item-form evidence and no-form,
  class/context evidence;
- locations include the nearest markdown section heading.

Quotes remain unedited apart from whitespace collapsing.
"""
import json
import re
from pathlib import Path

LIT = Path("literature")
OUT = Path("analysis/matrix-lesion/pilot3")
SOURCES = [
    "ameka1992-interjections.md",
    "wilkins1992.md",
    "dingemanse_2023_interjections-handbook-preprint.md",
    "dingemanse_2024_interjections-heart-of-language.md",
    "heine_2023_grammar-of-interactives_ch1.md",
    "heine_2023_grammar-of-interactives_ch2.md",
    "stange_2016_emotive-interjections-ch4.md",
    "libert_2019_interjections-obo.md",
    "norrick_2009_interjections-pragmatic-markers.md",
    "gehweiler2008-gee.md",
    "00-CGEL.md",
    "quirk-et-al-1985-comprehensive-grammar-of-the-english-language.md",
]
ITEMS = [
    ("OUCH", "ouch", "pain reaction", r"\bouch\b"),
    ("WOW", "wow", "amazement reaction", r"\bwow\b"),
    ("GEE", "gee", "surprise/emphasis reaction", r"\bgee\b"),
    ("DAMN_PRENOM", "damn",
     "prenominal modifier use, as in: the damn car", r"\bdamn\b"),
    ("BANG_DEPICT", "bang",
     "sound depiction in narrative, as in: Bang!", r"\bbang\b"),
    ("MMHM", "mm-hm", "continuer use in storytelling",
     r"\b(mm[- ]hm|mhm|uh[- ]huh)\b"),
    ("BLOODY_PRENOM", "bloody",
     "prenominal modifier use, as in: the bloody car", r"\bbloody\b"),
    ("COFFEE", "coffee",
     "the noun, including answer use (Coffee, in reply to: What would you like?)",
     r"\bcoffee\b"),
    ("STOP", "stop",
     "the imperative verb use, as in: Stop! Stop the car!",
     r"\bstop\b"),
    ("BLACK", "black",
     "the adjective, including answer use (Black, in reply to a question about colour)",
     r"\bblack\b"),
]
BEHAVIOUR = [
    (r"co-utterance", 6), (r"supplement", 5),
    (r"enter(?:s|ing)? into construction", 5),
    (r"not (?:normally )?(?:integrated|enter)", 4),
    (r"constitute an utterance", 4),
    (r"stand(?:s|ing)? alone|on (?:its|their) own", 3),
    (r"independent utterance|separate utterance", 3),
    (r"integrated (?:syntactic )?construction", 4),
    (r"syntactically independent|not integrated", 4),
    (r"structural slot", 3), (r"distribution", 2),
    (r"clausal anchor|anchor", 2), (r"interject", 2),
    (r"one-word utterance", 3), (r"accompan", 1),
]
BEHAVIOUR_RX = [(re.compile(p, re.I), w) for p, w in BEHAVIOUR]
CLASS_RX = re.compile(r"primary interjections|interjection category|"
                      r"class of interjections|interactives", re.I)
WINDOW = 550
MAX_FORM_CHARS = 8000
MAX_CLASS_CHARS = 2400
MAX_PER_SOURCE = 3


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


def nearest_heading(lines, line_no):
    for i in range(min(line_no, len(lines)) - 1, -1, -1):
        s = lines[i].strip()
        if s.startswith("#"):
            return collapse(s.lstrip("# "))[:90]
        if re.match(r"^(\d+(?:\.\d+)*\.?|[A-Z][A-Za-z ]{3,60})$", s) \
                and len(s) < 90 and i > 0:
            # conservative: only numbered or all-caps headings
            if re.match(r"^\d+(?:\.\d+)*\.?\s+\S", s) or s.isupper():
                return collapse(s)[:90]
    return "no heading found"


def score(seg, has_form):
    total = 6.0 if has_form else 0.0
    for rx, w in BEHAVIOUR_RX:
        total += w * min(len(rx.findall(seg)), 3)
    if CLASS_RX.search(seg):
        total += 3
    biblio = len(re.findall(r"\b(19|20)\d\d\b|doi:|journal|routledge|"
                            r"cambridge university press", seg, re.I))
    if biblio >= 4:
        total -= 8
    elif biblio >= 2:
        total -= 3
    return total


def candidates(text, pattern):
    joined = text
    centers = []
    for m in re.finditer(pattern, joined, re.I):
        centers.append((m.start(), True))
    for rx, _w in BEHAVIOUR_RX:
        for m in rx.finditer(joined):
            centers.append((m.start(), False))
    raw = []
    for pos, is_form_center in centers:
        s, e = max(0, pos - WINDOW), min(len(joined), pos + WINDOW)
        seg = joined[s:e]
        has_form = bool(re.search(pattern, seg, re.I))
        if not has_form and not CLASS_RX.search(seg):
            continue
        sc = score(seg, has_form)
        if sc < (8 if has_form else 11):
            continue
        raw.append({"start": s, "end": e, "score": sc,
                    "has_form": has_form})
    raw.sort(key=lambda c: (c["start"], -c["score"]))
    merged = []
    for c in raw:
        if merged and c["start"] <= merged[-1]["end"]:
            last = merged[-1]
            last["end"] = max(last["end"], c["end"])
            last["score"] = max(last["score"], c["score"])
            last["has_form"] = last["has_form"] or c["has_form"]
        else:
            merged.append(dict(c))
    return merged


def select(cands, char_cap, per_source=MAX_PER_SOURCE):
    """Round-robin by each source's best remaining candidate."""
    by_source = {}
    for c in cands:
        by_source.setdefault(c["source"], []).append(c)
    for v in by_source.values():
        v.sort(key=lambda c: -c["score"])
    chosen, total = [], 0
    while True:
        progressed = False
        sources = sorted(by_source,
                         key=lambda s: -(by_source[s][0]["score"]
                                         if by_source[s] else -999))
        for s in sources:
            if not by_source[s]:
                continue
            if sum(1 for c in chosen if c["source"] == s) >= per_source:
                by_source[s] = []
                continue
            c = by_source[s].pop(0)
            entry_len = len(c["entry"])
            if total + entry_len > char_cap and chosen:
                continue
            chosen.append(c)
            total += entry_len
            progressed = True
            if total >= char_cap:
                break
        if not progressed or total >= char_cap:
            break
    return chosen, total


def main():
    texts, lines_by_source = {}, {}
    for s in SOURCES:
        p = LIT / s
        if not p.exists():
            print("MISSING SOURCE:", s)
            continue
        texts[s] = p.read_text(encoding="utf-8", errors="ignore")
        lines_by_source[s] = texts[s].splitlines()

    packets = {}
    md = ["# P02 packet v2 (relevance-ranked; excerpts unedited apart "
          "from whitespace collapsing)\n"]
    for item_id, form, gloss, pat in ITEMS:
        form_c, class_c = [], []
        for src, txt in texts.items():
            lines = lines_by_source[src]
            for c in candidates(txt, pat):
                seg = collapse(txt[c["start"]:c["end"]])
                line_no = txt[:c["start"]].count("\n") + 1
                heading = nearest_heading(lines, line_no)
                entry = (f"[{src} line~{line_no}; section: {heading}; "
                         f"score {c['score']:.0f}] ...{seg}...")
                rec = {"source": src, "score": c["score"],
                       "entry": entry}
                (form_c if c["has_form"] else class_c).append(rec)
        chosen_f, total_f = select(form_c, MAX_FORM_CHARS)
        chosen_c, total_c = select(class_c, MAX_CLASS_CHARS)
        parts = []
        if chosen_f:
            parts.append("ITEM-FORM EVIDENCE:\n" +
                         "\n\n".join(c["entry"] for c in chosen_f))
        if chosen_c:
            parts.append("CLASS/CONTEXT PASSAGES (item form not in "
                         "passage):\n" +
                         "\n\n".join(c["entry"] for c in chosen_c))
        packet = "\n\n".join(parts) if parts else "(no passages found)"
        packets[item_id] = {
            "form": form, "use_gloss": gloss, "packet": packet,
            "n_excerpts": len(chosen_f) + len(chosen_c),
            "n_form_excerpts": len(chosen_f),
            "n_class_excerpts": len(chosen_c),
            "chars": total_f + total_c,
            "sources": sorted({c["source"] for c in
                                chosen_f + chosen_c})}
        md.append(f"\n## {item_id}: {form} ({gloss})\n")
        md.append(packet)
        print(f"{item_id:14s} form={len(chosen_f)} class="
              f"{len(chosen_c)} chars={total_f + total_c} "
              f"sources={len(packets[item_id]['sources'])}")
    (OUT / "packets-v2.md").write_text("\n".join(md))
    (OUT / "packets-v2.json").write_text(json.dumps(packets, indent=1))
    print("wrote packets-v2.md / packets-v2.json")


if __name__ == "__main__":
    main()
