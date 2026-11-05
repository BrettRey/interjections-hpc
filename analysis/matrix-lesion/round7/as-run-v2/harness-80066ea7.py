"""Round 7 fake-data harness for FREEZE-v4 (plan: RULE.md v2 in this folder).

Written 2026-11-05. The plan (RULE.md) was fixed and hashed before any
full run (DECISIONS.md). v1 of the plan set pass/fail thresholds; Brett
asked "Why are we using thresholds at all? What would Gelman do?" and
approved v2, which fixes what is simulated, computed and shown instead.
This version also takes in Codex's review of the v1 harness
(review-codex-2026-11-05/REPORT-codex.md; reviewed copy
harness-as-reviewed.py).

Simulates the FREEZE-v4 section 2 and 4 procedure on fake 46-row records
documented as patchily as the 12-item target audit suggests. No real
coded cell is used. Item tiers and universes come from items-v4.csv,
which is design data, not outcomes. Self-contained: it doesn't import
lesion.py, which holds the pre-v4 schema.

Usage (from analysis/matrix-lesion, with the project venv):
  .venv/bin/python -I round7/harness.py selftest
  .venv/bin/python -I round7/harness.py smoke   # bugs and timing only; prints no statistics
  .venv/bin/python -I round7/harness.py full [sims] [sims_reported]
"""
import csv
import gzip
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
SHARED = ["P06", "P09", "P12", "P13"]
# Entailed source-target pairs (FREEZE section 4): a use with no host is
# standalone, not a supplement and not integrated, so P11N's state is
# entailed by P01, P02 and P03.
ENTAILED = {("expr", "P01"): ["P11N"], ("expr", "P02"): ["P11N"],
            ("expr", "P03"): ["P11N"]}

# Bonds world: sign orientation (0 = independent) and field.
BOND_SIGN = {"P01": 1, "P02": 1, "P03": -1, "P04": -1, "P05": -1,
             "P06": -1, "P07": 1, "P08": 1, "P09": 0, "P10S": 1,
             "P11N": 1, "P12": 1, "P13": 1}
FIELD_I = {"P01", "P02", "P03", "P04", "P05", "P06", "P12", "P13"}
FIELD_E = {"P08", "P10S", "P11N"}

# Tier membership probabilities (assumed; RULE.md, world 1).
P_INTJ = {"core": .95, "boundary": .5, "control": .05, "extension": .3,
          "expr-core": .2, "expr-control": .05}
P_EXPR = {"core": .7, "boundary": .5, "control": .1, "extension": .3,
          "expr-core": .95, "expr-control": .05}

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
    the unrelated depictive grade c (0/1 for classes, [0, 1] for grades)."""
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
    pa = np.array([P_INTJ[t] for t in TIERS])
    pb = np.array([P_EXPR[t] for t in TIERS])
    if grades:
        def beta(p):
            p = np.clip(p, .05, .95)
            return rng.beta(2 * p, 2 * (1 - p))
        a, b = beta(pa), beta(pb)
    else:
        a = (rng.random(N) < pa).astype(float)
        b = (rng.random(N) < pb).astype(float)
    c = (rng.random(N) < .15).astype(float)
    X = (rng.random((N, M)) < _probs_cluster(a, b, c)).astype(int)
    return X, {"intj": a, "expr": b}


def world_bonds(rng, s_i, s_e, kappa=4.0, nb=40):
    bonds = rng.random((N, nb)) < .5
    X = np.empty((N, M), int)
    for p, j in C.items():
        sign = BOND_SIGN[p]
        if sign == 0:
            X[:, j] = rng.random(N) < .2
            continue
        s = s_i if p in FIELD_I else s_e if p in FIELD_E else (s_i + s_e) / 2
        S = rng.random(nb) < s
        if S.sum() == 0:
            S[rng.integers(nb)] = True
        k = S.sum()
        z = (bonds[:, S].sum(1) - k / 2) / np.sqrt(k / 4)
        o = rng.random(N) < 1 / (1 + np.exp(-kappa * z))
        X[:, j] = o if sign > 0 else ~o
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


def calibrate(seed=7, reps=200):
    """Choose (s_I, s_E) so each grouping's mean oriented phi among its
    diagnostics is within 0.02 of world 1's (RULE.md, world 2)."""
    rng = np.random.default_rng(seed)
    cross = [world_cross(rng)[0] for _ in range(reps)]
    target = {g: float(np.mean([oriented_phi(X, g) for X in cross]))
              for g in GROUPINGS}
    marg = np.mean(cross, axis=0).mean(axis=0)
    grid = np.round(np.arange(.5, 1.0001, .025), 3)

    def phi(si, se):
        # common random numbers: the same draws at every grid point
        r2 = np.random.default_rng(seed + 1)
        Xs = [world_bonds(r2, si, se)[0] for _ in range(reps)]
        return {g: float(np.mean([oriented_phi(X, g) for X in Xs]))
                for g in GROUPINGS}

    si = se = .8
    for _ in range(3):
        si = min(grid, key=lambda s: abs(phi(s, se)["intj"] - target["intj"]))
        se = min(grid, key=lambda s: abs(phi(si, s)["expr"] - target["expr"]))
    got = phi(si, se)
    err = max(abs(got[g] - target[g]) for g in GROUPINGS)
    return {"cross_phi": target, "s_i": float(si), "s_e": float(se),
            "bonds_phi": got, "max_error": float(err),
            "matched": bool(err <= .02), "kappa": 4.0,
            "indep_margins": marg.tolist()}


