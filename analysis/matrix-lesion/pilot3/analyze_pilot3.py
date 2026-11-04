"""Analyze pilot 3 by reusing the pilot-2 analyzer with patched paths.

The reused main() compares against pilot 2 through the prior-result
slot and writes pilot2-results.json under pilot3/. This wrapper then
renames that artifact and relabels the pilot-2 comparison fields,
and adds a direct pilot-1 comparison. The coding and verification
logic itself is unchanged across pilots.
"""
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "analyze_pilot2", "analysis/matrix-lesion/pilot2/analyze_pilot2.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

m.BASE = Path("analysis/matrix-lesion/pilot3")
m.P1 = Path("analysis/matrix-lesion/pilot2")
m.PACKETS = json.loads((m.BASE / "packets-v2.json").read_text())
m.ITEMS = list(m.PACKETS.keys())

# The inherited analyzer reads "pilot-results.json" from P1 for its
# comparison. Pilot 2 calls its result file "pilot2-results.json".
# Stage the expected name by pointing the comparison at a temporary
# alias created from the existing pilot-2 artifact, then remove it.
alias = m.P1 / "pilot-results.json"
created_alias = False
if not alias.exists():
    alias.write_text((m.P1 / "pilot2-results.json").read_text())
    created_alias = True

try:
    m.main()
finally:
    if created_alias:
        alias.unlink()

generated = m.BASE / "pilot2-results.json"
out = json.loads(generated.read_text())
out["changes_from_pilot2"] = out.pop("changes_from_pilot1", {})
out["consensus_changes_from_pilot2"] = out.pop(
    "consensus_changes_from_pilot1", {})
out["pilot2_kappa_indep"] = out.pop("pilot1_kappa_indep", None)

p1 = json.loads(Path(
    "analysis/matrix-lesion/pilot/pilot-results.json").read_text())
p1_values = {
    item: {fam.lower(): value for fam, value in fams.items()}
    for item, fams in p1.get("values", {}).items()}
changes1 = {}
for fam in m.FAMS:
    changes1[fam] = {
        item: [p1_values.get(item, {}).get(fam.lower()),
               out["values"][item][fam]]
        for item in m.ITEMS
        if p1_values.get(item, {}).get(fam.lower())
        != out["values"][item][fam]}
out["changes_from_pilot1"] = changes1
out["pilot1_kappa_indep"] = p1.get("fleiss_kappa_indep")

final = m.BASE / "pilot3-results.json"
final.write_text(json.dumps(out, indent=1))
generated.unlink()
print("\nchanges from pilot 1 by family:")
for fam in m.FAMS:
    print(f"  {fam}: {changes1[fam] or 'none'}")
print("wrote pilot3-results.json")
