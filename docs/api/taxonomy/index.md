# Metadata

Agate generates metadata at several levels.

At the **Article** level, Agate can generate arbitrary metadata, including classifications for subject, topics, user needs and more. Some of these are available as presets in Agate enrichment nodes. Others can be defined by the user.

At the **Mention** level, Agate uses a preset taxonomy to classify a number of attributes, such as the nature of the mention (is it central to the story vs. just context, etc.) and whether it is a direct quote. These taxonomies are fixed.

At the **Entity** level, Stylebook uses fixed taxonomies to identify the type of
entity (for example, a politician versus a community member) and typed scalar
attributes editors maintain on canonical records. Connections between entities
also have their own edge labels, known as the "nature" of a connection.

## Three families


| Family           | What it describes                            | Where it appears                                          | Reference                             |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- | ------------------------------------- |
| **Article Meta** | Story format, broad topics, concrete subject | `metadata[]` on articles; article-metadata filters        | [Article Meta](article-meta/index.md) |
| **Mention Meta** | Editorial role of an entity **in one story** | Mention and hub responses; mention/entity article filters | [Mention Meta](mention-meta/index.md) |
| **Entity Meta**  | People, organization and place types; typed canonical attributes | Canonical records; mention rows; entity search filters    | [Entity Meta](entity-meta/index.md)   |


## Discover values in your project

Often the best place to start is to discover the metadata values available in your project. These endpoints can help:

| You need | Endpoint | Doc |
| --- | --- | --- |
| Metadata types and values in project data | `GET …/articles/metadata/types`, `GET …/articles/metadata/types/{meta_type}/values` | [Article Meta](article-meta/index.md) |
| Article search filter UI in one call | `GET …/articles/facets` | [Article facets](../articles/facets.md) |
| Mention search filter UI in one call | `GET …/mentions/facets` | [Mention facets](../mentions/facets.md) |
| `person_type` in Stylebook | `GET …/people/types` | [People types](../people/types.md) |
| `organization_type` in Stylebook | `GET …/organizations/types` | [Organizations types](../organizations/types.md) |
| `location_type` in Stylebook | `GET …/locations/types` | [Locations types](../locations/types.md) |

[Article facets](../articles/facets.md) and [Mention facets](../mentions/facets.md) are convenience wrappers — one response with the filter values frontend applications typically need. Use the `…/metadata/types` routes or entity types endpoints when you need finer-grained or type-specific discovery.

Advanced metadata filtering uses **`meta`** clauses on every article-metadata filter endpoint — [List and search](../articles/search.md), [Semantic search](../articles/semantic-search.md), [Geographic search](../articles/geo-search.md), [Geo cells](../other/geo-cells/index.md), and [List and search mentions](../mentions/search.md). See [Article Meta](article-meta/index.md#querying-with-meta) for grammar and transport (GET query params vs POST JSON array).


## Quick filter map

Once you know your available metadata values, you can use them to search for articles using filters like the ones below.


| Filter parameter | Metadata page |
| --- | --- |
| `meta` (repeatable on article-metadata filter endpoints) | [Article Meta](article-meta/index.md) |
| `nature` (on mentions) | [Mention Meta](mention-meta/index.md) |
| `person_type`                                  | [Entity Meta → People](entity-meta/people.md)                 |
| `organization_type`                            | [Entity Meta → Organizations](entity-meta/organizations.md)   |
| `location_type`                                | [Entity Meta → Locations](entity-meta/locations.md)           |

## Canonical attributes

Stylebook stores one typed scalar value per attribute key on each canonical
person, organization, or location. Each attribute has `meta_type`, `value_type`
(`text`, `number`, or `boolean`), and `value`.

Entity **detail** responses always include a `metadata` array. **List**,
**search**, and **geo-search** responses include `metadata: []` unless you pass
`include=metadata`.

Filter canonical lists with repeatable **`attr`** query parameters (distinct from
article **`meta`** filters). Forms:

| Form | Meaning |
| --- | --- |
| `key` | Attribute exists |
| `!key` | Attribute missing |
| `key:value` | Equals |
| `key:op:value` | Compare with `eq`, `neq`, `ieq`, `ineq`, `lt`, `lte`, `gt`, or `gte` |

Use `|` within an `eq` or `ieq` value for OR; repeated `attr` clauses combine
with AND. Examples: `party`, `!party`, `party:Democrat`,
`population:gt:100000`, `party:eq:Democrat|Independent`.

See [Get person](../people/get-person.md), [List and search people](../people/search.md), and the matching organization and location routes.


## Related

- [Articles overview](../articles/index.md)
- [Mentions overview](../mentions/index.md)
- [Entities overview](../entities/index.md)

