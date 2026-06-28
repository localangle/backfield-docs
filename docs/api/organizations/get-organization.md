# Get organization

```
GET /public/v1/projects/{project_slug}/organizations/{organization_id}
```

Return one canonical organization by UUID.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `organization_id` | string | Canonical organization UUID |

## Response `200`

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "slug": "city-council",
  "label": "City Council",
  "stylebook_slug": "default",
  "organization_type": "government",
  "counts": {
    "mentions": 3,
    "stories": 2
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Canonical organization UUID |
| `slug` | string | URL-safe slug |
| `label` | string | Display name |
| `stylebook_slug` | string \| null | Stylebook catalog slug for this record |
| `organization_type` | string \| null | Organization type when set |
| `counts` | object | Project-scoped activity totals |
| `counts.mentions` | integer | Linked mention rows in the project |
| `counts.stories` | integer | Distinct articles with at least one linked mention |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/organizations/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project, organization, or inactive canonical record |

## Related

- [List articles](list-articles.md) — story feed for this organization
- [List mentions](mentions.md) — mention evidence per article
- [List connections](connections.md) — Stylebook relationships
- [List and search](search.md) — find organizations by name or filters
