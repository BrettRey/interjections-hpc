# Figure plan — English Interjections
<!-- SUMMARY: menu of 11 figure candidates for Brett to trim; the structural finding is that §3 (theoretical core) and §5 (the payoff) carry no floats at all and every data plot is exiled to an appendix · status: awaiting trim, nothing built · updated: 2026-07-27 -->

## The structural problem

Float distribution across the body:

| Section | Floats |
|---|---|
| §1 Introduction | 0 |
| §2 The property cluster | 1 (Table 1, diagnostic matrix) |
| §3 The causal-network framework | **0** |
| §4 Causal structure | 3 (Tables 2–3, Figure 1) |
| §5 Projectibility — *the payoff* | **0** |
| §6 Discussion | **0** |
| §7 Conclusion | 0 |
| Appendices | 3 figures (every data plot) |

Two consequences. The reader carries §1's eight distinctions (declaration,
warrant, profile, stability, network order, grounds, stabilizers, corrective
control) through §2 and §3 with no picture, and the paper's only diagram
arrives at l.1533, about page 26 of 41. And the section that cashes the
argument, §5, has nothing visual at all, while all three data plots sit in
appendices where a reader who stops at the conclusion never sees them.

## The menu

| # | Figure | Kind | Makes clearer | Type | Source | Keep |
|---|--------|------|---------------|------|--------|------|
| 1 | The four objects | conceptual | that §1's eight distinctions are four questions, not eight things: what the declaration commits you to, what warrants it, what the profile is, what grounds it | layered dependency schematic, TikZ | conceptual | **must** |
| 2 | Observed → licensed → defeated | conceptual | what projectibility actually claims: these observations license these expectations, and this would defeat them | two-column flow with defeat annotations, TikZ | conceptual | **must** |
| 3 | The three nodes as overlapping extensions | conceptual | that the nodes decouple, and exactly where: standalone *damn!* in all three, prenominal *damn* in sem alone, *mm-hm* in prag with syn debated, *bye* in syn+prag not sem | Euler diagram with the cases placed | conceptual, coded from Table 1 | **must** |
| 4 | Four gateways, one profile | conceptual | that vocative, optative, imperative and onomatopoeic sources converge on one profile while leaving different residues | convergence diagram, TikZ | conceptual | nice |
| 5 | Category vs function | conceptual | what the interjection *category* adds over the supplement *function* — the point a CGEL readership will press hardest | nested sets, the four extra predictions attached to the category | conceptual | nice |
| 6 | Domain of projection | conceptual | that a category's predictions fall in the domain its links operate in (nouns→morphosyntax, interjections→interaction, animacy→grammar, colour→ecology) | mapping diagram | conceptual | stretch |
| 7 | *fie*: three diagnostics decline together | data | the paper's honest negative result, currently invisible to anyone who skips the appendix | existing step plot, **promote to §4.7 or §6** | `figures/fie-raw-proportions.pdf` (exists) | **must** (move, no build) |
| 8 | Two entry profiles: *oof* vs *bruh* | data | that recruitment histories differ sharply — *oof* attested 1777 and continuously rare, *bruh* absent until the 1980s then ~100× in COCA with zero spoken tokens | small multiples, shared per-million scale | `analysis/hand-extracted/oof-coha-by-decade.csv`, `bruh-coha-by-decade.csv`, `bruh-coca-by-{period,genre}.csv` (exist) | nice |
| 9 | Three-coder agreement on the *fie* diagnostics | data | that the negative result isn't a coding artifact | per-diagnostic agreement, small multiples | `analysis/fie-coding-sheet-annotated.csv` (3 coders + human adjudication) | stretch |
| 10 | GloWbE country variation | data | regional/indexical conditioning — **leave in the appendix**, since appendix placement matches its status as the weakest link | existing | `figures/country-variation.pdf` | keep as is |
| 11 | morphgain derivative trajectories | data | that exit cases keep source semantics after syntactic integration | small multiples | **DATA PARTIAL**: 4 of 8 COHA captures (`booed`, `shooed`, `shooing`, `wowing`) are saved error pages, not tables | stretch |

## Improvements to existing floats, no new build

- **Figure 1 (causal network, p.26)** stays where it is: it summarizes §4's links and belongs after them. Candidates 1–3 relieve it of the job it currently does badly, which is carrying §1 through §3 from twenty pages away.
- **Table 2 (link-status)** already grades every link by evidential status. Cross-referencing it from §6.1's probes satisfies the one salvageable point in the 2026-07-27 ChatGPT review at the cost of a clause, and stops a sceptical reader treating all probes as equal weight.
- **Table 1** is now 6 property columns + 3 node columns. It survived the sixth column without going overfull; don't add a seventh.

## House-style build notes

Conceptual diagrams in TikZ, following Figure 1's existing style vocabulary
(blue for processes, white for diagnostics, green for field-relative nodes) so
the new figures and the old one read as one system. Data plots via
`.house-style/plot_style.py`. Then `/check-chart-style` on each. Watch the
house doctrine: direct labels over legends, range-framed axes, identical
scales across compared panels, and a redundant channel so each survives
greyscale.

## Trim prompt

Three **must** items (1, 2, 3) plus one free move (7) would put a figure in §1,
§3 and §5 and bring the negative result into the body. That is the minimum that
fixes the structural problem. Which of 4, 5, 6 earn their place, and is 8 worth
the build given the data is already extracted and saved?
