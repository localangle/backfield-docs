# Custom records

Custom records expose structured data extracted from articles by Custom Extract pipelines.

## Available today


| Method | Path                                     | Doc                                                      |
| ------ | ---------------------------------------- | -------------------------------------------------------- |
| `GET`  | `…/articles/{article_id}/custom-records` | [List custom records](../articles/hub/custom-records.md) |


Use [Get article](../articles/get-article.md) with `include=counts` to see which record types exist on an article (`counts.custom_records`) before fetching records.

## Response shape

Each record includes:

- `id`, `record_type`, `record_index`
- `fields` — structured record values
- `mentions` — evidence spans (no full article body)
- `field_schema` — field definitions stored with the record
- Optional `confidence`

See [List custom records](../articles/hub/custom-records.md) for the full field reference and examples.

## Related

- [Other overview](../other/index.md)
- [Articles overview](../articles/index.md)
- [Detail endpoints](../articles/hub/index.md)

