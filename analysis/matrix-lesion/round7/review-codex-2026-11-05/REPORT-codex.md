# Codex code review of the Round 7 harness (2026-11-05)
<!-- SUMMARY: verbatim Codex (read-only wrapper) review of round7/harness.py against RULE.md and FREEZE-v4, saved by the parent session from codex-stdout.txt · status: received, findings being checked by the parent · updated: 2026-11-05 -->

Saved verbatim by the parent session (Claude Opus 5.5) from `codex-stdout.txt`. Inputs hashed in `inputs.sha256`. Nothing below has been applied by Codex.

---

RESPONSIBILITY NOTICE: The harness can produce a go/no-go verdict without satisfying its declared calibration or post-concealment estimability procedure. Its provisional INAPPLICABLE encoding also exposes target-derived information. Possible consequence: the 552-packet audit proceeds—or stops—on an invalid comparison. I did not run `smoke` or `full`. Brett needs to resolve the encoding and estimability interpretation before approving the run.

I read the specified files. The permitted self-test passes. RULE.md’s SHA-256 matches `DECISIONS.md:1098`, which authorizes building the harness and explicitly leaves threshold approval pending.

All code references below are to `analysis/matrix-lesion/round7/harness.py`. Patches are proposed, unexecuted.

### Blocking

**1. Target-derived INAPPLICABLE information reaches predictors — lines 197–199, 328, 497–499.**

RULE itself requires this problematic encoding. For a row with true P01=1 and P02=0, P11N’s INAPPLICABLE indicator tells M1 both target values when EXPRESSIVE predicts P01 or P02—even if their documentation is absent or erroneous. Applicability also controls P11N visibility in membership fitting. The target-flip test leaves applicability unchanged, so misses this path.

A conservative repair hides the entire P11N channel for these two projections. This requires Brett’s approval as an amendment to RULE, rather than silently calling the original encoding safe.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
 def run_projection(doc, g, t, scheme, rng, capture=None):
     rows, d, Y, K, U, inap, signs = grouping_record(doc, g)
+    # Includes applicability and documentation status, not just its value.
+    if g == "expr" and t in ("P01", "P02"):
+        k = GROUPINGS[g]["diag"].index("P11N")
+        Y[:, k] = 0
+        K[:, k] = False
+        U[:, k] = -1
+        inap[:, k] = False
     tt = C[t]
```

**2. Calibration matches the wrong quantity and does not gate execution — lines 179–191, 712–714.**

RULE requires matching **each grouping** within 0.02. Averaging permits cancellation: cluster correlations 0.50/0.38 versus bonds correlations 0.44/0.44 would be declared matched despite both failing. Moreover, `matched=False` still permits a full verdict.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
-    target = np.mean([(oriented_phi(X, "intj") + oriented_phi(X, "expr")) / 2
-                      for X in cross])
+    target = {g: float(np.mean([oriented_phi(X, g) for X in cross]))
+              for g in GROUPINGS}
@@
-        phi = np.mean([(oriented_phi(X, "intj") + oriented_phi(X, "expr")) / 2
-                       for X in Xs])
-        if best is None or abs(phi - target) < abs(best[1] - target):
-            best = (float(s), float(phi))
-    return {"cross_phi": float(target), "bonds_overlap": best[0],
-            "bonds_phi": best[1], "matched": bool(abs(best[1] - target) <= .02),
+        phi = {g: float(np.mean([oriented_phi(X, g) for X in Xs]))
+               for g in GROUPINGS}
+        error = max(abs(phi[g] - target[g]) for g in GROUPINGS)
+        if best is None or error < best[2]:
+            best = (float(s), phi, error)
+    return {"cross_phi": target, "bonds_overlap": best[0],
+            "bonds_phi": best[1], "matched": bool(best[2] <= .02),
@@
 def run(sims_ruled, sims_reported, procs=10):
     cal = calibrate()
+    if not cal["matched"]:
+        raise RuntimeError("Bonds calibration failed for at least one grouping")
```

