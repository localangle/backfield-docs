# Geo cells

Geo cells endpoints support hex coverage maps: aggregate distinct-article counts across a viewport, then drill down into the articles behind one cell. [List articles](list-articles.md) and [Batch query](query.md) share the same H3 rollup and size-gate rules described in [Coverage](coverage.md).

## Endpoints

| Method | Path | Doc |
| --- | --- | --- |
| `GET` | `…/articles/geo-cells` | [Coverage](coverage.md) |
| `GET` | `…/articles/geo-cells/{h3_cell}` | [List articles](list-articles.md) |
| `POST` | `…/articles/geo-cells/query` | [Batch query](query.md) |

## Related

- [Geographic search](../../articles/geo-search.md) — list articles by point, radius, or bbox without hex aggregation
- [Other overview](../index.md)
