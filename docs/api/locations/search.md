# List and search locations

```
GET /public/v1/projects/{project_slug}/locations
GET /public/v1/projects/{project_slug}/locations/search
```

List or search canonical locations in a project. Both paths accept the same parameters and return the same response shape.

Use `GET …/locations` to browse the catalog. Use `GET …/locations/search` when you want a search-oriented entry point — the behavior is identical.

The `q` parameter matches label and formatted address (case-insensitive). Combine it with structured filters such as `location_type` and `nature`.

Use [Types](types.md) to discover available `location_type` values for filter controls. For map-based discovery of canonical locations, use [Geographic search](geo-search.md).

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `q` | string | — | Case-insensitive match on label or formatted address |
| `location_type` | string | — | Exact location type filter |
| `nature` | string | — | Locations with at least one linked mention of this nature in the project |
| `min_mentions` | integer | `0` | Minimum project mention count |
| `sort` | string | `label` | `label` or `recent` |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

See [Pagination](../conventions/pagination.md) for the list response envelope.

### Sort order

- **`label`** (default) — alphabetical by display label
- **`recent`** — most recently active locations first (based on canonical updates and linked mention activity)
- When `q` is set and `sort` is not `recent`, stronger label matches appear first

## Response `200`

```json
{
  "items": [
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
| `id` | string | Canonical location UUID |
| `slug` | string | URL-safe slug |
| `label` | string | Display name |
| `stylebook_slug` | string \| null | Stylebook catalog slug for this record |
| `location_type` | string \| null | Location type when set |
| `formatted_address` | string \| null | Formatted address when set |
| `geometry_type` | string \| null | GeoJSON geometry type when stored |
| `geometry_json` | object \| null | GeoJSON geometry when stored on the canonical |
| `counts` | object | Project-scoped activity totals |
| `counts.mentions` | integer | Linked mention rows in the project |
| `counts.stories` | integer | Distinct articles with at least one linked mention |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/locations/search\
?q=Main%20St&location_type=place&limit=10" \
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
- [Geographic search](geo-search.md) — find locations by map area
- [Get location](get-location.md) — fetch one result by id
- [Locations overview](index.md)
