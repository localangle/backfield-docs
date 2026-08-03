# Backfield

Backfield helps news organizations turn articles and reporting materials into
durable, structured data. Instead of treating every story as a block of text,
Backfield organizes it into entities, metadata, and relationships that can
support new products, services, and understanding.

The Backfield platform consists of three interconnected applications:

- **[Agate](agate/index.md)** lets users create customizable workflows that
  turn articles into structured data and gives editors a place to verify
  article-level results.
- **[Stylebook](stylebook/index.md)** cleans, standardizes and enriches the
  entities found across your reporting.
- **[Backfield API](../api/index.md)** makes the resulting data available for
  queries by location, entity, keyword, or meaning — and for products, services,
  tools, and story forms your organization builds.

Agate and Stylebook are primarily editorial interfaces. Backfield API is the
application-facing part of the same platform: it turns the structured and
curated work into something other tools and services can use.

## The three apps at a glance

| | Agate | Stylebook | Backfield API |
| --- | --- | --- | --- |
| **Think of it as** | The processing workspace | The reference desk | The delivery layer |
| **You use it to** | Build flows, process articles, and review results | Maintain canonical people, organizations, locations, and their relationships | Query structured data and power products, services, tools, and story forms |
| **Core idea** | A **flow** that runs on articles | A **canonical record** that many mentions can point to | A project-scoped interface to Backfield data |
| **Who uses it** | Flow builders and editors | Editors maintaining shared knowledge | Developers, data teams, and applications |

## How a story moves through Backfield

1. You feed text into an **Agate flow**.
2. The flow enriches the article, leaving behind a **processed item**. Editors
   can compare enrichments and extracted entities with the source text and
   correct article-specific mistakes.
3. Confirmed entity data flows into the project's assigned **Stylebook**.
   Repeated references to the same real-world person, organization, or place
   can point to one shared **canonical** record.
4. **Backfield API** exposes the saved data so your own applications can
   retrieve, search, and combine it.

## A useful mental model

Backfield separates what a story said from what your newsroom knows:

- **Processed items** belong to a project. They include the story itself, its
  extracted and enriched data, and the editor's additions and corrections.
- **Canonical knowledge** belongs to a Stylebook. It includes the durable
  identity, metadata, geography, and connections your newsroom maintains
  across stories.
- **Programmatic access** comes through Backfield API. It lets other systems
  use project data without turning the API into a separate source of truth.

This distinction determines where to make a correction. Fix a mistaken
extraction in the Agate processed item. Edit a person's newsroom-wide title,
aliases, or relationships on the canonical record in Stylebook.

## How the platform is organized

An **organization** is the top-level account. It contains **workspaces**, which
group related **projects**. Each project is assigned one Stylebook, and a
Stylebook may be shared by several projects in the same organization.

See [Organizations & workspaces](concepts/organizations.md),
[Projects](concepts/projects.md), and [Users & access](concepts/users.md) for
the boundaries that control navigation, settings, and editing rights.

## Where to start

| If you want to… | Go to |
| --- | --- |
| Get oriented on your first visit | [Getting Started](getting-started.md) |
| See one story go end to end | [Simple Example](simple-example.md) |
| Understand how accounts and projects are organized | [Organizations & workspaces](concepts/organizations.md) |
| Learn what a project contains | [Projects](concepts/projects.md) |
| Understand how Backfield models your data | [Data model](concepts/content-model.md) |
| Process and review articles | [Agate](agate/index.md) |
| Curate shared reference knowledge | [Stylebook](stylebook/index.md) |
| Search data or power another product | [Backfield API](../api/index.md) |
| Configure models, integrations, and keys | [Settings](settings/index.md) |
