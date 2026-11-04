"""Pilot 3 runner: pilot-2 prompt and call patterns, packet v2.

Imports the pilot-2 implementation and overrides only its packet
source and output directory, so the intended experimental change is
retrieval rather than accidental prompt drift.
"""
import importlib.util
import json
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "run_pilot2", "analysis/matrix-lesion/pilot2/run_pilot2.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

m.BASE = Path("analysis/matrix-lesion/pilot3")
m.PACKETS = json.loads((m.BASE / "packets-v2.json").read_text())

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("agy", "all"):
        m.run_agy()
    if which in ("copilot", "all"):
        m.run_copilot()
    if which in ("qwen", "all"):
        m.run_qwen()
    (m.BASE / "prompt-claude.txt").write_text(
        m.make_prompt(m.shuffled(3003)))
    print("prompt-claude.txt written")
