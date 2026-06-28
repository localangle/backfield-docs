# Locations

Locations are canonical records for places identified across project articles. Use location endpoints to browse and search the place catalog, find locations on a map, retrieve location detail, and explore mention evidence and Stylebook connections.

Each location record includes a display label, location type, optional formatted address, geometry when available, and project-scoped **`counts`** (`mentions`, `stories`).

## Endpoints

| Method | Path | Use when | Doc |
| --- | --- | --- | --- |
| `GET` | `…/locations/{location_id}` | Show one location's canonical fields | [Get location](get-location.md) |
| `GET` | `…/locations` | Find locations by name, address, type, or filters | [List and search](search.md) |
| `GET` | `…/locations/search` | Find locations by name, address, type, or filters | [List and search](search.md) |
| `GET` | `…/locations/geo-search` | Find locations whose geometry intersects a point radius or bounding box | [Geographic search](geo-search.md) |
| `GET` | `…/locations/{location_id}/articles` | Load paginated stories mentioning a location | [List articles](list-articles.md) |
| `GET` | `…/locations/{location_id}/mentions` | Load paginated mention evidence per article | [List mentions](mentions.md) |
| `GET` | `…/locations/{location_id}/mentions/timeline` | Chart mention counts by publication date | [Get timeline](../other/mention-timeline/get-timeline.md) |
| `GET` | `…/locations/{location_id}/connections` | Load Stylebook relationships involving a location | [List connections](connections.md) |

Location ids are UUID strings. Geographic search returns only locations with stored geometry that intersects the search area.

## Related

- [Entities overview](../entities/index.md) — shared entity-first pattern
- [People](../people/index.md) — similar entity routes
- [Organizations](../organizations/index.md) — similar entity routes
- [Entity Meta → Locations](../taxonomy/entity-meta/locations.md) — `location_type` catalog
- [Location types](types.md) — discover `location_type` values in your project
