# Review board synthesis: where do the field-relative node definitions belong?
<!-- SUMMARY: 4-reviewer non-redundant board (2 Opus, 2 Codex) on the §3.4/§5.2 node duplication and the 14 pre-definition uses; unanimous that definitions arrive too late but only criteria should move, and that the duplication is the graver defect · status: reported to Brett, not acted on · updated: 2026-07-26 -->

Run: `reviews/review-board-20260726-175333`. Four reviewers, personas split
across models with no overlap (non-redundant, at Brett's instruction).

| Model | Reviewer | File |
|---|---|---|
| Opus | Projectibility (mandatory for HPC papers) | task output |
| Opus | Formal linguist, CGEL tradition | task output |
| Codex | Structural editor / methodologist | `codex-structural.md` |
| Codex | Hostile reviewer | `codex-hostile.md` |

## Unanimous

1. **Brett's instinct is right in outcome: the definitions arrive too late.** All
   four say so independently.
2. **But only assignment criteria should move, not the definitions.** No reviewer
   endorsed moving §3.4's itemize. What the early site needs is a coding rule
   (the condition under which a form gets a given node), theory-light: no causal
   links, no field attributions, no projections, no Khalidi or Boyd.
3. **The duplication is the graver defect.** §3.4 and §5.2 overlap enough that
   §5.2 stops looking like a payoff. Counted against §3.4, §5.2 introduces 2 new
   items of 4 for `syn`, 1 of 4 for `int`, and **0 of 4 for `sem`** (same four
   properties, same Potts 2007: 166, differently inflected).
4. **`syn` already does it right; make `sem` and `int` look like `syn`.** §3.4
   gives `syn` defining properties and §5.2 gives it *tests* (resistance to
   *that*-complementation, to coordination). For `sem` and `int` the two sites
   give the same list twice.
5. **The circularity is self-indicted.** §1 sets the rule at l.212--214 ("The
   predicted outcome has to be something other than the property that admitted
   the form, or the prediction only restates membership"), and §5.1 restates the
   alarm at l.1807. §5.2's `sem` entry then projects the four properties that
   define it, ~90 lines later.
6. **§3.4's three "Projects X" clauses should be deleted.** They spend the payoff
   before §5.2 earns it.
7. **The subscript notation itself is fine.** No reviewer objected to it as
   notation; the hostile reviewer explicitly declined to make it grounds for
   rejection.

## The split: where does the early material go?

Perfectly model-correlated, which is a caution, not a result.

- **§2.6, immediately before Table 1** (both Opus reviewers). Rationale: that is
  where the criteria are *used*, so that is where they cost least; and moving
  full definitions early would *multiply* forward references, since §3.4's
  entries are partly defined by causal links that don't exist for the reader
  until §4.4 and Table 2.
- **§1, at first introduction (l.268--275)** (both Codex reviewers). Rationale:
  the paper already incurred the cost by using the nodes in §1, so make the
  commitment inspectable at first mention and defer only its causal
  justification.

Because the board was non-redundant, model is confounded with persona here: the
two who said §2.6 are also the two whose charges were reader-path and
projectibility-payoff. Do not read the 2--2 as a field split.

## Also split: which defect would a referee actually raise?

- **Forward dependency** (CGEL, structural): checkable, about the paper's central
  exhibit, and the paper invited it at l.296. Review sentence writes itself: "I
  could not evaluate the last three columns of Table 1 where they appear."
- **Duplication** (projectibility, hostile): goes at the central claim rather
  than the presentation, so it is the one that costs the argument.

All four nonetheless rank duplication as the more *severe* problem. CGEL:
"the placement problem costs a revision, the circularity costs the argument."

## Verified independently (main-agent checks, not reviewer claims)

1. **l.296 states something false.** "The three nodes regroup those five by what
   each field needs the category to predict, so the subscripts stay out of the
   way until Section 3.4 defines them." They do not stay out of the way: l.513,
   then ten times at l.662--774. Flagged by two reviewers; verified.
2. **`Intj_sem` reproduces the Emotive/stance column in all ten rows** of Table 1
   (full → ✓, partial → –, absent → –). Sharper than any reviewer put it: the
   column is not opaque, it is redundant, which is what makes it look
   terminological.
3. **`Intj_syn` is non-monotone in the property columns.** `mm-hm` and `huh?`
   score ✓ on both prosodic isolation and syntactic non-integration but get only
   partial `Intj_syn`, while `bye` and `bruh` with equal or weaker property rows
   get full ✓. The tie-breaker for `mm-hm` (O'Connell & Kowal) appears only at
   l.1918, about 1,100 lines later.
4. **Table 1's `the damn car` row contradicts both §2.4 and §2.6.** The row marks
   Non-inflecting and Non-referential as absent. But §2.4 (l.448--450) defines
   non-referentiality as "absence of ordinary entity/event denotation and
   argumental construal while allowing semantic content," which prenominal
   *damn* satisfies; and it doesn't inflect (\**the damns car*). §2.6's prose two
   paragraphs above (l.727--731) says prenominal *damn* "retains emotive force
   but loses prosodic-syntactic independence", i.e. loses two properties. The
   table strips four of five. The table overstates the erosion its own prose
   describes.

## Other findings worth keeping

- **§5.4 states the projections a third time** (l.2007--2011), where its actual
  job is the asymmetry claim (which node is richest). It re-establishes instead
  of comparing.
- **Figure 2 is a fourth site** (l.1547--1549), labelling nodes with projection
  targets. Leave it: a diagram must be legible standalone.
- **Extension differences are duplicated too**: `mm-hm` at l.1091--1093 and again
  l.1917--1918; *the damn car* at l.1082--1084 and again l.1933--1936.
- **§3.4's heading pre-spends §5's title.** It is "Field-relative
  projectibility"; §5 is "Projectibility: what the category lets you predict."
  Retitle §3.4 to name the nodes.
- **The Libert convergence is banked 360 lines early** (l.659--669), the paper's
  best independent evidence for a three-way cut, spent before the cut is
  proposed. Cross-reference it forward from §3.4.
- **CGEL-specific objection** (worth weighing, not obviously right): the three
  nodes are not three of a kind. `syn` is a lexical category, `sem` a meaning
  type, `int` a use category. Subscripting one word across all three implies
  three parallel categorizations of one kind.

## Source-grounding flags

Every reviewer flagged that it had not read Potts (2007). The proposed
split-the-list surgery on `sem` depends on which of Potts's four properties are
cheap observables and which are held-out consequences. **Read Potts 2007: 166
before doing that surgery.** Same caution for Libert (2012) and O'Connell &
Kowal (2005): claims above are about how `main.tex` reports them.

## Board self-check

Convergence on points 1--7 was high and arrived by different routes (reader-path,
payoff structure, referee behaviour), which is mild evidence it is not an
artifact. But the placement split falls exactly on model lines, and all four
reviewers accepted the framing of the brief, which named options A--D. A board
given a blanker prompt might have questioned the three-node apparatus itself
rather than where to define it. Treat this as a stress test of likely referee
reactions, not a sample of expert opinion.
