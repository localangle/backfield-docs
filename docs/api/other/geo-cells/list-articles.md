# List articles

```
GET /public/v1/projects/{project_slug}/articles/geo-cells/{h3_cell}
```

Return the articles and in-cell location mentions behind one coverage hex. Use this when a user clicks a cell from [Coverage](coverage.md).

Matching uses the same H3 rollup and size-gate rules as coverage. Forward the same filters from the coverage request so `pagination.total` matches the cell's `article_count`.

Display resolution `R` is derived from the path `h3_cell` — there is no `resolution` query parameter.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `h3_cell` | string | H3 cell ID from a [Coverage](coverage.md) response |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `location_type` | string | — | Filter matching locations by type |
| `nature` | string | — | Filter matching location mentions by role, such as `primary` or `secondary` |
| `meta` | string | — | Repeatable metadata filter clause (AND across clauses). Same grammar as [Article Meta](../../taxonomy/article-meta/index.md#querying-with-meta) |
| `pub_date_from` | string | — | ISO date `YYYY-MM-DD`, inclusive lower bound |
| `pub_date_to` | string | — | ISO date `YYYY-MM-DD`, inclusive upper bound |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

Nested `article` objects include a truncated `preview` (max 280 characters).

See [Pagination](../../conventions/pagination.md) for the list response envelope.

## Response `200`

```json
{
  "h3_cell": "872664c47ffffff",
  "resolution": 7,
  "items": [
    {
      "article": {
        "id": 1,
        "headline": "City council votes on budget",
        "url": "https://example.com/budget",
        "author": "Jane Doe",
        "pub_date": "2024-03-01",
        "source": {
          "id": "example.com",
          "name": "example.com"
        },
        "preview": "The city council approved a revised budget after…",
        "metadata": [],
      },
      "matching_locations": [
        {
          "mention_id": 10,
          "substrate_location_id": 4,
          "label": "City Hall",
          "location_type": "place",
          "formatted_address": "123 Main St",
          "geometry_type": "Point",
          "geometry_json": {
            "type": "Point",
            "coordinates": [-87.6, 41.8]
          },
          "h3_cell": "892664c1a97ffff",
          "h3_resolution": 11,
          "canonical": null,
          "nature": "primary",
          "role_in_story": null,
          "evidence": null
        }
      ]
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 12
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `h3_cell` | string | Requested H3 cell ID |
| `resolution` | integer | Display resolution derived from `h3_cell` |
| `items` | object[] | Articles with in-cell location mentions |
| `items[].article` | object | Article summary (same shape as [List and search](../../articles/search.md) items) |
| `items[].matching_locations` | object[] | Location mentions that rolled up to this cell |
| `pagination` | object | Page metadata |

Results are ordered by article `pub_date` descending (nulls last), then article `id` descending. A valid cell with no matching mentions returns `200` with empty `items` and `total: 0`.

### Matching location fields

| Field | Type | Description |
| --- | --- | --- |
| `mention_id` | integer | Mention id |
| `substrate_location_id` | integer | Location id |
| `label` | string | Display label |
| `location_type` | string \| null | Location type when set |
| `formatted_address` | string \| null | Formatted address when set |
| `geometry_type` | string \| null | GeoJSON geometry type when available |
| `geometry_json` | object \| null | GeoJSON geometry when available |
| `h3_cell` | string \| null | Native H3 cell on the location |
| `h3_resolution` | integer \| null | Native H3 resolution on the location |
| `canonical` | object \| null | Linked canonical record when available |
| `nature` | string \| null | Mention nature when set |
| `role_in_story` | string \| null | Role in story when set |
| `evidence` | object \| null | First occurrence evidence span when available |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/geo-cells/872664c47ffffff\
?meta=topic:public_safety_crime&nature=primary&limit=10" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Invalid `h3_cell`, invalid date format, or malformed `meta` clause |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` |

## Related

- [Coverage](coverage.md) — hex coverage map for a viewport
- [Batch query](query.md) — drill down into many cells at once
- [Get article](../../articles/get-article.md) — full article summary for one result
- [Geo cells overview](index.md)
