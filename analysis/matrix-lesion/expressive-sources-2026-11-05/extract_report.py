"""Save a subagent's SubagentHandback report verbatim from its transcript."""
import json, sys
src, out, label = sys.argv[1], sys.argv[2], sys.argv[3]
report = None
for l in open(src).read().splitlines():
    try:
        d = json.loads(l)
    except Exception:
        continue
    c = d.get("message", {}).get("content")
    if isinstance(c, list):
        for x in c:
            if x.get("type") == "tool_use" and x.get("name") == "SubagentHandback":
                inp = x.get("input", {})
                report = inp.get("message") or inp.get("report") or inp.get("result") or inp.get("text") or json.dumps(inp, ensure_ascii=False, indent=1)
if report is None:
    sys.exit("no SubagentHandback found")
with open(out, "w") as fh:
    fh.write(f"# {label}\n\nSaved verbatim by the parent session (Claude Opus 5.5) from the subagent's SubagentHandback report. Model output, not a source; every quotation is checked by the parent against the page-marked source text before use.\n\n---\n\n")
    fh.write(report)
print(out, len(report))
