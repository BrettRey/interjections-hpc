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


ROTATION_SOURCES = {
    "intj": [IDX[p] for p in ("P01", "P02", "P03", "P04", "P05", "P07")],
    "expr": [IDX[p] for p in ("P08", "P07")],
    "suppl": [IDX["P02"]],
    "depict": [IDX["P09"]],
}


def _distribution(vals, classes, alpha=1.0):
    vals = np.asarray(vals)
    counts = np.array([(vals == c).sum() for c in classes], dtype=float)
    return (counts + alpha) / (len(vals) + alpha * len(classes))


def _features_matched(X, vis, ref_rows, source_cols):
    """Features restricted to the permitted source columns.

    Each source contributes an imputed value and a missing indicator.
    Reference and scored rows receive exactly the same feature layout,
    so M1 does not train on richer profiles than the information state
    permits at prediction.
    """
    F = np.zeros((X.shape[0], 2 * len(source_cols)))
    for k, j in enumerate(source_cols):
        ref_vis = ref_rows & vis[:, j]
        mu = X[ref_vis, j].mean() if ref_vis.sum() >= 3 else 0.5
        F[:, 2 * k] = np.where(vis[:, j], X[:, j].astype(float), mu)
        F[:, 2 * k + 1] = (~vis[:, j]).astype(float)
    return F


def predict_column_matched(X, known, mask, j, assign, source_cols,
                           classes=(0, 1), min_group_ref=3):
    """Categorical prediction with an information-matched M1.

    Returns probabilities as an (n_scored, n_classes) matrix for each
    predictor. This is the v2 path; `predict_column` remains only to
    preserve the earlier simulation history.
    """
    classes = np.array(classes)
    vis = visible(known, mask)
    scored = np.where(known[:, j] & mask[:, j])[0]
    ref = np.where(known[:, j] & ~mask[:, j])[0]
    if len(scored) == 0 or len(ref) == 0:
        return None
    y = X[scored, j].astype(int)
    p_base = _distribution(X[ref, j], classes)
    P0 = np.tile(p_base, (len(scored), 1))

    P2 = P0.copy()
    for k, r in enumerate(scored):
        a = assign[r]
        if a != 2:
            same = ref[assign[ref] == a]
            if len(same) >= min_group_ref:
                P2[k] = _distribution(X[same, j], classes)

    ref_mask = np.zeros(X.shape[0], dtype=bool)
    ref_mask[ref] = True
    F = _features_matched(X, vis, ref_mask, source_cols)
    yref = X[ref, j]
    P1, P3 = P0.copy(), P0.copy()
    if len(ref) >= 10 and len(np.unique(yref)) >= 2 and F.shape[1] > 0:
        for tag in ("M1", "M3"):
            if tag == "M1":
                Ftr, Fte = F[ref], F[scored]
            else:
                oh = np.zeros((X.shape[0], 2))
                oh[assign == 1, 0] = 1.0
                oh[assign == 0, 1] = 1.0
                Fall = np.hstack([F, oh])
                Ftr, Fte = Fall[ref], Fall[scored]
            model = LogisticRegression(C=1.0, max_iter=300)
            model.fit(Ftr, yref)
            probs = model.predict_proba(Fte)
            aligned = np.zeros((len(scored), len(classes)))
            for ci, cls in enumerate(model.classes_):
                aligned[:, list(classes).index(cls)] = probs[:, ci]
            if tag == "M1":
                P1 = aligned
            else:
                P3 = aligned
    return {"rows": scored, "y": y, "classes": classes,
            "M0": P0, "M1": P1, "M2": P2, "M3": P3}


def cat_logloss(y, P, classes=(0, 1)):
    idx = {c: i for i, c in enumerate(classes)}
    p = np.array([P[k, idx[v]] for k, v in enumerate(y)])
    return float(-np.mean(np.log(np.clip(p, EPS, 1 - EPS))))


def _cell_logloss(y_value, probs, classes):
    ci = list(classes).index(y_value)
    return float(-np.log(np.clip(probs[ci], EPS, 1 - EPS)))


