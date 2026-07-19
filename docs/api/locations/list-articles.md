# List articles

```http
GET /public/v1/projects/{project_slug}/locations/{location_id}/articles
```

Return paginated articles that mention a canonical location in the project. Each article appears once, even when the location has multiple mentions in the same story.

Use this route to build a place's story feed. Use [List mentions](mentions.md) when you need mention-level evidence (nature, quote spans) for each article.

`nature` applies to matching mentions before articles are deduplicated and
paginated. The remaining filters apply to the parent articles. Query parameters
match [List articles for people](../people/list-articles.md).

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `location_id` | string | Canonical location UUID |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `nature` | string | — | Filter to articles with a mention of this editorial `nature` (exact match), such as `primary` or `secondary` |
| `author` | string | — | Filter by article byline (case-insensitive exact match) |
| `external_source` | string | — | Filter by publication or outlet (case-insensitive exact match) |
| `meta` | string | — | Repeatable article metadata clause; see [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta) |
| `include` | string | — | Repeatable include token. Supported: `counts` |
| `pub_date_from` | string | — | ISO date `YYYY-MM-DD`, inclusive lower bound on article `pub_date` |
| `pub_date_to` | string | — | ISO date `YYYY-MM-DD`, inclusive upper bound on article `pub_date` |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

Each item includes a truncated `preview` (max 280 characters).

## Sort order

Results are ordered by article `pub_date` descending (nulls last), then article `id` descending.

## Response `200`

```json
{
  "location_id": "660e8400-e29b-41d4-a716-446655440001",
  "label": "City Hall",
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
      "embedded": null,
      "counts": null,
      "images": null
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 1
  }
}
```

### Response fields

| Field | Type | Description |
| --- | --- | --- |
| `location_id` | string | Canonical location UUID |
| `label` | string | Location display label |
| `items` | array | Page of article objects (same shape as [List articles for people](../people/list-articles.md#article-fields)) |
| `pagination` | object | See [Pagination](../conventions/pagination.md) |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/locations/660e8400-e29b-41d4-a716-446655440001/articles\
?meta=topic:local_government_politics&include=counts&nature=primary" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Invalid dates, malformed `meta`, or unknown `include` token |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project, location, or inactive canonical record |

## Related

- [Get location](get-location.md)
- [List mentions](mentions.md) — mention evidence per article
- [Get article](../articles/get-article.md)
- [Locations overview](index.md)
