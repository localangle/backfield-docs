# List articles

```
GET /public/v1/projects/{project_slug}/people/{person_id}/articles
```

Return paginated articles that mention a canonical person in the project. Each article appears once, even when the person has multiple mentions in the same story.

Use this route to build a person's story feed. Use [List mentions](mentions.md) when you need mention-level evidence (nature, quote spans) for each article.

Optional `nature` and publication-date filters apply to matching mentions **before** articles are deduplicated and paginated.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `person_id` | string | Canonical person UUID |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `nature` | string | — | Filter to articles with a mention of this editorial `nature` (exact match) |
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
  "person_id": "550e8400-e29b-41d4-a716-446655440000",
  "label": "Jane Doe",
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
      ]
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
| `person_id` | string | Canonical person UUID |
| `label` | string | Person display label |
| `items` | array | Page of [article objects](#article-fields) |
| `pagination` | object | See [Pagination](../conventions/pagination.md) |

### Article fields

Each `items[]` entry uses the standard article list shape:

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Article id |
| `headline` | string | Headline |
| `url` | string \| null | Source URL |
| `author` | string \| null | Author |
| `pub_date` | string \| null | Publication date (`YYYY-MM-DD`) |
| `source` | object \| null | Publication or outlet when known |
| `source.id` | string | Stable source identifier |
| `source.name` | string | Display label for the outlet |
| `preview` | string \| null | Truncated body snippet (max 280 characters) |
| `metadata` | array | Metadata tags (`meta_type`, `category`, `confidence`) |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/people/550e8400-e29b-41d4-a716-446655440000/articles\
?pub_date_from=2024-01-01&pub_date_to=2024-12-31&nature=subject" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Invalid `pub_date_from` or `pub_date_to` |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project, person, or inactive canonical record |

## Related

- [Get person](get-person.md)
- [List mentions](mentions.md) — mention evidence per article
- [Get article](../articles/get-article.md) — full article summary for one result
- [People overview](index.md)
