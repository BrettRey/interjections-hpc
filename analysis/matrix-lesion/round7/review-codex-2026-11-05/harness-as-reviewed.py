"""Round 7 fake-data harness for FREEZE-v4 (rule: RULE.md in this folder).

Written 2026-11-05 after the rule was fixed and hashed (DECISIONS.md,
RULE.md SHA-256 61cbaff5...). Brett: "yes, write the rule first, then
build it".

Simulates the FREEZE-v4 section 2 and 4 procedure on fake 46-row records
whose documentation is as patchy as the 12-item target audit suggests,
and evaluates rules R1 to R3 of RULE.md. Self-contained: it doesn't
import lesion.py, which holds the pre-v4 schema.

Usage (from this folder, with the project venv):
  ../.venv/bin/python -I harness.py selftest
  ../.venv/bin/python -I harness.py smoke   # bugs and timing only; prints no statistics
  ../.venv/bin/python -I harness.py full    # writes results-round7.json

No real coded cell is used. Item tiers and universes come from
items-v4.csv, which is design data, not outcomes.
"""
import csv
import hashlib
import json
import os
import sys
import time
import warnings
from multiprocessing import Pool

import numpy as np
from sklearn.linear_model import LogisticRegression

warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, "..", "items-v4.csv")
EPS = 1e-9

COLS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09",
        "P10S", "P11N", "P12", "P13"]
C = {p: i for i, p in enumerate(COLS)}
M = len(COLS)

GROUPINGS = {
    "intj": {"diag": ["P01", "P02", "P03", "P04", "P05", "P07"],
             "sign": {"P01": 1, "P02": 1, "P03": -1, "P04": -1,
                      "P05": -1, "P07": 1},
             "targets": ["P06", "P08", "P09", "P10S", "P11N", "P12",
                         "P13"],
             "anchors": ["P01", "P02"]},
    "expr": {"diag": ["P07", "P08", "P10S", "P11N"],
             "sign": {"P07": 1, "P08": 1, "P10S": 1, "P11N": 1},
             "targets": ["P01", "P02", "P03", "P04", "P05", "P06", "P09",
                         "P12", "P13"],
             "anchors": ["P08"]},
}

# Sign orientation for the bonds world (0 = independent of the bonds).
BOND_SIGN = {"P01": 1, "P02": 1, "P03": -1, "P04": -1, "P05": -1,
             "P06": -1, "P07": 1, "P08": 1, "P09": 0, "P10S": 1,
             "P11N": 1, "P12": 1, "P13": 1}

# Tier membership probabilities (assumed; RULE.md, world 1).
P_INTJ = {"core": .95, "boundary": .5, "control": .05, "extension": .3,
          "expr-core": .2, "expr-control": .05}
P_EXPR = {"core": .7, "boundary": .5, "control": .1, "extension": .3,
          "expr-core": .95, "expr-control": .05}

# Fake sources of class-level testimony (RULE.md, Documentation).
SOURCES = [
    {"name": "grammar1", "grouping": "intj", "scale": 1.0,
     "states": {"P01": 1, "P02": 1, "P03": 0, "P04": 0, "P05": 0,
                "P06": 0, "P12": 1}},
    {"name": "grammar2", "grouping": "intj", "scale": 0.7,
     "states": {"P05": 0, "P07": 1, "P13": 1}},
    {"name": "expressive", "grouping": "expr", "scale": 1.0,
     "states": {"P07": 1, "P08": 1, "P10S": 1, "P11N": 1}},
]

HI, LO = .85, .12
LEVELS = {"audit": {"P10S": .33, "P11N": .33, "P12": .05, "incl": 1.0},
          "stress": {"P10S": .15, "P11N": .15, "P12": .05, "incl": 0.6}}
ASSUMED = [0.40, 0.55, 0.70]


def load_items():
    with open(ITEMS) as fh:
        rows = list(csv.DictReader(fh))
    tiers = [r["analyst_tier"] for r in rows]
    intj_bearer = np.array(["INTJ" in r["rotation_universes"] for r in rows])
    return tiers, intj_bearer


TIERS, INTJ_BEARER = load_items()
N = len(TIERS)
UNIVERSE = {"intj": INTJ_BEARER, "expr": np.ones(N, bool)}


# ------------------------------------------------------------------ worlds

