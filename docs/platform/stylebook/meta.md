# Metadata

**Metadata** (shown as **Meta** in Stylebook) is the set of editor-maintained facts you attach to a canonical record — details that aren't extracted from any single article but that your team wants to keep on file. For a person that might be a title or affiliation; for an organization, a category or identifier.

Metadata belongs to the canonical record and applies across the whole catalog, independent of any one article [mention](mentions.md).

## What belongs in Meta

Use Meta for stable, editor-maintained information that helps people understand
or classify the canonical record. Examples include:

- a person's current title, affiliation, public-figure status, or person type;
- an organization's type or newsroom identifier;
- a location's type and other reference attributes.

The exact fields differ by entity type. Some prominent fields appear in the
record's main Details section, while additional structured values appear under
Meta.

Each Meta item has a metadata type and a value. Simple, flat values can be
edited in a table; more complex structured data can be reviewed as JSON.
Editors can add, change, or remove these items from the canonical detail page.

## What does not belong in Meta

Article-specific facts belong to the article entity or mention. A person's role
as a quoted source in one story, for example, should remain with that story's
evidence rather than becoming a permanent canonical fact.

Article classifications such as topic, format, subject, or user need are also a
different kind of metadata. They are reviewed in Agate and apply to the article
as a whole. See [Data model](../concepts/content-model.md#article-metadata-vs-stylebook-metadata).

## Scope and editing

Canonical metadata is Stylebook-wide. If several projects share the Stylebook,
an editor's change is visible wherever that canonical is used. Project filters
on a detail page narrow mentions and evidence; they do not create separate
versions of the canonical metadata.

Treat canonical metadata as maintained reference information. Prefer clear,
current values and use [connections](connections.md) when the information is
really a relationship to another canonical record.
