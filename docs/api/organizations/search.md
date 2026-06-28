# List and search organizations

```
GET /public/v1/projects/{project_slug}/organizations
GET /public/v1/projects/{project_slug}/organizations/search
```

List or search canonical organizations in a project. Both paths accept the same parameters and return the same response shape.

Use `GET …/organizations` to browse the catalog. Use `GET …/organizations/search` when you want a search-oriented entry point — the behavior is identical.

The `q` parameter matches label (case-insensitive). Combine it with structured filters such as `organization_type` and `nature`.

Use [Types](types.md) to discover available `organization_type` values for filter controls.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `q` | string | — | Case-insensitive match on label |
| `organization_type` | string | — | Exact organization type filter |
| `nature` | string | — | Organizations with at least one linked mention of this nature in the project |
| `min_mentions` | integer | `0` | Minimum project mention count |
| `sort` | string | `label` | `label` or `recent` |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

See [Pagination](../conventions/pagination.md) for the list response envelope.

### Sort order

- **`label`** (default) — alphabetical by display label
- **`recent`** — most recently active organizations first (based on canonical updates and linked mention activity)
- When `q` is set and `sort` is not `recent`, stronger label matches appear first

## Response `200`

```json
{
  "items": [
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
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 1
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
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/organizations/search\
?q=Council&organization_type=government&limit=10" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` |

## Related

- [Types](types.md) — discover filter values
- [Get organization](get-organization.md) — fetch one result by id
- [Organizations overview](index.md)
