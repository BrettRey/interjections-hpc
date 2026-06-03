# CLAUDE.md -- English Interjections as HPC

## Role: Editor/Researcher

Deep editorial and research work welcome here. This is not a PM session.

## Project Overview

Paper arguing that English interjections form a stable causal-pragmatic projectible cluster, not a marginal or anomalous category. The empirical base is Brett's Wikipedia "Good Article" on English interjections, which covers phonology, morphology, syntax, semantics, pragmatics, variation, and historical treatments. The theoretical payoff: interjections are a particularly strong test case for pragmatic projectibility because they've been denied or marginalised as a category by major grammars.

**Working title:** What English Interjections Let Us Predict: Stable Causal-Pragmatic Clustering and Path Dependence
**Target:** Journal of Pragmatics (Elsevier)
**Backup:** Corpus Pragmatics, but only after making the GloWbE/COHA method more central.

### Core Argument

1. **The problem:** Interjections are denied category status (Jespersen), dismissed as uninteresting (Huddleston & Pullum Student's), or conceded as "marginal and anomalous" (Quirk et al.). Classical category theory can't handle the fuzziness.

2. **The property cluster:** Non-referential, non-inflecting, prosodically isolated, syntactically supplemental (supplement function), stance-laden, sequentially usable, freely coined via onomatopoeia.

3. **Mechanisms:** Semantic bleaching (noun→interjection paths like *God* → *gee*), prosodic isolation reinforcing syntactic independence, pragmatic conventionalisation.

4. **Pragmatic projectibility:** What does categorising something as an interjection let you *infer*? Primarily pragmatic: prosodic packaging, supplementarity, stance, sequential position, response function, and uptake. This is the paper's distinctive contribution to theoretical pragmatics.

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

**Before dispatching multiple agents, ALWAYS ask Brett:**

1. **Which model(s)?** Options: Claude, Codex, Gemini, Copilot
2. **Redundant outputs?** Should multiple models tackle the same task?

### CLI Command Patterns

| CLI | Command | Notes |
|-----|---------|-------|
| **Codex** | `codex -p 'prompt' > output.txt &` | Include "Read [PATH] first" in prompt |
| **Gemini** | `cat file.tex \| gemini --yolo -o text 'prompt'` | Must pipe content (file reading broken in YOLO) |
| **Copilot** | `copilot -p 'prompt' > output.txt &` | Fast; add `--allow-all-tools` for file ops |

**Token limits:** Gemini > Codex > Claude (most constrained)
