# Geographic search

```text
GET /public/v1/projects/{project_slug}/articles/geo-search
```

Find articles that mention locations near a point or inside a bounding box. Each result includes the matching article and the location mentions that satisfied the geographic filter.

This endpoint is useful for map views, local monitoring, and place-based discovery.

You can also narrow matches by location type (repeatable, OR across values) or by the role that location plays in the article.

## Search Modes

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
| `location_type` | string | — | Repeatable location type filter (OR). Include articles with a matching mention of any listed substrate `location_type`. Max 25 values. Discover types with `GET …/locations/types` — see [Entity Meta → Locations](../taxonomy/entity-meta/locations.md) |
| `nature` | string | — | Filter matching location mentions by role, such as `primary` or `secondary` |
| `meta` | string | — | Repeatable metadata filter clause (AND across clauses). Same grammar as [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta) |
| `pub_date_from` | string | — | ISO date `YYYY-MM-DD`, inclusive lower bound |
| `pub_date_to` | string | — | ISO date `YYYY-MM-DD`, inclusive upper bound |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |
| `include` | string | — | Repeatable include token. Supported: `counts` |

See [Pagination](../conventions/pagination.md) for the shared `items` and `pagination` envelope. Geographic search responses also **echo the effective geo and filter parameters** at the top level, consistent with [List and search](search.md) and [Semantic search](semantic-search.md).

## Response `200`

The response echoes the geographic query at the top level, then `items` and `pagination`.

Each **`items[]`** row uses the same article list shape as [List and search](search.md) plus **`matching_locations`**. Pass `include=counts` to add `counts` and `embedded` on each item.

```json
{
  "search_mode": "point",
  "center_lng": -87.6,
  "center_lat": 41.8,
  "radius_miles": 5,
  "bbox": null,
  "location_types": ["building"],
  "nature": null,
  "pub_date_from": null,
  "pub_date_to": null,
  "items": [
    {
      "id": 1,
      "headline": "City council votes on budget",
      "url": "https://example.com/budget",
      "author": "Jane Doe",
      "pub_date": "2024-03-01",
      "source": {
        "id": "example.com",
        "name": "example.com"
      },
      "preview": "City council members debated the revised spending plan…",
      "metadata": [],
      "matching_locations": [
        {
          "mention_id": 10,
          "substrate_location_id": 4,
          "label": "City Hall",
          "location_type": "building",
          "formatted_address": "100 Main St, Springfield",
          "geometry_type": "Point",
          "geometry_json": {
            "type": "Point",
            "coordinates": [-87.6, 41.8]
          },
          "h3_cell": "872664c1bffffff",
          "h3_resolution": 11,
          "canonical": null,
          "nature": null,
          "role_in_story": null,
          "evidence": null
        }
      ]
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 1
  }
}
```

In bbox mode, `search_mode` is `"bbox"` and `bbox` is an object with `min_lng`, `min_lat`, `max_lng`, and `max_lat`. Point-mode fields (`center_lng`, `center_lat`, `radius_miles`) are `null`.

### Envelope fields

| Field | Type | Description |
| --- | --- | --- |
| `search_mode` | string | `point` or `bbox` |
| `center_lng` | number \| null | Center longitude (point mode) |
| `center_lat` | number \| null | Center latitude (point mode) |
| `radius_miles` | number \| null | Search radius in miles (point mode) |
| `bbox` | object \| null | Bounding box (`min_lng`, `min_lat`, `max_lng`, `max_lat`) in bbox mode |
| `location_types` | array of string | Applied location type filters (empty when omitted) |
| `nature` | string \| null | Mention nature filter |
| `pub_date_from` | string \| null | Inclusive lower publication date bound |
| `pub_date_to` | string \| null | Inclusive upper publication date bound |
| `items[]` | array | Matching articles with geographic context |
| `pagination` | object | Pagination envelope |

`meta` filter clauses are applied server-side but are not echoed individually in the response envelope.

### Item fields

Each item is an article list row plus geographic matches. Core article fields match [List and search](search.md) and [Get article](get-article.md).

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Article id |
| `headline` | string | Headline |
| `url` | string \| null | Source URL |
| `author` | string \| null | Author |
| `pub_date` | string \| null | Publication date (`YYYY-MM-DD`) |
| `source` | object \| null | Publication or outlet when known |
| `preview` | string \| null | Truncated body snippet (max 280 characters) |
| `metadata` | array | Metadata tags (`meta_type`, `category`, `confidence`) |
| `embedded` | boolean \| null | Present with `include=counts` |
| `counts` | object \| null | Present with `include=counts` — see [Get article](get-article.md#counts-embed-includecounts) |
| `matching_locations` | array | Location mentions that matched the geographic filter |

Location objects use the same shape as [List locations](hub/locations.md).

Results are ordered by article `pub_date` descending (nulls last), then `id` descending.

## Location type filters

Repeat **`location_type`** to require a matching mention of **any** listed type (OR). Omit the parameter to match all geocoded location types in the search area.

```text
?location_type=place
?location_type=place&location_type=address
?bbox=-87.9,41.6,-87.4,42.0&location_type=building&location_type=venue&nature=primary
```

Use `GET …/locations/types` or [Mention facets](../mentions/facets.md) (`location_types`) to discover values in your project.

## Metadata filters

Use the repeatable **`meta`** query parameter to filter by article metadata. These filters apply to the article, while `location_type` and `nature` apply to the matching location mentions. Clause grammar, transport notes, limits, and discovery paths are documented under [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta).

Use [Article facets](facets.md) or `GET …/articles/metadata/types` to discover valid types and categories in your project.

```text
?bbox=-87.9,41.6,-87.4,42.0&meta=topic:local_government_politics&meta=!format:opinion
?center_lng=-87.6&center_lat=41.8&radius_miles=5&meta=subject:development_project
?bbox=-87.9,41.6,-87.4,42.0&meta=topic:pro_sports&nature=primary&location_type=place
```

## Examples

Search within 5 miles of a coordinate:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/geo-search\
?center_lng=-87.6&center_lat=41.8&radius_miles=5&include=counts&limit=10" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Search inside a map viewport:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/geo-search\
?bbox=-87.9,41.6,-87.4,42.0\
&meta=topic:local_government_politics&meta=\!format:opinion" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Search for articles where a primary location falls inside a map viewport:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/geo-search\
?bbox=-87.9,41.6,-87.4,42.0&nature=primary" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Filter to several location types (OR):

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/geo-search\
?center_lng=-87.6&center_lat=41.8&radius_miles=5\
&location_type=place&location_type=address&location_type=venue" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Missing geo parameters, mixed point and bbox modes, invalid bbox, invalid dates, malformed `meta` clause, more than 25 `meta` clauses or more than 50 categories in one clause, invalid or empty `location_type`, more than 25 `location_type` values, or unknown `include` token |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project |

## Related

- [Geo cells](../other/geo-cells/index.md) — H3 hex coverage map and cell drill-down
- [List locations](hub/locations.md) — locations for one known article
- [List and search](search.md) — keyword search
- [Semantic search](semantic-search.md) — natural-language search
- [Article Meta](../taxonomy/article-meta/index.md) — `meta` clause grammar
