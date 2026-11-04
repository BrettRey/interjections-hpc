"""Agy pilot coder, per-item print-mode calls with no-tools prefix.
Column-wise call returned empty stdout (recorded in raw-agy.txt);
per-item with explicit no-tools instruction is the working mode."""
import json
import subprocess
import time
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))
from run_pilot import DEFINITION, PACKETS, items_block, shuffled

BASE = Path("analysis/matrix-lesion/pilot")
order = shuffled(1001)
t0 = time.time()
for iid in order:
    prompt = ("Do not use any tools. Do not read or write any files. "
              "Answer directly from the text below.\n\n"
              "You are coding linguistic data from source excerpts.\n\n"
              + DEFINITION + "\n## ITEM\n" + items_block([iid]))
    done = subprocess.run(["agy", "-p", prompt], capture_output=True,
                          text=True, timeout=900)
    (BASE / "codings" / f"raw-agy-{iid}.txt").write_text(
        done.stdout + "\n[STDERR]\n" + done.stderr[-1000:])
    print(f"agy {iid}: exit={done.returncode} "
          f"stdout={len(done.stdout)} chars", flush=True)
print(f"agy total secs={time.time()-t0:.1f}")
