# Get article metadata

```http
GET /public/v1/projects/{project_slug}/articles/{article_id}/metadata
```

Return the metadata rows attached to one active article, along with the distinct metadata types represented in those rows. Use this endpoint when you need article metadata without the rest of the article detail response.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `article_id` | integer | Article id |

## Response `200`

```json
{
  "article_id": 1,
  "meta_types": ["format", "topic"],
  "metadata": [
    {
      "meta_type": "format",
      "category": "news",
      "confidence": 0.98
    },
    {
      "meta_type": "topic",
      "category": "local_government_politics",
      "confidence": 0.92
    }
  ]
}
```

## Response fields

| Field | Type | Description |
| --- | --- | --- |
| `article_id` | integer | Requested article id |
| `meta_types` | array of strings | Distinct types represented in `metadata`, in alphabetical order |
| `metadata` | array | Metadata rows, ordered by type and stored row order |
| `metadata[].meta_type` | string | Metadata type |
| `metadata[].category` | string | Category value |
| `metadata[].confidence` | number | Classifier confidence |

An article with no metadata returns empty `meta_types` and `metadata` arrays.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1/metadata" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project, unknown article, or article not in project |
| `422` | `article_id` is not an integer |

## Related

- [Get article](get-article.md) — article detail including the same metadata rows
- [List article metadata types](metadata-types.md)
- [List article metadata values](metadata-values.md)
- [Article Meta](../taxonomy/article-meta/index.md) — filter grammar and standard catalogs
