# Scientific Causal Reasoning for Interpretability

This repository is the shared writing and computational workspace for the project publication. The
publication combines narrative, citations, code, figures, and reproducible results in Quarto.

[Read the current publication](https://surrogate-sci.github.io/prism2026/)

## Quick start for PRISM fellows

1. Clone the repository and enter it:

   ```bash
   git clone https://github.com/surrogate-sci/prism2026.git
   cd prism2026
   ```

2. Follow the [environment setup guide](developer-docs/ENVIRONMENT_SETUP.md), then create a branch
   for one focused change:

   ```bash
   git switch -c initials/short-description
   ```

3. Write in `index.ipynb`. Put reusable analysis code in `src/analysis/`, bibliography entries in
   `ref.bib`, and publication-ready figures or data in clearly named project folders.

4. Preview the publication locally:

   ```bash
   make preview-warm
   ```

5. Run the checks, push your branch, and open a pull request. See the complete
   [contribution guide](pages/CONTRIBUTING.qmd).

## Publication themes

The project retains both Surrogate Science themes. **Warm Journal remains the default**; do not
change the project-wide theme as part of a writing contribution.

```bash
make preview-warm
make preview-technical
make render-warm
make render-technical
```

## Before requesting review

- Update `authors.yml` when the working author roster changes.
- Add sources to `ref.bib` and cite them from the manuscript rather than typing references by hand.
- Complete the [CRediT contribution intake](developer-docs/CREDIT_CONTRIBUTIONS.md) before release.
- Record author-specific AI use in `ai-use.yml`; first and last authors provide statements, and all
  other authors confirm that they read the complete disclosure.
- Run `make test`, `make render-warm`, and `make render-technical`.
- Confirm that generated output, private notes, credentials, and local session files are not in the
  pull request.

## Publishing

Every reviewed merge to `main` triggers the Quarto Publish workflow. It renders the default profile
and updates the `gh-pages` branch automatically. GitHub Pages serves that branch at the publication
URL above.

Create a GitHub release when the team is ready to preserve a citable version. Connect the repository
to Zenodo only after the title, author order, contribution statement, and release metadata have been
reviewed.

## Documentation

- [Contributing](pages/CONTRIBUTING.qmd)
- [Environment setup](developer-docs/ENVIRONMENT_SETUP.md)
- [AI usage disclosure](developer-docs/AI_USAGE.md)
- [CRediT author contributions](developer-docs/CREDIT_CONTRIBUTIONS.md)
- [Publishing guide](developer-docs/PUBLISHING_GUIDE.md)
