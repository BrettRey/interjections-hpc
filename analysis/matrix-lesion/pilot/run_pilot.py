"""Run the P02 pilot column through the coder families.

Blind by construction: each prompt contains one property definition,
its negative standard, and source packets per item. No other property,
no hypothesis, no item tiers. Items shuffled with a per-family seed.
Raw outputs are saved verbatim under codings/ before any parsing.

Families: agy (print mode), copilot (-p), qwen3.8:27b via the local
Ollama HTTP API (per-item calls: its 8192-context configuration in
the portfolio profile cannot take the whole column). The fourth
coder (Muse subagent) is dispatched separately with prompt-claude.txt.
"""
import json
import random
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

BASE = Path("analysis/matrix-lesion/pilot")
PACKETS = json.loads((BASE / "packets.json").read_text())

DEFINITION = """PROPERTY P02 (SUPPLEMENT).
In this use, the sign can function as a supplement to an intact clausal
or nominal anchor (supplement in the CGEL sense: outside the integrated
syntactic structure, with the anchor complete without it; compare the
interjection in "Ah, so you were there after all!", the relative clause
in "We called in to see Sue's parents, which made us rather late", and
the noun phrase in "A university lecturer, Dr Brown, was arrested").

VALUE Y: the packet states or directly exemplifies supplement use for
this item in the specified use, or for a class the source explicitly
includes this item in.
VALUE N: the packet states the use is always integrated into clause or
phrase structure, or always stands alone, in a passage that addresses
the supplement possibility. Mere silence is NOT an N.
VALUE U: the packet does not support Y or N under those standards.

RULES.
- Code ONLY from the excerpts in the item's packet. Do not use outside
  knowledge about these words. Do not look anything up.
- For Y or N, quote must be copied VERBATIM from the packet excerpt you
  rely on (a continuous substring, at most 300 characters), with its
  source filename and line location as marked in the packet.
- For U, quote must be null.
- Output ONLY a JSON object, no prose, of the form:
  {"cells": [{"item_id": "...", "value": "Y|N|U",
              "quote": "... or null", "source_file": "...",
              "location": "..."}]}
  with exactly one cell per item, in the order the items are given.
"""


def items_block(order):
    parts = []
    for iid in order:
        p = PACKETS[iid]
        parts.append(f"\n### ITEM {iid}\nForm: {p['form']}\n"
                     f"Use: {p['use_gloss']}\nPacket:\n{p['packet']}\n")
    return "".join(parts)


def make_prompt(order):
    return ("You are coding linguistic data from source excerpts.\n\n"
            + DEFINITION + "\n## ITEMS\n" + items_block(order))


def shuffled(seed):
    order = list(PACKETS.keys())
    random.Random(seed).shuffle(order)
    return order


def run_cli(name, cmd, prompt):
    prompt_path = BASE / f"prompt-{name}.txt"
    prompt_path.write_text(prompt)
    t0 = time.time()
    done = subprocess.run(cmd, capture_output=True, text=True,
                          timeout=1200)
    dt = time.time() - t0
    out = BASE / "codings" / f"raw-{name}.txt"
    out.write_text(f"<!-- cmd: {' '.join(cmd[:3])}... secs={dt:.1f} "
                   f"exit={done.returncode} -->\n"
                   + done.stdout + "\n[STDERR]\n" + done.stderr[-2000:])
    print(f"{name}: exit={done.returncode} secs={dt:.1f} "
          f"stdout={len(done.stdout)} chars -> {out}")
    return done.stdout


def run_qwen():
    order = shuffled(4003)
    cells = []
    t0 = time.time()
    for iid in order:
        prompt = ("You are coding linguistic data from source "
                  "excerpts.\n\n" + DEFINITION
                  + "\n## ITEM\n" + items_block([iid]))
        body = json.dumps({
            "model": "qwen3.8:27b", "prompt": prompt, "stream": False,
            "think": False, "format": "json",
            "options": {"temperature": 0, "num_ctx": 16384}}).encode()
        req = urllib.request.Request(
            "http://localhost:11434/api/generate", data=body,
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=900) as resp:
            text = json.loads(resp.read())["response"]
        (BASE / "codings" / f"raw-qwen-{iid}.txt").write_text(text)
        try:
            got = json.loads(text)["cells"]
            cells.extend(got)
        except Exception as e:  # recorded, parsed again in analysis
            print(f"  qwen {iid}: parse deferred ({e})")
        print(f"  qwen {iid} done", flush=True)
    out = BASE / "codings" / "raw-qwen.txt"
    out.write_text(json.dumps({"cells": cells,
                               "secs_total": round(time.time() - t0, 1)},
                              indent=1))
    print(f"qwen: {len(cells)} cells -> {out}")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("agy", "all"):
        run_cli("agy", ["agy", "-p", make_prompt(shuffled(1001))],
                make_prompt(shuffled(1001)))
    if which in ("copilot", "all"):
        p = make_prompt(shuffled(2002))
        run_cli("copilot", ["copilot", "-p", p], p)
    if which in ("qwen", "all"):
        run_qwen()
    # prompt for the Muse subagent dispatch
    (BASE / "prompt-claude.txt").write_text(make_prompt(shuffled(3003)))
    print("prompt-claude.txt written")
