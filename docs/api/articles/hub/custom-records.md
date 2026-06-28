# List custom records

```
GET /public/v1/projects/{project_slug}/articles/{article_id}/custom-records
```

List structured records extracted from one article — for example contracts, permits, ingredients, or other project-specific data types produced by Custom Extract pipelines.

Use [Get article](../get-article.md) with `include=counts` to see which record types exist on an article before calling this route. Counts appear under `counts.custom_records`.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `article_id` | integer | Article id |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `record_type` | string | — | Filter to one record type (exact match), such as `contracts` or `ingredients` |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

## Response `200`

```json
{
  "items": [
    {
      "id": 9,
      "record_type": "contracts",
      "record_index": 0,
      "fields": {
        "vendor": "Acme Corp",
        "amount": 125000
      },
      "mentions": [
        {
          "text": "Acme Corp was awarded a $125,000 contract",
          "start_char": 210,
          "end_char": 252
        }
      ],
      "field_schema": [
        {
          "name": "vendor",
          "field_type": "string"
        },
        {
          "name": "amount",
          "field_type": "number"
        }
      ],
      "confidence": 0.91
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 1
  }
}
```

### Record fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Record id |
| `record_type` | string | Record type slug from the extraction pipeline |
| `record_index` | integer | Zero-based position within the article for this type |
| `fields` | object | Structured field values for this record |
| `mentions` | array | Evidence spans pointing to text in the article |
| `field_schema` | array | Field definitions stored with the record so historical rows remain interpretable |
| `confidence` | number \| null | Classifier confidence when set |

Results are ordered by `record_type`, then `record_index`.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1/custom-records?record_type=contracts" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project or article |

## Related

- [Custom records overview](../../custom-records/index.md) — project-level search (planned)
- [Get article](../get-article.md) — `counts.custom_records`
- [Detail endpoints overview](index.md)
