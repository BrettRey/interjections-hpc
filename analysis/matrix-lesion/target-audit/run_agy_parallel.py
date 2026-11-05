"""Parallel completion of the agy audit queue.

Same prompts, same per-pair subprocess call, same raw/meta outputs as
run_audit.run_agy; only the scheduling changes (thread pool over the
pairs whose raw file does not yet exist). Added 2026-11-04 because the
sequential queue ran at ~3 min/pair. Meta records the parallel runner.
"""
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, "analysis/matrix-lesion/target-audit")
import run_audit as ra

WORKERS = 6


def one(version, prop, item):
    started = time.time()
    prompt = ("Do not use any tools. Do not read or write any files. "
              "Answer directly from the text below.\n\n"
              + ra.make_prompt(prop, item))
    try:
        done = subprocess.run(["agy", "-p", prompt],
                              capture_output=True, text=True, timeout=900)
        out, err, code = done.stdout, done.stderr, done.returncode
    except subprocess.TimeoutExpired as e:
        out, err, code = (e.stdout or b"").decode(errors="replace"), \
            "TIMEOUT after 900s", -1
    meta = ra.base_meta("agy", prop, item, prompt, started)
    meta.update({"cli_version": version, "configured_model": "not exposed",
                 "seconds": round(time.time() - started, 1),
                 "exit": code, "runner": "run_agy_parallel.py",
                 "workers": WORKERS})
    ra.save_raw("agy", prop, item, out + "\n[STDERR]\n" + err[-1000:], meta)
    return f"agy {prop} {item}: exit={code} stdout={len(out)}"


def main():
    version = subprocess.run(["agy", "--version"], capture_output=True,
                             text=True).stdout.strip()[:200]
    todo = [(p, i) for p, i in ra.shuffled(ra.PAIRS, 6101)
            if not (ra.OUT / f"raw-agy-{p}-{i}.txt").exists()]
    print(f"pairs remaining: {len(todo)}", flush=True)
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = [ex.submit(one, version, p, i) for p, i in todo]
        for f in as_completed(futs):
            print(f.result(), flush=True)


if __name__ == "__main__":
    main()
