# Metadata

**Metadata**, shown as **Meta** in Stylebook, enriches a canonical record with
structured information your newsroom wants to maintain. It can describe almost
anything useful about a person, organization, or location.

Metadata belongs to the shared canonical record, not to any one article
[mention](mentions.md). Once added, it can be used wherever that Stylebook
record appears.

## What belongs in Meta

The fields are defined by your newsroom and can vary by entity type. Examples
include:

- a person's political party, current title, affiliation, or public-figure
  status;
- an organization's type, jurisdiction, size, or newsroom identifier;
- a town's population, demographics, or other civic data;
- any other maintained category or value that makes the record more useful.

Some common fields appear under **Details** and others under **Meta**. Metadata
can be added or curated by editors, or included when canonical records are
imported.

## What metadata makes possible

Metadata turns a record from an identity into a richer source of information.
It allows newsroom tools and queries to combine what an entity *is* with what
appeared in reporting.

For example, if canonical people include political-party metadata, a newsroom
could ask:

> Show me all quotes by Republicans about issue X.

That question combines maintained information about people with article
evidence about quotes and issues. Similar combinations can support source
audits, geographic analysis, directories, election products, and other
newsroom uses.

## What does not belong in Meta

Article-specific facts belong to the article entity or mention. A person's role
as a quoted source in one story, for example, should remain with that story's
evidence rather than becoming a permanent canonical fact.

Article classifications such as topic, format, subject, or user need apply to
the article as a whole and are reviewed in Agate. See
[Data model](../concepts/content-model.md#article-facts-and-canonical-facts).

## Scope and editing

If several projects share a Stylebook, a metadata change is visible wherever
that canonical record is used. Project filters narrow the mentions shown; they
do not create project-specific metadata.

Metadata requires editorial maintenance. Population figures change, political
affiliations change, and categories may need clearer definitions over time.
The richer the metadata, the more powerful the catalog becomes—but the more
important ownership, sourcing, and regular review become.

Use [connections](connections.md) when the information is really a
relationship to another canonical record rather than a property of this one.

!!! note "Active development"
    Canonical metadata is an area of active development. The available editing,
    import, and query tools will continue to expand.
