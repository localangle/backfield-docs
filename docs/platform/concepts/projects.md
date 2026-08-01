# Projects

A **project** is the main container for a body of editorial processing. It
keeps a team's flows, runs, source articles, extracted evidence, and settings
together so that one project cannot accidentally mix operational data with
another.

When you query [Backfield API](../../api/index.md), you're always asking about
a specific project, identified by its **slug** (a short, URL-friendly name like
`general`).

## What lives in a project

| Area | What it holds |
| --- | --- |
| **Flows** | The pipelines you build in [Agate](../agate/flows.md) |
| **Runs** | Each time a flow is executed on your text — see [Runs](../agate/runs.md) |
| **Processed items** | The reviewable results of a run — see [Processed items](../agate/processed-items.md) |
| **Content** | The articles and extracted details produced by runs — see [Data model](content-model.md) |
| **Stylebook** | The shared catalog assigned to the project for confirmed people, places, and organizations |
| **Settings** | Project-level choices for [AI models](../settings/ai-models.md), [integrations](../settings/integrations.md), and [API keys](../settings/api-keys.md) |

## How projects relate to the rest of Backfield

- A project belongs to one [organization](organizations.md), optionally grouped into a [workspace](organizations.md).
- A project draws on shared organization settings such as models and
  integrations, and is assigned one same-organization
  [Stylebook](../stylebook/stylebooks.md). That Stylebook is authoritative for
  every flow and entity operation in the project.
- Access is granted per project, so different teams can work in different projects without seeing each other's data. See [Users & access](users.md).

## Flows, runs, and processed items

These terms describe different levels of the same work:

- A **flow** is the reusable recipe: the steps Agate should perform.
- A **run** is one execution of that recipe.
- A **processed item** is the result for one article within the run.

A batch run therefore has one run record and many processed items. Editing a
flow changes future runs; it does not rewrite runs that already finished.

## The project's Stylebook

When a project is created, it is assigned one Stylebook from the same
organization. Every flow in the project uses that Stylebook for canonical
people, organizations, and locations. The assignment is shown in project
settings and cannot be changed later.

Several projects may share one Stylebook. In that case, they contribute
separate article evidence to the same canonical reference catalog. Filters in
Stylebook let editors narrow mentions and candidate work by project without
changing Stylebook-wide canonical metadata or connections.

## Project overview and settings

The project page brings together its flows and runs and summarizes activity
such as article counts, processed items, and estimated AI cost. Its settings
also show:

- the assigned Stylebook;
- project-specific model and integration choices;
- a project system prompt that supplies shared model guidance where supported;
- project API keys for external applications.

Organization defaults reduce repeated setup, while project overrides let a
team use a different approved model or integration credential where supported.

## The project slug

Every project has a human-readable **slug**, unique within its organization.
Different organizations may use the same project slug. You'll use it when
calling the API:

```text
/projects/{project_slug}/…
```

You can find your slug in the project's settings, or confirm it with the [Get project](../../api/projects/get-project.md) endpoint.

A project API key is bound to one project. Backfield API resolves that binding
before validating the slug, so a matching slug in another organization cannot
redirect the request.
