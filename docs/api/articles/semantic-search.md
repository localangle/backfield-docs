# Semantic search

```http
POST /public/v1/projects/{project_slug}/articles/semantic-search
```

Search articles with natural language. Semantic search ranks articles by **meaning** — useful when you want conceptually related stories, not only exact keyword matches.

Responses use the same article list item shape as [List and search](search.md) and [Geographic search](geo-search.md), with query echo fields at the top level describing how the query was embedded.

Articles must have been embedded by a flow (via the Embed Text node) before they appear in semantic search results. Articles without an embedding row are omitted, not returned as errors.

**Tip**: Compare total and embedded counts in [Get project](../projects/get-project.md) (`stats.articles`) to see how many articles are eligible for semantic search.

For exact words, phrases, or simple date filtering, use [List and search](search.md).

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## JSON body

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `query` | string | required | Natural-language search text |
| `use_hyde` | boolean | `false` | When `true`, generate a hypothetical news passage from the query, embed that passage, and rank against it (HyDE) |
| `meta` | array of string | `[]` | Metadata filter clauses (AND across clauses). Same grammar as [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta) — pass as a JSON array, not query params |
| `pub_date_from` | string | — | ISO date `YYYY-MM-DD`, inclusive lower bound |
| `pub_date_to` | string | — | ISO date `YYYY-MM-DD`, inclusive upper bound |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |
| `include` | array of string | `[]` | Repeatable include token. Supported: `counts` |

Each **`items[]`** row uses the same article list shape as [List and search](search.md) — `id`, `headline`, `url`, `author`, `pub_date`, `source`, `preview`, and `metadata` — plus **`score`**. Pass `"include": ["counts"]` to populate `counts` and `embedded`; otherwise both are `null`. The `images` field is also `null`; use [Get article](get-article.md) for inline images.

See [Pagination](../conventions/pagination.md) for the list response envelope.

### HyDE (`use_hyde`)

When `use_hyde` is `true`, a generative model writes a [short hypothetical document](https://arxiv.org/abs/2212.10496) from your query. That passage is embedded and used for ranking instead of embedding the raw query text. This can improve recall for short or abstract queries.

HyDE requires a generative model to be configured for the project or organization (the `semantic.hyde` default role, or the sole enabled generative model). The response echoes whether HyDE was used and includes the generated passage for transparency.

## Response `200`

The response wraps ranked articles in a search envelope. Top-level fields describe how the query was embedded; `items[]` holds the article rows.

```json
{
  "query": "city budget debate",
  "embedding_model": "openai/text-embedding-3-small",
  "embedding_model_config_id": "cfg_123",
  "hyde_used": false,
  "hypothetical_document": null,
  "hyde_model": null,
  "hyde_model_config_id": null,
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
      "preview": "City council members debated the revised spending plan…",
      "metadata": [
        {
          "meta_type": "topic",
          "category": "local_government_politics",
          "confidence": 0.92
        }
      ],
      "images": null,
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
      },
      "score": 0.82
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 1
  }
}
```

The example above includes `embedded` and `counts` because the request used `"include": ["counts"]`.

### Envelope fields

| Field | Type | Description |
| --- | --- | --- |
| `query` | string | Normalized query text used for the search |
| `embedding_model` | string \| null | Embedding model used to encode the query (or HyDE passage) |
| `embedding_model_config_id` | string \| null | Embedding model configuration id |
| `hyde_used` | boolean | Whether HyDE generated a hypothetical passage for ranking |
| `hypothetical_document` | string \| null | Generated passage when `hyde_used` is `true` |
| `hyde_model` | string \| null | Generative model used for HyDE |
| `hyde_model_config_id` | string \| null | HyDE model configuration id |
| `items[]` | array | Matching articles, ordered by relevance |
| `pagination` | object | Pagination envelope |

### Item fields

Each item is an article list row plus a similarity score. Core article fields match [List and search](search.md) and [Get article](get-article.md).

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
| `embedded` | boolean \| null | `null` unless `"include": ["counts"]` is requested |
| `counts` | object \| null | `null` unless `"include": ["counts"]` is requested — see [Get article](get-article.md#counts-embed-includecounts) |
| `images` | null | Always `null` on search responses; use [Get article](get-article.md) for inline images |
| `score` | number | Cosine similarity; higher means more relevant |

Results are ordered by `score` descending, then `pub_date` descending (nulls last), then `id` descending.

## Metadata filters

Pass **`meta`** as a JSON string array in the request body. Filters are applied before results are ranked. See [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta) for clause grammar, transport notes, and limits.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/semantic-search" \
  -H "Authorization: Bearer bfk_your_project_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "playoff game preview",
    "use_hyde": true,
    "meta": ["topic:pro_sports", "subject:sports_contest", "!format:explainer_analysis"],
    "pub_date_from": "2024-01-01",
    "include": ["counts"],
    "limit": 10
  }'
```

## Errors

| Status | When |
| --- | --- |
| `400` | Invalid `pub_date_from` or `pub_date_to` format, malformed `meta` clause, or unknown `include` token |
| `422` | Missing or invalid JSON body fields, such as `query`, `limit`, or `offset` |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project |
| `503` | No embedding model configured, or `use_hyde` is `true` but no generative model is available |

## Related

- [List and search](search.md) — keyword search
- [Get article](get-article.md) — retrieve one result by id, inline images, and counts field reference
- [Article Meta](../taxonomy/article-meta/index.md) — `meta` clause grammar
