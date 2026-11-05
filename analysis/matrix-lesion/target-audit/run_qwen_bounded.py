"""Bounded completion of the local-Qwen audit queue.

Identical prompts and outputs to run_audit.run_qwen, with one added
generation bound: num_predict=5000 (the unbounded queue produced an
18 KB single-assertion response taking 1015 s; several such pairs
would stall the audit for many hours). The bound and runner are
recorded in every meta file. Pairs with an existing NON-EMPTY raw file
from the original queue are kept and skipped; a pair interrupted
mid-request produced no file and is simply run here.
"""
import json
import sys
import time
import urllib.request

sys.path.insert(0, "analysis/matrix-lesion/target-audit")
import run_audit as ra

NUM_PREDICT = 5000
TIMEOUT = 900


def main():
    digest = ra.qwen_digest()
    todo = [(p, i) for p, i in ra.shuffled(ra.PAIRS, 6404)
            if not (ra.OUT / f"raw-qwen-{p}-{i}.txt").exists()
            or not (ra.OUT / f"raw-qwen-{p}-{i}.txt").read_text().strip()]
    print(f"pairs remaining: {len(todo)}", flush=True)
    for prop, item in todo:
        started = time.time()
        prompt = ra.make_prompt(prop, item)
        body = json.dumps({
            "model": "qwen3.8:27b", "prompt": prompt, "stream": False,
            "think": False, "format": "json", "keep_alive": "30m",
            "options": {"temperature": 0, "num_ctx": 32768,
                        "num_predict": NUM_PREDICT}}).encode()
        req = urllib.request.Request(
            "http://localhost:11434/api/generate", data=body,
            headers={"Content-Type": "application/json"})
        text, error = "", None
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                text = json.loads(resp.read())["response"]
        except Exception as e:
            error = repr(e)
        meta = ra.base_meta("qwen", prop, item, prompt, started)
        meta.update({"configured_model": "qwen3.8:27b",
                     "model_digest": digest,
                     "temperature": 0, "num_ctx": 32768,
                     "num_predict": NUM_PREDICT,
                     "runner": "run_qwen_bounded.py",
                     "seconds": round(time.time() - started, 1),
                     "error": error})
        ra.save_raw("qwen", prop, item, text, meta)
        print(f"qwen {prop} {item}: chars={len(text)} err={error}",
              flush=True)


if __name__ == "__main__":
    main()
