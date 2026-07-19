# Pagination

List and search endpoints use offset-based pagination.

## Query parameters


| Name     | Type    | Default | Description                                          |
| -------- | ------- | ------- | ---------------------------------------------------- |
| `limit`  | integer | `25`    | Page size (1–100 unless a route specifies otherwise) |
| `offset` | integer | `0`     | Number of items to skip                              |


## Response envelope

Most list endpoints return `items` and `pagination`:

```json
{
  "items": [],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 0
  }
}
```

Article search endpoints ([List and search](../articles/search.md), [Semantic search](../articles/semantic-search.md), [Geographic search](../articles/geo-search.md)) extend this envelope with **query echo fields** at the top level — the effective filters or embedding metadata for the request — before `items` and `pagination`.

Entity connection routes also use this envelope. Older clients must read
connections from `items`; the unpaginated `connections` field is not part of
the v1 contract.


| Field               | Type    | Description                                                           |
| ------------------- | ------- | --------------------------------------------------------------------- |
| `items`             | array   | Page of results                                                       |
| `pagination.limit`  | integer | Applied page size                                                     |
| `pagination.offset` | integer | Applied offset                                                        |
| `pagination.total`  | integer | Total matching items after **server-side** filters, before pagination |


`pagination.total` reflects only filters the API applies (query parameters, path scope, and so on). If you filter results further in your client after fetching a page, the visible row count may differ from `total`. Do not use `total` as the count of client-filtered rows.

## Example

Fetch the second page of 50 articles:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/search?limit=50&offset=50" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Sorting

Default sort order depends on the endpoint. For example, [article search](../articles/search.md) sorts by publication date when `q` is omitted, and by relevance when `q` is set.