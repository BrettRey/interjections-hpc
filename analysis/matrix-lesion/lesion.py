"""Core lesion machinery for the property-matrix study.

Binary simplification for simulation: P10 coded 1 = STRENGTHENS,
P14 coded 1 = has a conventional sequential action. The real matrix
keeps the categorical columns; this core is what the fake-data check
exercises, and the categorical handling is added before any real run.

Conventions:
  X      : (n_items, 14) int array of 0/1 coded values
  KNOWN  : (n_items, 14) bool array, True where the coded value is known
  MASK   : (n_items, 14) bool array, True for cells hidden in a lesion run
  A cell is visible iff KNOWN and not MASK. Scored cells are KNOWN and MASK.
Assignment outcomes: 1 = MEMBER, 0 = NONMEMBER, 2 = UNRESOLVED.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression

PROPS = ["P01", "P02", "P03", "P04", "P05", "P06", "P07",
         "P08", "P09", "P10", "P11", "P12", "P13", "P14"]
IDX = {p: i for i, p in enumerate(PROPS)}
TARGET_ONLY = [IDX[p] for p in ("P10", "P11", "P12", "P13")]
EPS = 1e-7


def visible(known, mask):
    return known & ~mask


def assign_intj(X, vis):
    """R-INTJ-1 v2 (sparsity-aware, revised after fake-data round 1).

    v1 required an absolute score >= 3, unreachable when only one or
    two eligible cells are visible. v2 normalizes by the number of
    visible eligible cells and requires at least 2 of them.
    """
    pos = {"P01": 1, "P02": 1, "P03": 0, "P04": 0, "P05": 0, "P07": 1}
    score = np.zeros(X.shape[0], dtype=int)
    nvis = np.zeros(X.shape[0], dtype=int)
    for name, want in pos.items():
        j = IDX[name]
        hit = vis[:, j] & (X[:, j] == want)
        miss = vis[:, j] & (X[:, j] != want)
        score += hit.astype(int) - miss.astype(int)
        nvis += vis[:, j].astype(int)
    gate = (vis[:, IDX["P01"]] & (X[:, IDX["P01"]] == 1)) | \
           (vis[:, IDX["P02"]] & (X[:, IDX["P02"]] == 1))
    frac = np.where(nvis > 0, score / np.maximum(nvis, 1), 0.0)
    out = np.full(X.shape[0], 2, dtype=int)
    out[gate & (nvis >= 2) & (score >= 2) & (frac >= 0.5)] = 1
    out[(nvis >= 2) & (frac <= 0.0)] = 0
    return out


def assign_expr(X, vis):
    """R-EXPR-1 v2. v1 required both P08 and P07 visible (83%
    unresolved under lesion in round 1). v2: MEMBER if P08=Y visible
    and P07 is not a visible N."""
    p08v, p07v = vis[:, IDX["P08"]], vis[:, IDX["P07"]]
    p08, p07 = X[:, IDX["P08"]], X[:, IDX["P07"]]
    out = np.full(X.shape[0], 2, dtype=int)
    out[p08v & (p08 == 1) & ~(p07v & (p07 == 0))] = 1
    out[p08v & (p08 == 0)] = 0
    return out


def _assign_single(col):
    def f(X, vis):
        j = IDX[col]
        out = np.full(X.shape[0], 2, dtype=int)
        out[vis[:, j] & (X[:, j] == 1)] = 1
        out[vis[:, j] & (X[:, j] == 0)] = 0
        return out
    return f


assign_suppl = _assign_single("P02")   # supplement-capable grouping
assign_depict = _assign_single("P09")  # depictive grouping

ASSIGNERS = {"intj": assign_intj, "expr": assign_expr,
             "suppl": assign_suppl, "depict": assign_depict}


def _rate(vals):
    return (vals.sum() + 1.0) / (len(vals) + 2.0)


def _features(X, vis, ref_rows, target_col):
    """Visible property values with reference-mean imputation."""
    cols = [j for j in range(X.shape[1]) if j != target_col]
    F = np.full((X.shape[0], len(cols)), 0.5)
    for k, j in enumerate(cols):
        ref_vis = ref_rows & vis[:, j]
        mu = X[ref_vis, j].mean() if ref_vis.sum() >= 3 else 0.5
        F[:, k] = np.where(vis[:, j], X[:, j].astype(float), mu)
    return F


def predict_column(X, known, mask, j, assign):
    """Predict masked cells in column j under M0, M1, M2, M3.

    Returns dict of predicted probabilities aligned with the scored
    (row,) indices, or None when the column has no scored or no
    reference cells. `assign` is the precomputed assignment vector
    (from visible cells only) used by M2 and M3.
    """
    vis = visible(known, mask)
    scored = np.where(known[:, j] & mask[:, j])[0]
    ref = np.where(known[:, j] & ~mask[:, j])[0]
    if len(scored) == 0 or len(ref) == 0:
        return None
    p0 = _rate(X[ref, j])
    out = {"rows": scored, "y": X[scored, j].astype(float),
           "M0": np.full(len(scored), p0)}

    # M2 category-mediated
    p2 = np.full(len(scored), p0)
    for k, r in enumerate(scored):
        a = assign[r]
        if a != 2:
            same = ref[assign[ref] == a]
            if len(same) >= 3:
                p2[k] = _rate(X[same, j])
    out["M2"] = p2

    # M1 / M3 logistic on visible properties
    ref_mask = np.zeros(X.shape[0], dtype=bool)
    ref_mask[ref] = True
    F = _features(X, vis, ref_mask, j)
    yref = X[ref, j]
    if len(ref) >= 10 and 0 < yref.sum() < len(yref):
        for tag, extra in (("M1", None), ("M3", assign)):
            if extra is None:
                Ftr, Fte = F[ref], F[scored]
            else:
                oh = np.zeros((X.shape[0], 2))
                oh[extra == 1, 0] = 1.0
                oh[extra == 0, 1] = 1.0
                Fall = np.hstack([F, oh])
                Ftr, Fte = Fall[ref], Fall[scored]
            m = LogisticRegression(C=1.0, max_iter=300)
            m.fit(Ftr, yref)
            out[tag] = m.predict_proba(Fte)[:, 1]
    else:
        out["M1"] = out["M0"].copy()
        out["M3"] = out["M0"].copy()
    return out


def logloss(y, p):
    p = np.clip(p, EPS, 1 - EPS)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def lesion_run(X, known, mask, assignment="intj", cols=None):
    """One lesion run. Returns per-predictor mean log loss overall
    and restricted to TARGET_ONLY columns, plus the unresolved rate."""
    vis = visible(known, mask)
    assign = assign_intj(X, vis) if assignment == "intj" else assign_expr(X, vis)
    cols = range(X.shape[1]) if cols is None else cols
    acc = {k: [] for k in ("M0", "M1", "M2", "M3")}
    acc_t = {k: [] for k in acc}
    for j in cols:
        res = predict_column(X, known, mask, j, assign)
        if res is None:
            continue
        for k in acc:
            ll = logloss(res["y"], res[k]) * len(res["y"])
            acc[k].append((ll, len(res["y"])))
            if j in TARGET_ONLY:
                acc_t[k].append((ll, len(res["y"])))

    def pool(d):
        return {k: (sum(a for a, _ in v) / sum(n for _, n in v)
                    if v else float("nan")) for k, v in d.items()}

    return {"overall": pool(acc), "target": pool(acc_t),
            "unresolved_rate": float(np.mean(assign == 2))}


def random_mask(known, frac, rng):
    mask = np.zeros_like(known)
    cells = np.argwhere(known)
    take = rng.choice(len(cells), size=int(round(frac * len(cells))),
                      replace=False)
    mask[tuple(cells[take].T)] = True
    return mask


def leakage_test(seed=0):
    """Flipping masked cell values must not change any prediction."""
    rng = np.random.default_rng(seed)
    n, m = 20, 14
    X = (rng.random((n, m)) < 0.4).astype(int)
    known = rng.random((n, m)) < 0.8
    mask = random_mask(known, 0.5, rng)
    vis = visible(known, mask)
    a1 = assign_intj(X, vis)
    r1 = lesion_run(X, known, mask)
    X2 = X.copy()
    X2[mask] = 1 - X2[mask]  # corrupt every hidden value
    a2 = assign_intj(X2, vis)
    assert (a1 == a2).all(), "assignment used masked cells"
    # predictions must agree: compare predictor inputs indirectly via
    # predict_column on a target column
    for j in TARGET_ONLY:
        p1 = predict_column(X, known, mask, j, a1)
        p2 = predict_column(X2, known, mask, j, a1)
        if p1 is None:
            continue
        for k in ("M0", "M1", "M2", "M3"):
            assert np.allclose(p1[k], p2[k]), f"leakage in {k}, col {j}"
    return True


if __name__ == "__main__":
    print("leakage test:", "PASS" if leakage_test() else "FAIL")
