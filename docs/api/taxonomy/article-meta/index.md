# Article Meta

Article metadata is defined using `meta_type` keys that are paired with corresponding `category` values. Tags appear in article `metadata[]` and power metadata filters on every article-metadata filter endpoint.

## Meta types

Meta types can be defined arbitrarily by the user in Agate, which means the best place to start is often the discovery endpoints. But there are several preset metadata values that are commonly extracted in Agate flows. Among them:

| `meta_type` | Meaning                                                       | Reference             |
| ----------- | ------------------------------------------------------------- | --------------------- |
| `format`    | Story type or structural form                                 | [Format](format.md)   |
| `topic`     | Broad topic areas (what the story is about)                   | [Topic](topic.md)     |
| `subject`   | Concrete primary subject (the central thing the story covers) | [Subject](subject.md) |

## Querying with `meta`

Use the repeatable **`meta`** parameter for advanced metadata filtering on any endpoint that filters by article metadata. Provide one clause per value; all clauses are combined with **AND**.

Each `meta` value is one clause:

| Form | Meaning |
| --- | --- |
| `type` | Article has at least one tag of this metadata type (any category) |
| `type:category` | Article has this exact type + category |
| `type:cat1\|cat2\|cat3` | Article has this type with **any one** of the listed categories (OR within the type) |
| `!type` | Article must **not** have any tag of this type |
| `!type:category` | Article must **not** have this exact type + category |

Prefix with `!` to negate. The `|` character means OR **only within a single clause** — there is no cross-type OR.

To require **all** of several categories of the same type, repeat the type:

```text
meta=topic:pro_sports&meta=topic:analysis
```

Unknown types or categories match nothing (no error).

### Transport

How you send `meta` depends on the endpoint:

| Transport | Endpoints | Example |
| --- | --- | --- |
| **GET** — repeat `meta` as a query parameter | [List and search](../../articles/search.md), [Geographic search](../../articles/geo-search.md), [Coverage](../../other/geo-cells/coverage.md), [List articles (geo cell)](../../other/geo-cells/list-articles.md), [List and search mentions](../../mentions/search.md) | `?meta=topic:pro_sports&meta=!format:opinion` |
| **POST** — `meta` as a JSON string array | [Semantic search](../../articles/semantic-search.md), [Batch query (geo cells)](../../other/geo-cells/query.md) | `"meta": ["topic:pro_sports", "!format:opinion"]` |

On mention and geo routes, `meta` filters apply to the **article** that contains each mention or location — not to mention tags themselves.

### Worked example

Factual game previews and recaps — pro sports coverage of a specific contest, without explainer or analysis pieces:

```text
?meta=topic:pro_sports
 &meta=subject:sports_contest
 &meta=!format:explainer_analysis
```

The same clauses in a POST JSON body:

```json
"meta": ["topic:pro_sports", "subject:sports_contest", "!format:explainer_analysis"]
```

URL-encode `|` as `%7C` in GET query strings.

### Limits

- Max **25** `meta` clauses per request
- Max **50** categories per clause (the part after `:`)

Malformed clauses (empty type, trailing `:`, empty category in a list) return `400`.

## Discover values in your project

Projects may not use every category. Discover values with [Article facets](../../articles/facets.md) or the metadata types routes:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/metadata/types/topic/values" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

| Discovery | Filter clause |
| --- | --- |
| [Article facets](../../articles/facets.md) `format_categories` | `meta=format:…` — see [Format](format.md) |
| [Article facets](../../articles/facets.md) `topic_categories` or `…/metadata/types/topic/values` | `meta=topic:…` — see [Topic](topic.md) |
| [Article facets](../../articles/facets.md) `subject_categories` or `…/metadata/types/subject/values` | `meta=subject:…` — see [Subject](subject.md) |

Also available:

- `GET …/articles/metadata/types` — metadata types present in the project
- `GET …/articles/metadata/types/{meta_type}/values` — categories for one type

## Related

- [Metadata overview](../index.md)
- [List and search](../../articles/search.md)
- [Semantic search](../../articles/semantic-search.md)
- [Geographic search](../../articles/geo-search.md)
- [Geo cells](../../other/geo-cells/index.md)
- [List and search mentions](../../mentions/search.md)
