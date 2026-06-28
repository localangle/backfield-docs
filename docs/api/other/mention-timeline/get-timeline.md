# Get timeline

```
GET /public/v1/projects/{project_slug}/people/{person_id}/mentions/timeline
GET /public/v1/projects/{project_slug}/organizations/{organization_id}/mentions/timeline
GET /public/v1/projects/{project_slug}/locations/{location_id}/mentions/timeline
```

Return mention counts grouped by article publication date for one canonical entity. Each `items` row is one calendar day with a non-null article `pub_date` and the number of mentions on that day.

This is an aggregation endpoint, not a paginated mention list. For individual mention rows, use [List mentions](../../people/mentions.md).

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `person_id` | string | Canonical person UUID (people route) |
| `organization_id` | string | Canonical organization UUID (organizations route) |
| `location_id` | string | Canonical location UUID (locations route) |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `pub_date_from` | string | — | ISO date `YYYY-MM-DD`, inclusive lower bound on article `pub_date` |
| `pub_date_to` | string | — | ISO date `YYYY-MM-DD`, inclusive upper bound on article `pub_date` |
| `quote` | boolean | — | When `true`, count only mentions whose first evidence span is a quote |

Unlike [List mentions](../../people/mentions.md), timeline routes do not accept `nature`, `author`, `meta`, `sort`, or pagination parameters.

## Response `200`

People example:

```json
{
  "person_id": "550e8400-e29b-41d4-a716-446655440000",
  "label": "Jane Doe",
  "items": [
    { "pub_date": "2024-02-01", "mention_count": 1 },
    { "pub_date": "2024-03-01", "mention_count": 2 }
  ]
}
```

Organizations and locations use the same `items` shape with `organization_id` or `location_id` instead of `person_id`.

### Timeline item fields

| Field | Type | Description |
| --- | --- | --- |
| `pub_date` | string | Article publication date (`YYYY-MM-DD`) |
| `mention_count` | integer | Number of mentions on that date |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/people/550e8400-e29b-41d4-a716-446655440000/mentions/timeline\
?pub_date_from=2024-01-01&pub_date_to=2024-12-31&quote=true" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Invalid `pub_date_from` or `pub_date_to` |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project or entity |

## Related

- [Mention timeline overview](index.md)
- [List mentions](../../people/mentions.md) — paginated mention evidence for the same entity
- [List articles](../../people/list-articles.md) — deduplicated story feed for the same entity
