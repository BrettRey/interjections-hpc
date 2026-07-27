# Review Board #2 Synthesis
<!-- SUMMARY: six-reviewer Codex board on main.tex, 5 R&R + 1 Reject; headline problem is undemonstrated incremental predictive payoff · status: synthesized, revisions pending · updated: 2026-07-27 -->

Run `review-board-20260727-123033`. Six reviewers, all Codex, model `gpt-5.6-sol`,
xhigh. Personas: projectibility, cgel, methods, worldenglishes, philosopher,
hostile.

**Verdicts:** 5 Revise & Resubmit, 1 Reject (hostile).

## Board self-check first

All six ran on one model. Convergence here is much weaker evidence than in the
earlier split-model board: where four reviewers ask the same key question in
nearly the same words, the likeliest explanation is a shared prior in the model,
not a fact about how *Journal of Linguistics* referees would react. Everything
below that I recommend acting on, I recommend because it is checkable against
the text, and I have checked the specific line references. Treat the counts
("four reviewers flagged") as a heat map of where the manuscript invites the
objection, not as a vote.

The verdict spread is also not a disagreement. The hostile reviewer rejects on
exactly the ground the other five raise as their principal revision. Read the
Reject as a severity reading of one shared problem.

## Consensus strengths

- **The failed *fie* prediction, reported as a failure** (5 of 6). Pr(predicted
  ordering) = 0.13, declared unobserved, not rescued by post-hoc narrowing
  (l.1828–1858, l.2947). Every reviewer who mentioned it treated it as the
  paper's best evidence of good faith.
- **The §1 apparatus** (4 of 6): declaration / warrant / profile / stability /
  network order / grounds, plus the refusal to infer homeostasis from stability
  (l.218–245). The philosopher calls the non-homeostatic positioning "coherent
  and unusually disciplined" and correctly identifies it as Khalidi-style.
- **The §6.1 measurement disclosures** (3 of 6). Methods calls the transparency
  "exemplary" and singles out the precision/recall distinction at l.2619.
- **Pathway residue as the strongest empirical contribution** (cgel, hostile).
  Notable that the hostile reviewer grants this one.

## Consensus weaknesses

### 1. No demonstrated incremental predictive payoff (4 of 6; the key question in 4 of 6)

Stated four ways, same target:

- projectibility: "What independently measured outcome does assigning a held-out
  form to *interjection* predict better than the exact cues used to assign it?"
- philosopher: an intersection of three projectible nodes is not automatically
  itself projectible; show the payoff belonging to the intersection over its
  components.
- hostile: the paper concedes at l.2072–2078 that the syntactic predictions are
  available to any framework recognising the morphosyntactic properties, and at
  l.2098–2114 calls the label "the analyst's bookkeeping device." That largely
  concedes the point.
- methods: what exactly is held out, a token for a known item×country, a new
  item, or a new variety?

The paper's own two concessions are what all four are pointing at. Two of them
quote them back.

### 2. The three field-relative nodes (3 of 6, three different objections)

- **cgel:** `interjection_sem` is an expressive meaning type and
  `interjection_prag` an interactional function. Neither is a lexical category;
  relabelling them *interjection* does not establish independent nodes
  (l.1155–1177). The intersection at l.1218–1222 then builds the desired
  extension into the notation.
- **philosopher:** the intersection may not itself be a causal or projectible
  node (l.335, l.1218, l.1983). Either demonstrate its incremental payoff or
  revise the thesis toward three overlapping field-relative categories.
- **hostile:** the nodes function as an unfalsifiability device. Failures get
  relocated between nodes; *fie* becomes a boundary condition; loss of prosodic
  isolation becomes reclassification (l.2286–2296).

### 3. The GloWbE prose outruns model m1 (3 of 6)

m1 adds a common country random intercept. It tests whether overall token rates
differ by corpus section, not whether item types or category boundaries behave
differently by country. The varying-slope model that would test that (m3) is
exploratory and can't be ranked (l.2694, l.2710). Observation-level LOO also
predicts a missing cell for an already-observed item and country, so it isn't a
test of generalisation to a new item or variety.

Flagged sentences, verified in the text 2026-07-27:

- l.2366 "Conditioning on country recovers structure at every level of this
  sample."
- l.2370–2374 "the conditioned model outperforms" (ΔELPD 17.9, SE 13.3: the SE
  is three quarters of the estimate).
- Figure caption `fig:fie-tau`: "The three distributions overlap almost
  completely, indicating simultaneous decline." These are marginal posteriors;
  overlapping marginals don't establish simultaneity.

### 4. Circularity in §5 (2 of 6)

- *bruh* (l.2050–2068) begins from observed "standalone position, prosodic
  isolation, morphological bareness, and stance meaning" and then predicts
  expressive meaning; l.2098–2105 derives "the stance reading" from a package
  already containing stance meaning.
- `interjection_prag` is defined partly through backchannel use (l.1168–1176),
  while §5 presents backchannel availability as a projection (l.2148–2154).
