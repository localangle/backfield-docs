# Stylebook

Stylebook is your newsroom's shared catalog of the people, organizations, and
places in its reporting. [Agate](../agate/index.md) finds them article by
article; Stylebook connects those findings to records your newsroom can
maintain and reuse.

## Mentions and canonical records

The key distinction is between a **mention** and a **canonical record**:

- A **mention** is one reference to something in one article — "Mayor Jane Doe" appearing in last Tuesday's story.
- A **canonical record** represents the real-world person, organization, or
  place — *the* Jane Doe — to which those mentions point.

A person mentioned in a hundred articles should usually have one canonical
record, not a hundred near-duplicates.

The canonical record holds shared details, metadata, geography, and
connections. Each mention remains tied to the project, article, and passage
that produced it.

## What you can do in Stylebook

- Find and filter canonical people, organizations, and locations.
- Review the article mentions linked to each record.
- Correct names, aliases, metadata, and location geography.
- Add relationships between records, such as a person working for an
  organization.
- Resolve uncertain matches and review possible duplicates.

## How records get into the catalog

There are three ways an entity ends up in Stylebook:

1. **From reporting.** When an Agate flow saves its results,
   [canonicalization](canonicalization.md) links each extracted entity to a
   known record, creates a record when appropriate, or asks an editor to
   decide.
2. **By hand.** Editors can create records directly.
3. **By import.** Editors can load records from spreadsheets or geographic
   files. Administrators can also copy supported records from another
   Stylebook. See [Import & export](import-export.md).

## Two kinds of review

- **Candidate queues** contain article entities that are not yet linked to a
  canonical. Editors can link an existing record, create a new one, or defer
  the decision.
- **Stylebook Review** checks existing canonical records for possible
  duplicates, questionable records, mismatches, and geography-quality issues.
  Editors decide whether to merge, keep, remove, or dismiss the flagged items.

Candidate queues combine work from all accessible projects assigned to the
Stylebook and identify which project produced each item.

Some screens offer AI suggestions. These remain suggestions until an editor
accepts them.

The **Recent** view helps editors follow additions, links, merges, and review
decisions. It is an activity feed, not a backup or undo history.

## More than one Stylebook

An organization can keep more than one Stylebook — for example, separate
catalogs for different publications or intentionally separate reference sets —
with one designated as the default. Each project is assigned one Stylebook when
created. See [Managing Stylebooks](stylebooks.md).

## In this section

| Page | What it covers |
| --- | --- |
| [Entity types](entity-types.md) | The kinds of records you can catalog |
| [Managing Stylebooks](stylebooks.md) | Creating, sharing, and administering catalogs |
| [Canonicalization](canonicalization.md) | How article entities are linked, created, or sent for review |
| [Mentions & evidence](mentions.md) | The article references behind each record |
| [Metadata](meta.md) | Editor-maintained facts |
| [Connections](connections.md) | Relationships between entities |
| [Geography](geography.md) | Locations on a map |
| [Import & export](import-export.md) | Bulk loading records and copying supported Stylebook content |
