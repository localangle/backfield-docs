# Shared content store

Both Backfield apps work over a common pool of data we call the **shared content store**. It's the connective tissue between [Agate](../agate/index.md) and [Stylebook](../stylebook/index.md): Agate writes to it, Stylebook organizes part of it, and the [Public API](../../api/index.md) serves it to your applications.

Understanding this shared layer explains why the same article, person, or place shows up consistently across the whole product.

## What's in it

| Thing | What it is |
| --- | --- |
| **Articles** | The stories and documents you process, plus their text and basic details (headline, author, publication date, source) |
| **Mentions** | Each time a person, organization, or place is referred to in an article — with the exact passage it came from |
| **Metadata** | Topic and format tags applied to articles (for example, a subject category) |
| **Extracted records** | Other structured details a flow pulls out, including custom record types you define |

Think of it as the raw, article-by-article record of *what was found and where*. [Stylebook](../stylebook/index.md) then sits on top of this, merging repeated mentions of the same real-world thing into clean **canonical** records.

## Articles vs. catalog entries

It's worth being precise about two related ideas:

- An **article** is a piece of content. It carries mentions and metadata, but it is not itself a "person" or "place."
- A **canonical entity** (a specific person, organization, or location in Stylebook) is the deduplicated, master record that many article mentions point to.

So a single politician mentioned in fifty articles produces fifty **mentions** but ideally one **canonical** person in the catalog. The shared content store holds the mentions; Stylebook holds the canonical record and the link between them. See [Mentions & evidence](../stylebook/mentions.md).

## Where you encounter it

- In Agate, after a run, the extracted details for each article appear as a [processed item](../agate/processed-items.md) you can review.
- In Stylebook, mentions are grouped under the canonical people, places, and organizations they refer to.
- Through the API, you can search [articles](../../api/articles/index.md), explore [mentions](../../api/mentions/index.md), and retrieve [entities](../../api/entities/index.md).

!!! note "Article metadata"
    The standard topic and format categories used for article tagging are listed in [Article Meta](../../api/taxonomy/article-meta/index.md).