def _probs_cluster(a, b, c):
    """Property probabilities given INTJ grade a, EXPRESSIVE grade b and
    the unrelated depictive grade c (all in [0, 1]; 0/1 for classes)."""
    pr = np.empty((len(a), M))
    for p in ("P01", "P02"):
        pr[:, C[p]] = a * HI + (1 - a) * LO
    for p in ("P03", "P04", "P05"):
        pr[:, C[p]] = a * LO + (1 - a) * HI
    for p in ("P08", "P10S", "P11N"):
        pr[:, C[p]] = b * HI + (1 - b) * LO
    either = 1 - (1 - a) * (1 - b)
    pr[:, C["P07"]] = either * .85 + (1 - either) * .15
    pr[:, C["P06"]] = a * .05 + (1 - a) * (b * .25 + (1 - b) * .55)
    pr[:, C["P12"]] = a * .85 + (1 - a) * (b * .5 + (1 - b) * .12)
    pr[:, C["P13"]] = a * .30 + (1 - a) * .03
    pr[:, C["P09"]] = c * .85 + (1 - c) * .05
    return pr


def world_cross(rng, grades=False):
    pa = np.array([P_INTJ[t] for t in TIERS]) * INTJ_BEARER
    pb = np.array([P_EXPR[t] for t in TIERS])
    if grades:
        def beta(p):
            p = np.clip(p, .05, .95)
            return rng.beta(2 * p, 2 * (1 - p))
        a = beta(pa) * INTJ_BEARER
        b = beta(pb)
    else:
        a = (rng.random(N) < pa).astype(float)
        b = (rng.random(N) < pb).astype(float)
    c = (rng.random(N) < .15).astype(float)
    X = (rng.random((N, M)) < _probs_cluster(a, b, c)).astype(int)
    return X, {"intj": a, "expr": b}


def world_bonds(rng, overlap, kappa=4.0, nb=40):
    bonds = rng.random((N, nb)) < .5
    X = np.empty((N, M), int)
    for p, j in C.items():
        s = BOND_SIGN[p]
        if s == 0:
            X[:, j] = rng.random(N) < .2
            continue
        S = rng.random(nb) < overlap
        if S.sum() == 0:
            S[rng.integers(nb)] = True
        k = S.sum()
        z = (bonds[:, S].sum(1) - k / 2) / np.sqrt(k / 4)
        o = rng.random(N) < 1 / (1 + np.exp(-kappa * z))
        X[:, j] = o if s > 0 else ~o
    return X, {"intj": None, "expr": None}


def world_indep(rng, marg):
    return (rng.random((N, M)) < marg).astype(int), {"intj": None,
                                                     "expr": None}


def oriented_phi(X, g):
    cols = GROUPINGS[g]["diag"]
    rows = UNIVERSE[g]
    O = np.column_stack([X[rows, C[p]] if GROUPINGS[g]["sign"][p] > 0
                         else 1 - X[rows, C[p]] for p in cols]).astype(float)
    phis = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            a, b = O[:, i], O[:, j]
            if a.std() == 0 or b.std() == 0:
                continue
            phis.append(np.corrcoef(a, b)[0, 1])
    return float(np.mean(phis)) if phis else 0.0


def calibrate(seed=7, reps=300):
    """Match the bonds overlap to world 1's within-grouping association
    (RULE.md, world 2), and the independence null's margins to world 1."""
    rng = np.random.default_rng(seed)
    cross = [world_cross(rng)[0] for _ in range(reps)]
    target = np.mean([(oriented_phi(X, "intj") + oriented_phi(X, "expr")) / 2
                      for X in cross])
    marg = np.mean(cross, axis=0).mean(axis=0)
    grid = np.round(np.linspace(.05, 1.0, 20), 3)
    best = None
    for s in grid:
        Xs = [world_bonds(rng, s)[0] for _ in range(reps)]
        phi = np.mean([(oriented_phi(X, "intj") + oriented_phi(X, "expr")) / 2
                       for X in Xs])
        if best is None or abs(phi - target) < abs(best[1] - target):
            best = (float(s), float(phi))
    return {"cross_phi": float(target), "bonds_overlap": best[0],
            "bonds_phi": best[1], "matched": bool(abs(best[1] - target) <= .02),
            "kappa": 4.0, "indep_margins": marg.tolist()}


# ----------------------------------------------------------- documentation

def applicability(X):
    """P11N is INAPPLICABLE for standalone-only uses (true P01=Y, P02=N)."""
    return ~((X[:, C["P01"]] == 1) & (X[:, C["P02"]] == 0))


def profile_score(X, g, applic):
    cols = GROUPINGS[g]["diag"]
    num = np.zeros(N)
    den = np.zeros(N)
    for p in cols:
        ok = applic if p == "P11N" else np.ones(N, bool)
        v = X[:, C[p]] if GROUPINGS[g]["sign"][p] > 0 else 1 - X[:, C[p]]
        num += np.where(ok, v, 0)
        den += ok
    return num / np.maximum(den, 1)


