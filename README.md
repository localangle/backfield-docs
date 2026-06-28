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
| `docs/stylesheets/extra.css` | Custom styling on top of the Material theme |
