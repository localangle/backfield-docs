# Stylebook

Stylebook is your newsroom's reference catalog — the authoritative, deduplicated list of the people, organizations, and places that appear in your reporting. Where [Agate](../agate/index.md) finds details article by article, Stylebook turns those scattered findings into clean, trustworthy records you can reuse.

## The core idea: canonicals and mentions

The single most important concept in Stylebook is the difference between a **mention** and a **canonical**.

- A **mention** is one reference to something in one article — "Mayor Jane Doe" appearing in last Tuesday's story.
- A **canonical** is the master record for the real-world thing — *the* Jane Doe — that all of those mentions point to.

A person mentioned in a hundred articles should be **one** canonical record with a hundred mentions attached — not a hundred near-duplicates. Keeping that mapping clean is what Stylebook is for.

## What Stylebook keeps for each entity

| Part | What it is |
| --- | --- |
| **[Entity types](entity-types.md)** | The kinds of things you catalog — locations, people, organizations (and more over time) |
| **[Mentions & evidence](mentions.md)** | Every article reference to the entity, with the quoted passage it came from |
| **[Metadata](meta.md)** | Editor-maintained facts about the entity (its "Meta") |
| **[Connections](connections.md)** | Relationships between entities — who works for what, what's located where |
| **[Geography](geography.md)** | For locations: coordinates and shapes on a map |

## How records get into the catalog

There are three ways an entity ends up in Stylebook:

1. **From your reporting.** When an Agate flow saves its results, it tries to match each extracted person or place to an existing canonical. This matching step is called **[canonicalization](canonicalization.md)** — it either links to a known record, proposes a new one, or sets the item aside for an editor to decide.
2. **By hand.** Editors can create records directly.
3. **By import.** You can bulk-load records from spreadsheets or geographic files, or copy a whole catalog between organizations. See [Import & export](import-export.md).

Items that need a human decision land in a **candidate** queue, where editors confirm matches, create new records, or merge duplicates.

## Multiple catalogs

An organization can keep more than one Stylebook — for example, separate catalogs for different desks or datasets — with one designated as the default. See [Stylebooks & the library](stylebooks.md).

## In this section

| Page | What it covers |
| --- | --- |
| [Entity types](entity-types.md) | The kinds of records you can catalog |
| [Stylebooks & the library](stylebooks.md) | Managing one or more catalogs |
| [Canonicalization](canonicalization.md) | How mentions get matched and merged into canonical records |
| [Mentions & evidence](mentions.md) | The article references behind each record |
| [Metadata](meta.md) | Editor-maintained facts |
| [Connections](connections.md) | Relationships between entities |
| [Geography](geography.md) | Locations on a map |
| [Import & export](import-export.md) | Bulk loading and transferring catalogs |
