# List article metadata values

```http
GET /public/v1/projects/{project_slug}/articles/metadata/types/{meta_type}/values
```

Return the distinct category values attached to active articles for one metadata type. Obtain type names from [List article metadata types](metadata-types.md).

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `meta_type` | string | Metadata type, such as `topic`, `format`, or `subject` |

## Response `200`

```json
{
  "meta_type": "topic",
  "values": [
    "local_government_politics",
    "public_safety_crime"
  ]
}
```

## Response fields

| Field | Type | Description |
| --- | --- | --- |
| `meta_type` | string | Requested metadata type after surrounding whitespace is removed |
| `values` | array of strings | Distinct, non-empty categories in alphabetical order |

An unknown type returns `200` with the requested `meta_type` and an empty `values` array.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/metadata/types/topic/values" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | `meta_type` is empty after normalization |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project |

## Related

- [List article metadata types](metadata-types.md)
- [Get article metadata](get-metadata.md)
- [Article Meta](../taxonomy/article-meta/index.md) — use a returned value in a `meta=type:value` filter
- [List and search](search.md) — filter articles with discovered values
