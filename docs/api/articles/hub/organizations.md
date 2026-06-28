# List organizations

```
GET /public/v1/projects/{project_slug}/articles/{article_id}/organizations
```

List organizations mentioned in an article. Results include organization type, optional linked canonical records, mention nature, and evidence spans.

Use [List mentions](mentions.md) with `entity_type=organization` when you need a unified index across entity types. Use this route when you are building an organization-focused view for one story.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `article_id` | integer | Article id |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `nature` | string | — | Filter to mentions with this editorial `nature` (exact match), such as `actor` or `subject` |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

## Response `200`

```json
{
  "items": [
    {
      "mention_id": 18,
      "label": "City Council",
      "organization_type": "government",
      "canonical": {
        "id": "660e8400-e29b-41d4-a716-446655440002",
        "slug": "city-council",
        "label": "City Council",
        "stylebook_slug": "default"
      },
      "nature": "actor",
      "role_in_story": null,
      "evidence": {
        "mention_text": "City Council",
        "quote_text": "The City Council approved the budget",
        "start_char": 0,
        "end_char": 12
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

### Organization fields

| Field | Type | Description |
| --- | --- | --- |
| `mention_id` | integer | Mention id |
| `label` | string | Display name |
| `organization_type` | string \| null | Organization type when set |
| `canonical` | object \| null | Linked canonical record (`id`, `slug`, `label`, `stylebook_slug`), when available |
| `nature` | string \| null | Mention nature when set |
| `role_in_story` | string \| null | Role in story when set |
| `evidence` | object \| null | First occurrence evidence span |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1/organizations?nature=actor" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project or article |

## Related

- [List mentions](mentions.md) — unified mentions across entity types
- [Get organization](../../organizations/get-organization.md) — canonical organization detail
- [Detail endpoints overview](index.md)