def document(X, rng, level, q_assumed, err=.05, p_same_obs=.05):
    lv = LEVELS[level]
    applic = applicability(X)
    q = np.full(M, q_assumed)
    for p in ("P10S", "P11N", "P12"):
        q[C[p]] = lv[p]
    pk = np.where(X == 1, np.minimum(.95, q * 4 / 3), q * 2 / 3)
    known = rng.random(X.shape) < pk
    known[~applic, C["P11N"]] = False
    Xc = X.copy()
    flip = known & (rng.random(X.shape) < err)
    Xc[flip] = 1 - Xc[flip]
    unit = np.full(X.shape, -1)
    for si, src in enumerate(SOURCES):
        g = src["grouping"]
        z = profile_score(X, g, applic)
        pin = np.clip(1.5 * z - .6, .02, .9) * src["scale"] * lv["incl"]
        incl = (rng.random(N) < pin) & UNIVERSE[g]
        for r in np.where(incl)[0]:
            for p, v in src["states"].items():
                j = C[p]
                if known[r, j] or (p == "P11N" and not applic[r]):
                    continue
                known[r, j] = True
                Xc[r, j] = v
                unit[r, j] = si * N + r
    couple = rng.random((N, M, M)) < p_same_obs
    return {"Xc": Xc, "known": known, "unit": unit, "couple": couple,
            "applic": applic}


# --------------------------------------------------------------- the model

def unit_weights(V, U, scheme):
    W = V.astype(float)
    inh = V & (U >= 0)
    if scheme == "cap":
        W[inh] = .5
    elif scheme == "split":
        for i in np.where(inh.any(1))[0]:
            ids = U[i, inh[i]]
            uniq, counts = np.unique(ids, return_counts=True)
            share = dict(zip(uniq, 1.0 / counts))
            for k in np.where(inh[i])[0]:
                W[i, k] = share[U[i, k]]
    return W


def estep(Y, W, theta, pi):
    Yw = W * Y
    ll = Yw @ np.log(theta).T + (W - Yw) @ np.log(1 - theta).T + np.log(pi)
    mx = ll.max(1, keepdims=True)
    post = np.exp(ll - mx)
    norm = post.sum(1, keepdims=True)
    return post / norm, float((mx[:, 0] + np.log(norm[:, 0])).sum())


def fit_lca(Y, W, rng, K=2, starts=8, iters=500, tol=1e-8):
    """Weighted binary latent-class model by EM, MAP with add-one smoothing
    (Beta(2,2) rates, Dirichlet(2) sizes). Returns the best fit and every
    start's penalized log-likelihood and hard partition."""
    n, m = Y.shape
    Yw = W * Y
    fits = []
    for _ in range(starts):
        theta = rng.uniform(.2, .8, (K, m))
        pi = np.full(K, 1.0 / K)
        prev = -np.inf
        for _ in range(iters):
            post, ll = estep(Y, W, theta, pi)
            theta = np.clip((post.T @ Yw + 1) / (post.T @ W + 2), 1e-4,
                            1 - 1e-4)
            pi = (post.sum(0) + 1) / (n + K)
            obj = ll + np.log(theta).sum() + np.log(1 - theta).sum() \
                + np.log(pi).sum()
            if abs(obj - prev) < tol:
                break
            prev = obj
        post, ll = estep(Y, W, theta, pi)
        obj = ll + np.log(theta).sum() + np.log(1 - theta).sum() \
            + np.log(pi).sum()
        fits.append((obj, post, theta, pi))
    fits.sort(key=lambda f: -f[0])
    return fits


def member_class(theta, signs):
    score = np.zeros(theta.shape[0])
    for k, s in enumerate(signs):
        score += theta[:, k] if s > 0 else 1 - theta[:, k]
    return int(np.argmax(score))


def logloss(y, p1):
    p = p1 if y == 1 else 1 - p1
    return float(-np.log(np.clip(p, EPS, 1 - EPS)))


def lr_prob(F, ref, r, y):
    model = LogisticRegression(C=1.0, solver="lbfgs", max_iter=300)
    model.fit(F[ref], y[ref])
    return float(model.predict_proba(F[[r]])[0, list(model.classes_).index(1)])


# ------------------------------------------------------ grouping and target

