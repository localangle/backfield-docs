# Get person

```
GET /public/v1/projects/{project_slug}/people/{person_id}
```

Return one canonical person by UUID.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `person_id` | string | Canonical person UUID |

## Response `200`

```json
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

`counts.stories` differs from `counts.mentions`: one person mentioned three times in the same article has `mentions` 3 and `stories` 1. Use [List articles](list-articles.md) for a deduplicated story feed; [List mentions](mentions.md) returns passage-level rows and may repeat the same article.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/people/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project, person, or inactive canonical record |

## Related

- [List mentions](mentions.md) — article evidence for this person
- [List articles](list-articles.md) — story feed for this person
- [List connections](connections.md) — Stylebook relationships
- [List and search](search.md) — find people by name or filters
