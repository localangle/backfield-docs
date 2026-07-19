# List connections

```http
GET /public/v1/projects/{project_slug}/locations/{location_id}/connections
```

Return Stylebook connections where the location is either the `from` or `to` endpoint. Labels are resolved from canonical records when available.

Connections describe relationships between canonical entities — for example, a person who works at a location or an organization headquartered at a place.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `location_id` | string | Canonical location UUID |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `to_entity_type` | string | — | Filter the entity connected to this location to `person`, `organization`, or `location` |
| `nature` | string | — | Filter by relationship nature (exact match) |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

## Response `200`

```json
{
  "items": [
    {
      "id": 1,
      "from_entity_type": "person",
      "from_entity_id": "660e8400-e29b-41d4-a716-446655440001",
      "from_label": "Jane Doe",
      "to_entity_type": "location",
      "to_entity_id": "550e8400-e29b-41d4-a716-446655440000",
      "to_label": "City Hall",
      "description": "Jane Doe works from the mayor's office at City Hall.",
      "nature": "works_at"
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 1
  }
}
```

Connections are ordered by the connected entity's label, then entity type and
connection id. Despite its name, `to_entity_type` filters the entity on the
other side of the connection regardless of stored direction.

### Connection fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Connection id |
| `from_entity_type` | string | Source entity type (e.g. `person`, `location`, `organization`) |
| `from_entity_id` | string | Source entity UUID |
| `from_label` | string | Resolved display label for the source |
| `to_entity_type` | string | Target entity type |
| `to_entity_id` | string | Target entity UUID |
| `to_label` | string | Resolved display label for the target |
| `description` | string \| null | Human-readable description of the relationship when set |
| `nature` | string \| null | Relationship nature when set (e.g. `works_at`) |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/locations/550e8400-e29b-41d4-a716-446655440000/connections?to_entity_type=person&limit=10" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project or location |

## Related

- [Get location](get-location.md) — canonical location fields
- [Locations overview](index.md)