def grouping_record(doc, g):
    rows = np.where(UNIVERSE[g])[0]
    d = [C[p] for p in GROUPINGS[g]["diag"]]
    Y = doc["Xc"][np.ix_(rows, d)].astype(float)
    K = doc["known"][np.ix_(rows, d)]
    U = doc["unit"][np.ix_(rows, d)]
    inap = np.zeros_like(K)
    if "P11N" in GROUPINGS[g]["diag"]:
        inap[:, GROUPINGS[g]["diag"].index("P11N")] = ~doc["applic"][rows]
    signs = [GROUPINGS[g]["sign"][p] for p in GROUPINGS[g]["diag"]]
    return rows, d, Y, K, U, inap, signs


def visible_count(V, U):
    out = np.zeros(V.shape[0], int)
    for i in range(V.shape[0]):
        item = V[i] & (U[i] < 0)
        inh = V[i] & (U[i] >= 0)
        out[i] = item.sum() + len(np.unique(U[i, inh]))
    return out


def ppc(Y, V, theta, pi, rng, reps=200):
    """Posterior predictive check of pairwise residual dependence: summed
    Pearson X2 over diagnostic pairs, expected counts from the fitted
    marginal model, replicates on the same visibility pattern."""
    m = Y.shape[1]
    pairs = [(i, j) for i in range(m) for j in range(i + 1, m)]
    P = {}
    for (i, j) in pairs:
        tab = np.zeros((2, 2))
        for a in (0, 1):
            for b in (0, 1):
                pa = theta[:, i] if a else 1 - theta[:, i]
                pb = theta[:, j] if b else 1 - theta[:, j]
                tab[a, b] = float((pi * pa * pb).sum())
        P[(i, j)] = tab

    def stat(Ys):
        T = 0.0
        for (i, j) in pairs:
            both = V[:, i] & V[:, j]
            nb = both.sum()
            if nb < 2:
                continue
            E = nb * P[(i, j)]
            O = np.zeros((2, 2))
            for a in (0, 1):
                for b in (0, 1):
                    O[a, b] = np.sum((Ys[both, i] == a) & (Ys[both, j] == b))
            T += float(((O - E) ** 2 / np.maximum(E, 1e-6)).sum())
        return T

    t_obs = stat(Y)
    n = Y.shape[0]
    t_rep = np.empty(reps)
    for k in range(reps):
        z = rng.choice(len(pi), size=n, p=pi / pi.sum())
        t_rep[k] = stat((rng.random(Y.shape) < theta[z]).astype(float))
    return float(np.mean(t_rep >= t_obs)), t_obs


def grouping_checks(doc, g, scheme, rng, truth, boot=50):
    rows, d, Y, K, U, inap, signs = grouping_record(doc, g)
    W = unit_weights(K, U, scheme)
    fits = fit_lca(Y, W, rng)
    best = fits[0]
    mc = member_class(best[2], signs)
    pm = best[1][:, mc]
    hard = pm > .5
    near = [f for f in fits if f[0] >= best[0] - 1.0]
    agree = []
    for f in near[1:]:
        h = f[1][:, member_class(f[2], signs)] > .5
        agree.append(float(np.mean(h == hard)))
    m = len(d)
    # (a) support, (b) overlap
    a_ok = int((visible_count(K, U) >= 3).sum()) >= 10
    joint = [int((K[:, i] & K[:, j]).sum()) for i in range(m)
             for j in range(i + 1, m)]
    b_ok = min(joint) >= 5
    # (c) stability over bootstrap refits, plus spread of member rates
    cors, rates = [], []
    n = len(rows)
    for _ in range(boot):
        idx = rng.integers(0, n, n)
        bf = fit_lca(Y[idx], W[idx], rng, starts=4)[0]
        bmc = member_class(bf[2], signs)
        bpost, _ = estep(Y, W, bf[2], bf[3])
        bp = bpost[:, bmc]
        if bp.std() > 0 and pm.std() > 0:
            cors.append(float(np.corrcoef(bp, pm)[0, 1]))
        else:
            cors.append(0.0)
        rates.append(bf[2][bmc])
    c_med = float(np.median(cors))
    c_ok = c_med >= .8
    # (d) anchor compatibility
    gaps = [float(best[2][mc, GROUPINGS[g]["diag"].index(p)]
                  - best[2][1 - mc, GROUPINGS[g]["diag"].index(p)])
            for p in GROUPINGS[g]["anchors"]]
    d_ok = max(gaps) >= .3
    p_ppc, t_obs = ppc(Y, K, best[2], best[3], rng)
    out = {"a": a_ok, "b": b_ok, "c": c_ok, "d": d_ok,
           "all": bool(a_ok and b_ok and c_ok and d_ok),
           "c_median": c_med, "c_q10": float(np.quantile(cors, .1)),
           "rate_sd": np.std(rates, axis=0).tolist(),
           "anchor_gap": max(gaps), "near_best": len(near),
           "near_agree_min": min(agree) if agree else 1.0,
           "ppc_p": p_ppc, "ppc_T": t_obs, "min_joint": min(joint)}
    if truth is not None:
        tr = truth[rows]
        brier = float(np.mean((pm - tr) ** 2))
        ref = float(np.mean((tr - tr.mean()) ** 2))
        out["bss"] = 1 - brier / ref if ref > 0 else None
        out["brier"] = brier
        binary = set(np.unique(tr)) <= {0.0, 1.0}
        if binary and 0 < tr.sum() < len(tr):
            pos, neg = pm[tr == 1], pm[tr == 0]
            out["auc"] = float(np.mean(pos[:, None] > neg[None, :])
                               + .5 * np.mean(pos[:, None] == neg[None, :]))
        elif not binary:
            out["corr"] = float(np.corrcoef(pm, tr)[0, 1]) \
                if pm.std() > 0 else 0.0
    return out


