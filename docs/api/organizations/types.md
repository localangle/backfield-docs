# Types

```
GET /public/v1/projects/{project_slug}/organizations/types
```

Return distinct organization type values for the project's assigned Stylebook. Use this to populate filter dropdowns before calling [List and search](search.md).

For the full catalog of allowed values and meanings, see [Entity Meta → Organizations](../taxonomy/entity-meta/organizations.md). The response includes both catalog defaults and types stored on active canonical records.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `stylebook_slug` | string | — | Optional compatibility check; when set, must match the project's assigned Stylebook |

## Response `200`

```json
{
  "types": ["company", "government"]
}
```

| Field | Type | Description |
| --- | --- | --- |
| `types` | string[] | Distinct organization type values, sorted alphabetically |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/organizations/types" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | `stylebook_slug` names a different Stylebook in the project organization |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` or unknown/foreign `stylebook_slug` |

## Related

- [Entity Meta → Organizations](../taxonomy/entity-meta/organizations.md) — catalog values and meanings
- [List and search](search.md) — filter by `organization_type`
- [Organizations overview](index.md)
