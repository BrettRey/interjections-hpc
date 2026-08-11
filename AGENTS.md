# CLAUDE.md -- English Interjections as HPC

## Role: Editor/Researcher

Deep editorial and research work welcome here. This is not a PM session.

## Project Overview

Paper arguing that interjection is a genuine lexical category of English, not a marginal or anomalous one, and that what earns it that status is projectibility rather than a defining property. The empirical base is Brett's Wikipedia "Good Article" on English interjections, which covers phonology, morphology, syntax, semantics, pragmatics, variation, and historical treatments. The theoretical payoff: interjections are a strong test case for projectibility-as-criterion, because they've been denied or marginalised as a category by major grammars. That the projections turn out to be largely pragmatic is a result about the category, not a claim about which subfield owns it.

**Working title:** What English Interjections Let Us Predict: Stable Causal-Pragmatic Clustering and Path Dependence
**Target:** *Journal of Linguistics* (CUP) -- intended but HELD until LIN-2026-0100 (definiteness) resolves ~Dec 2026; do not run two Reynolds projectibility papers at JL at once.
**Closed:** Journal of Pragmatics (rejected 2026-07-23, PRAGMA-D-26-00584, blanket citation-integrity policy, permanent). Corpus Pragmatics and the other pragmatics venues ruled out 2026-07-24 with the reframe. Stretch: *Language*. Fallback: *Glossa* (fit unverified).

### Core Argument

1. **The problem:** Interjections are denied category status (Jespersen), dismissed as uninteresting (Huddleston & Pullum Student's), or conceded as "marginal and anomalous" (Quirk et al.). Classical category theory can't handle the fuzziness.

2. **The property cluster:** Non-referential, non-inflecting, prosodically isolated, syntactically supplemental (supplement function), stance-laden, sequentially usable, freely coined via onomatopoeia.

3. **Mechanisms:** Semantic bleaching (noun→interjection paths like *God* → *gee*), prosodic isolation reinforcing syntactic independence, pragmatic conventionalisation.

4. **Projectibility:** What does categorising something as an interjection let you *infer*? Prosodic packaging, supplementarity, stance, sequential position, response function, and uptake. The domain those projections fall in is set by the domain the causal links operate in, which is why they come out largely pragmatic, a finding rather than the thesis. Do not write "pragmatic projectibility" as a standing phrase: it is Journal-of-Pragmatics residue and it pre-empts the paper's own section 5.4.

5. **Diachronic dimension:** Bleaching paths as sources of pragmatic profile stability and path dependence; *nay* -> *yeah* shift; regional variation (*lah*, *yaar*, *haba*) as evidence that the cluster is dynamic but stable.

6. **Boundary disputes as projectibility tests:** Graded boundaries with nouns, verbs, adverbs, fillers, and routine formulae are predicted by the causal-pragmatic cluster analysis, not anomalous.

### Key Sources

| Source | Role |
|--------|------|
| Ameka (1992) | Interjections as neglected category; routine formulae debate |
| Wilkins (1992) | Routine formulae as interjection subtype |
| Gehweiler (2008) | Diachronic bleaching (*gee!*) |
| Meinard (2015) | Interjection vs. onomatopoeia distinction |
| Dingemanse (2020) | Liminal signs in interaction |
| CGEL (Huddleston & Pullum 2002) | Interjection phrases, supplement function |
| Quirk et al. (1985) | "Marginal and anomalous class" |
| Boyd (1999) | HPC / projectibility theory |
| O'Connell & Kowal (2005) | Interjections vs. fillers |

### Connections to Brett's Research Programme

- **Pragmatic projectibility:** The centre of the JoP pitch: category membership as a guide to use, uptake, stance, and sequential distribution
- **HPC theory in linguistics:** A calibrated category case study, but not a strict homeostasis claim without corrective-control evidence
- **Boundary phenomena:** Interjections *are* boundary phenomena (graded membership in every direction)
- **Projectibility:** The pragmatic (not truth-conditional) nature of interjection-inference extends the theory
- **CGEL syntax:** Supplement function, interjection phrases, category vs. function distinction

## Build

```bash
make              # Full build (xelatex + biber + 2x xelatex)
make quick        # Single xelatex pass
make clean        # Remove artifacts, keep PDF
```

Requires XeLaTeX (not pdfLaTeX or LuaLaTeX).

## House Style

See `.house-style/style-rules.yaml`. Key rules:
- `\term{}` for concepts, `\mention{}` for forms, `\enquote{}` for quotes
- En-dash with spaces (`~-- `), never em-dashes
- Contractions preferred, ~60 word paragraphs
- `\textcite{}` narrative, `\citep{}` parenthetical

## Multi-Agent Dispatch (MANDATORY)

**Before dispatching multiple agents, ALWAYS ask Brett which model(s) to use
and whether redundant outputs are wanted.**

The invocations are deliberately not copied here. They live in
`../../../.claude/rules/multi-model-dispatch.md`
and change faster than a copy can track. This section used to carry them,
and every copy in the portfolio was still routing agents to the deprecated
Gemini CLI and passing codex its prompt through a flag that selects a
config profile, months after both were superseded. In a Claude Code
session opened anywhere inside the portfolio the portfolio rules load
automatically, and you do not need to read them by hand.
