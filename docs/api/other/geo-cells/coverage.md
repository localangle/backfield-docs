# Coverage

```http
GET /public/v1/projects/{project_slug}/articles/geo-cells
```

Return H3 hex cells within a bounding box with distinct article counts each. Use this to build zoomable coverage maps — each cell shows how many unique articles mention places in that area.

Each article counts once per cell, even if it has multiple location mentions in the same hex. This is an aggregation endpoint, not a paginated article list. To drill into one cell, use [List articles](list-articles.md). For a flat article list by map area without hex aggregation, use [Geographic search](../../articles/geo-search.md).

## Path parameters


| Name           | Type   | Description  |
| -------------- | ------ | ------------ |
| `project_slug` | string | Project slug |


## Query parameters


| Name            | Type    | Default      | Description                                                                                                                                                   |
| --------------- | ------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bbox`          | string  | **required** | Bounding box `min_lng,min_lat,max_lng,max_lat`                                                                                                                |
| `resolution`    | integer | —            | Optional H3 display resolution (0–15). When omitted, derived from bbox viewport size. Used as the starting resolution; the API may coarsen further if needed. |
| `location_type` | string  | —            | Filter matching locations by type — see [Entity Meta → Locations](../../taxonomy/entity-meta/locations.md)                                                    |
| `nature`        | string  | —            | Filter matching location mentions by role — see [Mention Meta → Locations](../../taxonomy/mention-meta/locations.md)                                          |
| `meta`          | string  | —            | Repeatable metadata filter clause (AND across clauses). Same grammar as [Article Meta](../../taxonomy/article-meta/index.md#querying-with-meta)               |
| `pub_date_from` | string  | —            | ISO date `YYYY-MM-DD`, inclusive lower bound                                                                                                                  |
| `pub_date_to`   | string  | —            | ISO date `YYYY-MM-DD`, inclusive upper bound                                                                                                                  |


### Article and mention filters

Filters fall into two groups:

- **Article filters** — repeatable `meta` clauses plus `pub_date_from` and `pub_date_to` narrow which articles can contribute to a cell count.
- **Mention filters** — `location_type` and `nature` narrow which location mentions qualify inside those articles.

Use [Article facets](../../articles/facets.md) to discover filter values in your project. See [Metadata](../../taxonomy/index.md) for article, subject, and mention catalogs.

Forward the same filters on [List articles](list-articles.md) and [Batch query](query.md) so drill-down totals match coverage counts.

The `bbox` format is:

```text
min_lng,min_lat,max_lng,max_lat
```

### Resolution, rollup, and size gate

Each response uses a single display resolution `R`:

- **Omit `resolution`** — the API derives a default from bbox viewport size and returns it as `derived_resolution`.
- **Pass `resolution`** — the API uses your value as the starting resolution. The bbox does not clamp it down.
- **Auto-coarsen** — if aggregation would exceed 5,000 cells, the API lowers `R` until under the cap and sets `coarsened: true`. Check `resolution` in the response for the effective value used to draw cells.

**Rollup:** locations stored at a finer native H3 resolution roll up to their parent cell at `R`.

**Size gate:** locations with native `h3_resolution` coarser than `R` are excluded. A city-scale mention does not appear in block-level views; it returns when the display resolution is coarse enough to represent that footprint. No per-zoom configuration is required.

Only locations with geometry, `h3_cell`, and `h3_resolution` contribute to counts.

### Map clients

On pan or zoom, send the current map bounds as `bbox` and map your zoom level to an H3 `resolution`. Draw every returned cell at `response.resolution` — do not subdivide or merge hexes on the client. When `coarsened` is `true`, the effective resolution is lower than requested because of data density.

## Response `200`

```json
{
  "resolution": 7,
  "derived_resolution": 5,
  "requested_resolution": 8,
  "bbox_extent_km": 12.4,
  "coarsened": true,
  "cells": [
    {
      "h3_cell": "872664c47ffffff",
      "article_count": 12
    }
  ]
}
```


| Field                   | Type           | Description                                                                      |
| ----------------------- | -------------- | -------------------------------------------------------------------------------- |
| `resolution`            | integer        | Effective H3 display resolution after auto-coarsen — draw cells at this level    |
| `derived_resolution`    | integer        | Default resolution the bbox would use when `resolution` is omitted               |
| `requested_resolution`  | integer \| null | Echo of the client-provided `resolution`, or `null` when omitted                 |
| `bbox_extent_km`        | number         | Characteristic viewport size in kilometers                                       |
| `coarsened`             | boolean        | `true` when the cell ceiling forced a lower resolution than requested or derived |
| `cells`                 | object[]       | Hex cells with article counts                                                    |
| `cells[].h3_cell`       | string         | H3 cell index                                                                    |
| `cells[].article_count` | integer        | Distinct articles with at least one matching location mention in this cell       |


Cells are ordered by `article_count` descending, then `h3_cell` ascending.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/geo-cells\
?bbox=-88,41,-87,42&resolution=8&meta=topic:public_safety_crime&nature=primary&pub_date_from=2024-01-01" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors


| Status | When                                                                                                                                          |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `400`  | Invalid or inverted `bbox`, invalid date format, malformed `meta` clause, or aggregation still exceeds 5,000 cells at the coarsest resolution |
| `401`  | Missing or invalid API key                                                                                                                    |
| `403`  | API key not valid for this project                                                                                                            |
| `404`  | Unknown `project_slug`                                                                                                                        |
| `422`  | Missing required `bbox`                                                                                                                       |


## Related

- [List articles](list-articles.md) — drill down into one coverage cell
- [Batch query](query.md) — drill down into many cells at once
- [Geographic search](../../articles/geo-search.md) — list articles with location mentions in an area
- [Geo cells overview](index.md)

