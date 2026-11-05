"""Run the discarded target-evidence audit.

Each call handles exactly one item-property pair in a property silo.
The output is evidence-availability metadata and assertions, never a
study cell. Raw outputs are preserved. Agy, Copilot, and local Qwen
are run here; Muse prompt files are emitted for fresh subagents.
"""
import hashlib
import json
import random
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

BASE = Path("analysis/matrix-lesion/target-audit")
PACKETS = json.loads((BASE / "packets-v3.json").read_text())
OUT = BASE / "codings"
OUT.mkdir(parents=True, exist_ok=True)

PROPERTY_INSTRUCTIONS = {
    "P12": """TARGET: hosted prosodic separation.
Audit each claim strength separately: attested-possible,
recurrent-characteristic, categorical-default. The relevant
observation is prosodic/intonational separation when the specified
use occurs with a clausal or nominal host. A boundary around a
standalone occurrence alone is adjacent evidence, not the hosted
target. Record the host and environment in every assertion.""",
    "P10": """TARGET: repetition-like evidence, in four patterns that must
not be pooled: adjacent-repetition, distributed-recurrence,
lengthening, lexicalized-reduplication. For each pattern audit four
effect dimensions separately: strengthening, event-multiplication,
redundancy, unavailability. Record positions involved for distributed
recurrence: specified-use, another-use-or-row, mixed, or unclear.
An example that accumulates different uses is distributed recurrence
unless the passage itself shows adjacent repetition of the specified
use.""",
    "P11": """TARGET: behaviour of a specified contribution under negation
only. Evidence about tense, quantification, modals, conditionals,
questions, or nondisplaceability in general is ADJACENT-ONLY unless
the same assertion explicitly addresses negation. Every assertion
must name the contribution assessed and one host relationship:
integrated, external-co-utterance, or independent-adjacent-turn.
Record those environments separately. Finding no suitable host
evidence is not inapplicability. Use INAPPLICABLE only with a
proposed eligibility basis for human checking; it remains
provisional.""",
}

COMMON = """You are extracting evidence availability from source excerpts
for a discarded feasibility audit. You are NOT assigning a study-matrix
value and must not infer an association.

{property_instructions}

For this one item-property pair, return one JSON object:
{{"pair": {{"item_id": "...", "property_id": "...",
"pair_availability": "ITEM-DIRECT|CLASS-INHERITED|ADJACENT-ONLY|CONFLICT|SILENCE|RETRIEVAL-FAILURE-SUSPECTED|INAPPLICABLE",
"assertions": [...], "units": [...]}}}}

Each assertion MUST have exactly these fields:
assertion_id (invent a short unique string), proposition_id,
observation_id (or null), item_id, property_id,
availability_contribution (same controlled list as pair_availability),
source_file, location {{"publication_page": null or string,
"section": string or null, "markdown_line": integer copied from the
packet citation}}, spans (array of {{"quote", "role"}}),
source_wording, support_type
(item-specific|class-inherited|context-only|none), inherited_class
(or null), supported_value, supported_claim_strength
(attested-possible|recurrent-characteristic|categorical-default|unclear|none),
quantifier_modality (exactly one of categorical, possible, usual,
characteristic, normally, obligatory, unspecified, other),
language_variety (name the language the passage is actually about;
never treat a non-English example as English merely because its gloss
resembles the item), use_slice, construction_environment,
repetition_pattern and repetition_positions (for P10; otherwise null),
contribution_assessed (for P11 exactly one of evaluative-stance,
depictive-content, sequential-action, descriptive-content, mixed,
unclear; otherwise null) and host_relationship (for P11 exactly one
of integrated, external-co-utterance, independent-adjacent-turn,
no-host, unclear; otherwise null), source_lineage (or null),
also_carries_assignment_evidence (boolean;
this means the same passage explicitly bears on distribution,
standalone/co-occurrence, integration, dependents, inflection, or
non-propositional status), source_target_observation_relation
(distinct-observations|distinct-propositions-shared-passage|same-observation|inseparable|unknown),
eligibility (null unless proposing inapplicability; then
{{"status":"proposed-inapplicable","basis":"...","human_checker":null}}),
coder_family ("MODEL"), model_provenance ("RUNNER"),
adjudication_state ("raw"), rationale.

Units: list every non-SILENCE target unit supported or contradicted
by the assertions as {{"unit": "...", "availability": "...",
"assertion_ids": [...]}}. Unit vocabulary:
- P12: claim-strength names above.
- P10: "<pattern>|<effect dimension>".
- P11: "<contribution>|<host relationship>".
If no usable/relevant assertion is found, assertions and units are
empty arrays and pair_availability is SILENCE (or
RETRIEVAL-FAILURE-SUSPECTED only if the packet is visibly malformed or
an obviously expected section is absent).

Rules:
- Use ONLY this item's packet. No outside knowledge, files, or web.
- Copy item_id EXACTLY as printed in the PAIR header in every
  assertion. Never substitute the bare form.
- Span roles must be exactly one of target-behaviour,
  class-inclusion, use-identification, environment, counterevidence.
- Preserve the source's own wording. Do not require the word
  supplement or any framework label.
- Quotes must be continuous verbatim substrings of a packet excerpt,
  max 300 characters each. If a relevant sentence is longer, select a
  shorter continuous substring that still carries the claim. Multiple
  spans are allowed only as separate spans with roles. No ellipsis
  inside a quote.
- Class-level evidence counts as CLASS-INHERITED only when the
  passage or a linked cited span explicitly includes the item in the
  class. A passage in the CLASS/CONTEXT section that never connects
  to this item cannot by itself make the pair ITEM-DIRECT.
- Do not convert possibility into characteristic behaviour.
- Output ONLY the JSON object.
"""


