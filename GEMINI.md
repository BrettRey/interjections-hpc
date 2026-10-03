# CLAUDE.md -- English Interjections as HPC

## Role: Editor/Researcher

Deep editorial and research work welcome here. This is not a PM session.

## Project Overview

Paper arguing that English linguists use *interjection* for three overlapping but non-identical classifications (a grammar-facing lexical category, a semantics-facing category of expressive or use-conditional signs, and an interaction-facing category of conventionalized sequential resources), that none has priority over the others, and that their overlap isn't a fourth category and supplies no independent projective force. The empirical argument concerns path dependence: recruitment histories remain visible in source-specific residues. The project grew out of Brett's Wikipedia "Good Article" on English interjections. The abstract in `main.tex` is the authoritative statement of the thesis.

**Title:** English Interjections Across Grammar, Meaning, and Interaction: Field-Relative Categories and Path Dependence (`main.tex` is authoritative)
**Venue:** see `STATUS.md`. *Journal of Pragmatics* is closed permanently (blanket citation-integrity rejection, 2026-07-23); the other pragmatics venues were ruled out with the 2026-07-24 reframe.

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

## Multi-agent dispatch

Model routing and dispatch commands follow the portfolio rule
`../../../.claude/rules/multi-model-dispatch.md`. Claude Code sessions inside
the portfolio load it automatically; Codex (reading this file as `AGENTS.md`)
and Antigravity (reading `GEMINI.md`) should read it directly.
