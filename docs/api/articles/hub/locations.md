# List locations

```http
GET /public/v1/projects/{project_slug}/articles/{article_id}/locations
```

List locations mentioned in an article, including map-friendly fields such as formatted address and geometry when available.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `article_id` | integer | Article id |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

## Response `200`

```json
{
  "items": [
    {
      "mention_id": 15,
      "label": "City Hall",
      "location_type": "building",
      "formatted_address": "100 Main St, Springfield",
      "geometry_type": "Point",
      "geometry_json": {
        "type": "Point",
        "coordinates": [-93.265, 44.9778]
      },
      "canonical": {
        "id": "660e8400-e29b-41d4-a716-446655440001",
        "slug": "city-hall-springfield",
        "label": "City Hall",
        "stylebook_slug": "default"
      },
      "nature": "primary",
      "role_in_story": null,
      "evidence": {
        "mention_text": "The vote took place at City Hall",
        "quote": true,
        "start_char": 45,
        "end_char": 54
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

### Location fields

| Field | Type | Description |
| --- | --- | --- |
| `mention_id` | integer | Location mention id |
| `label` | string | Location name |
| `location_type` | string \| null | Location type when set |
| `formatted_address` | string \| null | Formatted address when available |
| `geometry_type` | string \| null | GeoJSON geometry type |
| `geometry_json` | object \| null | GeoJSON geometry |
| `canonical` | object \| null | Linked canonical location (`id`, `slug`, `label`, `stylebook_slug`), when available |
| `nature` | string \| null | Role this location plays in the article, such as `primary` or `secondary` |
| `role_in_story` | string \| null | Role in story when set |
| `evidence` | object \| null | First occurrence evidence span |

Evidence uses `mention_text`, `quote`, `start_char`, and `end_char`. `mention_text` contains quote text when available; otherwise it contains the matched mention text. `quote` can still be `true` when the occurrence is labeled as a quote but no separate quote text was stored.

Results are ordered newest first.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1/locations" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project or article |

## Related

- [List mentions](mentions.md) — people, organizations, and locations in one list
- [Geographic search](../geo-search.md) — search articles by map area and location role
- [Locations resource](../../locations/index.md) — entity-first location queries
