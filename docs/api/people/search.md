# List and search people

```http
GET /public/v1/projects/{project_slug}/people/
GET /public/v1/projects/{project_slug}/people/search
```

List or search canonical people in a project. Both paths accept the same parameters and return the same response shape.

Use `GET …/people/` to browse the catalog. Use `GET …/people/search` when you want a search-oriented entry point — the behavior is identical.

The `q` parameter matches label, title, and affiliation (case-insensitive). Combine it with structured filters such as `person_type`, `public_figure`, and `nature`.

Use [Types](types.md) to discover available `person_type` values in your project. See [Entity Meta → People](../taxonomy/entity-meta/people.md) for the full catalog.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `q` | string | — | Case-insensitive match on label, title, or affiliation |
| `person_type` | string | — | Exact person type filter |
| `public_figure` | boolean | — | Filter by public-figure flag |
| `title` | string | — | Case-insensitive substring match on title |
| `affiliation` | string | — | Case-insensitive substring match on affiliation |
| `nature` | string | — | People with at least one linked mention of this nature in the project |
| `min_mentions` | integer | `0` | Minimum project mention count |
| `sort` | string | `sort_key` | `sort_key`, `recent`, or `label` (alias for `sort_key`) |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

See [Pagination](../conventions/pagination.md) for the list response envelope.

### Sort order

- **`sort_key`** (default) — last name, then full display label (catalog sort order)
- **`recent`** — most recently active people first (based on canonical updates and linked mention activity)
- When `q` is set and `sort` is not `recent`, stronger label matches appear first

## Response `200`

```json
{
  "items": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "slug": "jane-doe",
      "label": "Jane Doe",
      "stylebook_slug": "default",
      "title": "Mayor",
      "affiliation": "City Hall",
      "public_figure": true,
      "person_type": "elected_official",
      "counts": {
        "mentions": 3,
        "stories": 2
      }
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 1
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Canonical person UUID |
| `slug` | string | URL-safe slug |
| `label` | string | Display name |
| `stylebook_slug` | string \| null | Stylebook catalog slug for this record |
| `title` | string \| null | Job title or role when set |
| `affiliation` | string \| null | Organization or affiliation when set |
| `public_figure` | boolean | Whether the person is flagged as a public figure |
| `person_type` | string \| null | Person type when set |
| `counts` | object | Project-scoped activity totals |
| `counts.mentions` | integer | Linked mention rows in the project |
| `counts.stories` | integer | Distinct articles with at least one linked mention |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/people/search\
?q=Mayor&affiliation=City%20Hall&person_type=elected_official&limit=10" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` |

## Related

- [Metadata](../taxonomy/index.md) — Mention Meta and Entity Meta
- [Types](types.md) — discover filter values in your project
- [Get person](get-person.md) — fetch one result by id
- [People overview](index.md)
