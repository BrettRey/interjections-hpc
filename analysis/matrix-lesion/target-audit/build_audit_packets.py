"""Build property-siloed packets for the discarded target audit.

Packets are retrieval artifacts only. They are not study data and no
value in them may be imported into a later production matrix.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path("analysis/matrix-lesion")
OUT = ROOT / "target-audit"
LIT = Path("literature")

COMMON = [
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
SOURCES = {
    "P12": COMMON + [
        "dingemanse_2018_redrawing-margins-ideophones.md",
        "dingemanse-akita_2017_inverse-relation-expressiveness-integration.md",
    ],
    "P10": COMMON + [
        "Potts - 2007 - The expressive dimension.md",
        "dingemanse_2018_redrawing-margins-ideophones.md",
        "dingemanse-akita_2017_inverse-relation-expressiveness-integration.md",
        "Gonzalez-Diaz-2018-old-old-story-intensificatory-repetition.md",
    ],
    "P11": COMMON + [
        "Potts - 2007 - The expressive dimension.md",
        "Kaplan - 1999 - The meaning of ouch and oops.md",
        "wharton2000-showing-saying-continuum.md",
    ],
}
PATTERNS = {
    "OUCH": r"\bouch\b", "WOW": r"\bwow\b", "GEE": r"\bgee\b",
    "DAMN_REACT": r"\bdamn\b", "DAMN_PRENOM": r"\bdamn\b",
    "BANG_DEPICT": r"\bbang\b",
    "MMHM": r"\b(mm[- ]hm|mhm|uh[- ]huh)\b",
    "HUH": r"\bhuh\b", "OKAY": r"\b(okay|ok)\b",
    "BLOODY_PRENOM": r"\bbloody\b", "COFFEE": r"\bcoffee\b",
    "STOP": r"\bstop\b",
}
CONCEPTS = {
    "P12": [(r"intonation(?:al|ally)? (?:unit|phrase|separat|integrat)", 6),
            (r"separate (?:intonation|prosod)", 6),
            (r"prosodically (?:separate|independent|detached|integrated)", 6),
            (r"supplement", 4), (r"pitch|tone contour|intonation", 3),
            (r"prosodic boundary|set off|detached|parenthetical", 3),
            (r"co-utterance|enter(?:s|ing)? into construction", 3),
            (r"host|anchor|clause", 1)],
    "P10": [(r"repetition|repeated|repeatability", 6),
            (r"reduplicat", 6), (r"multiple events|event plurality", 5),
            (r"iterative|iteration|again and again", 4),
            (r"accumulat", 4), (r"lengthening|prolong", 4),
            (r"intensif|strengthen|stronger", 3),
            (r"redundant|unavailable|cannot be repeated", 3),
            (r"event", 1)],
    "P11": [(r"scope of negation|under negation|negation.*scope", 7),
            (r"surviv.*negation|outside.*scope|scope.*outside", 6),
            (r"nondisplaceab|independence", 4),
            (r"negat(?:ion|ive|ed)", 4), (r"denied|denial", 3),
            (r"scope-bearing|scope", 3),
            (r"embedded|embedding", 2), (r"not\b", 1)],
}
CLASS_RX = re.compile(
    r"primary interjections|interjection category|class of interjections|"
    r"interactives|expressives|expressive(s| items| expressions)?", re.I)
BIBLIO_RX = re.compile(
    r"doi:|journal|routledge|cambridge university press|oxford university press",
    re.I)
WINDOW = 700
MAX_FORM_CHARS = 9000
MAX_CLASS_CHARS = 2600
MAX_PER_SOURCE = 3


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


def nearest_context(lines, line_no):
    heading = "no heading found"
    caption = None
    page = None
    for i in range(min(line_no, len(lines)) - 1, max(-1, line_no - 350), -1):
        s = collapse(lines[i])
        if caption is None and re.search(
                r"\bTable\b|\bFigure\b|\bSiwu\b|\bJapanese\b|\bEnglish\b", s):
            if len(s) < 240:
                caption = s
        if heading == "no heading found":
            if s.startswith("#"):
                heading = collapse(s.lstrip("# "))[:100]
            elif re.match(r"^\d+(?:\.\d+)*\.?\s+\S", s) and len(s) < 100:
                heading = s
        if page is None and re.fullmatch(r"\d{2,4}", s):
            page = s
        if heading != "no heading found" and caption and page:
            break
    bits = [f"section: {heading}"]
    if caption:
        bits.append(f"nearby caption/context: {caption}")
    if page:
        bits.append(f"printed page nearby: {page}")
    return "; ".join(bits)


def score(seg, has_form, prop):
    total = 6.0 if has_form else 0.0
    for pat, w in CONCEPTS[prop]:
        total += w * min(len(re.findall(pat, seg, re.I)), 3)
    if CLASS_RX.search(seg):
        total += 3
    biblio = len(BIBLIO_RX.findall(seg))
    total -= 8 if biblio >= 3 else 3 if biblio == 2 else 0
    return total


def candidates(text, pattern, prop, form_word):
    form_rx = re.compile(pattern, re.I)
    centers = [(m.start(), True) for m in form_rx.finditer(text)]
    repeated_rx = re.compile(
        rf"\b{re.escape(form_word)}\W+(?:\w+\W+){{0,2}}?"
        rf"{re.escape(form_word)}\b", re.I)
    if prop == "P10":
        centers += [(m.start(), True) for m in repeated_rx.finditer(text)]
    for pat, _w in CONCEPTS[prop]:
        centers += [(m.start(), False)
                    for m in re.finditer(pat, text, re.I)]
    raw = []
    for pos, _ in centers:
        s, e = max(0, pos - WINDOW), min(len(text), pos + WINDOW)
        seg = text[s:e]
        has_form = bool(form_rx.search(seg))
        if not has_form and not CLASS_RX.search(seg):
            continue
        if prop == "P11" and not re.search(
                r"negat|scope|nondisplaceab|independence", seg, re.I):
            continue
        sc = score(seg, has_form, prop)
        if prop == "P10" and repeated_rx.search(seg):
            sc += 5
        if sc < (8 if has_form else 12):
            continue
        raw.append({"start": s, "end": e, "score": sc,
                    "has_form": has_form})
    raw.sort(key=lambda c: (c["start"], -c["score"]))
    merged = []
    for c in raw:
        if merged and c["start"] <= merged[-1]["end"] \
                and max(merged[-1]["end"], c["end"]) \
                - merged[-1]["start"] <= 2400:
            last = merged[-1]
            last["end"] = max(last["end"], c["end"])
            last["score"] = max(last["score"], c["score"])
            last["has_form"] = last["has_form"] or c["has_form"]
        else:
            merged.append(dict(c))
    return merged


def select(cands, cap):
    by_source = {}
    for c in cands:
        by_source.setdefault(c["source"], []).append(c)
    for vals in by_source.values():
        vals.sort(key=lambda c: -c["score"])
    chosen, total = [], 0
    while True:
        progressed = False
        sources = sorted(
            by_source,
            key=lambda s: -(by_source[s][0]["score"]
                            if by_source[s] else -999))
        for src in sources:
            if not by_source[src]:
                continue
            if sum(c["source"] == src for c in chosen) >= MAX_PER_SOURCE:
                by_source[src] = []
                continue
            c = by_source[src].pop(0)
            if chosen and total + len(c["entry"]) > cap:
                continue
            chosen.append(c)
            total += len(c["entry"])
            progressed = True
            if total >= cap:
                break
        if not progressed or total >= cap:
            break
    return chosen, total


def inventory():
    rows = {r["item_id"]: r for r in csv.DictReader(
        open(ROOT / "items.csv"))}
    return [(r["item_id"], rows[r["item_id"]])
            for r in csv.DictReader(open(OUT / "sample.csv"))]


def main():
    texts, line_maps = {}, {}
    all_sources = sorted({s for vals in SOURCES.values() for s in vals})
    for src in all_sources:
        p = LIT / src
        if not p.exists():
            print("MISSING SOURCE:", src)
            continue
        texts[src] = p.read_text(encoding="utf-8", errors="ignore")
        line_maps[src] = texts[src].splitlines()

    packets = {}
    md = ["# Target-audit packet set (v3 retrieval; discarded audit only)\n"]
    for prop in ("P10", "P11", "P12"):
        packets[prop] = {}
        md.append(f"\n# {prop}\n")
        for item_id, item in inventory():
            form_c, class_c = [], []
            for src in SOURCES[prop]:
                if src not in texts:
                    continue
                txt, lines = texts[src], line_maps[src]
                for c in candidates(txt, PATTERNS[item_id], prop,
                                    item["form"]):
                    line_no = txt[:c["start"]].count("\n") + 1
                    seg = collapse(txt[c["start"]:c["end"]])
                    context = nearest_context(lines, line_no)
                    entry = (f"[{src} line~{line_no}; {context}; "
                             f"score {c['score']:.0f}] ...{seg}...")
                    rec = {"source": src, "score": c["score"],
                           "entry": entry}
                    (form_c if c["has_form"] else class_c).append(rec)
            chosen_f, total_f = select(form_c, MAX_FORM_CHARS)
            chosen_c, total_c = select(class_c, MAX_CLASS_CHARS)
            parts = []
            if chosen_f:
                parts.append("ITEM-FORM EVIDENCE:\n" + "\n\n".join(
                    c["entry"] for c in chosen_f))
            if chosen_c:
                parts.append("CLASS/CONTEXT PASSAGES (item form not in "
                             "passage):\n" + "\n\n".join(
                                 c["entry"] for c in chosen_c))
            packet = "\n\n".join(parts) if parts else "(no passages found)"
            packets[prop][item_id] = {
                "form": item["form"], "use_gloss": item["use_gloss"],
                "packet": packet,
                "n_excerpts": len(chosen_f) + len(chosen_c),
                "n_form_excerpts": len(chosen_f),
                "n_class_excerpts": len(chosen_c),
                "chars": total_f + total_c,
                "sources": sorted({c["source"] for c in
                                    chosen_f + chosen_c})}
            md.append(f"\n## {prop} / {item_id}: {item['form']} "
                      f"({item['use_gloss']})\n")
            md.append(packet)
            print(f"{prop} {item_id:14s} form={len(chosen_f)} "
                  f"class={len(chosen_c)} chars={total_f + total_c} "
                  f"sources={len(packets[prop][item_id]['sources'])}")
    (OUT / "packets-v3.md").write_text("\n".join(md))
    (OUT / "packets-v3.json").write_text(json.dumps(packets, indent=1))
    print("wrote packets-v3.md / packets-v3.json")


if __name__ == "__main__":
    main()