def run_projection(doc, g, t, scheme, rng, capture=None):
    rows, d, Y, K, U, inap, signs = grouping_record(doc, g)
    tt = C[t]
    y = doc["Xc"][rows, tt].astype(int)
    tk = doc["known"][rows, tt].copy()
    tu = doc["unit"][rows, tt]
    t_item = tk & (tu < 0)
    item = K & (U < 0)
    same = K & (U >= 0) & (U == tu[:, None]) & tk[:, None]
    so = item & t_item[:, None] & doc["couple"][np.ix_(rows, d, [tt])][:, :, 0]
    conc = same | so
    V = K & ~conc
    W = unit_weights(V, U, scheme)
    best = fit_lca(Y, W, rng)[0]
    mc = member_class(best[2], signs)
    post = best[1][:, [mc, 1 - mc]]
    pm = post[:, 0]
    nd = ~K & ~inap
    miss = ~V & ~inap
    inap_cols = inap.any(0)
    sgn = np.array(signs, float)
    wsum = W.sum(1)
    conv = np.where(wsum > 0, (W * sgn * (2 * Y - 1)).sum(1)
                    / np.maximum(wsum, EPS), 0.0)[:, None]
    scored = np.where(tk)[0]
    keys = ["M0", "M1", "M1noind", "M1ud", "M2", "M3", "conv"] + \
        [f"single_{GROUPINGS[g]['diag'][k]}" for k in range(len(d))]
    losses = {k: [] for k in keys}
    for r in scored:
        ref = scored[scored != r]
        yr = y[ref]
        if yr.min() == yr.max():
            continue
        p0 = (yr.sum() + 1) / (len(ref) + 2)
        ll = {"M0": logloss(y[r], p0)}
        rates = []
        for c in range(2):
            w = post[ref, c]
            rates.append((w @ yr + 1) / (w.sum() + 2) if w.sum() >= 3
                         else p0)
        ll["M2"] = logloss(y[r], float(post[r] @ np.array(rates)))
        cols = {"full": [], "noind": [], "ud": []}
        for k in range(len(d)):
            refv = ref[V[ref, k]]
            mu = Y[refv, k].mean() if len(refv) else .5
            val = np.where(V[:, k], Y[:, k], mu)
            for v in cols:
                cols[v].append(val)
            cols["full"].append(miss[:, k].astype(float))
            cols["ud"].append(nd[:, k].astype(float))
            if inap_cols[k]:
                for v in cols:
                    cols[v].append(inap[:, k].astype(float))
        F = {v: np.column_stack(c) for v, c in cols.items()}
        ll["M1"] = logloss(y[r], lr_prob(F["full"], ref, r, y))
        ll["M1noind"] = logloss(y[r], lr_prob(F["noind"], ref, r, y))
        ll["M1ud"] = logloss(y[r], lr_prob(F["ud"], ref, r, y))
        ll["M3"] = logloss(y[r], lr_prob(
            np.column_stack([F["full"], pm]), ref, r, y))
        ll["conv"] = logloss(y[r], lr_prob(conv, ref, r, y))
        for k in range(len(d)):
            p = p0
            if V[r, k]:
                sel = ref[V[ref, k] & (Y[ref, k] == Y[r, k])]
                if len(sel) >= 3:
                    p = (y[sel].sum() + 1) / (len(sel) + 2)
            ll[f"single_{GROUPINGS[g]['diag'][k]}"] = logloss(y[r], p)
        for k_, v_ in ll.items():
            losses[k_].append(v_)
        if capture is not None:
            capture[int(r)] = ll
    n = len(losses["M0"])
    if n == 0:
        return None
    mean = {k: float(np.mean(v)) for k, v in losses.items()}
    return {"n": n, "loss": mean, "concealed": int(conc.sum())}


