"""Fake-data check: convergence (latent-class) assignment vs the tally.

Written 2026-11-04 by the Claude Code session that evaluated FREEZE-v3
(`reviews/matrix-lesion-evaluation-2026-11-04/EVALUATION.md`), after
Brett: "a simple tally is not the way to go. That's not how HPC works.
absences count, surely. No property on its own can 'decide
membership'."

Question: is graded membership from a latent-class model over a
grouping's diagnostics a workable replacement for the +/-1 tally at
the declared inventory size (n = 33), and does it behave acceptably
under null and adversarial worlds?

Rules compared, per rotation:
  tally        FREEZE-v3 rules as implemented in lesion.py
               (INTJ: presence gate + score/fraction thresholds;
               EXPRESSIVE: P08 with a P07 veto)
  tally_nogate INTJ tally without the P01/P02 presence gate
  lca2, lca3   2- and 3-class latent-class models fitted by EM with
               missing cells ignored (MAR) and Beta(1,1)/Dirichlet(1)
               smoothing; membership is the posterior of the class
               whose profile best matches the anchor signature; M2 is
               the posterior-weighted mixture of class target rates.

Convergence rotations use the grouping's own field as diagnostics:
  INTJ        P01 P02 P03 P04 P05 P07  -> targets P06 P08 P09 P12 P13
  EXPRESSIVE  P07 P08 P10 P11          -> targets P01-P06 P09 P12 P13
The EXPRESSIVE tally keeps its FREEZE-v3 sources (P07, P08) and is
scored on the same targets, so both rules face identical cells.

Source-complete one-cell lesions: with disjoint source and target
columns, the assignment input does not change across lesion runs for a
given target, so each model is fitted once per dataset and rotation.
Only target-dependent quantities are recomputed per scored cell.

Not simulated here (named limitations): testimony weighting of
inherited cells, same-inclusion concealment, value-coupled copied
evidence, the section 8 evidence gate. Those belong to Round 7.
Diagnostic only: nothing is frozen by running this script, and no
real coded cell is used.
"""
import json
import sys
import time

import numpy as np

from lesion import (IDX, PROPS, assign_intj, assign_expr,
                    predict_column_matched, _cell_logloss)
from sim_round6_eligibility import degrade_regime

P = IDX
EPS = 1e-9
BASE = np.array([.55, .45, .35, .25, .30, .20, .55,
                 .40, .15, .35, .40, .50, .15, .45])

INTJ_SRC = [P[p] for p in ("P01", "P02", "P03", "P04", "P05", "P07")]
INTJ_SIGN = {P["P01"]: 1, P["P02"]: 1, P["P03"]: -1, P["P04"]: -1,
             P["P05"]: -1, P["P07"]: 1}
INTJ_TGT = [P[p] for p in ("P06", "P08", "P09", "P12", "P13")]
EXPR_SRC = [P[p] for p in ("P07", "P08", "P10", "P11")]
EXPR_SIGN = {P["P07"]: 1, P["P08"]: 1, P["P10"]: 1, P["P11"]: 1}
EXPR_TALLY_SRC = [P["P07"], P["P08"]]
EXPR_TGT = [P[p] for p in ("P01", "P02", "P03", "P04", "P05", "P06",
                           "P09", "P12", "P13")]


# ---------------------------------------------------------------- worlds
# Mirrors simulate.py's generators, but also returns the latent truth.

def _bern(rng, pr):
    return (rng.random(pr.shape) < pr).astype(int)


def w_null(rng, n):
    X = _bern(rng, np.tile(BASE, (n, 1)))
    return X, {"intj": None, "expr": None}


def w_latent_class(rng, n):
    core = np.array([.9, .85, .05, .05, .02, .05, .9,
                     .8, .1, .8, .85, .9, .25, .5])
    ordinary = np.array([.15, .05, .85, .7, .8, .7, .15,
                         .1, .05, .1, .1, .15, .02, .2])
    expr_integr = np.array([.05, .05, .9, .1, .05, .02, .9,
                            .9, .05, .8, .85, .1, .05, .1])
    z = rng.choice(3, size=n, p=[.4, .4, .2])
    X = _bern(rng, np.choose(z[:, None], [core, ordinary, expr_integr]))
    return X, {"intj": (z == 0).astype(int),
               "expr": np.isin(z, [0, 2]).astype(int)}


