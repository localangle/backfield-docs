# List and search articles

```
GET /public/v1/projects/{project_slug}/articles/search
```

Search articles in a project by keyword, metadata tags, and publication date. Returns a paginated list without full body text.

The `q` parameter performs a keyword search over **headline**, **article body text**, and **URL**. Search uses full-text matching with web-style query syntax.

## Path parameters


| Name           | Type   | Description  |
| -------------- | ------ | ------------ |
| `project_slug` | string | Project slug |


## Query parameters


| Name              | Type    | Default | Description                                                                                                                          |
| ----------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `q`               | string  | —       | Keyword match on headline, body text, or URL. Web-style syntax: `"exact phrase"`, `term1 OR term2`, `-exclude`, implicit AND between terms |
| `meta`            | string  | —       | Repeatable metadata filter clause (AND across clauses). See [Metadata filters](#metadata-filters)                                    |
| `author`          | string  | —       | Filter by article byline (case-insensitive exact match)                                                                              |
| `has_mentions`    | string  | —       | Require mentions of `location`, `person`, or `organization`                                                                          |
| `pub_date_from`   | string  | —       | ISO date `YYYY-MM-DD`, inclusive lower bound                                                                                         |
| `pub_date_to`     | string  | —       | ISO date `YYYY-MM-DD`, inclusive upper bound                                                                                         |
| `limit`           | integer | `25`    | Page size (1–100)                                                                                                                    |
| `offset`          | integer | `0`     | Offset for pagination                                                                                                                |
| `include`         | string  | —       | Repeatable include token. Supported: `counts`                                                                                        |


See [Pagination](../conventions/pagination.md) for the shared `items` and `pagination` envelope. Search responses also **echo the effective query filters** at the top level (alongside `items` and `pagination`), consistent with [Semantic search](semantic-search.md) and [Geographic search](geo-search.md).

## Keyword search (`q`)

Full-text search over headline, body, and URL combined. You can use web-style syntax:


| Syntax        | Example              | Meaning                                       |
| ------------- | -------------------- | --------------------------------------------- |
| Implicit AND  | `budget council`     | Both terms must appear                        |
| Quoted phrase | `"city council"`     | Exact adjacent phrase                         |
| OR            | `budget OR spending` | Either term                                   |
| Exclude       | `budget -opinion`    | Must match `budget`, must not match `opinion` |


Semantic (meaning-based) search is a separate endpoint — see [Semantic search](semantic-search.md).

## Metadata filters

Use the repeatable **`meta`** query parameter for metadata filtering. Clause grammar, transport notes, limits, and discovery paths are documented under [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta).

Use [Article facets](facets.md) or `GET …/articles/metadata/types` to discover valid types and categories in your project.

```text
?meta=topic:local_government_politics&meta=!format:opinion
?meta=subject:development_project
?meta=topic:local_government_politics&author=Jane Doe&has_mentions=location
```

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/search\
?q=budget&meta=topic:local_government_politics&meta=\!format:opinion\
&include=counts&pub_date_from=2024-01-01&limit=10" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Response `200`

The response echoes the effective keyword and filter parameters at the top level, then `items` and `pagination`.

Each **`items[]`** row uses the standard article list shape — `id`, `headline`, `url`, `author`, `pub_date`, `source`, `preview`, and `metadata`. Pass `include=counts` to add `counts` and `embedded` on each item. List responses do not include inline `images`; use [Get article](get-article.md) for those.

```json
{
  "q": "budget",
  "meta_type": null,
  "meta_category": null,
  "exclude_meta_type": null,
  "exclude_meta_category": null,
  "author": null,
  "external_source": null,
  "has_mentions": null,
  "pub_date_from": "2024-01-01",
  "pub_date_to": null,
  "items": [
    {
      "id": 1,
      "headline": "City council votes on budget",
      "url": "https://example.com/budget",
      "author": "Jane Doe",
      "pub_date": "2024-03-01",
      "source": {
        "id": "example.com",
        "name": "example.com"
      },
      "preview": "The city council approved a revised budget after…",
      "metadata": [
        {
          "meta_type": "topic",
          "category": "local_government_politics",
          "confidence": 0.92
        }
      ],
      "embedded": true,
      "counts": {
        "mentions": {
          "locations": 1,
          "people": 1,
          "organizations": 1,
          "total": 3
        },
        "entities": {
          "locations": 1,
          "people": 1,
          "organizations": 1,
          "total": 3
        },
        "images": 1,
        "custom_records": {
          "contracts": 1
        }
      }
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 1
  }
}
```

The example above includes `embedded` and `counts` because the request used `include=counts`. Advanced `meta` clauses are applied server-side but are not echoed individually — only legacy `meta_type` / `exclude_*` fields appear in the query echo when used.

### Envelope fields

| Field | Type | Description |
| --- | --- | --- |
| `q` | string \| null | Keyword query after normalization |
| `meta_type` | string \| null | Legacy include metadata type filter |
| `meta_category` | string \| null | Legacy include metadata category filter |
| `exclude_meta_type` | string \| null | Legacy exclude metadata type filter |
| `exclude_meta_category` | string \| null | Legacy exclude metadata category filter |
| `author` | string \| null | Byline filter |
| `external_source` | string \| null | Publication or outlet filter |
| `has_mentions` | string \| null | Required mention type (`location`, `person`, or `organization`) |
| `pub_date_from` | string \| null | Inclusive lower publication date bound |
| `pub_date_to` | string \| null | Inclusive upper publication date bound |
| `items[]` | array | Matching articles |
| `pagination` | object | Pagination envelope |

### Item fields

Each item is an article list row. Core fields match [Get article](get-article.md).

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Article id |
| `headline` | string | Headline |
| `url` | string \| null | Source URL |
| `author` | string \| null | Author |
| `pub_date` | string \| null | Publication date (`YYYY-MM-DD`) |
| `source` | object \| null | Publication or outlet when known |
| `preview` | string \| null | Truncated body snippet (max 280 characters) |
| `metadata` | array | Metadata tags (`meta_type`, `category`, `confidence`) |
| `embedded` | boolean \| null | Present with `include=counts` — `true` when the article has a populated embedding row |
| `counts` | object \| null | Present with `include=counts` — see [Get article](get-article.md#counts-embed-includecounts) |

Results are ordered by relevance when `q` is set, otherwise by `pub_date` descending (nulls last), then `id` descending.

Omit `include=counts` when you do not need `counts` or `embedded` on list items.

## Errors


| Status | When                                                                            |
| ------ | ------------------------------------------------------------------------------- |
| `400`  | Invalid `pub_date_from` or `pub_date_to` format                                 |
| `400`  | Unknown `include` token                                                         |
| `400`  | Malformed `meta` clause (empty type, trailing `:`, empty category, and similar) |
| `400`  | More than 25 `meta` clauses or more than 50 categories in one clause            |
| `401`  | Missing or invalid API key                                                      |
| `403`  | API key not valid for this project                                              |
| `404`  | Unknown `project_slug`                                                          |


## Related

- [Get article](get-article.md) — fetch one result by id
- [Article facets](facets.md) — discover filter values for search UI
- [Article Meta](../taxonomy/article-meta/index.md) — metadata catalogs and `meta` clause grammar
- [Metadata](../taxonomy/index.md) — Article Meta, Mention Meta, and Entity Meta
- [Semantic search](semantic-search.md) — natural-language search
- [Geographic search](geo-search.md) — location-based article search
- [Articles overview](index.md) — article hub model