def one_dataset(task):
    world, level, q, scheme, seed, cal = task
    rng = np.random.default_rng(seed)
    if world == "cross":
        X, truth = world_cross(rng)
    elif world == "gom":
        X, truth = world_cross(rng, grades=True)
    elif world == "bonds":
        X, truth = world_bonds(rng, cal["bonds_overlap"], cal["kappa"])
    else:
        X, truth = world_indep(rng, np.array(cal["indep_margins"]))
    doc = document(X, rng, level, q)
    rec = {}
    for g in GROUPINGS:
        tr = truth[g]
        out = grouping_checks(doc, g, scheme, rng,
                              None if tr is None else np.asarray(tr, float))
        targets = {}
        for t in GROUPINGS[g]["targets"]:
            res = run_projection(doc, g, t, scheme, rng)
            if res is not None:
                targets[t] = res
        out["targets"] = targets
        if targets:
            fam = {}
            keys = targets[next(iter(targets))]["loss"].keys()
            for k in keys:
                fam[k] = float(np.mean([v["loss"]["M0"] - v["loss"][k]
                                        for v in targets.values()]))
            fam["suff_gap"] = float(np.mean(
                [v["loss"]["M2"] - v["loss"]["M3"] for v in targets.values()]))
            fam["anchor_best"] = max(fam[f"single_{a}"]
                                     for a in GROUPINGS[g]["anchors"])
            out["family_gain"] = fam
        rec[g] = out
    return {"world": world, "level": level, "q": q, "scheme": scheme,
            "rec": rec}


# ---------------------------------------------------------------- the rule

