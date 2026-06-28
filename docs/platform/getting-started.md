# Getting Started

Run Backfield locally from the [Backfield repository](https://github.com/localangle/backfield). The **`backfield`** command is a project launcher that bootstraps your environment, starts the Docker stack, migrates the database, and seeds your first organization and admin user.

This guide covers local development setup. For querying data from your own code after the stack is running, see the [API Reference](../api/index.md).

## Prerequisites

Install these before you begin:

- **[Docker and Docker Compose](https://docs.docker.com/compose/)** — runs Postgres, Redis, APIs, and the worker
- **[uv](https://docs.astral.sh/uv/)** — installs Python dependencies for the monorepo
- **Git** — clone the Backfield repository

You do not need a separate cloud account or a published `pip install backfield` package for local setup.

## 1. Clone and bootstrap

```bash
git clone git@github.com:localangle/backfield.git
cd backfield
make bootstrap
source .venv/bin/activate    # once per shell
```

`make bootstrap` runs `uv sync` for the whole workspace and copies the project launcher into `.venv/bin/backfield`. After activating the venv, the `backfield` command is available in that shell.

You can also run `./scripts/backfield` or `make up` without activating the venv, as long as you are in the repo root.

Optional — use `backfield` from any directory without activating the venv:

```bash
make install-user-cli        # symlinks ~/.local/bin/backfield -> scripts/backfield
```

Ensure `~/.local/bin` is on your `PATH`. Reverse with `make uninstall-user-cli`.

Run **`backfield doctor`** anytime to check repo root, `uv`, Docker, `.venv`, `.env`, and the compose file.

## 2. First-run setup with `backfield init`

From the repo root (with the venv activated or the user CLI installed):

```bash
backfield init
```

The interactive wizard walks through five steps:

1. **Prepare environment secrets** — creates `.env` from `.env.example` when missing and generates local secrets
2. **Start the Docker Compose stack** — builds and starts services (APIs, worker, databases, UIs)
3. **Run database migrations** — applies Alembic schema via a one-off compose migrate service
4. **Wait for API readiness** — blocks until core services respond
5. **Seed organization and admin user** — creates your org, default Stylebook, and superuser login

You will be prompted for superuser email, password, display name, organization name, and Stylebook name. Press Enter to accept the suggested defaults.

When `init` finishes, it prints your local app URLs and admin email. By default it also opens **Settings → AI models** in Agate so you can add provider credentials.

### Non-interactive init

For CI or scripted setup, pass a JSON config file:

```bash
backfield init --non-interactive --config path/to/init-config.json
```

Use `--skip-stack` when the stack is already running, and `--no-browser` to skip opening Agate in a browser.

## 3. Open the apps

After a successful `init`, use these local URLs:

| App | URL |
| --- | --- |
| **Agate** | [http://localhost:5173](http://localhost:5173) |
| **Stylebook** | [http://localhost:5175](http://localhost:5175) |
| **Public API** | [http://localhost:8004/public/v1](http://localhost:8004/public/v1) |

Log in to Agate and Stylebook with the superuser email and password you chose during `init`.

## 4. Configure models and integrations

Before running flows, add credentials in Agate:

1. **Settings → AI models** — provider API keys and approved models for extractors ([AI models](settings/ai-models.md))
2. **Settings → Integrations** — geocoding, search, and storage credentials ([Integrations](settings/integrations.md))

Project API keys for the Public API are also created in Agate under the project's **API** section — see [Authentication](../api/authentication.md).

## Day-to-day stack commands

After the first run, you usually start and stop the stack with:

| Command | Purpose |
| --- | --- |
| `backfield up` | Start the stack in the foreground (Ctrl+C stops) |
| `backfield up --detached` | Start in the background |
| `backfield down` | Stop the stack |
| `backfield logs` | Follow service logs |
| `backfield ps` | List running containers |
| `backfield restart` | Restart services |

Equivalent `make` targets exist (`make up`, `make down`, `make logs`, …).

Other operator commands:

| Command | Purpose |
| --- | --- |
| `backfield doctor` | Verify local setup |
| `backfield migrate` | Apply migrations from the host (Postgres on `:5433`) |
| `backfield seed` | Ensure org and admin exist (idempotent; used in production provisioning) |
| `backfield reset-db` | Stop the stack and remove volumes — **deletes all local data** |
| `backfield clear-entity-data` | Truncate entity and run tables while keeping identity rows (local dev) |

`reset-db` and `clear-entity-data` prompt for confirmation unless you pass `--yes`.

## Troubleshooting

If `backfield` fails with **`ModuleNotFoundError: No module named 'backfield_cli'`**, run **`make bootstrap`** from the repo root, then **`backfield doctor`**. Avoid bare `uv sync` from an app or package subdirectory — use **`uv sync --all-packages`** at the repo root.

Do not use **`uv run backfield`** — there is no Python console script named `backfield`. Use **`backfield`**, **`./scripts/backfield`**, or **`make`** wrappers instead.

## Next steps

- Understand how accounts are organized in [Organizations & workspaces](concepts/organizations.md)
- Learn what a [Project](concepts/projects.md) contains
- Build a pipeline in [Agate](agate/index.md), or curate your catalog in [Stylebook](stylebook/index.md)
- Query your data from code in the [API Reference](../api/index.md)
- Follow the [Quickstart tutorial](../tutorials/quickstart.md) for a first end-to-end workflow
