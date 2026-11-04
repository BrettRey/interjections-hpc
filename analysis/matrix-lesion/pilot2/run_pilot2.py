"""Controlled P02 re-pilot on the pilot-1 packets.

Only the coder-facing instructions change. Pilot 1 asked for
supplement "in the CGEL sense"; pilot 2 asks for a described
distributional behaviour and preserves the source's own wording.
Packets, items, orderings, evidence rules, and call patterns are
otherwise inherited from pilot 1 so outcomes are comparable.
Values from both pilots are feasibility artifacts, not study data.
"""
import json
import random
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

BASE = Path("analysis/matrix-lesion/pilot2")
PACKETS = json.loads(
    Path("analysis/matrix-lesion/pilot/packets.json").read_text())

DEFINITION = """PROPERTY P02 (revised pilot wording).
Question: does the packet describe or exemplify this sign, in the
specified use, occurring together with another complete clausal,
nominal, or utterance unit while retaining a separate, utterance-like
status, rather than entering into that unit as one of its integrated
constituents?

Record the behaviour the source describes, in the source's own terms.
A source does NOT need to use the word "supplement" (or any
particular framework's term) for its description to count. Relevant
source evidence is discussion, in distributional or constructional
terms, of such matters as: occurring by itself as an utterance versus
occurring with other units; entering or not entering into
construction with other words; separate status alongside a complete
unit. Judge such wording in its local context and from the source's
examples.

VALUE Y: the packet describes or directly exemplifies that behaviour
for this item in the specified use, OR states it as a generalization
over a class in which the source explicitly includes this item.
VALUE N: the packet positively restricts this use to an integrated
constituent role, or to occurring only on its own, in a passage that
addresses occurrence with other units. Mere silence is NOT an N.
VALUE U: the packet does not support Y or N under those standards.

ADDITIONAL FIELDS (for every cell):
- source_wording: the source's own word or short phrase for the
  relevant behaviour, copied from the quote where one is given
  (for example a term like "co-utterances"); null for U.
- evidence_scope: "ITEM" if the quote's evidence is about this item
  itself, "CLASS" if it is a generalization over a class explicitly
  including this item, "NONE" for U.

RULES.
- Code ONLY from the excerpts in the item's packet. Do not use
  outside knowledge about these words. Do not look anything up.
- For Y or N, quote must be copied VERBATIM from the packet excerpt
  you rely on (a continuous substring, at most 300 characters), with
  its source filename and line location as marked in the packet.
- For U, quote, source_file, location, and source_wording must be
  null, and evidence_scope must be "NONE".
- Output ONLY a JSON object, no prose, of the form:
  {"cells": [{"item_id": "...", "value": "Y|N|U",
              "quote": "... or null", "source_file": "...",
              "location": "...", "source_wording": "... or null",
              "evidence_scope": "ITEM|CLASS|NONE"}]}
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


def run_agy():
    # per-item, no-tools: the only Agy mode that worked in pilot 1
    t0 = time.time()
    for iid in shuffled(1001):
        prompt = ("Do not use any tools. Do not read or write any "
                  "files. Answer directly from the text below.\n\n"
                  "You are coding linguistic data from source "
                  "excerpts.\n\n" + DEFINITION + "\n## ITEM\n"
                  + items_block([iid]))
        done = subprocess.run(["agy", "-p", prompt],
                              capture_output=True, text=True, timeout=900)
        (BASE / "codings" / f"raw-agy-{iid}.txt").write_text(
            done.stdout + "\n[STDERR]\n" + done.stderr[-1000:])
        print(f"agy {iid}: exit={done.returncode} "
              f"stdout={len(done.stdout)} chars", flush=True)
    print(f"agy total secs={time.time()-t0:.1f}")


def run_copilot():
    prompt = make_prompt(shuffled(2002))
    t0 = time.time()
    done = subprocess.run(["copilot", "-p", prompt],
                          capture_output=True, text=True, timeout=1200)
    dt = time.time() - t0
    (BASE / "codings" / "raw-copilot.txt").write_text(
        f"<!-- secs={dt:.1f} exit={done.returncode} -->\n"
        + done.stdout + "\n[STDERR]\n" + done.stderr[-2000:])
    print(f"copilot: exit={done.returncode} secs={dt:.1f} "
          f"stdout={len(done.stdout)} chars")


def run_qwen():
    cells = []
    t0 = time.time()
    for iid in shuffled(4003):
        prompt = ("You are coding linguistic data from source "
                  "excerpts.\n\n" + DEFINITION + "\n## ITEM\n"
                  + items_block([iid]))
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
            cells.extend(json.loads(text)["cells"])
        except Exception as e:
            print(f"  qwen {iid}: parse deferred ({e})")
        print(f"  qwen {iid} done", flush=True)
    (BASE / "codings" / "raw-qwen.txt").write_text(json.dumps(
        {"cells": cells, "secs_total": round(time.time() - t0, 1)},
        indent=1))
    print(f"qwen: {len(cells)} cells")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("agy", "all"):
        run_agy()
    if which in ("copilot", "all"):
        run_copilot()
    if which in ("qwen", "all"):
        run_qwen()
    (BASE / "prompt-claude.txt").write_text(make_prompt(shuffled(3003)))
    print("prompt-claude.txt written")
