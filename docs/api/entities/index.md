# Entities

Entities are canonical records for people, places, and organizations identified across project articles. Entity endpoints let you search the catalog, retrieve detail, and explore mention evidence and Stylebook connections — starting from the entity rather than from a single article.

## Entity types

| Entity | Status | Overview |
| --- | --- | --- |
| **People** | ✅ Available | [People](../people/index.md) — get, list and search, mentions, connections |
| **Locations** | ✅ Available | [Locations](../locations/index.md) — get, list and search, geographic search, mentions, connections |
| **Organizations** | ✅ Available | [Organizations](../organizations/index.md) — get, list and search, mentions, connections |

## Shared pattern

Each entity type follows the same structure:

| Endpoint type | Use when |
| --- | --- |
| **Detail** | Show one canonical record |
| **List and search** | Find records by name, type, or filters |
| **Mentions** | Load paginated mention evidence |
| **Articles** | Load paginated stories mentioning the entity |
| **Connections** | Load Stylebook relationships |

Entity ids are UUID strings. Canonical records include a `stylebook_slug` identifying which Stylebook catalog they belong to. List, detail, and geographic search responses include **`counts`** with project-scoped **`mentions`** and **`stories`** totals.

For `person_type`, `organization_type`, and `location_type` catalogs, see [Entity Meta](../taxonomy/entity-meta/index.md).

## Article-first vs entity-first

You can reach entity data two ways:

- **Article-first** — start from [Get article](../articles/get-article.md) or [List and search](../articles/search.md) articles, then use [List mentions](../articles/hub/mentions.md) or other [detail endpoints](../articles/hub/index.md).
- **Entity-first** — start from an entity [List and search](../people/search.md) route, open detail, then follow [List articles](../people/list-articles.md), [List mentions](../people/mentions.md), or connections to find related stories.
- **Mention-first** — start from [List and search mentions](../mentions/search.md) to find evidence across articles, then follow to entity or article detail.

Use article-first flows when you already have a story in context. Use entity-first flows when you are building person, place, or organization directories, profile pages, or relationship views.

## Related

- [Articles](../articles/index.md) — article search and [detail endpoints](../articles/hub/index.md)
- [Mentions](../mentions/index.md) — project-wide mention search
