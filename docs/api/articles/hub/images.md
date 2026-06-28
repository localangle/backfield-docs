# List images

```
GET /public/v1/projects/{project_slug}/articles/{article_id}/images
```

List images attached to an article.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `article_id` | integer | Article id |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

## Response `200`

```json
{
  "items": [
    {
      "id": 9,
      "image_id": "img_abc123",
      "url": "https://cdn.example.com/photos/council.jpg",
      "caption": "Council members after the vote"
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 1
  }
}
```

### Image fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Image record id |
| `image_id` | string | Stable image identifier |
| `url` | string | Image URL |
| `caption` | string \| null | Caption when set |

Results are ordered by `id` ascending.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1/images" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project or article |

## Related

- [Get article](../get-article.md) — inline images (up to 10) and `counts.images` with `include=counts`
- [Articles overview](../index.md)