def w_crosscutting(rng, n):
    A = rng.random(n) < .45
    B = rng.random(n) < .45
    C = rng.random(n) < .15
    hi, lo = .85, .12
    pr = np.tile(BASE, (n, 1)).astype(float)
    for name in ("P01", "P02", "P12", "P13"):
        pr[:, P[name]] = np.where(A, hi, lo)
    for name in ("P03", "P04", "P05"):
        pr[:, P[name]] = np.where(A, lo, hi)
    for name in ("P08", "P10", "P11"):
        pr[:, P[name]] = np.where(B, hi, lo)
    pr[:, P["P07"]] = np.where(A | B, .85, .15)
    pr[:, P["P09"]] = np.where(C, .85, .05)
    pr[:, P["P06"]] = np.where(A, .05, .5)
    pr[:, P["P14"]] = np.where(A, .7, .3)
    return _bern(rng, pr), {"intj": A.astype(int), "expr": B.astype(int)}


def w_hub(rng, n):
    hub = rng.random(n) < .5
    pr = np.where(hub[:, None], .8, .2) * np.ones((n, 14))
    for name in ("P03", "P04", "P05"):
        pr[:, P[name]] = np.where(hub, .2, .8)
    X = _bern(rng, pr)
    X[:, P["P07"]] = hub.astype(int)
    return X, {"intj": None, "expr": None}


def w_multianchor(rng, n):
    A = rng.random(n) < .40
    B = rng.random(n) < .40
    F = rng.random(n) < .35
    D = rng.random(n) < .18
    hi, lo = .85, .12
    pr = np.tile(BASE, (n, 1)).astype(float)
    pr[:, P["P01"]] = np.where(A, hi, lo)
    pr[:, P["P02"]] = np.where(A | F, hi, lo)
    for name in ("P03", "P04", "P05"):
        pr[:, P[name]] = np.where(A, lo, hi)
    pr[:, P["P06"]] = np.where(A, .05, .5)
    pr[:, P["P07"]] = np.where(A | B | D, .85, .15)
    pr[:, P["P08"]] = np.where(B, hi, lo)
    pr[:, P["P09"]] = np.where(D, hi, .05)
    pr[:, P["P10"]] = np.where(D, .05, np.where(B, hi, .25))
    pr[:, P["P11"]] = np.where(B, hi, lo)
    pr[:, P["P12"]] = np.where(A | F, hi, lo)
    pr[:, P["P13"]] = np.where(A | D, .30, .03)
    pr[:, P["P14"]] = np.where(A, .7, .3)
    return _bern(rng, pr), {"intj": A.astype(int), "expr": B.astype(int)}


WORLDS = {"null": w_null, "latent_class": w_latent_class,
          "crosscutting": w_crosscutting, "hub": w_hub,
          "multianchor": w_multianchor}


# ------------------------------------------------------------------- LCA

def fit_lca(Y, V, K, rng, starts=8, iters=300, tol=1e-7):
    """Binary latent-class model by EM; invisible cells are ignored.

    Returns (posterior n x K, theta K x m, pi K). MAP estimates under
    Beta(1,1) item priors and a Dirichlet(1) class prior keep the
    solution off the boundary at small n.
    """
    n, m = Y.shape
    Yf = np.where(V, Y, 0).astype(float)
    Vf = V.astype(float)
    best = None
    for _ in range(starts):
        theta = rng.uniform(0.2, 0.8, size=(K, m))
        pi = np.full(K, 1.0 / K)
        prev = -np.inf
        for _ in range(iters):
            lt, l1t = np.log(theta), np.log(1 - theta)
            ll = (Yf @ lt.T + (Vf - Yf) @ l1t.T) + np.log(pi)
            mx = ll.max(axis=1, keepdims=True)
            post = np.exp(ll - mx)
            norm = post.sum(axis=1, keepdims=True)
            post /= norm
            obj = float((mx[:, 0] + np.log(norm[:, 0])).sum()
                        + np.log(theta).sum() + np.log(1 - theta).sum()
                        + np.log(pi).sum())
            theta = (post.T @ Yf + 1.0) / (post.T @ Vf + 2.0)
            theta = np.clip(theta, 1e-4, 1 - 1e-4)
            pi = (post.sum(axis=0) + 1.0) / (n + K)
            if abs(obj - prev) < tol:
                break
            prev = obj
        if best is None or obj > best[0]:
            best = (obj, post, theta, pi)
    return best[1], best[2], best[3]


def member_class(theta, cols, sign):
    score = np.zeros(theta.shape[0])
    for k, j in enumerate(cols):
        s = sign[j]
        score += theta[:, k] if s > 0 else 1 - theta[:, k]
    return int(np.argmax(score))


def graded_m2(post, y_ref, ref, scored, p0, min_ref=3.0, alpha=1.0):
    """Posterior-weighted class target rates, M0 for thin classes."""
    K = post.shape[1]
    rates = np.empty(K)
    for c in range(K):
        w = post[ref, c]
        if w.sum() >= min_ref:
            rates[c] = (np.dot(w, y_ref) + alpha) / (w.sum() + 2 * alpha)
        else:
            rates[c] = p0
    p1 = post[scored] @ rates
    return np.column_stack([1 - p1, p1])


