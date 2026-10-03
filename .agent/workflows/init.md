---
description: Initialize the {{PAPER_TITLE}} project environment
---

# {{PAPER_TITLE}} Project Initialization

This workflow orients you to the project. Use it at the start of any new session.

## Quick Start (Returning Session)

1. **Scan the repo for orientation docs**
   ```
   ls -la
   ```

2. **Read orchestration + status files (if present)**
   ```
   [ -f AGENTS.md ] && cat AGENTS.md
   [ -f STATUS.md ] && cat STATUS.md
   [ -f TODO.md ] && cat TODO.md
   ```

3. **Check house style (if present)**
   ```
   [ -f .house-style/style-guide.md ] && cat .house-style/style-guide.md
   [ -f .house-style/style-rules.yaml ] && cat .house-style/style-rules.yaml
   ```

4. **Identify the build entrypoint**
   ```
   ls -la *.tex 2>/dev/null || true
   [ -f Makefile ] && sed -n '1,160p' Makefile
   ```

## Key Retrieval Points

**For argument/outline:**
- `outline.md`, `PLAN.md`, `docs/`, `notes/`

**For current draft:**
- `main.tex` (or the largest `*.tex` in the repo root)

**For bibliography:**
- `references.bib` or `refs.bib`

**For figures/data:**
- `figures/`, `Fig/`, `data/`

**For source PDFs (if present):**
- `literature/`, `sources/`, `pdf/`

Search PDFs quickly:
```
pdftotext "PATH/filename.pdf" - | rg -n "keyword"
```

## Full Initialization (New to Project)

1. **Read `CLAUDE.md` and `AGENTS.md` (if present)** — overview, build commands, house style
2. **Skim the main TeX file** (`main.tex` or equivalent) for structure and macro conventions
3. **Locate bibliography + figure folders** so you know where to add assets
4. **Run a quick build** (optional, if you have TeX installed)
   - `make quick` or `make`
   - otherwise: `latexmk -xelatex main.tex`

## Process Reminders

**For drafting/revision:** editing passes, their order, and which are due are
tracked by `python3 ../../../Project-Management/tools/passes.py` (schema in
`../../../passes/README.md`).

**For citation work:**
1. Add BibTeX entries carefully (protect capitalization)
2. Use `\textcite{}` for narrative and `\citep{}` for parenthetical citations
3. Rebuild after citation edits to catch missing keys

**Git:**
- Commit after each logical unit of work; use `/git-hygiene` if you need reminders

## Other Workflows

- `/git-hygiene` — Reminders for clean commits and branch management
- `/multi-agent-review` — Where the portfolio's multi-model review rules and templates live
