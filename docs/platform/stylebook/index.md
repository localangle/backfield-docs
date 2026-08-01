# Stylebook

Stylebook is your newsroom's reference catalog — the authoritative, deduplicated list of the people, organizations, and places that appear in your reporting. Where [Agate](../agate/index.md) finds details article by article, Stylebook turns those scattered findings into clean, trustworthy records you can reuse.

## The core idea: canonicals and mentions

The single most important concept in Stylebook is the difference between a **mention** and a **canonical**.

- A **mention** is one reference to something in one article — "Mayor Jane Doe" appearing in last Tuesday's story.
- A **canonical** is the master record for the real-world thing — *the* Jane Doe — that all of those mentions point to.

A person mentioned in a hundred articles should be **one** canonical record with a hundred mentions attached — not a hundred near-duplicates. Keeping that mapping clean is what Stylebook is for.

Stylebook separates the newsroom-wide identity from project evidence. Canonical
details, metadata, geography, and connections belong to the Stylebook. Mentions
and article-specific records remain tied to the projects and stories that
produced them.

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

1. **From your reporting.** When an Agate flow saves its results, it tries to
   match each extracted person, organization, or place to an existing
   canonical. This matching step is called
   **[canonicalization](canonicalization.md)** — it either links to a known
   record, creates one when policy allows, or sets the item aside for an editor
   to decide.
2. **By hand.** Editors can create records directly.
3. **By import.** You can bulk-load records from spreadsheets or geographic
   files, or copy the supported people and location records from a downloaded
   Stylebook package. See [Import & export](import-export.md).

## The two editorial work areas

Stylebook has two kinds of review:

- **Candidate queues** resolve article entities that are not yet linked to a
  canonical. Editors can link an existing record, create a new one, or defer
  the decision.
- **Stylebook Review** checks the canonical catalog itself for possible
  duplicates, questionable records, mismatches, and geography-quality issues.
  Editors can merge records, keep them separate, delete empty records, or
  dismiss an issue.

Candidate queues combine work from all accessible projects assigned to the
Stylebook. When more than one project contributes, Stylebook shows the source
project and offers a project filter.

Some review screens can request AI suggestions. These suggestions do not
replace the editorial decision; accepted suggestions use the same link, create,
defer, merge, or dismissal actions available to an editor.

The **Recent** view provides an activity trail for additions, links, merges, and
review decisions. It can be filtered by event type, entity type, and source,
helping editors understand how the Stylebook has changed without treating the
activity feed as a separate copy of the records.

## Multiple catalogs

An organization can keep more than one Stylebook — for example, separate
catalogs for different publications or intentionally separate reference sets —
with one designated as the default. Each project is permanently assigned one
Stylebook when created. See [Stylebooks & the library](stylebooks.md).

## Finding and filtering records

Canonical lists support text search, type filters, minimum mention counts,
sorting, and pagination. People add fields such as public-figure status, title,
and affiliation. A project filter narrows the evidence and mention counts shown
for shared records; it does not turn canonical metadata or connections into
project-specific values.

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
| [Import & export](import-export.md) | Bulk loading records and copying supported Stylebook content |