# ----------------------------------------------------------- documentation

def applicability(X):
    """P11N is INAPPLICABLE for standalone-only uses (true P01=Y, P02=N)."""
    return ~((X[:, C["P01"]] == 1) & (X[:, C["P02"]] == 0))


def profile_score(X, g, applic):
    num = np.zeros(N)
    den = np.zeros(N)
    for p in GROUPINGS[g]["diag"]:
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


def _objective(ll, theta, pi):
    return ll + np.log(theta).sum() + np.log(1 - theta).sum() \
        + np.log(pi).sum()


def fit_lca(Y, W, rng, K=2, starts=8, iters=500, tol=1e-8):
    """Weighted binary latent-class model by EM, MAP with add-one smoothing
    (Beta(2,2) rates, Dirichlet(2) sizes). Returns every start's fit,
    best penalized log-likelihood first."""
    n, m = Y.shape
    Yw = W * Y
    fits = []
    for _ in range(starts):
        theta = rng.uniform(.2, .8, (K, m))
        pi = np.full(K, 1.0 / K)
        prev = -np.inf
        for _ in range(iters):
            post, _ = estep(Y, W, theta, pi)
            theta = np.clip((post.T @ Yw + 1) / (post.T @ W + 2), 1e-4,
                            1 - 1e-4)
            pi = (post.sum(0) + 1) / (n + K)
            _, ll = estep(Y, W, theta, pi)
            obj = _objective(ll, theta, pi)
            if abs(obj - prev) < tol:
                break
            prev = obj
        post, ll = estep(Y, W, theta, pi)
        fits.append((_objective(ll, theta, pi), post, theta, pi))
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
    yr = y[ref]
    if np.unique(yr).size == 1:
        return float((yr.sum() + 1) / (len(ref) + 2))
    model = LogisticRegression(C=1.0, solver="lbfgs", max_iter=300)
    model.fit(F[ref], yr)
    return float(model.predict_proba(F[[r]])[0, list(model.classes_).index(1)])


# ------------------------------------------------------ grouping and target

def grouping_record(doc, g):
    rows = np.where(UNIVERSE[g])[0]
    d = [C[p] for p in GROUPINGS[g]["diag"]]
    Y = doc["Xc"][np.ix_(rows, d)].astype(float)
    K = doc["known"][np.ix_(rows, d)].copy()
    U = doc["unit"][np.ix_(rows, d)].copy()
    inap = np.zeros_like(K)
    if "P11N" in GROUPINGS[g]["diag"]:
        inap[:, GROUPINGS[g]["diag"].index("P11N")] = ~doc["applic"][rows]
    signs = [GROUPINGS[g]["sign"][p] for p in GROUPINGS[g]["diag"]]
    return rows, d, Y, K, U, inap, signs


def projection_state(doc, g, t):
    """Information state for projection (g, t) after concealment."""
    rows, d, Y, K, U, inap, signs = grouping_record(doc, g)
    for p in ENTAILED.get((g, t), []):
        k = GROUPINGS[g]["diag"].index(p)
        K[:, k] = False
        U[:, k] = -1
        inap[:, k] = False
        Y[:, k] = 0
    tt = C[t]
    tk = doc["known"][rows, tt].copy()
    tu = doc["unit"][rows, tt]
    t_item = tk & (tu < 0)
    item = K & (U < 0)
    same = K & (U >= 0) & (U == tu[:, None]) & tk[:, None]
    so = item & t_item[:, None] & doc["couple"][np.ix_(rows, d, [tt])][:, :, 0]
    conc = same | so
    V = K & ~conc
    return {"rows": rows, "d": d, "Y": Y, "K": K, "U": U, "inap": inap,
            "signs": signs, "V": V, "conc": conc, "tk": tk}


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
    both = {(i, j): V[:, i] & V[:, j] for (i, j) in pairs}

    def stat(Ys):
        T = 0.0
        for (i, j) in pairs:
            bm = both[(i, j)]
            nb = bm.sum()
            if nb < 2:
                continue
            E = nb * P[(i, j)]
            yi, yj = Ys[bm, i], Ys[bm, j]
            O = np.array([[np.sum((yi == a) & (yj == b)) for b in (0, 1)]
                          for a in (0, 1)], float)
            T += float(((O - E) ** 2 / np.maximum(E, 1e-6)).sum())
        return T

    t_obs = stat(Y)
    n = Y.shape[0]
    t_rep = np.empty(reps)
    for k in range(reps):
        z = rng.choice(len(pi), size=n, p=pi / pi.sum())
        t_rep[k] = stat((rng.random(Y.shape) < theta[z]).astype(float))
    return float(np.mean(t_rep >= t_obs)), t_obs


