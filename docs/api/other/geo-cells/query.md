# Batch query

```http
POST /public/v1/projects/{project_slug}/articles/geo-cells/query
```

Return articles and in-cell location mentions for **many H3 hex cells** in one request. Use this when a map selection or retriever spans multiple cells — instead of calling [List articles](list-articles.md) once per cell.

Results are **deduplicated by article**. An article that matches several requested cells appears once, with all matching cells listed in `matched_cells` and location mentions combined in `matching_locations`.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## JSON body

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `cells` | string[] | **required** | H3 cell IDs (1–200 entries), all at the same display resolution |
| `resolution` | integer | **required** | Shared display resolution (0–15); each cell must match this resolution |
| `location_type` | string | — | Filter matching locations by type |
| `nature` | string | — | Filter matching location mentions by role, such as `primary` or `secondary` |
| `meta` | array of string | `[]` | Metadata filter clauses (AND across clauses). Same grammar as [Article Meta](../../taxonomy/article-meta/index.md#querying-with-meta) — pass as a JSON array |
| `external_source` | string | — | Filter articles by publication or outlet (case-insensitive exact match) |
| `pub_date_from` | string | — | ISO date `YYYY-MM-DD`, inclusive lower bound |
| `pub_date_to` | string | — | ISO date `YYYY-MM-DD`, inclusive upper bound |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

Nested `article` objects include a truncated `preview` (max 280 characters).

Use POST so large `cells` arrays are not limited by URL length.

## Metadata filters

Pass **`meta`** as a JSON string array in the request body. Filters apply to the article before H3 drill-down results are deduplicated. See [Article Meta](../../taxonomy/article-meta/index.md#querying-with-meta) for clause grammar.

### Semantics

Batch query uses the same H3 rollup and size-gate rules as [Coverage](coverage.md) and [List articles](list-articles.md):

- `resolution` is the display resolution shared by every cell in `cells`
- A location mention is included when its native `h3_resolution` is at least `R` and it rolls up to one of the requested cells
- Coarse-native locations are excluded at fine cells
- Forward the same article and mention filters from coverage (`meta`, `pub_date_from`/`pub_date_to`, `location_type`, `nature`) so `per_cell_totals` matches [Coverage](coverage.md) counts

When `cells` contains a single cell and `resolution` matches that cell's level, the merged article set matches the single-cell GET route (aside from `matched_cells` on each item).

## Response `200`

```json
{
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
        "embedded": null,
        "counts": null,
        "images": null
      },
      "matching_locations": [
        {
          "mention_id": 10,
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
      ],
      "matched_cells": ["872664c47ffffff", "872664c1effffff"]
    }
  ],
  "per_cell_totals": [
    { "h3_cell": "872664c47ffffff", "article_count": 12 },
    { "h3_cell": "872664c1effffff", "article_count": 8 }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 15
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `resolution` | integer | Display resolution from the request |
| `items` | object[] | Deduplicated articles with in-cell location mentions |
| `items[].article` | object | Article summary (same shape as [List and search](../../articles/search.md) items) |
| `items[].matching_locations` | object[] | Location mentions that rolled up to one or more requested cells |
| `items[].matched_cells` | string[] | Which requested hexes this article matched through |
| `per_cell_totals` | object[] | Distinct-article count per requested cell after filters — use to cross-check [Coverage](coverage.md) counts |
| `per_cell_totals[].h3_cell` | string | Requested cell ID |
| `per_cell_totals[].article_count` | integer | Distinct articles in that cell |
| `pagination` | object | Page metadata over the merged, deduplicated article set |

Results are ordered by article `pub_date` descending (nulls last), then article `id` descending — same as single-cell drill-down.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/geo-cells/query" \
  -H "Authorization: Bearer bfk_your_project_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "cells": ["872664c47ffffff", "872664c1effffff"],
    "resolution": 7,
    "meta": ["topic:public_safety_crime"],
    "external_source": "springfield-daily",
    "pub_date_from": "2024-01-01",
    "limit": 100,
    "offset": 0
  }'
```

## Errors

| Status | When |
| --- | --- |
| `400` | Empty `cells`, invalid cell ID, resolution mismatch, more than 200 cells, invalid date format, or malformed `meta` clause |
| `422` | Missing or invalid JSON body fields, such as `cells`, `resolution`, or pagination bounds |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` |

## Related

- [Coverage](coverage.md) — hex coverage map for a viewport
- [List articles](list-articles.md) — drill down into one cell
- [Geo cells overview](index.md)
