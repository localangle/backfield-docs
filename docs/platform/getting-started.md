# Getting Started

This page orients you after your newsroom has given you a Backfield account.
It explains what to choose when you sign in and where the main kinds of work
live. Detailed task tutorials can build on these concepts later.

## Before you sign in

An organization administrator normally prepares:

- your account and temporary password;
- access to the workspaces where your projects live;
- editing access to any Stylebooks you will curate;
- approved AI models and integrations for the flows your team uses.

There is no public self-registration screen. If you cannot see an expected
workspace, project, or Stylebook, ask an organization administrator to check
your access.

## 1. Sign in and choose an organization

Sign in with your Backfield email and password. If your account belongs to more
than one organization, choose the newsroom or company you want to work in.
You can switch organizations later from the account menu.

A temporary password must be changed before the rest of the platform opens.

## 2. Find your workspace and project

Agate opens on the workspace grid. A workspace groups related projects, often
by desk, publication, beat, or initiative. Open a workspace, then choose the
project that contains the work you need.

The project page brings together:

- **Flows** — reusable processing recipes;
- **Runs** — individual executions and their progress;
- **Models** and **Integrations** — the project's approved processing services;
- **API** — credentials for external applications.

See [Organizations & workspaces](concepts/organizations.md) and
[Projects](concepts/projects.md) for how these boundaries affect what you can
see and change.

## 3. Know the three applications

Use **Agate** when the question is about a particular article or processing
job:

- build or inspect a flow;
- start and monitor a run;
- review extracted people, organizations, places, and article metadata;
- correct evidence or geography for one story.

Use **Stylebook** when the question is about shared reference knowledge:

- decide whether an extracted item matches an existing canonical record;
- create or merge canonical people, organizations, and locations;
- maintain newsroom-wide metadata, geography, and connections;
- review possible duplicates or other catalog-quality issues.

Use **Backfield API** when a product, service, tool, or analysis needs to use
the structured data:

- retrieve articles and their extracted details;
- search by keyword, meaning, entity, metadata, or geography;
- follow mentions and connections across reporting;
- trigger approved flows from trusted automation.

The API is a first-class part of Backfield, even though people usually interact
with it through software rather than an editorial screen. The hosted
[API Playground](../api/playground.md) provides an interactive way to explore
it, while the [API Reference](../api/index.md) contains the complete contract.

Your project already has one assigned Stylebook. You do not choose a different
Stylebook for each flow.

## 4. Understand what your edits affect

Before editing, ask whether the change belongs to one story or to the shared
record:

- Fix a wrong extraction, quote attribution, article tag, or story-specific
  place in the Agate processed item.
- Fix a canonical name, alias, maintained geography, metadata value, or
  relationship in Stylebook.

The [Data model](concepts/content-model.md) explains this distinction in more
detail.

## For local development

Developers and technical evaluators can run the source checkout locally. See
the repository's
[Quickstart](https://github.com/localangle/backfield#quickstart) for current
requirements, setup commands, local addresses, and stack operations.

## Next steps

- See one story go from raw text to queryable data in the [Simple Example](simple-example.md)
- Understand how accounts are organized in [Organizations & workspaces](concepts/organizations.md)
- Learn what a [Project](concepts/projects.md) contains
- Learn how article processing works in [Agate](agate/index.md), or how shared
  records are curated in [Stylebook](stylebook/index.md)
- Explore and use project data through [Backfield API](../api/index.md)
- Follow the [Quickstart tutorial](../tutorials/quickstart.md) for a first end-to-end workflow
