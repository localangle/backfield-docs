# Platform

Backfield helps newsrooms turn unstructured reporting — articles, documents, and other text — into structured, searchable information: the people, organizations, and places that stories are about, plus the relationships between them.

You work with Backfield through two connected apps:

- **[Agate](agate/index.md)** is where you build and run the pipelines that read your text and pull out structured details.
- **[Stylebook](stylebook/index.md)** is where that extracted information becomes a clean, deduplicated reference catalog your team can trust and reuse.

Everything the two apps produce lands in a [shared content store](concepts/content-store.md) — the common pool of articles and extracted details that both apps read from, and that the [Public API](../api/index.md) serves to your own tools.

## The two apps at a glance

| | Agate | Stylebook |
| --- | --- | --- |
| **Think of it as** | The assembly line | The reference desk |
| **You use it to** | Build pipelines, run them on your text, review the results | Curate the master list of people, places, and organizations |
| **Core idea** | A **flow** that runs on your articles | A **canonical** record that many mentions point to |
| **Who spends time here** | People setting up extraction and checking output | Editors keeping the catalog accurate |

## How a story moves through Backfield

1. You feed text into an **Agate flow**.
2. The flow extracts details — places, people, organizations, topics — and saves each result as a **processed item** you can review and correct.
3. Confirmed details flow into **Stylebook**, where repeated mentions of the same real-world person or place are merged into a single **canonical** record.
4. Your own applications read the finished data through the **Public API**.

## Where to start

| If you want to… | Go to |
| --- | --- |
| Set up Backfield locally | [Getting Started](getting-started.md) |
| Understand how accounts and projects are organized | [Organizations & workspaces](concepts/organizations.md) |
| Learn what a project contains | [Projects](concepts/projects.md) |
| Understand the data both apps share | [Shared content store](concepts/content-store.md) |
| Build a pipeline | [Agate](agate/index.md) |
| Curate your catalog | [Stylebook](stylebook/index.md) |
| Configure models, integrations, and keys | [Settings](settings/index.md) |
| Query your data from code | [API Reference](../api/index.md) |

!!! note "Work in progress"
    The platform is under active development. These pages explain the concepts and vocabulary; some sections are still being filled in.
