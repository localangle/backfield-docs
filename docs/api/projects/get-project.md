# Get project

```
GET /public/v1/projects/{project_slug}
```

Return project metadata and substrate summary counts for the given slug. Use this to confirm that your API key can access a project and to read high-level inventory stats before querying articles or mentions.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug (e.g. `general`) |

## Response `200`

```json
{
  "id": 1,
  "name": "Local News Feed",
  "slug": "general",
  "stylebook_slug": "cpm-stylebook",
  "stylebook_name": "CPM Stylebook",
  "stats": {
    "articles": {
      "total": 3593,
      "embedded": 49
    },
    "mentions": {
      "total": 74529,
      "embedded": 17206
    },
    "images": {
      "total": 3648,
      "embedded": 0
    }
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Project id |
| `name` | string | Display name |
| `slug` | string | URL slug |
| `stylebook_slug` | string \| null | Catalog slug used for entity data |
| `stylebook_name` | string \| null | Catalog display name |
| `stats` | object | Summary counts for non-deleted content in the project |
| `stats.articles` | object | Article inventory |
| `stats.articles.total` | integer | Non-deleted articles |
| `stats.articles.embedded` | integer | Articles with a populated embedding row (eligible for [Semantic search](../articles/semantic-search.md)) |
| `stats.mentions` | object | Location, person, and organization mention aggregates |
| `stats.mentions.total` | integer | Non-deleted mentions across all three entity types |
| `stats.mentions.embedded` | integer | Distinct mentions with a ready semantic document embedding |
| `stats.images` | object | Image inventory |
| `stats.images.total` | integer | Images attached to non-deleted articles |
| `stats.images.embedded` | integer | Images with a populated embedding row |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` or project outside caller scope |

## Related

- [Projects overview](index.md)
- [Authentication](../authentication.md)
