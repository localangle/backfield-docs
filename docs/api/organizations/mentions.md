# List mentions

```http
GET /public/v1/projects/{project_slug}/organizations/{organization_id}/mentions
```

Return paginated mention evidence for one canonical organization, scoped to the project. Each item includes the article headline, mention fields, and optional evidence spans.

Filters use the same mention and article vocabulary as [List and search mentions](../mentions/search.md) — `nature`, `author`, repeatable **`meta`**, publication dates, and `quote`. Entity-first routes add **`sort`** and **`sort_direction`**, and omit project-wide-only params such as `entity_type`, `q`, and `has_canonical`.

The response echoes **`organization_id`** and **`label`**, then `items` and `pagination`.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `organization_id` | string | Canonical organization UUID |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `sort` | string | `created_at` | `created_at` or `article` (headline) |
| `sort_direction` | string | `desc` | `asc` or `desc` |
| `nature` | string | — | Filter by mention `nature` (exact match) |
| `author` | string | — | Filter by article byline (case-insensitive exact match) |
| `external_source` | string | — | Filter by article publication or outlet (case-insensitive exact match) |
| `meta` | string | — | Repeatable metadata filter clause on the parent article (AND across clauses). Same grammar as [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta) |
| `pub_date_from` | string | — | ISO date `YYYY-MM-DD`, inclusive lower bound on article `pub_date` |
| `pub_date_to` | string | — | ISO date `YYYY-MM-DD`, inclusive upper bound on article `pub_date` |
| `quote` | boolean | — | When `true`, return only mentions whose first evidence span is a quote |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

See [Pagination](../conventions/pagination.md) for the list response envelope.

## Metadata filters

Article metadata filters apply to the **article** that contains each mention, not to the mention itself. Use the repeatable **`meta`** query parameter — see [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta) for clause grammar.

```text
?nature=actor&meta=topic:local_government_politics
?quote=true&pub_date_from=2024-01-01
?sort=article&meta=topic:pro_sports&meta=!format:opinion
```

## Response `200`

```json
{
  "organization_id": "550e8400-e29b-41d4-a716-446655440000",
  "label": "City Council",
  "items": [
    {
      "mention_id": 12,
      "article": {
        "id": 1,
        "headline": "City council votes on budget",
        "url": "https://example.com/budget",
        "pub_date": "2024-03-01"
      },
      "label": "City Council",
      "organization_type": "government",
      "nature": "actor",
      "role_in_story": null,
      "evidence": {
        "mention_text": "The City Council approved the budget",
        "quote": true,
        "start_char": null,
        "end_char": null
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

Item rows omit `entity_type`, `canonical`, and internal entity ids — the route is already scoped to one organization.

### Mention fields

| Field | Type | Description |
| --- | --- | --- |
| `mention_id` | integer | Mention id |
| `article` | object | Article summary for this mention |
| `article.id` | integer | Article id |
| `article.headline` | string | Article headline |
| `article.url` | string \| null | Source URL when available |
| `article.pub_date` | string \| null | Publication date (`YYYY-MM-DD`) when available |
| `label` | string | Display label for this mention |
| `organization_type` | string \| null | Organization type when set |
| `nature` | string \| null | Mention nature when set |
| `role_in_story` | string \| null | Role in story when set |
| `evidence` | object \| null | First occurrence evidence span when available |
| `evidence.mention_text` | string \| null | Quote text when available; otherwise the matched mention text |
| `evidence.quote` | boolean | Whether the first occurrence is a quote |
| `evidence.start_char` | integer \| null | Start character offset in the article |
| `evidence.end_char` | integer \| null | End character offset in the article |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/organizations/550e8400-e29b-41d4-a716-446655440000/mentions\
?sort=article&nature=actor&quote=true&meta=topic:local_government_politics&pub_date_from=2024-01-01" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Invalid `pub_date_from` or `pub_date_to`, or malformed `meta` clause |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project or organization |

## Related

- [Get organization](get-organization.md) — canonical organization fields
- [List articles](list-articles.md) — deduplicated story feed for this organization
- [List and search mentions](../mentions/search.md) — project-wide mention search with the same filter vocabulary
- [Get timeline](../other/mention-timeline/get-timeline.md) — mention counts grouped by article publication date
- [Organizations overview](index.md)
