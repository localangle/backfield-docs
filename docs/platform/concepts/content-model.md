# Data model

Backfield turns the articles you process into a few simple, connected building
blocks. Understanding them explains why the same article, person, or place
shows up consistently across [Agate](../agate/index.md),
[Stylebook](../stylebook/index.md), and
[Backfield API](../../api/index.md).

## The building blocks

| Thing | What it is |
| --- | --- |
| **Articles** | The stories and documents you process, plus their text and basic details (headline, author, publication date, source) |
| **Mentions** | Each time a person, organization, or place is referred to in an article — with the exact passage it came from |
| **Article entities** | The people, places, and organizations found in one article, including their article-specific fields and mentions |
| **Canonical entities** | Durable Stylebook records that identify the same real-world person, place, or organization across articles |
| **Metadata** | Article-level tags such as topic, format, subject, scope, timeframe, user need, and custom categories |
| **Custom records** | Project-defined structured records, such as events or recipes, extracted from an article |
| **Images** | Images attached to an article, including captions and generated descriptions when a flow creates them |

Together these form the article-by-article record of *what was found and
where*. [Stylebook](../stylebook/index.md) connects that evidence to clean
canonical identities.

## Article entities, mentions, and canonicals

These three ideas are related but not interchangeable:

- An **article entity** says that a particular person, organization, or place
  appears in this article. It can carry story-specific context, such as whether
  a person was quoted or what role an organization played.
- A **mention** is the supporting reference in the text. One article entity may
  have several mentions if the same person appears repeatedly.
- A **canonical entity** is the Stylebook identity that article entities from
  many stories can link to.

So a politician covered in fifty articles may have fifty article-level records
and many more textual mentions, but ideally one canonical person in Stylebook.
The story evidence remains project-scoped; the canonical identity can be shared
by every project assigned to that Stylebook. See
[Mentions & evidence](../stylebook/mentions.md).

## Article metadata vs. Stylebook metadata

Backfield uses “metadata” in two places:

- **Article metadata** classifies a story as a whole: topic, format, subject,
  scope, timeframe, user need, critical information need, or a custom category.
- **Stylebook metadata** records editor-maintained information about a
  canonical person, organization, or location.

Changing an article's topic does not change a canonical person. Changing a
canonical person's metadata does not rewrite the articles where that person
appeared.

## Original output and reviewed output

Agate preserves what a flow originally produced. Editor corrections are stored
as a review layer and combined with the original to form reviewed output. This
lets a newsroom see what automation did, what a person changed, and which
version should be exported.

Edits made on a processed item apply to that article's evidence. Canonical
fields remain authoritative in Stylebook.

## Where this shows up

- In Agate, after a run, the extracted details for each article appear as a [processed item](../agate/processed-items.md) you can review.
- In Stylebook, mentions are grouped under the canonical people, places, and organizations they refer to.
- Through the API, you can search [articles](../../api/articles/index.md), explore [mentions](../../api/mentions/index.md), and retrieve [entities](../../api/entities/index.md).

!!! note "Article metadata"
    Predefined article tagging categories are listed in [Article Meta](../../api/taxonomy/article-meta/index.md).