# ------------------------------------------------------------- one cell set

def rotation_records(Xc, known, rotation, rng, truth):
    if rotation == "intj":
        src, sign, tgts = INTJ_SRC, INTJ_SIGN, INTJ_TGT
        tally_fns = {"tally": assign_intj, "tally_nogate": assign_nogate}
        tally_src = INTJ_SRC
    else:
        src, sign, tgts = EXPR_SRC, EXPR_SIGN, EXPR_TGT
        tally_fns = {"tally": assign_expr}
        tally_src = EXPR_TALLY_SRC
    n = Xc.shape[0]
    vis_src = np.zeros_like(known)
    vis_src[:, src] = known[:, src]
    fits = {}
    for K in (2, 3):
        post, theta, _ = fit_lca(Xc[:, src], known[:, src], K, rng)
        fits[f"lca{K}"] = (post, member_class(theta, src, sign))
    vis_tally = np.zeros_like(known)
    vis_tally[:, tally_src] = known[:, tally_src]
    tallies = {name: f(Xc, vis_tally) for name, f in tally_fns.items()}

    membership = {}
    if truth is not None:
        for name, a in tallies.items():
            pm = np.where(a == 2, 0.5, a.astype(float))
            membership[name] = {
                "brier": float(np.mean((pm - truth) ** 2)),
                "coverage": float(np.mean(a != 2))}
        for name, (post, mc) in fits.items():
            pm = post[:, mc]
            membership[name] = {
                "brier": float(np.mean((pm - truth) ** 2)),
                "coverage": 1.0}

    per_target = {}
    for j in tgts:
        cells = []
        for r in np.where(known[:, j])[0]:
            mask = np.zeros_like(known)
            mask[r, known[r]] = True
            keep = [c for c in src if known[r, c]]
            mask[r, keep] = False
            if rotation == "expr":
                mask[r, [c for c in tally_src if known[r, c]]] = False
            ref = np.where(known[:, j] & ~mask[:, j])[0]
            if len(ref) < 10:
                continue
            y = int(Xc[r, j])
            p0 = (Xc[ref, j].sum() + 1.0) / (len(ref) + 2.0)
            P0 = np.array([1 - p0, p0])
            row = {"y": y, "M0": _cell_logloss(y, P0, (0, 1))}
            for name, a in tallies.items():
                res = predict_column_matched(Xc, known, mask, j, a,
                                             tally_src)
                k = list(res["rows"]).index(r)
                row[f"M2_{name}"] = _cell_logloss(y, res["M2"][k], (0, 1))
                row["M1"] = _cell_logloss(y, res["M1"][k], (0, 1))
            if rotation == "expr":
                res = predict_column_matched(Xc, known, mask, j,
                                             tallies["tally"], src)
                k = list(res["rows"]).index(r)
                row["M1_conv"] = _cell_logloss(y, res["M1"][k], (0, 1))
            else:
                row["M1_conv"] = row["M1"]
            for name, (post, mc) in fits.items():
                Pm = graded_m2(post, Xc[ref, j], ref, np.array([r]), p0)
                row[f"M2_{name}"] = _cell_logloss(y, Pm[0], (0, 1))
            cells.append(row)
        if len(cells) < 18:
            continue
        mean = {k: float(np.mean([c[k] for c in cells]))
                for k in cells[0] if k != "y"}
        rules = ["tally"] + (["tally_nogate"] if rotation == "intj"
                             else []) + ["lca2", "lca3"]
        per_target[PROPS[j]] = {
            "n": len(cells),
            "gain": {rule: mean["M0"] - mean[f"M2_{rule}"]
                     for rule in rules},
            "gain_M1": mean["M0"] - mean["M1"],
            "gain_M1_conv": mean["M0"] - mean["M1_conv"]}
    return {"membership": membership, "targets": per_target}


def assign_nogate(X, vis):
    """INTJ tally without the presence gate (same thresholds)."""
    pos = {"P01": 1, "P02": 1, "P03": 0, "P04": 0, "P05": 0, "P07": 1}
    score = np.zeros(X.shape[0], dtype=int)
    nvis = np.zeros(X.shape[0], dtype=int)
    for name, want in pos.items():
        j = IDX[name]
        hit = vis[:, j] & (X[:, j] == want)
        miss = vis[:, j] & (X[:, j] != want)
        score += hit.astype(int) - miss.astype(int)
        nvis += vis[:, j].astype(int)
    frac = np.where(nvis > 0, score / np.maximum(nvis, 1), 0.0)
    out = np.full(X.shape[0], 2, dtype=int)
    out[(nvis >= 2) & (score >= 2) & (frac >= 0.5)] = 1
    out[(nvis >= 2) & (frac <= 0.0)] = 0
    return out