def source_complete_records(X, known, rotation, target_cols,
                            membership_mode="infer",
                            retained_assign=None, eligible_rows=None,
                            concealed_source_cols=(), classes=(0, 1),
                            blocked_sources_by_cell=None,
                            direct_source_cols=None):
    """One-cell-at-a-time source-complete lesions for one rotation.

    membership_mode='infer' assigns the target row from its surviving
    permitted sources. 'retain' uses assignments computed before any
    lesion (or `retained_assign`) and therefore tests the stored
    summary rather than inferability from surviving evidence.

    `blocked_sources_by_cell` maps (row, target_col) to source columns
    whose only support for that row shares the target observation.
    Those sources are concealed for that run. `direct_source_cols`
    optionally gives M1 a wider, shared information bundle than the
    assignment rule uses, for cross-inquiry comparisons.
    """
    source_cols = [j for j in ROTATION_SOURCES[rotation]
                   if j not in target_cols]
    if set(source_cols) & set(target_cols):
        raise ValueError("source and target columns must be disjoint")
    assigner = ASSIGNERS[rotation]
    if retained_assign is None:
        retained_assign = assigner(X, known.copy())
    rows = (range(X.shape[0]) if eligible_rows is None
            else eligible_rows)
    records = []
    for r in rows:
        for j in target_cols:
            if not known[r, j]:
                continue
            mask = np.zeros_like(known)
            mask[r, known[r]] = True
            blocked = set((blocked_sources_by_cell or {}).get(
                (int(r), int(j)), ()))
            keep = [c for c in source_cols
                    if c not in concealed_source_cols
                    and c not in blocked]
            direct_keep = [c for c in (direct_source_cols or keep)
                           if c not in target_cols
                           and c not in concealed_source_cols
                           and c not in blocked]
            visible_cols = sorted(set(keep) | set(direct_keep))
            mask[r, [c for c in visible_cols if known[r, c]]] = False
            vis = visible(known, mask)
            assign = (assigner(X, vis) if membership_mode == "infer"
                      else retained_assign)
            res = predict_column_matched(
                X, known, mask, j, assign, direct_keep, classes=classes)
            if res is None:
                continue
            for k, row in enumerate(res["rows"]):
                if row != r:
                    continue
                rec = {"row": int(r), "target": int(j),
                       "target_name": PROPS[j], "y": int(res["y"][k]),
                       "assignment": int(assign[r]),
                       "resolved": bool(assign[r] != 2),
                       "blocked_source_cols": sorted(int(c)
                                                     for c in blocked),
                       "classes": [int(c) for c in res["classes"]]}
                for tag in ("M0", "M1", "M2", "M3"):
                    rec[tag] = [float(x) for x in res[tag][k]]
                records.append(rec)
    return records


def summarize_records(records):
    def mean_for(subset, tag):
        if not subset:
            return float("nan")
        return float(np.mean([
            _cell_logloss(r["y"], r[tag], r["classes"])
            for r in subset]))

    resolved = [r for r in records if r["resolved"]]
    out = {"n": len(records), "n_resolved": len(resolved),
           "assignment_coverage": (
               len(resolved) / len(records) if records else float("nan"))}
    for subset_name, subset in (("all", records),
                                ("resolved", resolved)):
        losses = {tag: mean_for(subset, tag)
                  for tag in ("M0", "M1", "M2", "M3")}
        out[subset_name] = {
            **losses,
            "gain_M2_vs_M0": losses["M0"] - losses["M2"],
            "gain_M1_vs_M0": losses["M0"] - losses["M1"],
            "compression_cost_M2_minus_M1": losses["M2"] - losses["M1"],
            "estimator_M3_vs_M1": losses["M1"] - losses["M3"],
        }
    return out


