# Projects

A **project** is the main container you work in. It holds the pipelines you build, the text you process, the results you review, and the catalog of people, places, and organizations that work produces.

When you query the [Public API](../../api/index.md), you're always asking about a specific project, identified by its **slug** (a short, URL-friendly name like `general`).

## What lives in a project

| Area | What it holds |
| --- | --- |
| **Flows** | The pipelines you build in [Agate](../agate/flows.md) |
| **Runs** | Each time a flow is executed on your text — see [Runs](../agate/runs.md) |
| **Processed items** | The reviewable results of a run — see [Processed items](../agate/processed-items.md) |
| **Content** | The articles and extracted details produced by runs — see [Shared content store](content-store.md) |
| **Catalog** | The project's confirmed people, places, and organizations in [Stylebook](../stylebook/index.md) |
| **Settings** | Project-level choices for [AI models](../settings/ai-models.md), [integrations](../settings/integrations.md), and [API keys](../settings/api-keys.md) |

## How projects relate to the rest of Backfield

- A project belongs to one [organization](organizations.md), optionally grouped into a [workspace](organizations.md).
- A project draws on shared organization settings (models, integrations, Stylebook catalogs) but can override many of them for its own needs.
- Access is granted per project, so different teams can work in different projects without seeing each other's data. See [Users & access](users.md).

## The project slug

Every project has a human-readable **slug**. You'll use it when calling the API:

```text
/projects/{project_slug}/…
```

You can find your slug in the project's settings, or confirm it with the [Get project](../../api/projects/get-project.md) endpoint.

!!! note "Work in progress"
    Project creation and management walkthroughs will be added here.