def recovery(pm, tr):
    out = {}
    brier = float(np.mean((pm - tr) ** 2))
    ref = float(np.mean((tr - tr.mean()) ** 2))
    out["bss"] = 1 - brier / ref if ref > 0 else None
    binary = set(np.unique(tr)) <= {0.0, 1.0}
    if binary and 0 < tr.sum() < len(tr):
        pos, neg = pm[tr == 1], pm[tr == 0]
        out["auc"] = float(np.mean(pos[:, None] > neg[None, :])
                           + .5 * np.mean(pos[:, None] == neg[None, :]))
    elif not binary:
        out["corr"] = float(np.corrcoef(pm, tr)[0, 1]) if pm.std() > 0 \
            else 0.0
    bins = np.minimum((pm * 5).astype(int), 4)
    out["calib"] = [[int((bins == b).sum()), float(tr[bins == b].sum())]
                    for b in range(5)]
    return out


def checks(Y, V, U, W, signs, anchor_idx, rng, boot):
    """FREEZE section 2 estimability checks a to d on this information
    state. Returns (checks, all fits, member class)."""
    m = Y.shape[1]
    a_ok = int((visible_count(V, U) >= 3).sum()) >= 10
    joint = [int((V[:, i] & V[:, j]).sum()) for i in range(m)
             for j in range(i + 1, m)]
    b_ok = min(joint) >= 5
    fits = fit_lca(Y, W, rng)
    best = fits[0]
    mc = member_class(best[2], signs)
    pm = best[1][:, mc]
    out = {"a": a_ok, "b": b_ok, "min_joint": min(joint)}
    gaps = [float(best[2][mc, k] - best[2][1 - mc, k]) for k in anchor_idx]
    out["anchor_gap"] = max(gaps)
    out["d"] = max(gaps) >= .3
    if boot:
        cors, rates = [], []
        n = Y.shape[0]
        for _ in range(boot):
            idx = rng.integers(0, n, n)
            bf = fit_lca(Y[idx], W[idx], rng)[0]
            bmc = member_class(bf[2], signs)
            bp = estep(Y, W, bf[2], bf[3])[0][:, bmc]
            cors.append(float(np.corrcoef(bp, pm)[0, 1])
                        if bp.std() > 0 and pm.std() > 0 else 0.0)
            rates.append(bf[2][bmc])
        out["c_median"] = float(np.median(cors))
        out["c"] = out["c_median"] >= .8
        out["rate_sd"] = float(np.mean(np.std(rates, axis=0)))
        out["all"] = bool(a_ok and b_ok and out["c"] and out["d"])
    near = [f for f in fits if f[0] >= best[0] - 1.0]
    hard = pm > .5
    agree = [float(np.mean((f[1][:, member_class(f[2], signs)] > .5) == hard))
             for f in near[1:]]
    out["near_best"] = len(near)
    out["near_agree_min"] = min(agree) if agree else 1.0
    return out, fits, mc


def run_projection(doc, g, t, scheme, rng, truth=None, score_mask=None,
                   boot=50, capture=None):
    st = projection_state(doc, g, t)
    rows, Y, U, V, inap, K = (st["rows"], st["Y"], st["U"], st["V"],
                              st["inap"], st["K"])
    names = GROUPINGS[g]["diag"]
    anchor_idx = [names.index(p) for p in GROUPINGS[g]["anchors"]]
    W = unit_weights(V, U, scheme)
    chk, fits, mc = checks(Y, V, U, W, st["signs"], anchor_idx, rng, boot)
    best = fits[0]
    post = best[1][:, [mc, 1 - mc]]
    pm = post[:, 0]
    out = {"checks": chk, "concealed": int(st["conc"].sum())}
    if truth is not None:
        out["recovery"] = recovery(pm, truth[rows])
    y = doc["Xc"][rows, C[t]].astype(int)
    tk = st["tk"] if score_mask is None else st["tk"] & score_mask[rows]
    scored = np.where(tk)[0]
    if len(scored) < 2 or len(np.unique(y[scored])) < 2:
        out["computable"] = False
        return out
    nd = ~K & ~inap
    miss = ~V & ~inap
    inap_cols = inap.any(0)
    sgn = np.array(st["signs"], float)
    nv = V.sum(1)
    conv = np.where(nv > 0, (V * sgn * (2 * Y - 1)).sum(1)
                    / np.maximum(nv, 1), 0.0)[:, None]
    keys = ["M0", "M1", "M1noind", "M1ud", "M2", "M3", "conv"] + \
        [f"single_{p}" for p in names]
    losses = {k: [] for k in keys}
    for r in scored:
        ref = scored[scored != r]
        yr = y[ref]
        p0 = (yr.sum() + 1) / (len(ref) + 2)
        ll = {"M0": logloss(y[r], p0)}
        rates = []
        for c in range(2):
            w = post[ref, c]
            rates.append((w @ yr + 1) / (w.sum() + 2) if w.sum() >= 3
                         else p0)
        ll["M2"] = logloss(y[r], float(post[r] @ np.array(rates)))
        cols = {"full": [], "noind": [], "ud": []}
        for k in range(len(names)):
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
        for k, p in enumerate(names):
            pk = p0
            if V[r, k]:
                sel = ref[V[ref, k] & (Y[ref, k] == Y[r, k])]
                if len(sel) >= 3:
                    pk = (y[sel].sum() + 1) / (len(sel) + 2)
            ll[f"single_{p}"] = logloss(y[r], pk)
        for k_, v_ in ll.items():
            losses[k_].append(v_)
        if capture is not None:
            capture[int(r)] = ll
    out.update({"computable": True, "n": len(scored),
                "loss": {k: float(np.mean(v)) for k, v in losses.items()}})
    return out