- philosopher's version: most examples complete one item's profile from other
  properties of the same item, which is not the two-stage Goodmanian induction
  (observations across cases warrant a lawlike conditional, which then supports
  prediction about a new incompletely observed case). Either state the two-stage
  form or call it cross-property prediction.

### 5. The regional trio flattened (worldenglishes, solo but source-grounded)

*Lah* is a host-dependent clause-final particle, *haba* a free-standing borrowed
emotive interjection, *yaar* partly an address term or vocative-derived
discourse particle. §4 says they aren't the same kind of case (l.1591) and
assigns *lah* to sem and prag but not syn, then l.2334–2339 calls all three
"regional interjections" with near-categorical distributions and the appendix
models them as one item type (l.2604). "Substrate-derived" (l.2446) collapses
three different contact histories.

This reviewer read Unuabonah & Daniel (2020) in full and reports that their
analysis manually excludes Nigerian Pidgin, indigenous-language, duplicate,
nominal and metalinguistic tokens, retaining 248 where our raw-string rate of
8.78 pmw rests on 373. Lange (2009) is in the bibliography, uncited, and unread:
a live NOSOURCE for the *yaar* characterisation.

## Contradictions worth preserving

1. **What to do with the nodes.** cgel wants *interjection* reserved for the
   independently established morphosyntactic category, with the other two
   renamed (expressive meaning, interactional function) and then tested as
   things membership predicts. The philosopher offers the opposite retreat:
   pluralise into three overlapping field-relative categories. One collapses to
   a single category with two dependent dimensions; the other abandons the
   single category. Both can't be the fix, and the choice changes the thesis.
2. **Where the syntax stands.** cgel says `interjection_syn` is under-established
   and needs distributional paradigms separating Intj heads from N, V, Adj, Adv.
   projectibility and hostile say the syntactic predictions are the part that
   earns the framework least, because any framework recognising the properties
   gets them. More syntactic work, or syntax isn't where the problem is.
3. **Boundary sharpness.** The philosopher wants the sharp-but-non-locatable
   edge dropped or quarantined, noting the paper itself concedes nothing in the
   argument requires it (l.776, l.788). The hostile reviewer wants a *sharper*
   falsification threshold. Different axes; easy to conflate into "be more
   precise about boundaries," which would satisfy neither.

## Prioritised revision list

1. **Decide what the incremental-payoff claim is, then run it or retreat to it.**
   The non-circular targets (recipient uptake, sequential position, semantic
   repeatability) need annotated spoken interaction. GloWbE is web text, and
   English-Corpora is Turnstile-blocked, so this is a data-acquisition decision
   before it's a writing decision. Options: (a) a held-out study with fixed
   source cues, held-out targets, tolerance, and a cue-only baseline; (b) declare
   the test prospectively with defeat conditions and say plainly it isn't run.
   Option (b) is what the hostile reviewer rejects on, so choosing it means
   accepting that cost knowingly.
2. **Circularity audit of §5.** Freeze the admission features, exclude every
   target from them. Sites: l.2050–2068, l.2098–2105, l.1168–1176 vs
   l.2148–2154. Cheap and self-contained.
3. **Downgrade the three overreaching sentences** at l.2366, l.2370–2374, and
   the `fig:fie-tau` caption. Also reword the morphology-gain result: the sample
   selects overt derivatives and the success criterion includes
   `verbal_syntax = 1`, so syntactic integration is partly built into the
   sampling frame (l.2774, l.2823). Report the conditional result.
4. **The node fork** (contradiction 1). Brett's call; it changes the thesis.
5. **Regional trio.** Item-by-item diagnostic table (matrix language, lexical
   source, construction, prosodic status, syntactic integration, meaning,
   interactional function); item-specific contact histories in place of
   "substrate-derived"; reconcile *haba*'s 373 raw against Unuabonah & Daniel's
   cleaned 248; read Lange (2009) before the *yaar* claim stands. Sources are
   all local already.

### Smaller concrete items

- Table 1 gives *damn these …!* parenthesised checks on the syn-relevant
  columns; §5.2 (l.2167–2178) says `interjection_syn` "holds (it heads an IntjP)
  but with limited complement-taking." Reconcile the two, or say why partial in
  the table and holding in the prose are the same verdict.
- §4.3 (l.1390–1406) derives *damn him* from *God damn him* by subject loss and
  says "Tense goes with the subject." The source construction already has a
  subject with plain-form *damn*, so subject loss can't explain the verb form.
  Separate source-clause syntax, verb form, optative force, and the synchronic
  IntjP analysis. The CGEL attribution needs checking against the text; p.944
  supports optative as a minor clause type, not this derivation.
- The same over-attribution recurs at l.1421–1439: properties supplied by an
  imperative source (no overt subject, plain form) are counted as later
  deactivation in *come on* and *look*.
- Methods asks for audit sample sizes, sampling protocol, and coding reliability
  to be reported for the `ha` audit. We have all of these in
  `analysis/hand-extracted/`; they just aren't in the manuscript.