If one overlap cannot match both groupings, report calibration failure; changing the generator requires a declared revision.

**3. Estimability is assessed on the unlesioned record — lines 382–429, 540–547.**

FREEZE requires all four checks **after concealment**. Here projections refit membership but never check that refit. Ten rows can initially have three independent diagnostics, then lose one each through same-inclusion concealment: check (a) should fail, yet their gains enter R2/R3 under the original passing status.

RULE’s single dataset-level R1 does not specify how multiple projection-specific checks and recovery scores collapse into one dataset result. That needs an explicit interpretation; inventing an aggregation would change the rule. The immediate safe patch prevents a premature full run:

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
     elif mode == "full":
+        raise RuntimeError(
+            "Resolve RULE's dataset-level R1 mapping to FREEZE's "
+            "post-concealment checks; implement checks per projection first."
+        )
         sims_ruled = int(sys.argv[2]) if len(sys.argv) > 2 else 150
```

This is a temporary interlock, not the completed scientific repair.

### Important

**4. One-class references silently change the scoring denominator — lines 475–479.**

With targets `[1,0,0]`, the positive cell is omitted because its references are all zero. FREEZE requires scoring it. With two opposite-valued targets, neither is scored. Support single-class logistic training with a smoothed constant prediction.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
 def lr_prob(F, ref, r, y):
+    if np.unique(y[ref]).size == 1:
+        return float((y[ref].sum() + 1) / (len(ref) + 2))
@@
         ref = scored[scored != r]
+        if len(ref) == 0:
+            continue
         yr = y[ref]
-        if yr.min() == yr.max():
-            continue
```

**5. World 1 overrides declared tier probabilities — lines 120, 126.**

RULE assigns A by tier to every row. The code forces A=0 outside the INTJ scoring universe. For an excluded bearer with declared probability 0.2, that changes EXPRESSIVE’s target distribution. Scoring eligibility should not alter the specified generator.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
-    pa = np.array([P_INTJ[t] for t in TIERS]) * INTJ_BEARER
+    pa = np.array([P_INTJ[t] for t in TIERS])
@@
-        a = beta(pa) * INTJ_BEARER
+        a = beta(pa)
```

**6. The convergence comparator is weighted rather than the declared mean — lines 468–470.**

Two inherited positive diagnostics sharing one unit plus one direct negative produce 0 here, versus the specified unweighted signed mean of 1/3. This changes R3’s comparator.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
-    wsum = W.sum(1)
-    conv = np.where(wsum > 0, (W * sgn * (2 * Y - 1)).sum(1)
+    wsum = V.sum(1)
+    conv = np.where(wsum > 0, (V * sgn * (2 * Y - 1)).sum(1)
```

**7. Bootstrap refits use four starts, not eight — line 406.**

A bootstrap fit can select an inferior local optimum and change check (c), hence R1 eligibility.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
-        bf = fit_lca(Y[idx], W[idx], rng, starts=4)[0]
+        bf = fit_lca(Y[idx], W[idx], rng)[0]
```

### Minor

**8. EM stopping mixes old likelihood with updated priors — lines 283–288.**

Final start selection correctly recomputes the penalized objective. The convergence test, however, can stop on cancellation between quantities from different parameter iterates.

```diff
--- a/analysis/matrix-lesion/round7/harness.py
+++ b/analysis/matrix-lesion/round7/harness.py
@@
             pi = (post.sum(0) + 1) / (n + K)
+            _, ll = estep(Y, W, theta, pi)
             obj = ll + np.log(theta).sum() + np.log(1 - theta).sum() \
```

Otherwise, finite binary hidden values are correctly zero-weighted; reference-row concealment, M1 missingness variants, split/cap weights, MAP updates, Brier skill, orientation AUC, R2 directions, and paired R3 differences are implemented correctly. The PPC statistic reads jointly visible cells only.

**Proceed only after the substantive fixes, Brett’s two rule interpretations, and renewed verification; the temporary interlock alone does not make the run ready.**