def grouping_full(doc, g, scheme, rng, truth):
    """Full-record fit (no target concealment): recovery and the
    posterior predictive check."""
    rows, d, Y, K, U, inap, signs = grouping_record(doc, g)
    W = unit_weights(K, U, scheme)
    best = fit_lca(Y, W, rng)[0]
    mc = member_class(best[2], signs)
    pm = best[1][:, mc]
    out = {}
    if truth is not None:
        out["recovery"] = recovery(pm, truth[rows])
    out["ppc_p"], out["ppc_T"] = ppc(Y, K, best[2], best[3], rng)
    return out


def family(targets, anchors):
    comp = {t: v for t, v in targets.items() if v.get("computable")}
    if not comp:
        return None
    keys = next(iter(comp.values()))["loss"].keys()
    fam = {k: float(np.mean([v["loss"]["M0"] - v["loss"][k]
                             for v in comp.values()])) for k in keys}
    fam["suff_gap"] = float(np.mean([v["loss"]["M2"] - v["loss"]["M3"]
                                     for v in comp.values()]))
    fam["anchor_best"] = max(fam[f"single_{a}"] for a in anchors)
    fam["n_targets"] = len(comp)
    return fam


def one_dataset(task):
    world, level, q, scheme, seed, cal, boot = task
    rng = np.random.default_rng(seed)
    if world == "cross":
        X, truth = world_cross(rng)
    elif world == "gom":
        X, truth = world_cross(rng, grades=True)
    elif world == "bonds":
        X, truth = world_bonds(rng, cal["s_i"], cal["s_e"], cal["kappa"])
    else:
        X, truth = world_indep(rng, np.array(cal["indep_margins"]))
    doc = document(X, rng, level, q)
    rec = {}
    for g in GROUPINGS:
        tr = None if truth[g] is None else np.asarray(truth[g], float)
        out = grouping_full(doc, g, scheme, rng, tr)
        out["targets"] = {t: run_projection(doc, g, t, scheme, rng, tr,
                                            boot=boot)
                          for t in GROUPINGS[g]["targets"]}
        out["family"] = family(out["targets"], GROUPINGS[g]["anchors"])
        rec[g] = out
    rec["expr_shared"] = {t: run_projection(doc, "expr", t, scheme, rng,
                                            None, score_mask=INTJ_BEARER,
                                            boot=0)
                          for t in SHARED}
    return {"world": world, "level": level, "q": q, "scheme": scheme,
            "rec": rec}


# ------------------------------------------------------------- true values

def _mi(cls, t):
    """Mutual information (nats) between a binary class and a binary
    target, from pooled draws."""
    def H(p):
        p = np.clip(p, 1e-12, 1 - 1e-12)
        return -(p * np.log(p) + (1 - p) * np.log(1 - p))
    h = H(t.mean())
    for c in (0, 1):
        sel = cls == c
        if sel.any():
            h -= sel.mean() * H(t[sel].mean())
    return float(h)


def true_values(seed=11, reps=4000):
    """RULE.md: D for each grouping and target in world 1, and on the 41
    shared rows for the cross-inquiry comparison."""
    rng = np.random.default_rng(seed)
    Xs, As, Bs = [], [], []
    for _ in range(reps):
        X, tr = world_cross(rng)
        Xs.append(X)
        As.append(tr["intj"])
        Bs.append(tr["expr"])
    X = np.vstack(Xs)
    A = np.concatenate(As)
    B = np.concatenate(Bs)
    app = applicability(X)
    univ = {"intj": np.tile(INTJ_BEARER, reps), "expr": np.ones(len(A), bool)}
    cls = {"intj": A, "expr": B}
    D = {}
    for g in GROUPINGS:
        D[g] = {}
        for t in GROUPINGS[g]["targets"]:
            sel = univ[g] & (app if t == "P11N" else True)
            D[g][t] = _mi(cls[g][sel], X[sel, C[t]])
    shared = np.tile(INTJ_BEARER, reps)
    Ds = {t: {g: _mi(cls[g][shared], X[shared, C[t]]) for g in GROUPINGS}
          for t in SHARED}
    return {"D": D, "D_shared": Ds}


# ---------------------------------------------------------------- summaries

def q3(v):
    v = np.asarray([x for x in v if x is not None], float)
    if len(v) == 0:
        return None
    return {"median": float(np.median(v)), "q05": float(np.quantile(v, .05)),
            "q95": float(np.quantile(v, .95)), "n": int(len(v))}


