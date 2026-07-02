# The content model

Backfield turns the articles you process into a few simple, connected building blocks. Understanding them explains why the same article, person, or place shows up consistently across [Agate](../agate/index.md), [Stylebook](../stylebook/index.md), and the [Public API](../../api/index.md).

## The building blocks

| Thing | What it is |
| --- | --- |
| **Articles** | The stories and documents you process, plus their text and basic details (headline, author, publication date, source) |
| **Mentions** | Each time a person, organization, or place is referred to in an article — with the exact passage it came from |
| **Entities** | Structured data extracted from articles, including people, places, organizations and custom record types you define |
| **Metadata** | Topic and format tags applied to articles (for example, a subject category) |

Together these are the raw, article-by-article record of *what was found and where*. [Stylebook](../stylebook/index.md) sits on top, merging repeated mentions of the same real-world thing into clean **canonical** records.

## Mentions vs. entities

It's worth being precise about two related ideas:

- A **mention** is a single reference to a person, organization, or place in a single article — tied to the exact passage it came from.
- A **canonical entity** (a specific person, organization, or location in Stylebook) is the deduplicated, master record that many mentions point to.

So a single politician mentioned in fifty articles produces fifty **mentions** but ideally one **canonical** person in the catalog. The mentions stay attached to the stories they came from; Stylebook holds the canonical record and the link between them. See [Mentions & evidence](../stylebook/mentions.md).

## Where this shows up

- In Agate, after a run, the extracted details for each article appear as a [processed item](../agate/processed-items.md) you can review.
- In Stylebook, mentions are grouped under the canonical people, places, and organizations they refer to.
- Through the API, you can search [articles](../../api/articles/index.md), explore [mentions](../../api/mentions/index.md), and retrieve [entities](../../api/entities/index.md).

!!! note "Article metadata"
    Several predefined topic and format categories used for article tagging are listed in [Article Meta](../../api/taxonomy/article-meta/index.md).
