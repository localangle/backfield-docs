# Get location

```
GET /public/v1/projects/{project_slug}/locations/{location_id}
```

Return one canonical location by UUID.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `location_id` | string | Canonical location UUID |

## Response `200`

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "slug": "city-hall",
  "label": "City Hall",
  "stylebook_slug": "default",
  "location_type": "place",
  "formatted_address": "123 Main St",
  "geometry_type": "Point",
  "geometry_json": {
    "type": "Point",
    "coordinates": [-87.6, 41.8]
  },
  "counts": {
    "mentions": 3,
    "stories": 2
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Canonical location UUID |
| `slug` | string | URL-safe slug |
| `label` | string | Display name |
| `stylebook_slug` | string \| null | Stylebook catalog slug for this record |
| `location_type` | string \| null | Location type when set |
| `formatted_address` | string \| null | Formatted address when set |
| `geometry_type` | string \| null | GeoJSON geometry type when geometry is stored |
| `geometry_json` | object \| null | GeoJSON geometry when stored on the canonical |
| `counts` | object | Project-scoped activity totals |
| `counts.mentions` | integer | Linked mention rows in the project |
| `counts.stories` | integer | Distinct articles with at least one linked mention |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/locations/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project, location, or inactive canonical record |

## Related

- [List articles](list-articles.md) — story feed for this location
- [List mentions](mentions.md) — mention evidence per article
- [List connections](connections.md) — Stylebook relationships
- [List and search](search.md) — find locations by name or filters
- [Geographic search](geo-search.md) — find locations by map area
