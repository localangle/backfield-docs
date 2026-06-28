# List articles

```
GET /public/v1/projects/{project_slug}/organizations/{organization_id}/articles
```

Return paginated articles that mention a canonical organization in the project. Each article appears once, even when the organization has multiple mentions in the same story.

Use this route to build an organization's story feed. Use [List mentions](mentions.md) when you need mention-level evidence (nature, quote spans) for each article.

Optional `nature` and publication-date filters apply to matching mentions **before** articles are deduplicated and paginated. Query parameters match [List articles for people](../people/list-articles.md).

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `organization_id` | string | Canonical organization UUID |

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
  "organization_id": "660e8400-e29b-41d4-a716-446655440002",
  "label": "City Council",
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
| `organization_id` | string | Canonical organization UUID |
| `label` | string | Organization display label |
| `items` | array | Page of article objects (same shape as [List articles for people](../people/list-articles.md#article-fields)) |
| `pagination` | object | See [Pagination](../conventions/pagination.md) |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/organizations/660e8400-e29b-41d4-a716-446655440002/articles\
?pub_date_from=2024-01-01&pub_date_to=2024-12-31&nature=actor" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Invalid `pub_date_from` or `pub_date_to` |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project, organization, or inactive canonical record |

## Related

- [Get organization](get-organization.md)
- [List mentions](mentions.md) — mention evidence per article
- [Get article](../articles/get-article.md)
- [Organizations overview](index.md)