def bootstrap_records(records, row_groups, n_boot=1000, seed=0):
    """Cluster bootstrap over supplied row groups (form families or
    assertion clusters). Contrasts use all scored records."""
    rng = np.random.default_rng(seed)
    groups = sorted(set(row_groups))
    by_group = {g: [r for r in records if row_groups[r["row"]] == g]
                for g in groups}
    vals = {"gain_M2_vs_M0": [], "gain_M1_vs_M0": [],
            "compression_cost_M2_minus_M1": []}
    for _ in range(n_boot):
        sampled = []
        for g in rng.choice(groups, size=len(groups), replace=True):
            sampled.extend(by_group[g])
        s = summarize_records(sampled)["all"]
        for key in vals:
            vals[key].append(s[key])
    return {key: [float(np.quantile(v, 0.025)),
                  float(np.quantile(v, 0.975))]
            for key, v in vals.items()}


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


def v2_self_tests(seed=4):
    rng = np.random.default_rng(seed)
    n = 36
    X = np.zeros((n, 14), dtype=int)
    latent = np.repeat([0, 1], n // 2)
    rng.shuffle(latent)
    for j in ROTATION_SOURCES["intj"]:
        want = 1 if PROPS[j] in ("P01", "P02", "P07") else 0
        X[:, j] = np.where(latent == 1, want, 1 - want)
        flip = rng.random(n) < 0.12
        X[flip, j] = 1 - X[flip, j]
    # three-class target for categorical handling
    p = np.where(latent[:, None] == 1,
                 [0.65, 0.25, 0.10], [0.10, 0.30, 0.60])
    X[:, IDX["P10"]] = [rng.choice(3, p=row / row.sum()) for row in p]
    X[:, IDX["P12"]] = latent
    flip = rng.random(n) < 0.15
    X[flip, IDX["P12"]] = 1 - X[flip, IDX["P12"]]
    known = rng.random((n, 14)) < 0.85
    target = [IDX["P12"]]
    base = source_complete_records(X, known, "intj", target)
    assert base, "no source-complete records"
    assert all(abs(sum(r["M0"]) - 1) < 1e-9 for r in base)
    # Flipping every concealed target-row target must not alter
    # predictions for that same record in infer mode.
    X2 = X.copy()
    # Flip only the first record's row target and rebuild that row.
    r0 = base[0]["row"]
    X2[r0, IDX["P12"]] = 1 - X2[r0, IDX["P12"]]
    one = [r for r in source_complete_records(
        X2, known, "intj", target, eligible_rows=[r0])]
    orig = [r for r in base if r["row"] == r0][0]
    assert one and all(np.allclose(one[0][t], orig[t])
                       for t in ("M0", "M1", "M2", "M3")), \
        "concealed target leaked into infer-mode prediction"
    # Categorical path produces a 3-column distribution.
    cat = source_complete_records(X, known, "intj", [IDX["P10"]],
                                  classes=(0, 1, 2))
    assert cat and all(len(r["M2"]) == 3 for r in cat)
    assert summarize_records(cat)["n"] == len(cat)
    # Retaining membership keeps assignment when the gate sources are
    # concealed; inferring it from surviving evidence can differ.
    retained = assign_intj(X, known.copy())
    conceal = tuple(ROTATION_SOURCES["intj"][:2])
    a = source_complete_records(
        X, known, "intj", target, membership_mode="retain",
        retained_assign=retained, concealed_source_cols=conceal)
    assert all(r["assignment"] == retained[r["row"]] for r in a)
    # Proposition-level blocking: conceal gate sources only for one
    # row/target, leaving other runs untouched.
    member_rows = np.where((retained == 1)
                           & known[:, IDX["P12"]])[0]
    if len(member_rows):
        r = int(member_rows[0])
        gate = (IDX["P01"], IDX["P02"])
        blocked = {(r, IDX["P12"]): gate}
        rec = [x for x in source_complete_records(
            X, known, "intj", target, eligible_rows=[r],
            blocked_sources_by_cell=blocked)]
        if rec and known[r, IDX["P12"]]:
            assert rec[0]["assignment"] != 1
            assert rec[0]["blocked_source_cols"] == sorted(gate)
    return True


if __name__ == "__main__":
    print("leakage test:", "PASS" if leakage_test() else "FAIL")
    print("v2 self-tests:", "PASS" if v2_self_tests() else "FAIL")