def auc(a, b):
    """P(a > b) + 0.5 P(a = b) over all pairs."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    if len(a) == 0 or len(b) == 0:
        return None
    return float(np.mean(a[:, None] > b[None, :])
                 + .5 * np.mean(a[:, None] == b[None, :]))


GAIN_KEYS = ["M1", "M1noind", "M1ud", "M2", "M3", "conv"]


def summarize_cell(ds, world, tv):
    s = {}
    for g in GROUPINGS:
        rs = [d["rec"][g] for d in ds]
        names = GROUPINGS[g]["diag"]
        out = {"n": len(rs)}
        proj = [v for r in rs for v in r["targets"].values()]
        if rs and "recovery" in rs[0]:
            out["recovery_full_bss"] = q3([r["recovery"]["bss"] for r in rs])
            out["oriented_share"] = float(np.mean(
                [r["recovery"].get("auc", 0) > .5 for r in rs])) \
                if "auc" in rs[0]["recovery"] else None
            cal = np.zeros((5, 2))
            for r in rs:
                cal += np.array(r["recovery"]["calib"])
            out["calibration"] = [{"bin": f"{b / 5:.1f}-{(b + 1) / 5:.1f}",
                                   "rows": int(cal[b, 0]),
                                   "member_share": float(cal[b, 1] / cal[b, 0])
                                   if cal[b, 0] else None}
                                  for b in range(5)]
            out["recovery_projection_bss_pass"] = q3(
                [v["recovery"]["bss"] for v in proj if v["checks"]["all"]])
            out["recovery_projection_bss_fail"] = q3(
                [v["recovery"]["bss"] for v in proj if not v["checks"]["all"]])
        out["checks_pass_projection"] = {
            c: float(np.mean([v["checks"][c] for v in proj]))
            for c in ("a", "b", "c", "d", "all")}
        out["near_best_median"] = float(np.median(
            [v["checks"]["near_best"] for v in proj]))
        out["near_agree_min_median"] = float(np.median(
            [v["checks"]["near_agree_min"] for v in proj]))
        out["rate_sd_mean"] = float(np.mean(
            [v["checks"]["rate_sd"] for v in proj]))
        out["ppc_p"] = q3([r["ppc_p"] for r in rs])
        targets = {}
        for t in GROUPINGS[g]["targets"]:
            tv_ = [r["targets"][t] for r in rs]
            comp = [v for v in tv_ if v.get("computable")]
            e = {"share_computable": len(comp) / len(tv_),
                 "concealed": q3([v["concealed"] for v in tv_]),
                 "checks_all": float(np.mean([v["checks"]["all"]
                                              for v in tv_]))}
            if comp:
                e["n_cells"] = q3([v["n"] for v in comp])
                e["gain"] = {k: q3([v["loss"]["M0"] - v["loss"][k]
                                    for v in comp])
                             for k in GAIN_KEYS + [f"single_{p}"
                                                   for p in names]}
                e["suff_gap"] = q3([v["loss"]["M2"] - v["loss"]["M3"]
                                    for v in comp])
            if world == "cross":
                D = tv["D"][g][t]
                e["D"] = D
                est = [v["loss"]["M0"] - v["loss"]["M2"] for v in comp]
                if comp and D > 1e-9:
                    e["type_s"] = float(np.mean(np.array(est) < 0))
                    e["ratio"] = q3(np.array(est) / D)
            targets[t] = e
        out["targets"] = targets
        fam = [r["family"] for r in rs if r["family"]]
        if fam:
            out["family"] = {k: q3([f[k] for f in fam])
                             for k in GAIN_KEYS + ["suff_gap", "anchor_best"]}
            da = [f["M2"] - f["anchor_best"] for f in fam]
            dc = [f["M2"] - f["conv"] for f in fam]
            out["m2_minus_anchor"] = dict(q3(da), share_pos=float(
                np.mean(np.array(da) > 0)))
            out["m2_minus_conv"] = dict(q3(dc), share_pos=float(
                np.mean(np.array(dc) > 0)))
            out["m1_indicator_leak"] = q3([f["M1"] - f["M1noind"]
                                           for f in fam])
        if world == "cross":
            win_p09, win_err, n_win = 0, [], 0
            for r in rs:
                comp = {t: v for t, v in r["targets"].items()
                        if v.get("computable")}
                if not comp:
                    continue
                gains = {t: v["loss"]["M0"] - v["loss"]["M2"]
                         for t, v in comp.items()}
                w = max(gains, key=gains.get)
                n_win += 1
                win_p09 += w == "P09"
                win_err.append(gains[w] - tv["D"][g][w])
            out["winner"] = {"share_P09": win_p09 / n_win if n_win else None,
                             "estimate_minus_D": q3(win_err)}
        s[g] = out
    shared = {}
    for t in SHARED:
        diffs = []
        for d in ds:
            a = d["rec"]["intj"]["targets"][t]
            b = d["rec"]["expr_shared"][t]
            if a.get("computable") and b.get("computable"):
                diffs.append((a["loss"]["M0"] - a["loss"]["M2"])
                             - (b["loss"]["M0"] - b["loss"]["M2"]))
        e = {"estimate": q3(diffs),
             "share_computable_both": len(diffs) / len(ds)}
        if world == "cross" and diffs:
            Dd = tv["D_shared"][t]["intj"] - tv["D_shared"][t]["expr"]
            e["D_diff"] = Dd
            if abs(Dd) > 1e-9:
                e["type_s"] = float(np.mean(np.sign(diffs) != np.sign(Dd)))
        shared[t] = e
    s["shared"] = shared
    return s


def summarize(cells, tv):
    out = {}
    for (world, level, q, scheme), ds in cells.items():
        out[f"{world}/{level}/q={q}/{scheme}"] = summarize_cell(ds, world, tv)
    overlap = {}
    for level in LEVELS:
        for q in ASSUMED:
            cr = cells.get(("cross", level, q, "split"), [])
            for other in ("bonds", "indep"):
                ot = cells.get((other, level, q, "split"), [])
                key = f"cross_vs_{other}/{level}/q={q}"
                overlap[key] = {}
                for g in GROUPINGS:
                    fc = [d["rec"][g]["family"] for d in cr
                          if d["rec"][g]["family"]]
                    fo = [d["rec"][g]["family"] for d in ot
                          if d["rec"][g]["family"]]
                    overlap[key][g] = {
                        "ppc": auc([-d["rec"][g]["ppc_p"] for d in ot],
                                   [-d["rec"][g]["ppc_p"] for d in cr]),
                        "suff_gap": auc([f["suff_gap"] for f in fo],
                                        [f["suff_gap"] for f in fc]),
                        "record_gain": auc([-f["M2"] for f in fo],
                                           [-f["M2"] for f in fc])}
    out["overlap_auc"] = overlap
    return out


# ------------------------------------------------------------------ figures

def _gain(v, k="M2"):
    return v["loss"]["M0"] - v["loss"][k]


def figures(cells, tv, outdir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    os.makedirs(outdir, exist_ok=True)
    regimes = [(lv, q) for lv in LEVELS for q in ASSUMED]
    rlab = [f"{lv[:5]} {q:.2f}" for lv, q in regimes]
    gl = {"intj": "INTJ", "expr": "EXPRESSIVE"}

    def interval(ax, xpos, e, col, label=None, marker="o", ms=5):
        lo, md, hi = np.quantile(e, [.05, .5, .95])
        ax.plot([xpos, xpos], [lo, hi], color=col, lw=.9)
        ax.plot(xpos, md, marker, color=col, ms=ms, label=label)

    # 1. recovery across the documentation grid (world 1)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
    for ax, g in zip(axes, GROUPINGS):
        data = [[d["rec"][g]["recovery"]["bss"]
                 for d in cells.get(("cross", lv, q, "split"), [])]
                for lv, q in regimes]
        ax.boxplot(data, tick_labels=rlab, showfliers=False)
        ax.axhline(0, color="grey", lw=.8)
        ax.set_title(f"{gl[g]}: membership recovery (world 1)")
        ax.tick_params(axis="x", rotation=45)
    axes[0].set_ylabel("Brier skill score vs true membership")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "1-recovery.png"), dpi=130)
    plt.close(fig)

    # 2. calibration (world 1, audit-like level)
    fig, axes = plt.subplots(1, 2, figsize=(9, 4), sharey=True)
    for ax, g in zip(axes, GROUPINGS):
        for q in ASSUMED:
            cal = np.zeros((5, 2))
            for d in cells.get(("cross", "audit", q, "split"), []):
                cal += np.array(d["rec"][g]["recovery"]["calib"])
            x = (np.arange(5) + .5) / 5
            yv = np.where(cal[:, 0] > 0,
                          cal[:, 1] / np.maximum(cal[:, 0], 1), np.nan)
            ax.plot(x, yv, marker="o", label=f"assumed {q:.2f}")
        ax.plot([0, 1], [0, 1], color="grey", lw=.8)
        ax.set_title(f"{gl[g]}: calibration (audit-like)")
        ax.set_xlabel("member posterior (fifths)")
    axes[0].set_ylabel("share truly members")
    axes[0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "2-calibration.png"), dpi=130)
    plt.close(fig)

    # 3. each target's M2 gain by world, audit-like 0.55
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    for ax, g in zip(axes, GROUPINGS):
        ts = GROUPINGS[g]["targets"]
        for k, (world, col) in enumerate((("cross", "C0"), ("bonds", "C1"),
                                          ("indep", "C7"))):
            ds = cells.get((world, "audit", .55, "split"), [])
            for i, t in enumerate(ts):
                e = [_gain(d["rec"][g]["targets"][t]) for d in ds
                     if d["rec"][g]["targets"][t].get("computable")]
                if e:
                    interval(ax, i + (k - 1) * .25, e, col,
                             world if i == 0 else None)
        ax.plot(range(len(ts)), [tv["D"][g][t] for t in ts], "k_", ms=14,
                label="true D (world 1)")
        ax.axhline(0, color="grey", lw=.8)
        ax.set_xticks(range(len(ts)))
        ax.set_xticklabels(ts)
        ax.set_title(f"{gl[g]}: loss(M0) - loss(M2), audit-like, assumed 0.55",
                     fontsize=9)
    axes[0].set_ylabel("nats (median, 5-95%)")
    axes[0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "3-target-gains-by-world.png"), dpi=130)
    plt.close(fig)

    # 4. cluster vs bonds vs independence, audit-like 0.55
    fig, axes = plt.subplots(2, 3, figsize=(13, 7))
    stats = [("ppc_p", "residual-dependence PPC p-value"),
             ("suff_gap", "family sufficiency gap"),
             ("M2", "family record gain M0-M2")]
    for row, g in enumerate(GROUPINGS):
        for colk, (key, lab) in enumerate(stats):
            ax = axes[row, colk]
            for world, col in (("cross", "C0"), ("bonds", "C1"),
                               ("indep", "C7")):
                ds = cells.get((world, "audit", .55, "split"), [])
                if key == "ppc_p":
                    v = [d["rec"][g]["ppc_p"] for d in ds]
                else:
                    v = [d["rec"][g]["family"][key] for d in ds
                         if d["rec"][g]["family"]]
                if v:
                    ax.hist(v, bins=20, alpha=.45, color=col, label=world)
            ax.set_title(f"{gl[g]}: {lab}", fontsize=9)
    axes[0, 0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "4-cluster-vs-bonds.png"), dpi=130)
    plt.close(fig)

    # 5. design analysis: estimate against D, world 1, every regime
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    for ax, g in zip(axes, GROUPINGS):
        ts = GROUPINGS[g]["targets"]
        for k, (lv, q) in enumerate(regimes):
            ds = cells.get(("cross", lv, q, "split"), [])
            for i, t in enumerate(ts):
                e = [_gain(d["rec"][g]["targets"][t]) for d in ds
                     if d["rec"][g]["targets"][t].get("computable")]
                if e:
                    interval(ax, i + (k - 2.5) * .12, e, f"C{k}",
                             rlab[k] if i == 0 else None, ".", 6)
        ax.plot(range(len(ts)), [tv["D"][g][t] for t in ts], "k_", ms=16,
                label="true D")
        ax.axhline(0, color="grey", lw=.8)
        ax.set_xticks(range(len(ts)))
        ax.set_xticklabels(ts)
        ax.set_title(f"{gl[g]}: estimated gain vs true D (world 1)")
    axes[0].set_ylabel("nats (median, 5-95%)")
    axes[0].legend(fontsize=7, ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "5-design-analysis.png"), dpi=130)
    plt.close(fig)

    # 6. INTJ - EXPRESSIVE on shared targets, world 1
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for k, (lv, q) in enumerate(regimes):
        ds = cells.get(("cross", lv, q, "split"), [])
        for i, t in enumerate(SHARED):
            e = [_gain(d["rec"]["intj"]["targets"][t])
                 - _gain(d["rec"]["expr_shared"][t]) for d in ds
                 if d["rec"]["intj"]["targets"][t].get("computable")
                 and d["rec"]["expr_shared"][t].get("computable")]
            if e:
                interval(ax, i + (k - 2.5) * .12, e, f"C{k}",
                         rlab[k] if i == 0 else None, ".", 6)
    ax.plot(range(len(SHARED)), [tv["D_shared"][t]["intj"]
                                 - tv["D_shared"][t]["expr"] for t in SHARED],
            "k_", ms=16, label="true difference")
    ax.axhline(0, color="grey", lw=.8)
    ax.set_xticks(range(len(SHARED)))
    ax.set_xticklabels(SHARED)
    ax.set_title("INTJ - EXPRESSIVE gain on shared targets (world 1)")
    ax.set_ylabel("nats (median, 5-95%)")
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "6-cross-inquiry.png"), dpi=130)
    plt.close(fig)

    # 7. M2 against the comparators, every regime, worlds 1 to 3
    fig, axes = plt.subplots(2, 2, figsize=(12, 7), sharey="row")
    for row, g in enumerate(GROUPINGS):
        for colk, (comp, lab) in enumerate((("anchor_best",
                                             "anchor diagnostic"),
                                            ("conv", "convergence score"))):
            ax = axes[row, colk]
            for k, (world, col) in enumerate((("cross", "C0"),
                                              ("bonds", "C1"),
                                              ("indep", "C7"))):
                for i, (lv, q) in enumerate(regimes):
                    ds = cells.get((world, lv, q, "split"), [])
                    e = [d["rec"][g]["family"]["M2"]
                         - d["rec"][g]["family"][comp] for d in ds
                         if d["rec"][g]["family"]]
                    if e:
                        interval(ax, i + (k - 1) * .25, e, col,
                                 world if i == 0 else None, "o", 4)
            ax.axhline(0, color="grey", lw=.8)
            ax.set_xticks(range(len(regimes)))
            ax.set_xticklabels(rlab, rotation=45, fontsize=8)
            ax.set_title(f"{gl[g]}: M2 minus {lab} (family gain)", fontsize=9)
    axes[0, 0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "7-m2-vs-comparators.png"), dpi=130)
    plt.close(fig)


# -------------------------------------------------------------------- run

def tasks(sims, sims_reported, cal, boot, seed=20261105):
    spec = []
    for level in LEVELS:
        for q in ASSUMED:
            for world in ("cross", "bonds", "indep"):
                spec.append((world, level, q, "split", sims))
    for world in ("cross", "bonds", "indep"):
        spec.append((world, "audit", .55, "cap", sims_reported))
    spec.append(("gom", "audit", .55, "split", sims_reported))
    ss = np.random.SeedSequence(seed)
    out = []
    for (world, level, q, scheme, k) in spec:
        for child in ss.spawn(k):
            out.append((world, level, q, scheme,
                        int(child.generate_state(1)[0]), cal, boot))
    return out


def run(sims, sims_reported, boot=50, procs=10):
    cal = calibrate()
    if not cal["matched"]:
        raise RuntimeError(f"bonds calibration not matched: {cal}")
    tl = tasks(sims, sims_reported, cal, boot)
    with Pool(procs) as pool:
        recs = pool.map(one_dataset, tl, chunksize=2)
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
    assert np.allclose(unit_weights(Vt, Ut, "split"), [[.5, .5, 1, 0]])
    assert np.allclose(unit_weights(Vt, Ut, "cap"), [[.5, .5, 1, 0]])
    # 3. Rows with nothing visible get the class prior.
    best = fit_lca(Y[:5], np.zeros((5, m)), rng)[0]
    assert np.allclose(best[1], np.tile(best[3], (5, 1)), atol=1e-6)
    # 4. Same-inclusion concealment hits reference rows too.
    X, _ = world_cross(rng)
    doc = document(X, rng, "audit", .55)
    st = projection_state(doc, "intj", "P06")
    tu = doc["unit"][st["rows"], C["P06"]]
    shared = st["K"] & (st["U"] >= 0) & (st["U"] == tu[:, None])
    assert shared.sum() >= 2 and not (st["V"] & shared).any()
    # 5. Entailed concealment: no P11N state reaches EXPRESSIVE's
    #    projections onto P01 to P03, and it does reach the others.
    k = GROUPINGS["expr"]["diag"].index("P11N")
    for t in ("P01", "P02", "P03"):
        st = projection_state(doc, "expr", t)
        assert not st["V"][:, k].any() and not st["inap"][:, k].any()
    st = projection_state(doc, "expr", "P12")
    assert st["inap"][:, k].any()
    # 6. INAPPLICABLE P11N rows are never known.
    assert not doc["known"][~doc["applic"], C["P11N"]].any()
    # 7. One-valued references give the smoothed reference rate.
    yy = np.array([1, 0, 0, 0])
    assert abs(lr_prob(np.zeros((4, 1)), np.array([1, 2, 3]), 0, yy)
               - 1 / 5) < 1e-12
    # 8. Mutual information: independent is 0, identical is H(p).
    cls = rng.random(20000) < .5
    assert _mi(cls.astype(int), (rng.random(20000) < .3).astype(int)) < 1e-3
    assert abs(_mi(cls.astype(int), cls.astype(int)) - np.log(2)) < 1e-3
    return "self-tests passed"


def leak_test(seed=5):
    """The scored cell's own value must not enter its prediction. With the
    value flipped and the same random stream, every predictor gives that
    cell the same probability, so p(y) + p(1 - y) = 1."""
    rng = np.random.default_rng(seed)
    X, _ = world_cross(rng)
    doc = document(X, rng, "audit", .70)
    for g, t in (("intj", "P06"), ("expr", "P12"), ("expr", "P01")):
        rows = np.where(UNIVERSE[g])[0]
        cap_a = {}
        run_projection(doc, g, t, "split", np.random.default_rng(9),
                       boot=0, capture=cap_a)
        for s in list(cap_a)[:4]:
            d2 = {k: (v.copy() if isinstance(v, np.ndarray) else v)
                  for k, v in doc.items()}
            d2["Xc"][rows[s], C[t]] = 1 - d2["Xc"][rows[s], C[t]]
            cap_b = {}
            run_projection(d2, g, t, "split", np.random.default_rng(9),
                           boot=0, capture=cap_b)
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
        print(self_tests())
        print(leak_test())
        cal = calibrate(reps=60)
        print("calibration (reps=60): matched =", cal["matched"],
              "s_i =", cal["s_i"], "s_e =", cal["s_e"],
              "max error =", round(cal["max_error"], 3))
    elif mode == "smoke":
        t0 = time.time()
        cal, cells = run(sims=1, sims_reported=1)
        n = sum(len(v) for v in cells.values())
        tv = true_values(reps=200)
        summarize(cells, tv)
        print(f"smoke: {n} datasets, calibration matched, summaries built; "
              f"{time.time() - t0:.0f} s total")
    elif mode == "full":
        sims = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        sims_rep = int(sys.argv[3]) if len(sys.argv) > 3 else 100
        t0 = time.time()
        cal, cells = run(sims, sims_rep)
        tv = true_values()
        result = {"meta": {
            "plan_sha256": file_sha(os.path.join(HERE, "RULE.md")),
            "harness_sha256": file_sha(os.path.abspath(__file__)),
            "items_sha256": file_sha(ITEMS),
            "sims": sims, "sims_reported": sims_rep,
            "calibration": cal, "true_values": tv,
            "python": sys.executable, "runtime_s": None},
            "summary": summarize(cells, tv)}
        result["meta"]["runtime_s"] = round(time.time() - t0, 1)
        with open(os.path.join(HERE, "results-round7.json"), "w") as fh:
            json.dump(result, fh, indent=1)
        raw = {"|".join(map(str, k)): v for k, v in cells.items()}
        with gzip.open(os.path.join(HERE, "results-round7-raw.json.gz"),
                       "wt") as fh:
            json.dump(raw, fh)
        figures(cells, tv, os.path.join(HERE, "figures"))
        print("written results-round7.json, raw records and figures; "
              "runtime", result["meta"]["runtime_s"], "s")
