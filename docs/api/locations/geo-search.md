# Geographic search

```
GET /public/v1/projects/{project_slug}/locations/geo-search
```

Find canonical locations whose stored geometry intersects a point radius or bounding box. Results include map-friendly fields such as `geometry_json` and `formatted_address`.

Only locations with geometry on the canonical record are included. Point mode results are ordered by distance from the center.

For article-centric map views — stories that mention places in an area — use [Geographic search](../articles/geo-search.md) under Articles instead.

## Search modes

Use exactly one search mode per request.

| Mode | Required parameters | Use when |
| --- | --- | --- |
| Point + radius | `center_lng`, `center_lat`, `radius_miles` | Search around a coordinate |
| Bounding box | `bbox` | Search inside a map viewport |

The `bbox` format is:

```text
min_lng,min_lat,max_lng,max_lat
```

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `center_lng` | number | — | Center longitude for point mode |
| `center_lat` | number | — | Center latitude for point mode |
| `radius_miles` | number | — | Radius in miles for point mode |
| `bbox` | string | — | Bounding box `min_lng,min_lat,max_lng,max_lat` |
| `q` | string | — | Optional case-insensitive match on label or formatted address |
| `location_type` | string | — | Exact location type filter |
| `nature` | string | — | Locations with at least one linked mention of this nature in the project |
| `min_mentions` | integer | `0` | Minimum project mention count |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

## Response `200`

```json
{
  "search_mode": "point",
  "items": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "slug": "city-hall",
      "label": "City Hall",
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
| `search_mode` | string | `point` or `bbox` — which mode was used |
| `items` | object[] | Matching location records (same shape as [List and search](search.md)) |
| `pagination` | object | Page metadata |

## Examples

Point + radius:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/locations/geo-search\
?center_lng=-87.6&center_lat=41.8&radius_miles=5&location_type=place" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Bounding box:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/locations/geo-search\
?bbox=-87.7,41.7,-87.5,41.9" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Missing search area, both modes provided, or invalid `bbox` |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` |

## Related

- [List and search](search.md) — keyword and filter search without a map area
- [Get location](get-location.md) — fetch one result by id
- [Geographic search (articles)](../articles/geo-search.md) — find articles by map area
- [Locations overview](index.md)
