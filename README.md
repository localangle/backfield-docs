# Backfield Docs

Documentation site for the Backfield platform and APIs, built with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

The site will be available at http://127.0.0.1:8000 with live reload.

Port **8000** serves this documentation site only. The Backfield Public API runs separately (local default: http://localhost:8004/public/v1). See the [API overview](docs/api/index.md) for base URLs and local setup.

## Building

```bash
mkdocs build
```

Static output is written to `site/`.

## Deployment

Pushes to `main` deploy the complete documentation site to the `gh-pages`
branch through `.github/workflows/deploy-docs.yml`.

To deploy the full site manually:

```bash
mkdocs gh-deploy --strict --force
```

The Pages deployment intentionally uses the default `mkdocs.yml`. The
`mkdocs-api.yml` configuration is reserved for API-only builds and must not be
used for the main documentation deployment.

## Export API reference as PDF

One command builds the site and writes a merged PDF to `dist/backfield-api.pdf`:

```bash
./scripts/build-api-pdf.sh
```

First run installs Playwright/Chromium via `requirements-dev.txt`. Useful flags:

```bash
./scripts/build-api-pdf.sh --skip-build              # reuse existing site/
./scripts/build-api-pdf.sh --output dist/my-api.pdf  # custom output path
```

Pages are exported in **API Reference** nav order from `mkdocs.yml`.

## Structure

| Path | Contents |
| --- | --- |
| `docs/platform/` | Platform documentation (concepts, architecture, setup) |
| `docs/api/` | Public API reference (resources and endpoints) |
| `docs/tutorials/` | Step-by-step guides |
| `docs/support/` | FAQ and support channels |
| `docs/meta/` | Maintainer contracts (not part of the public nav) |
| `docs/stylesheets/extra.css` | Custom styling on top of the Material theme |

## Release documentation updates

When Backfield cuts a SemVer release, a Cursor cloud agent may open a PR against
this repository to update the changelog and targeted product pages. The agent
must follow [`docs/meta/release-update-contract.md`](docs/meta/release-update-contract.md).
Humans review and merge those PRs; deploy still happens only from `main`.
