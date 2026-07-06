# Geo cells

Geo cells endpoints support hex coverage maps using [H3 cells](https://h3geo.org/), which are assigned to every geocoded location. Each endpoint returns a count of distinct articles with location mentions in each cell.

Use the same article and mention filters across coverage and drill-down requests so map counts match the article lists behind them. Article filters use repeatable `meta` clauses (or a JSON `meta` array on batch query) plus publication dates; mention filters use `location_type` and `nature`.

## Endpoints


| Method | Path                             | Doc                               |
| ------ | -------------------------------- | --------------------------------- |
| `GET`  | `…/articles/geo-cells`           | [Coverage](coverage.md)           |
| `GET`  | `…/articles/geo-cells/{h3_cell}` | [List articles](list-articles.md) |
| `POST` | `…/articles/geo-cells/query`     | [Batch query](query.md)           |


## Related

- [Geographic search](../../articles/geo-search.md) — list articles by point, radius, or bbox without hex aggregation
- [Other overview](../index.md)

