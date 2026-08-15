# PRISM fellow quick start

1. Clone the project:

   ```bash
   git clone https://github.com/surrogate-sci/prism2026.git
   cd prism2026
   ```

2. Follow the [environment setup guide](ENVIRONMENT_SETUP.md).

3. Create a focused branch from an up-to-date `main`:

   ```bash
   git switch main
   git pull --ff-only
   git switch -c initials/short-description
   ```

4. Write in `index.ipynb`, add citations to `ref.bib`, and keep reusable analysis code in
   `src/analysis/`.

5. Preview the existing Warm Journal default:

   ```bash
   make preview-warm
   ```

   The Technical Notebook view remains available with `make preview-technical`. Do not change the
   project-wide theme during a writing contribution.

6. Follow the [contribution guide](../pages/CONTRIBUTING.qmd) for author metadata, CRediT, AI-use
   disclosure, required checks, and pull-request review.

7. Before requesting review, run:

   ```bash
   make test
   make render-warm
   make render-technical
   ```

Reviewed changes merge into `main`; GitHub Actions then updates the published site automatically.