# ------------------------------------------------------------------ tests

def self_tests(seed=11):
    rng = np.random.default_rng(seed)
    # 1. LCA recovers planted classes on a large clean sample.
    n, m = 400, 6
    z = rng.random(n) < 0.5
    th = np.where(z[:, None], 0.9, 0.1) * np.ones((n, m))
    Y = (rng.random((n, m)) < th).astype(int)
    V = rng.random((n, m)) < 0.7
    post, theta, _ = fit_lca(Y, V, 2, rng)
    mc = int(np.argmax(theta.mean(axis=1)))
    acc = np.mean((post[:, mc] > 0.5) == z)
    assert acc > 0.9, f"LCA recovery {acc:.2f}"
    # 2. Graded M2 with one-hot posteriors equals the hard group rate.
    post = np.zeros((6, 2))
    post[[0, 1, 2], 0] = 1
    post[[3, 4, 5], 1] = 1
    y_ref = np.array([1, 1, 0, 0, 0])
    ref = np.array([1, 2, 3, 4, 5])
    pm = graded_m2(post, y_ref, ref, np.array([0]), 0.5, min_ref=1)
    assert abs(pm[0, 1] - (2 + 1) / (2 + 2)) < 1e-12
    # 3. Rows with nothing visible get the prior.
    post, _, pi = fit_lca(Y[:5], np.zeros((5, m), bool), 2, rng)
    assert np.allclose(post, np.tile(pi, (5, 1)), atol=1e-6)
    return "self-tests passed"


# -------------------------------------------------------------------- run

def run(sims=100, seed=20261104, n=33):
    rng = np.random.default_rng(seed)
    out = {"meta": {"sims": sims, "n": n, "seed": seed,
                    "regimes": ["uniform", "scarce_negative"]}}
    for world, gen in WORLDS.items():
        for regime in ("uniform", "scarce_negative"):
            key = f"{world}/{regime}"
            acc = {"intj": [], "expr": []}
            for _ in range(sims):
                X, truth = gen(rng, n)
                Xc, known = degrade_regime(X, rng, regime)
                for rot in ("intj", "expr"):
                    acc[rot].append(rotation_records(
                        Xc, known, rot, rng, truth[rot]))
            out[key] = summarize(acc)
            print(key, "done", flush=True)
    return out


def summarize(acc):
    res = {"family": {}, "targets": {}, "membership": {}}
    for rot, runs in acc.items():
        rules = (["tally", "tally_nogate", "lca2", "lca3"]
                 if rot == "intj" else ["tally", "lca2", "lca3"])
        fam = {r: [] for r in rules + ["M1", "M1_conv"]}
        tg = {}
        for run_ in runs:
            t = run_["targets"]
            if not t:
                continue
            for r in rules:
                fam[r].append(np.mean([v["gain"][r] for v in t.values()]))
            fam["M1"].append(np.mean([v["gain_M1"] for v in t.values()]))
            fam["M1_conv"].append(
                np.mean([v["gain_M1_conv"] for v in t.values()]))
            for name, v in t.items():
                d = tg.setdefault(name, {r: [] for r in
                                         rules + ["M1", "M1_conv"]})
                for r in rules:
                    d[r].append(v["gain"][r])
                d["M1"].append(v["gain_M1"])
                d["M1_conv"].append(v["gain_M1_conv"])
        res["family"][rot] = {
            r: {"median": float(np.median(v)) if v else None,
                "q05": float(np.quantile(v, .05)) if v else None,
                "q95": float(np.quantile(v, .95)) if v else None,
                "p_ge_0.03": float(np.mean(np.array(v) >= 0.03))
                if v else None,
                "n_datasets": len(v)}
            for r, v in fam.items()}
        res["targets"][rot] = {
            name: {r: {"median": float(np.median(v)),
                       "p_ge_0.03": float(np.mean(np.array(v) >= 0.03))}
                   for r, v in d.items()}
            for name, d in tg.items()}
        mem = [run_["membership"] for run_ in runs if run_["membership"]]
        if mem:
            res["membership"][rot] = {
                r: {"brier_median": float(np.median(
                        [m[r]["brier"] for m in mem])),
                    "coverage_median": float(np.median(
                        [m[r]["coverage"] for m in mem]))}
                for r in mem[0]}
    return res


if __name__ == "__main__":
    print(self_tests())
    sims = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    t0 = time.time()
    results = run(sims=sims)
    results["meta"]["runtime_s"] = round(time.time() - t0, 1)
    with open("results-convergence-assignment.json", "w") as fh:
        json.dump(results, fh, indent=1)
    print("runtime", results["meta"]["runtime_s"], "s")
