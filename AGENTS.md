# CLAUDE.md -- English Interjections as HPC

## Role: Editor/Researcher

Deep editorial and research work welcome here. This is not a PM session.

## Project Overview

Paper arguing that English interjections constitute a homeostatic property cluster (HPC), not a marginal or anomalous category. The empirical base is Brett's Wikipedia "Good Article" on English interjections, which covers phonology, morphology, syntax, semantics, pragmatics, variation, and historical treatments. The theoretical payoff: interjections are a particularly strong test case for HPC because they've been denied or marginalised as a category by major grammars.

**Working title:** English Interjections as a Homeostatic Property Cluster
**Target:** Journal of Historical Pragmatics (John Benjamins)

### Core Argument

1. **The problem:** Interjections are denied category status (Jespersen), dismissed as uninteresting (Huddleston & Pullum Student's), or conceded as "marginal and anomalous" (Quirk et al.). Classical category theory can't handle the fuzziness.

2. **The property cluster:** Non-referential, non-inflecting, prosodically isolated, syntactically supplemental (supplement function), emotively laden, freely coined via onomatopoeia.

3. **Mechanisms:** Semantic bleaching (noun→interjection paths like *God* → *gee*), prosodic isolation reinforcing syntactic independence, pragmatic conventionalisation.

4. **Projectibility:** What does categorising something as an interjection let you *infer*? Primarily pragmatic (prosodic behaviour, syntactic non-integration, emotive/interpersonal force) rather than truth-conditional. This is the paper's distinctive contribution to HPC theory.

5. **Diachronic dimension:** Bleaching paths as mechanism trajectories; *nay* → *yeah* shift; regional variation (*lah*, *yaar*, *haba*) as evidence of dynamic stability. This is the JHP angle.

6. **Boundary disputes as HPC predictions:** Graded boundaries with nouns, verbs, adverbs, fillers, and routine formulae are predicted by HPC, not anomalous.

### Key Sources

| Source | Role |
|--------|------|
| Ameka (1992) | Interjections as neglected category; routine formulae debate |
| Wilkins (1992) | Routine formulae as interjection subtype |
| Gehweiler (2008) | Diachronic bleaching (*gee!*); published in JHP |
| Meinard (2015) | Interjection vs. onomatopoeia distinction |
| Dingemanse (2020) | Liminal signs in interaction |
| CGEL (Huddleston & Pullum 2002) | Interjection phrases, supplement function |
| Quirk et al. (1985) | "Marginal and anomalous class" |
| Boyd (1999) | HPC theory |
| O'Connell & Kowal (2005) | Interjections vs. fillers |

### Connections to Brett's Research Programme

- **HPC theory in linguistics:** Another category case study, but one that tests HPC at the margins
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
