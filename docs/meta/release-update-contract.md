# Release documentation update contract

This contract tells a Cursor cloud agent how to update **product documentation**
when Backfield cuts a SemVer release (`vX.Y.Z`). The agent runs against this
repository (`localangle/backfield-docs`) and opens a pull request for human
review. Documentation never deploys until that PR is merged to `main`.

Engineering docs that live inside the Backfield application repo are out of
scope.

## When this runs

Only on SemVer tags pushed to `localangle/backfield`. Not on every merge to
`main`.

## Inputs (from the Backfield Release job)

The launcher provides:

| Field | Meaning |
| --- | --- |
| `RELEASE_TAG` | New SemVer tag (for example `v0.8.0`) |
| `PREVIOUS_TAG` | Prior SemVer tag, or empty when this is the first public baseline |
| Commit summary | Subject lines (and optional bodies) between the tags |
| Release notes | GitHub-generated notes for the Backfield release, when available |
| Release URL | Link to the Backfield GitHub Release page |

Treat those inputs as the source of truth for *what changed in the product*.
Do not invent features that are not supported by the inputs.

## Required outputs

Open or update a pull request with:

1. **Changelog** — Prepend one row to [`docs/changelog.md`](../changelog.md)
   using the existing table style. Date it with the release calendar day. Use
   short, product-facing bullets (what a newsroom user gains), not commit hashes,
   package names, or internal file paths.
2. **Targeted page updates** — Only when user-visible platform, tutorial, API
   prose, or support guidance must change. Prefer editing existing pages under:
   - `docs/platform/`
   - `docs/tutorials/`
   - `docs/api/` (explanatory prose only)
   - `docs/support/`
3. **PR title** — `docs: Backfield <tag> release notes`
4. **PR body** — Include the tag, Backfield release URL, list of files touched,
   and an explicit note if the release warranted a **changelog-only** update.

Never merge the PR. A human reviews and merges.

## Hard rules

- Write for a non-technical end user. Avoid internal database terms, repo paths,
  and developer jargon in user-facing copy.
- Do **not** invent API endpoints, query parameters, response fields, or UI
  labels. If unsure, omit the detail rather than guessing.
- Do **not** edit `mkdocs.yml` unless you add a new page that must appear in the
  nav.
- Do **not** touch `site/`, `dist/`, `hooks/`, `.github/workflows/`, or build
  scripts.
- If the release is documentation/CI-only with no product surface change, still
  open a PR, but limit it to the changelog (and say so in the PR body).
- Idempotent: if an open PR already exists for this `RELEASE_TAG`, update that
  branch instead of opening a duplicate.

## Path allowlist

| Writable | Notes |
| --- | --- |
| `docs/**/*.md` | Primary edit surface |
| `mkdocs.yml` | Only when a new page requires a nav entry |

Everything else is out of scope.

## Suggested workflow for the agent

1. Read this contract and skim [`docs/changelog.md`](../changelog.md) for tone.
2. Decide which product areas the release touches from the commit summary and
   release notes.
3. Update the changelog first.
4. Update the smallest set of existing pages that need to stay accurate.
5. Open or update the PR with the required title and body.
6. Stop. Do not merge, deploy, or expand scope.
