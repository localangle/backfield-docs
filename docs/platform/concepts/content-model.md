# Data model

Backfield keeps two related kinds of information:

- **Article evidence** records what appeared in a particular story and what a
  processing flow found there.
- **Canonical knowledge** records what your organization knows about a person,
  organization, or place across many stories.

Keeping these layers separate allows editors to correct one article without
accidentally changing a shared record—or improve a shared record without
rewriting the reporting that supports it.

## From one article to shared knowledge

When an [Agate](../agate/index.md) flow processes an article, it can produce
several kinds of structured data:

```text
Article
├── Basic details and source text
├── Article metadata
├── People, organizations, and locations
│   └── Mentions and supporting evidence
├── Custom records
├── Images
└── Embeddings for semantic search
```

If the flow ends with **Backfield Output**, the article and its structured data
are saved in the project. Its people, organizations, and locations can then be
linked to shared canonical records in the project's
[Stylebook](../stylebook/index.md):

```text
Canonical entity
├── Names, aliases, and identifying details
├── Mentions from linked articles
├── Editor-maintained metadata
├── Geography, when relevant
└── Connections to other canonical entities
```

A flow result is not automatically part of this stored model. **JSON Output**
can leave results available for inspection without saving an article or
linking entities to Stylebook. See [Output nodes](../agate/nodes/outputs.md).

## The main records

| Record | What it represents | Scope |
| --- | --- | --- |
| **Article** | A story or document, including its text, headline, byline, publication date, source identifiers, and other basic details | Project |
| **Article metadata** | Classifications that apply to the article as a whole, such as topic, format, subject, scope, timeframe, user need, and custom categories | Project |
| **Article entity** | One person, organization, or location as represented in one article, including story-specific context | Project |
| **Mention** | One textual reference to an article entity, tied to the passage that supports it | Project |
| **Custom record** | A project-defined structure extracted from an article, such as an event, inspection, or recipe | Project |
| **Image** | An image associated with an article, including available source information, captions, and generated descriptions | Project |
| **Embedding** | A machine-readable representation used to compare articles or images by meaning | Project |
| **Canonical entity** | The durable Stylebook identity for a real-world person, organization, or location | Stylebook |
| **Canonical metadata and geography** | Editor-maintained reference information about a canonical entity | Stylebook |
| **Connection** | A directional relationship between two canonical entities, optionally supported by article evidence | Stylebook |

Workspaces help people find projects, but they do not create another copy of
the article data. Projects own article evidence. Stylebooks belong to the
organization and can be shared by several projects.

## Entities, mentions, and canonicals

An **article entity**, a **mention**, and a **canonical entity** describe
different levels of the same reporting:

- An article entity says that a particular person, organization, or place
  appears in one article. It can record story-specific context, such as whether
  a person was quoted or what role an organization played.
- A mention is one occurrence of that entity in the source material. One
  article entity may have several mentions—for example, a full name in the
  opening paragraph, a surname later, and a quoted passage near the end.
- A canonical entity is the shared Stylebook identity to which article
  entities from many stories can link.

A mayor covered in fifty articles may therefore have fifty article entities
and many more mentions, but ideally one canonical person in Stylebook. The
mentions remain traceable to their source articles even though they point to a
shared identity. See [Mentions & evidence](../stylebook/mentions.md).

## How article entities become canonical knowledge

When Backfield Output saves an extracted person, organization, or location,
[canonicalization](../stylebook/canonicalization.md) determines what happens:

- link it to an existing canonical record;
- create a new canonical record when policy allows; or
- place it in a candidate queue when an editor needs to decide.

Linking an article entity does not replace the canonical record's maintained
fields with the latest extraction. It adds article evidence to the shared
identity. Custom records and images remain attached to articles and do not
become additional canonical entity types.

## Article facts and canonical facts

Some information can look similar while belonging to different layers.

**Article metadata** classifies a story as a whole. It includes categories such
as topic, format, subject, scope, timeframe, user need, critical information
need, and newsroom-defined values. A flow may also retain a rationale and
confidence score for editorial review.

**Canonical metadata** describes a shared person, organization, or location.
Examples include a person's title or affiliation, an organization's type, or
reference information your editors maintain.

Geography follows the same distinction. An article can contain a geocoded
place as it was understood in that story, while the canonical location keeps
the maintained coordinates or geometry used across the Stylebook.

Changing an article's topic, mention role, or story-specific geography does not
change the canonical entity. Changing canonical metadata or geography does not
rewrite the articles linked to it.

## Connections

[Connections](../stylebook/connections.md) relate canonical entities to one
another—for example, a person who works for an organization or an organization
based in a location. A connection has direction and may be:

- maintained manually as editorial knowledge; or
- inferred from reporting and supported by project and article evidence.

Connections belong to the Stylebook knowledge graph. Their supporting evidence,
when present, still points back to the project and article from which it came.

## Original, reviewed, and stored results

Each processed item begins with the output produced by its Agate flow. Editor
corrections are saved as a separate review layer, which Agate combines with the
original result to produce **reviewed output**. This preserves the distinction
between what automation produced and what a person changed.

Edits in a [processed item](../agate/processed-items.md) apply to that article's
results and, where supported, its stored evidence. They do not silently change
the linked canonical record. Canonical names, metadata, geography, and
connections remain authoritative in Stylebook.

Rerunning an item creates a new result from the flow settings stored with its
original run and clears that run-local review layer. When Backfield Output
saves an article that already exists, its reconciliation policy determines how
new machine-generated results are combined with stored data while preserving
supported editorial changes.

## Where the model appears

- **Agate** presents each flow result as a processed item, where editors can
  compare structured results with the source and make article-level
  corrections.
- **Stylebook** groups evidence under canonical people, organizations, and
  locations, and provides tools for metadata, geography, connections,
  candidates, and catalog review.
- **Backfield API** exposes project-scoped
  [articles](../../api/articles/index.md),
  [mentions](../../api/mentions/index.md), and
  [entities](../../api/entities/index.md), including links to canonical
  identities where available.

!!! note "Article metadata"
    The predefined article classification categories are listed in
    [Article Meta](../../api/taxonomy/article-meta/index.md).
