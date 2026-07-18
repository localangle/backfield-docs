# List connections

```http
GET /public/v1/projects/{project_slug}/organizations/{organization_id}/connections
```

Return Stylebook connections where the organization is either the `from` or `to` endpoint. Labels are resolved from canonical records when available.

Connections describe relationships between canonical entities — for example, an organization that employs a person or is located at a place.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `organization_id` | string | Canonical organization UUID |

## Response `200`

```json
{
  "organization_id": "550e8400-e29b-41d4-a716-446655440000",
  "connections": [
    {
      "id": 1,
      "from_entity_type": "organization",
      "from_entity_id": "550e8400-e29b-41d4-a716-446655440000",
      "from_label": "City Council",
      "to_entity_type": "person",
      "to_entity_id": "660e8400-e29b-41d4-a716-446655440001",
      "to_label": "Jane Doe",
      "description": null,
      "nature": "employs"
    }
  ]
}
```

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
| `nature` | string \| null | Relationship nature when set (e.g. `employs`) |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/organizations/550e8400-e29b-41d4-a716-446655440000/connections" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project or organization |

## Related

- [Get organization](get-organization.md) — canonical organization fields
- [Organizations overview](index.md)
