"""Build source packets for the P02 pilot column.

For each pilot item, scripted search over a fixed list of held
sources for passages mentioning the item's form together with
distribution-relevant vocabulary. Excerpts are unedited apart from
whitespace collapsing; each carries its source filename and a line
number so returned quotes can be verified. Output: packets.md
(human/auditor copy) and packets.json (per-item, for qwen batches).
"""
import json
import re
from pathlib import Path

LIT = Path("literature")
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
# whole-grammar sources: excerpt must also mention interjections
STRONG = {"00-CGEL.md",
          "quirk-et-al-1985-comprehensive-grammar-of-the-english-language.md"}
ITEMS = [
    ("OUCH", "ouch", "pain reaction", r"\bouch\b"),
    ("WOW", "wow", "amazement reaction", r"\bwow\b"),
    ("GEE", "gee", "surprise/emphasis reaction", r"\bgee\b"),
    ("DAMN_PRENOM", "damn", "prenominal modifier use, as in: the damn car",
     r"\bdamn\b"),
    ("BANG_DEPICT", "bang", "sound depiction in narrative, as in: Bang!",
     r"\bbang\b"),
    ("MMHM", "mm-hm", "continuer use in storytelling",
     r"\b(mm[- ]hm|mhm|uh[- ]huh)\b"),
    ("BLOODY_PRENOM", "bloody", "prenominal modifier use, as in: the bloody car",
     r"\bbloody\b"),
    ("COFFEE", "coffee", "the noun, including answer use (Coffee, in reply to: What would you like?)",
     r"\bcoffee\b"),
    ("STOP", "stop", "the imperative verb use, as in: Stop! Stop the car!",
     r"\bstop\b"),
    ("BLACK", "black", "the adjective, including answer use (Black, in reply to a question about colour)",
     r"\bblack\b"),
]
# distribution-relevant vocabulary that must co-occur near a form hit
KEYS = re.compile(
    r"supplement|stand.?alone|on (its|their) own|utterance|integrat|"
    r"distribution|combin|clause|sentence|modifier|adverb|noun|verb|"
    r"adject|ellip|fragment|independent|insert", re.I)
MAX_EXCERPTS_PER_SOURCE = 4
MAX_CHARS_PER_ITEM = 7000
WINDOW = 700


def excerpts(text, pattern, strong=False):
    out = []
    lines = text.splitlines()
    joined = "\n".join(lines)
    for m in re.finditer(pattern, joined, re.I):
        s = max(0, m.start() - WINDOW)
        e = min(len(joined), m.end() + WINDOW)
        seg = joined[s:e]
        if not KEYS.search(seg):
            continue
        if strong and not re.search(r"interject", seg, re.I):
            continue
        line_no = joined[:m.start()].count("\n") + 1
        seg = re.sub(r"\s+", " ", seg).strip()
        out.append((line_no, seg))
        if len(out) >= MAX_EXCERPTS_PER_SOURCE:
            break
    return out


def main():
    texts = {}
    for s in SOURCES:
        p = LIT / s
        if p.exists():
            texts[s] = p.read_text(encoding="utf-8", errors="ignore")
        else:
            print("MISSING SOURCE:", s)
    packets = {}
    md = ["# P02 pilot packets (unedited excerpts; whitespace collapsed)\n"]
    for item_id, form, gloss, pat in ITEMS:
        chunks, total = [], 0
        for s, txt in texts.items():
            for line_no, seg in excerpts(txt, pat, strong=s in STRONG):
                entry = f"[{s} line~{line_no}] ...{seg}..."
                if total + len(entry) > MAX_CHARS_PER_ITEM:
                    break
                chunks.append(entry)
                total += len(entry)
            if total > MAX_CHARS_PER_ITEM:
                break
        packet = "\n\n".join(chunks) if chunks else "(no passages found)"
        packets[item_id] = {"form": form, "use_gloss": gloss,
                            "packet": packet,
                            "n_excerpts": len(chunks), "chars": total}
        md.append(f"\n## {item_id}: {form} ({gloss})\n")
        md.append(packet)
        print(f"{item_id:14s} excerpts={len(chunks):2d} chars={total}")
    Path("analysis/matrix-lesion/pilot/packets.md").write_text(
        "\n".join(md))
    Path("analysis/matrix-lesion/pilot/packets.json").write_text(
        json.dumps(packets, indent=1))
    print("wrote packets.md / packets.json")


if __name__ == "__main__":
    main()
