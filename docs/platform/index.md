# Platform

Backfield helps newsrooms turn narrative articles into durable, structured data that can be used to create new products, generate new insights and better transact in the AI economy.

You work with Backfield through two connected apps:

- **[Agate](agate/index.md)** is where you build and run composable pipelines that enrich articles with data — and allow editors to verify that data and clean it up.
- **[Stylebook](stylebook/index.md)** is where that data is consolidated into a clean, deduplicated canonical entity store that editorial teams can manage and build on.

The data from both tools is available via a [Public API](../api/index.md) that can be used to power your own tools and services.

## The two apps at a glance

| | Agate | Stylebook |
| --- | --- | --- |
| **Think of it as** | The assembly line | The reference desk |
| **You use it to** | Build pipelines, run them on your articles, review the results | Curate a master list of entities, such as people places, and organizations, and manage information about them |
| **Core idea** | A **flow** that runs on your articles | A **canonical** record that many mentions point to |
| **Who spends time here** | Administrators setting up extraction flows; optionally editors and reporters checking output | Editors enriching the catalog or keeping it accurate |

## How a story moves through Backfield

1. You feed text into an **Agate flow**.
2. The flow extracts details — places, people, organizations, topics — and saves each result as a **processed item** you can optionally review and correct.
3. Confirmed details flow into **Stylebook**, where repeated mentions of the same real-world person or place are merged into a single **canonical** record that can be enriched with metadata or connected to others.
4. Your own applications read the finished data through the **Public API**.

## Where to start

| If you want to… | Go to |
| --- | --- |
| Set up Backfield locally | [Getting Started](getting-started.md) |
| See one story go end to end | [Simple Example](simple-example.md) |
| Understand how accounts and projects are organized | [Organizations & workspaces](concepts/organizations.md) |
| Learn what a project contains | [Projects](concepts/projects.md) |
| Understand how Backfield models your data | [Data model](concepts/content-model.md) |
| Build a pipeline | [Agate](agate/index.md) |
| Curate your catalog | [Stylebook](stylebook/index.md) |
| Configure models, integrations, and keys | [Settings](settings/index.md) |
| Query your data from code | [API Reference](../api/index.md) |