def auc(a, b):
    """P(a > b) + 0.5 P(a = b) over all pairs."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    if len(a) == 0 or len(b) == 0:
        return None
    return float(np.mean(a[:, None] > b[None, :])
                 + .5 * np.mean(a[:, None] == b[None, :]))


def evaluate(cells):
    """Apply RULE.md R1 to R3 to every (level, assumed rate) cell."""
    out = {}
    for level in LEVELS:
        for q in ASSUMED:
            cross = cells.get(("cross", level, q, "split"), [])
            bonds = cells.get(("bonds", level, q, "split"), [])
            key = f"{level}/q={q}"
            res = {}
            for g in GROUPINGS:
                cr = [d["rec"][g] for d in cross]
                bo = [d["rec"][g] for d in bonds]
                passed = [r for r in cr if r["all"]]
                pr = float(np.mean([r["all"] for r in cr])) if cr else 0.0
                bss = float(np.median([r["bss"] for r in passed])) \
                    if passed else None
                orient = float(np.mean([r.get("auc", 0) > .5
                                        for r in passed])) if passed else None
                r1 = bool(pr >= .5 and bss is not None and bss >= .30
                          and orient is not None and orient >= .9)
                fam_c = [r for r in cr if "family_gain" in r]
                fam_b = [r for r in bo if "family_gain" in r]
                auc_ppc = auc([-r["ppc_p"] for r in bo],
                              [-r["ppc_p"] for r in cr])
                auc_gap = auc([r["family_gain"]["suff_gap"] for r in fam_b],
                              [r["family_gain"]["suff_gap"] for r in fam_c])
                auc_gain = auc([r["family_gain"]["M2"] for r in fam_c],
                               [r["family_gain"]["M2"] for r in fam_b])
                r2 = bool(max(x for x in (auc_ppc or 0, auc_gap or 0))
                          >= .75)
                pf = [r for r in passed if "family_gain" in r]
                da = [r["family_gain"]["M2"] - r["family_gain"]["anchor_best"]
                      for r in pf]
                dc = [r["family_gain"]["M2"] - r["family_gain"]["conv"]
                      for r in pf]
                r3 = bool(pf and np.median(da) >= .01
                          and np.mean(np.array(da) > 0) >= .6
                          and np.median(dc) >= .01
                          and np.mean(np.array(dc) > 0) >= .6)
                res[g] = {
                    "R1": r1, "R1_pass_rate": pr, "R1_bss_median": bss,
                    "R1_oriented": orient, "n_cross": len(cr),
                    "n_passing": len(passed),
                    "R2": r2, "R2_auc_ppc": auc_ppc, "R2_auc_suffgap": auc_gap,
                    "auc_record_gain": auc_gain,
                    "R3": r3,
                    "R3_median_vs_anchor": float(np.median(da)) if da else None,
                    "R3_share_pos_anchor": float(np.mean(np.array(da) > 0))
                    if da else None,
                    "R3_median_vs_conv": float(np.median(dc)) if dc else None,
                    "R3_share_pos_conv": float(np.mean(np.array(dc) > 0))
                    if dc else None}
            res["met_R1_R2_both"] = all(res[g]["R1"] and res[g]["R2"]
                                        for g in GROUPINGS)
            out[key] = res
    verdict = {}
    met = [q for q in ASSUMED if out[f"audit/q={q}"]["met_R1_R2_both"]]
    if len(met) == len(ASSUMED):
        verdict["consequence"] = "met at all three assumed rates"
    elif met:
        verdict["consequence"] = "met at some assumed rates"
        verdict["lowest_rate_met"] = min(met)
    else:
        verdict["consequence"] = "met at none"
    out["verdict"] = verdict
    return out


def summarize(cells):
    """Reported statistics per cell (not ruled on)."""
    out = {}
    for (world, level, q, scheme), ds in cells.items():
        key = f"{world}/{level}/q={q}/{scheme}"
        s = {}
        for g in GROUPINGS:
            rs = [d["rec"][g] for d in ds]
            fam = [r["family_gain"] for r in rs if "family_gain" in r]
            s[g] = {
                "n": len(rs),
                "checks_pass": {c: float(np.mean([r[c] for r in rs]))
                                for c in ("a", "b", "c", "d", "all")},
                "near_best_median": float(np.median([r["near_best"]
                                                     for r in rs])),
                "near_agree_min_median": float(np.median(
                    [r["near_agree_min"] for r in rs])),
                "rate_sd_mean": float(np.mean([np.mean(r["rate_sd"])
                                               for r in rs])),
                "ppc_p_median": float(np.median([r["ppc_p"] for r in rs])),
                "ppc_p_le_0.05": float(np.mean([r["ppc_p"] <= .05
                                                for r in rs])),
                "family_gain_median": {k: float(np.median([f[k] for f in fam]))
                                       for k in fam[0]} if fam else None,
                "family_gain_q05_q95": {k: [float(np.quantile([f[k] for f in fam], .05)),
                                            float(np.quantile([f[k] for f in fam], .95))]
                                        for k in fam[0]} if fam else None,
                "m1_indicator_leak_median": float(np.median(
                    [f["M1"] - f["M1noind"] for f in fam])) if fam else None,
            }
            if rs and "bss" in rs[0]:
                s[g]["bss_median"] = float(np.median(
                    [r["bss"] for r in rs if r.get("bss") is not None]))
            targets = {}
            for t in GROUPINGS[g]["targets"]:
                tv = [r["targets"][t] for r in rs if t in r["targets"]]
                if tv:
                    targets[t] = {
                        "share_computable": len(tv) / len(rs),
                        "n_cells_median": float(np.median([v["n"] for v in tv])),
                        "concealed_median": float(np.median(
                            [v["concealed"] for v in tv])),
                        "gain_median": {k: float(np.median(
                            [v["loss"]["M0"] - v["loss"][k] for v in tv]))
                            for k in ("M1", "M1noind", "M1ud", "M2", "M3",
                                      "conv")}}
            s[g]["targets"] = targets
        out[key] = s
    return out


def tasks(sims_ruled, sims_reported, cal, seed=20261105):
    spec = []
    for level in LEVELS:
        for q in ASSUMED:
            for world in ("cross", "bonds", "indep"):
                spec.append((world, level, q, "split", sims_ruled))
    for world in ("cross", "bonds", "indep"):
        spec.append((world, "audit", .55, "cap", sims_reported))
    spec.append(("gom", "audit", .55, "split", sims_reported))
    ss = np.random.SeedSequence(seed)
    out = []
    for (world, level, q, scheme, k) in spec:
        for child in ss.spawn(k):
            out.append((world, level, q, scheme,
                        int(child.generate_state(1)[0]), cal))
    return out


def run(sims_ruled, sims_reported, procs=10):
    cal = calibrate()
    tl = tasks(sims_ruled, sims_reported, cal)
    with Pool(procs) as pool:
        recs = pool.map(one_dataset, tl, chunksize=4)
    cells = {}
    for t, r in zip(tl, recs):
        cells.setdefault(t[:4], []).append(r)
    return cal, cells


# ------------------------------------------------------------------- tests

def self_tests(seed=3):
    rng = np.random.default_rng(seed)
    # 1. Weighted EM with unit weights recovers planted classes.
    n, m = 400, 6
    z = rng.random(n) < .5
    Y = (rng.random((n, m)) < np.where(z[:, None], .9, .1)).astype(float)
    V = rng.random((n, m)) < .7
    best = fit_lca(Y, V.astype(float), rng)[0]
    mc = member_class(best[2], [1] * m)
    assert np.mean((best[1][:, mc] > .5) == z) > .9, "LCA recovery"
    # 2. Split weighting: a unit's visible cells share a total weight of 1.
    Vt = np.array([[True, True, True, False]])
    Ut = np.array([[5, 5, -1, 5]])
    Wt = unit_weights(Vt, Ut, "split")
    assert np.allclose(Wt, [[.5, .5, 1.0, 0.0]]), Wt
    assert np.allclose(unit_weights(Vt, Ut, "cap"), [[.5, .5, 1.0, 0.0]])
    # 3. Rows with nothing visible get the class prior.
    best = fit_lca(Y[:5], np.zeros((5, m)), rng)[0]
    assert np.allclose(best[1], np.tile(best[3], (5, 1)), atol=1e-6)
    # 4. Same-inclusion concealment hits reference rows too, and the
    #    scored target value never enters its own prediction.
    X, _ = world_cross(rng)
    doc = document(X, rng, "audit", .55)
    g, t = "intj", "P06"
    rows, d, Y4, K4, U4, inap, signs = grouping_record(doc, g)
    tu = doc["unit"][rows, C[t]]
    shared = (K4 & (U4 >= 0) & (U4 == tu[:, None])).any(1)
    assert shared.sum() >= 2, "need rows with a shared inclusion"
    r1 = run_projection(doc, g, t, "split", np.random.default_rng(1))
    assert r1["concealed"] >= shared.sum()
    # 5. INAPPLICABLE P11N rows are never visible or scored.
    assert not doc["known"][~doc["applic"], C["P11N"]].any()
    # 6. Bonds calibration reaches the declared match.
    cal = calibrate(reps=60)
    assert cal["matched"], cal
    return "self-tests passed", cal


def leak_test(seed=5):
    """The scored cell's own value must not enter its prediction. With the
    value flipped and the same random stream, every predictor gives that
    cell the same probability, so p(y) + p(1 - y) = 1."""
    rng = np.random.default_rng(seed)
    X, _ = world_cross(rng)
    doc = document(X, rng, "audit", .70)
    for g, t in (("intj", "P06"), ("expr", "P12")):
        rows = np.where(UNIVERSE[g])[0]
        cap_a = {}
        run_projection(doc, g, t, "split", np.random.default_rng(9), cap_a)
        for s in list(cap_a)[:4]:
            d2 = {k: (v.copy() if isinstance(v, np.ndarray) else v)
                  for k, v in doc.items()}
            r = rows[s]
            d2["Xc"][r, C[t]] = 1 - d2["Xc"][r, C[t]]
            cap_b = {}
            run_projection(d2, g, t, "split", np.random.default_rng(9), cap_b)
            for k in cap_a[s]:
                tot = np.exp(-cap_a[s][k]) + np.exp(-cap_b[s][k])
                assert abs(tot - 1) < 1e-6, (g, t, k, tot)
    return "leak test passed"


# ------------------------------------------------------------------- main

def file_sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "selftest"
    if mode == "selftest":
        msg, cal = self_tests()
        print(msg)
        print(leak_test())
        print("calibration (reps=60):", json.dumps(cal)[:200])
    elif mode == "smoke":
        t0 = time.time()
        cal, cells = run(sims_ruled=2, sims_reported=1)
        n = sum(len(v) for v in cells.values())
        ok = all(np.isfinite(r["rec"][g]["ppc_p"]) for v in cells.values()
                 for r in v for g in GROUPINGS)
        print(f"smoke: {n} datasets, finite={ok}, "
              f"{(time.time() - t0) / n:.2f} s per dataset (10 procs)")
    elif mode == "full":
        sims_ruled = int(sys.argv[2]) if len(sys.argv) > 2 else 150
        sims_rep = int(sys.argv[3]) if len(sys.argv) > 3 else 100
        t0 = time.time()
        cal, cells = run(sims_ruled, sims_rep)
        result = {"meta": {
            "rule_sha256": file_sha(os.path.join(HERE, "RULE.md")),
            "harness_sha256": file_sha(os.path.abspath(__file__)),
            "items_sha256": file_sha(ITEMS),
            "sims_ruled": sims_ruled, "sims_reported": sims_rep,
            "calibration": cal, "python": sys.executable,
            "runtime_s": None},
            "rule": evaluate(cells), "reported": summarize(cells)}
        result["meta"]["runtime_s"] = round(time.time() - t0, 1)
        with open(os.path.join(HERE, "results-round7.json"), "w") as fh:
            json.dump(result, fh, indent=1)
        print("written results-round7.json; runtime",
              result["meta"]["runtime_s"], "s")
