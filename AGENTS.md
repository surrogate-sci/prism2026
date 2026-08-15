# PRISM 2026 repository guidance

## Scope

This repository is a project publication. Preserve author intent and treat
scientific claims, methods, interpretation, author order, and credit as author decisions. Flag
questions rather than silently changing substantive content.

## Working agreement

- Work on a focused branch and submit changes through a pull request into `main`.
- Write the main publication in `index.ipynb`; keep citations in `ref.bib` and reusable analysis code
  in `src/analysis/`.
- Do not change the publication theme, the Warm Journal default, brand colors, fonts, or logo unless
  the repository owner explicitly requests a design change.
- Keep `authors.yml`, the CRediT contribution record, and `ai-use.yml` consistent with the author-
  approved manuscript metadata.
- Do not invent author names, affiliations, ORCIDs, contributions, citations, results, or AI-use
  statements.
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
