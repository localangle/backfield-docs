# List article metadata types

```http
GET /public/v1/projects/{project_slug}/articles/metadata/types
```

Return the distinct metadata types attached to active articles in a project. Use this endpoint to discover the type names that can be used in [`meta` filters](../taxonomy/article-meta/index.md#querying-with-meta).

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Response `200`

```json
{
  "meta_types": ["format", "subject", "topic"]
}
```

## Response fields

| Field | Type | Description |
| --- | --- | --- |
| `meta_types` | array of strings | Distinct, non-empty metadata types in alphabetical order |

A project with no article metadata returns an empty array.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/metadata/types" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project |

## Related

- [List metadata values](metadata-values.md) — discover categories for one returned type
- [Get article metadata](get-metadata.md) — metadata attached to one article
- [Article Meta](../taxonomy/article-meta/index.md) — filter grammar and standard catalogs
- [Article facets](facets.md) — common metadata categories plus author and source facets