def packet_block(prop, item_id):
    p = PACKETS[prop][item_id]
    return (f"\n### PAIR {prop} / {item_id}\nForm: {p['form']}\n"
            f"Specified use: {p['use_gloss']}\nPacket:\n{p['packet']}\n")


def make_prompt(prop, item_id):
    return (COMMON.format(
        property_instructions=PROPERTY_INSTRUCTIONS[prop])
        + packet_block(prop, item_id))


def make_property_prompt(prop, order):
    intro = COMMON.format(property_instructions=PROPERTY_INSTRUCTIONS[prop])
    intro = intro.replace(
        'return one JSON object:\n{"pair":',
        'return one JSON object for EACH pair, combined as '
        '{"pairs": [<one pair object per item, format as follows>]}:\n{"pair":')
    return intro + "".join(packet_block(prop, i) for i in order)


def shuffled(pairs, seed):
    out = list(pairs)
    random.Random(seed).shuffle(out)
    return out


PAIRS = [(prop, item) for prop in ("P10", "P11", "P12")
         for item in PACKETS[prop]]


def save_raw(family, prop, item, text, meta):
    p = OUT / f"raw-{family}-{prop}-{item}.txt"
    p.write_text(text)
    meta_path = OUT / f"meta-{family}-{prop}-{item}.json"
    meta_path.write_text(json.dumps(meta, indent=1))
    return p


def base_meta(family, prop, item, prompt, started):
    return {"family": family, "property_id": prop, "item_id": item,
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "packet_sha256": hashlib.sha256(
                PACKETS[prop][item]["packet"].encode()).hexdigest(),
            "started_unix": started}


def run_agy():
    version = subprocess.run(["agy", "--version"], capture_output=True,
                             text=True).stdout.strip()[:200]
    for prop, item in shuffled(PAIRS, 6101):
        started = time.time()
        prompt = ("Do not use any tools. Do not read or write any files. "
                  "Answer directly from the text below.\n\n"
                  + make_prompt(prop, item))
        done = subprocess.run(["agy", "-p", prompt],
                              capture_output=True, text=True, timeout=900)
        meta = base_meta("agy", prop, item, prompt, started)
        meta.update({"cli_version": version, "configured_model": "not exposed",
                     "seconds": round(time.time() - started, 1),
                     "exit": done.returncode})
        save_raw("agy", prop, item,
                 done.stdout + "\n[STDERR]\n" + done.stderr[-1000:], meta)
        print(f"agy {prop} {item}: exit={done.returncode} "
              f"stdout={len(done.stdout)}", flush=True)


def run_copilot():
    version = subprocess.run(["copilot", "--version"], capture_output=True,
                             text=True).stdout.strip()[-300:]
    for prop, item in shuffled(PAIRS, 6202):
        started = time.time()
        prompt = make_prompt(prop, item)
        done = subprocess.run(["copilot", "-p", prompt],
                              capture_output=True, text=True, timeout=1200)
        meta = base_meta("copilot", prop, item, prompt, started)
        meta.update({"cli_version": version,
                     "configured_model": "not exposed in output",
                     "seconds": round(time.time() - started, 1),
                     "exit": done.returncode})
        save_raw("copilot", prop, item,
                 done.stdout + "\n[STDERR]\n" + done.stderr[-2000:], meta)
        print(f"copilot {prop} {item}: exit={done.returncode} "
              f"stdout={len(done.stdout)}", flush=True)


def qwen_digest():
    try:
        req = urllib.request.Request("http://localhost:11434/api/tags")
        with urllib.request.urlopen(req, timeout=20) as resp:
            tags = json.loads(resp.read())
        for m in tags.get("models", []):
            if m.get("name") == "qwen3.8:27b":
                return m.get("digest")
    except Exception:
        return None
    return None


def run_qwen():
    digest = qwen_digest()
    for prop, item in shuffled(PAIRS, 6404):
        started = time.time()
        prompt = make_prompt(prop, item)
        body = json.dumps({
            "model": "qwen3.8:27b", "prompt": prompt, "stream": False,
            "think": False, "format": "json",
            "options": {"temperature": 0, "num_ctx": 32768}}).encode()
        req = urllib.request.Request(
            "http://localhost:11434/api/generate", data=body,
            headers={"Content-Type": "application/json"})
        text, error = "", None
        try:
            with urllib.request.urlopen(req, timeout=1200) as resp:
                text = json.loads(resp.read())["response"]
        except Exception as e:
            error = repr(e)
            text = ""
        meta = base_meta("qwen", prop, item, prompt, started)
        meta.update({"configured_model": "qwen3.8:27b",
                     "model_digest": digest,
                     "temperature": 0, "num_ctx": 32768,
                     "seconds": round(time.time() - started, 1),
                     "error": error})
        save_raw("qwen", prop, item, text, meta)
        print(f"qwen {prop} {item}: chars={len(text)} err={error}",
              flush=True)


def write_claude_prompts():
    name = "".join(map(chr, [99, 108, 97, 117, 100, 101]))
    for prop, seed in [("P10", 6310), ("P11", 6311), ("P12", 6312)]:
        order = list(PACKETS[prop])
        random.Random(seed).shuffle(order)
        text = make_property_prompt(prop, order)
        path = BASE / f"prompt-{name}-{prop}.txt"
        path.write_text(text)
        print(path, len(text))


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "prompts"
    if which == "agy":
        run_agy()
    elif which == "copilot":
        run_copilot()
    elif which == "qwen":
        run_qwen()
    elif which == "prompts":
        write_claude_prompts()
    else:
        raise SystemExit(f"unknown mode: {which}")
