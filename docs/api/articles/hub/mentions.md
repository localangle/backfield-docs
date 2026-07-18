# List mentions

```http
GET /public/v1/projects/{project_slug}/articles/{article_id}/mentions
```

Return all mentions from an article (including people, organizations, and locations) in a single list. Results are ordered by mention `created_at` descending (newest first).

This route is **not paginated** — it returns the full filtered set as a JSON array. Use [List people](people.md), [List organizations](organizations.md), or [List locations](locations.md) when you need paginated, entity-type-specific rows with extra fields such as geometry or person title.

## Path parameters


| Name           | Type    | Description  |
| -------------- | ------- | ------------ |
| `project_slug` | string  | Project slug |
| `article_id`   | integer | Article id   |


## Query parameters


| Name          | Type    | Default | Description                                                                                                                                            |
| ------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `entity_type` | string  | —       | Filter to `location`, `person`, or `organization`                                                                                                      |
| `nature`      | string  | —       | Filter to mentions with this editorial `nature` (exact match). Values depend on entity type — see [Mention Meta](../../taxonomy/mention-meta/index.md) |
| `quote`       | boolean | —       | When `true`, return only mentions whose first evidence span is a quote                                                                                 |


Combine filters to narrow results. For example, `?entity_type=person&nature=subject` returns only people tagged as subjects in the story. `?quote=true` returns only quoted mentions.

## Response `200`

The response is a JSON **array** of mention objects:

```json
[
  {
    "entity_type": "person",
    "label": "Jane Doe",
    "nature": "subject",
    "role_in_story": null,
    "canonical": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "slug": "jane-doe",
      "label": "Jane Doe",
      "stylebook_slug": "default"
    },
    "evidence": {
      "mention_text": "Mayor Jane Doe announced the plan",
      "quote": true,
      "start_char": 120,
      "end_char": 128
    }
  },
  {
    "entity_type": "location",
    "label": "City Hall",
    "nature": "primary",
    "role_in_story": null,
    "canonical": null,
    "evidence": {
      "mention_text": "debate downtown",
      "quote": false,
      "start_char": 340,
      "end_char": 355
    }
  }
]
```

### Mention fields


| Field                      | Type          | Description                                              |
| -------------------------- | ------------- | -------------------------------------------------------- |
| `entity_type`              | string        | `location`, `person`, or `organization`                  |
| `label`                    | string        | Display label                                            |
| `nature`                   | string \| null | Editorial role when set                                  |
| `role_in_story`            | string \| null | Free-text summary of how the entity figures in the story |
| `canonical`                | object \| null | Linked canonical record, when available                  |
| `canonical.id`             | string        | Canonical UUID                                           |
| `canonical.slug`           | string \| null | Canonical slug                                           |
| `canonical.label`          | string        | Canonical display label                                  |
| `canonical.stylebook_slug` | string \| null | Stylebook catalog slug for the linked record             |
| `evidence`                 | object \| null | First non-suppressed occurrence span                     |


### Evidence fields

Article mention evidence uses a compact shape suited for story highlighting:


| Field          | Type           | Description                                                                                 |
| -------------- | -------------- | ------------------------------------------------------------------------------------------- |
| `mention_text` | string \| null  | Text to highlight — quote text when available, otherwise the matched mention text |
| `quote`        | boolean        | Whether the first occurrence is a quote                                                     |
| `start_char`   | integer \| null | Start character offset in the article                                                       |
| `end_char`     | integer \| null | End character offset in the article                                                         |


When `evidence` is `null`, no non-suppressed occurrence was found for the mention.

All public mention routes use this same evidence shape. Typed and entity-first routes also include `mention_id` on each row.

## Examples

All mentions for an article:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1/mentions" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

People who are subjects in the story:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1/mentions?entity_type=person&nature=subject" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Quoted mentions only:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1/mentions?quote=true" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors


| Status | When                               |
| ------ | ---------------------------------- |
| `400`  | Invalid `entity_type`              |
| `401`  | Missing or invalid API key         |
| `403`  | API key not valid for this project |
| `404`  | Unknown project or article         |


## Related

- [List people](people.md) — paginated people with title, affiliation, and type fields
- [List organizations](organizations.md) — paginated organizations with type fields
- [List locations](locations.md) — paginated locations with map-ready geometry
- [Articles overview](../index.md)

