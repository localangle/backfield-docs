# Types

```
GET /public/v1/projects/{project_slug}/locations/types
```

Return distinct location type values for the project's catalog. Use this to populate filter dropdowns before calling [List and search](search.md) or [Geographic search](geo-search.md).

For the full catalog of allowed values and meanings, see [Entity Meta → Locations](../taxonomy/entity-meta/locations.md). The response includes both catalog defaults and types stored on active canonical records.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Response `200`

```json
{
  "types": ["place", "address"]
}
```

| Field | Type | Description |
| --- | --- | --- |
| `types` | string[] | Distinct location type values, sorted alphabetically |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/locations/types" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` |

## Related

- [Entity Meta → Locations](../taxonomy/entity-meta/locations.md) — catalog values and meanings
- [List and search](search.md) — filter by `location_type`
- [Locations overview](index.md)
