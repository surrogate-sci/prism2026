# PRISM 2026 repository guidance

## Human authorship boundary

This project publication and any related blog posts must remain human-authored.
Agents may operate the publishing machinery, but they must not supply the
writing, analysis, or scientific reasoning.

- Do not draft, rewrite, paraphrase, polish, translate, or autocomplete
  publication or blog prose. This includes titles, summaries, body text,
  captions, appendices, disclosures, contribution statements, and repository
  prose such as README or CONTRIBUTING text.
- Do not invent or add scientific claims, methods, results, interpretations,
  citations, examples, mathematical arguments, or analysis code whose output
  supports a scientific conclusion.
- Do not directly apply grammar, style, clarity, citation, or mathematical
  corrections to authored content. A human author must decide and make the
  final change.
- Text or analysis code supplied by a human may be inserted verbatim when the
  user explicitly directs where it belongs. Do not silently revise it while
  inserting it.
- Do not author AI-use disclosures or CRediT statements on anyone else's
  behalf. Agents may validate author-supplied records and report omissions.

Agents may:

- Compile, render, convert, package, and debug Quarto, Jupyter, LaTeX, HTML,
  and PDF outputs.
- Work on CI, configuration, templates, stylesheets, layout, accessibility,
  and web design without changing authored prose, analyses, or scientific
  meaning.
- Run human-authored analysis code to reproduce outputs and report failures
  without changing the analysis.
- Inspect human-authored writing and return a checklist of possible grammar
  problems, awkward sentences, unclear passages, citation problems, or
  mathematical inconsistencies. Give that checklist in chat or an untracked
  local review artifact; never commit or push it, and never apply its proposed
  edits automatically.

Before every commit or push, inspect the complete diff. If it contains
agent-authored publication or blog prose, scientific analysis, or scientific
reasoning, remove that content from the change and stop for a human author to
provide it. Do not transfer AI-written prose between this repository, the
publication template, or another blog repository. This `AGENTS.md` policy is
an explicitly authorized exception.

## Working agreement

- Work on a focused branch and submit changes through a pull request into `main`.
- Write the main publication in `index.ipynb`; keep citations in `ref.bib` and reusable analysis code
  in `src/analysis/`.
- Do not change the publication theme, the Warm Journal default, brand colors, fonts, or logo unless
  the repository owner explicitly requests a design change.
- Keep `authors.yml`, the CRediT contribution record, and `ai-use.yml` consistent with the exact
  author-approved manuscript metadata.
- Do not commit session notes, internal design records, private correspondence, credentials, local
  agent artifacts, or generated `_site/` directories.
- Do not edit `gh-pages` directly. Merges to `main` publish through GitHub Actions.

## Required checks

Before requesting review, run:

```bash
make test
make render-warm
make render-technical
```

If computational outputs changed intentionally, run `make execute` and review the corresponding
`_freeze/` changes. Verify the rendered narrative, figures, citations, links, author display, and AI
disclosure in both profiles.
