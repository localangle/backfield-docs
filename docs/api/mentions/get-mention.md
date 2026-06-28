# Get mention

```
GET /public/v1/projects/{project_slug}/mentions/{entity_type}/{mention_id}
```

Return one mention with full occurrence evidence and article context. Use this after [List and search mentions](search.md) when you need every text span for a mention, not just the first occurrence.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `entity_type` | string | `location`, `person`, or `organization` |
| `mention_id` | integer | Mention id from search, typed article detail routes, or entity-first mention lists |

## Response `200`

Same core fields as [List and search](search.md) items, but `evidence` is replaced by `occurrences` — all non-suppressed spans ordered by `occurrence_order`.

```json
{
  "entity_type": "person",
  "mention_id": 2,
  "substrate_entity_id": 1,
  "label": "Jane Doe",
  "nature": "subject",
  "role_in_story": null,
  "location_type": null,
  "person_type": "elected_official",
  "organization_type": null,
  "title": "Mayor",
  "affiliation": "City Hall",
  "public_figure": true,
  "canonical": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "slug": "jane-doe",
    "label": "Jane Doe",
    "stylebook_slug": "default"
  },
  "occurrences": [
    {
      "mention_text": "Jane Doe",
      "quote_text": "Mayor Jane Doe announced the plan",
      "start_char": 120,
      "end_char": 128,
      "occurrence_order": 0
    }
  ],
  "article": {
    "id": 1,
    "headline": "City council votes on budget",
    "url": "https://example.com/budget",
    "pub_date": "2024-03-01"
  }
}
```

### Occurrence fields

| Field | Type | Description |
| --- | --- | --- |
| `mention_text` | string \| null | Matched mention text |
| `quote_text` | string \| null | Surrounding quote |
| `start_char` | integer \| null | Start character offset in the article |
| `end_char` | integer \| null | End character offset in the article |
| `occurrence_order` | integer \| null | Order of this span within the mention |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/mentions/person/2" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project, invalid `entity_type`, or mention not found in project |

## Related

- [List and search mentions](search.md)
- [Get article](../articles/get-article.md) — article summary for the same story
- [Get person](../people/get-person.md) / [Get organization](../organizations/get-organization.md) / [Get location](../locations/get-location.md) — canonical entity detail when `canonical` is set
- [Mentions overview](index.md)
