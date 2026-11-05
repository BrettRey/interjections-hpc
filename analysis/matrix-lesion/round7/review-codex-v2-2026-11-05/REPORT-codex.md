# Codex review of Round 7 harness v2 (2026-11-05)
<!-- SUMMARY: verbatim Codex (read-only wrapper) review of round7/harness.py v2 against RULE.md v2: no blocking findings; P09 true value must be exactly zero, shared-target mean missing, some promised summaries and calibration displays missing, entailed cells uncounted; all fixable from raw records · status: received; fixes to be applied after the running simulation finishes · updated: 2026-11-05 -->

Saved verbatim by the parent session (Claude Opus 5.5) from `codex-stdout.txt`. The full run was in progress during this review and its results had not been opened.

---

RESPONSIBILITY NOTICE: P09’s declared zero true gain is replaced by a positive Monte Carlo estimate, producing meaningless Type S/M summaries for the null target. The promised shared-target mean is also absent. Results inspection remains paused under your instruction; correct these summaries before Brett interprets them.

I read RULE v2, the complete harness, the earlier report, and the specified FREEZE sections. `DECISIONS.md:1100` records Brett’s approval of the revised plan. The permitted self-test and leak test pass; its calibration check matches both groupings.

All references below are to `analysis/matrix-lesion/round7/harness.py`. Patches are proposed only.

**Blocking: none found.**

All eight v1 findings were correctly repaired: whole-channel P11N concealment, separate calibration with an execution stop, post-concealment projection checks, exhaustive scoring for computable targets, unweighted convergence, A drawn for every row, eight-start bootstrap refits, and the synchronized EM objective.

The implemented per-target shared comparison uses the same scored cells, reference outcomes and M0 on the 41 single-word rows, while fitting each grouping on its own universe. The overlap AUC directions are correct: lower PPC p, higher sufficiency gap and lower record gain point toward “no cluster.” Winner selection correctly maximizes estimated M2 gain among computable targets. Signed estimate/D and wrong-sign frequencies implement RULE’s definitions.

**Important — 1. P09’s true gain must be exactly zero (lines 658–661, 741–743).**

Independent finite samples almost always have positive empirical mutual information. For example, a chance class–P09 imbalance gives `D=0.00001`; estimated gain `0.01` then becomes a ratio of 1,000, and P09 receives a Type S analysis despite being the declared null. Its winner error and shared “true difference” are also contaminated. Preserve the exact known zero.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
-            D[g][t] = _mi(cls[g][sel], X[sel, C[t]])
+            D[g][t] = 0.0 if t == "P09" else _mi(cls[g][sel], X[sel, C[t]])
@@
-    Ds = {t: {g: _mi(cls[g][shared], X[shared, C[t]]) for g in GROUPINGS}
+    Ds = {t: {g: (0.0 if t == "P09" else
+                   _mi(cls[g][shared], X[shared, C[t]])) for g in GROUPINGS}
           for t in SHARED}
```

**Important — 2. The shared-target mean is never computed (lines 774–791).**

RULE explicitly promises its distribution and wrong-sign frequency. Four individual contrasts cannot supply the distribution of their paired mean. If one target is uncomputable, averaging different target sets would also require a correspondingly matched true difference. The following reports the fixed four-target mean when all four are jointly computable and makes its availability explicit.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
-    s["shared"] = shared
+    means = []
+    for d in ds:
+        pairs = [(d["rec"]["intj"]["targets"][t],
+                  d["rec"]["expr_shared"][t]) for t in SHARED]
+        if all(a.get("computable") and b.get("computable")
+               for a, b in pairs):
+            means.append(float(np.mean([
+                _gain(a) - _gain(b) for a, b in pairs])))
+    shared["mean"] = {
+        "estimate": q3(means),
+        "share_computable_both": len(means) / len(ds)}
+    if world == "cross":
+        dd = float(np.mean([
+            tv["D_shared"][t]["intj"] - tv["D_shared"][t]["expr"]
+            for t in SHARED]))
+        shared["mean"]["D_diff"] = dd
+        if means and abs(dd) > 1e-9:
+            shared["mean"]["type_s"] = float(
+                np.mean(np.asarray(means) * dd < 0))
+    s["shared"] = shared
```

**Important — 3. Several promised outputs are stored only as raw records or omitted from figures (lines 707–710, 748–749, 858–875).**

Projection recovery is pooled across targets rather than summarized for each projection; family summaries omit individual single-diagnostic comparators. The calibration plot selects only world 1’s audit regimes, omitting stress and world 4. Consequently, a stress-specific calibration failure would be invisible in the plotted calibration display.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
             if comp:
@@
                 e["suff_gap"] = q3([v["loss"]["M2"] - v["loss"]["M3"]
                                     for v in comp])
+            if tv_ and "recovery" in tv_[0]:
+                e["recovery_bss"] = q3(
+                    [v["recovery"]["bss"] for v in tv_])
+                for passed in (True, False):
+                    e[f"recovery_bss_pass={passed}"] = q3([
+                        v["recovery"]["bss"] for v in tv_
+                        if v["checks"]["all"] == passed])
@@
-                             for k in GAIN_KEYS + ["suff_gap", "anchor_best"]}
+                             for k in GAIN_KEYS + ["suff_gap", "anchor_best"]
+                             + [f"single_{p}" for p in names]}
@@
-        for q in ASSUMED:
+        for world, lv, q, scheme in cells:
+            if world not in ("cross", "gom") or scheme != "split":
+                continue
             cal = np.zeros((5, 2))
-            for d in cells.get(("cross", "audit", q, "split"), []):
+            for d in cells[(world, lv, q, scheme)]:
@@
-            ax.plot(x, yv, marker="o", label=f"assumed {q:.2f}")
+            ax.plot(x, yv, marker="o",
+                    label=f"{world}/{lv}/{q:.2f}")
@@
-        ax.set_title(f"{gl[g]}: calibration (audit-like)")
+        ax.set_title(f"{gl[g]}: calibration")
```

**Minor — 4. Concealed-cell counts exclude entailed concealment (lines 359–373, 498).**

If ten P11N values are visible before an EXPRESSIVE→P01 projection, all ten disappear, but `concealed` can still report zero. Count known entailed cells alongside the other concealed values.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
     rows, d, Y, K, U, inap, signs = grouping_record(doc, g)
+    entailed = np.zeros_like(K)
     for p in ENTAILED.get((g, t), []):
         k = GROUPINGS[g]["diag"].index(p)
+        entailed[:, k] = K[:, k]
@@
-    conc = same | so
+    conc = same | so | entailed
```

**Running simulations can be retained; regenerate corrected true values, summaries and displays from the raw records—no simulation rerun is required by these findings.**
