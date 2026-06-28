# Types

```
GET /public/v1/projects/{project_slug}/people/types
```

Return distinct person type values for the project's catalog. Use this to populate filter dropdowns before calling [List and search](search.md).

For the full catalog of allowed values and meanings, see [Entity Meta → People](../taxonomy/entity-meta/people.md). The response includes both catalog defaults and types stored on active canonical records.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Response `200`

```json
{
  "types": ["elected_official", "other"]
}
```

| Field | Type | Description |
| --- | --- | --- |
| `types` | string[] | Distinct person type values, sorted alphabetically |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/people/types" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` |

## Related

- [Entity Meta → People](../taxonomy/entity-meta/people.md) — catalog values and meanings
- [List and search](search.md) — filter by `person_type`
- [People overview](index.md)
