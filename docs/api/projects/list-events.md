# List project events

```
GET /public/v1/projects/{project_slug}/events
```

Return an ascending, immutable feed of project events retained for 90 days.
Use this endpoint to recover missed [webhook](../../platform/settings/webhooks.md)
deliveries by replaying from the last cursor your consumer processed.

Events share the same versioned envelope as webhook payloads. Each item
includes a `cursor` you pass on the next request to continue forward.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug (e.g. `general`) |

## Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `cursor` | string | Opaque forward cursor from a previous response item. Omit on the first request. |
| `flow_id` | string | Repeat to limit results to events from specific flows. |
| `type` | string | Repeat to limit results to specific event types (for example `agate.run.completed`). |
| `limit` | integer | Page size from 1 to 100. Default `25`. |

## Response `200`

```json
{
  "items": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "cursor": "opaque-cursor-string",
      "type": "agate.run.completed",
      "schema_version": 1,
      "occurred_at": "2026-08-10T12:00:00Z",
      "flow": {"id": "flow-uuid", "name": "Daily extract"},
      "run": {"id": "run-uuid", "attempt": 1, "url": "https://..."},
      "article_id": null,
      "entity": {"type": null, "id": null},
      "data": {
        "outcome": "succeeded",
        "completion_reason": "completed",
        "failure_category": null,
        "counts": {"total": 3, "succeeded": 3, "failed": 0},
        "article_count": 2
      },
      "links": {
        "run": "https://.../runs/run-uuid",
        "articles": "https://.../articles?attempt=1"
      }
    }
  ],
  "next_cursor": "opaque-cursor-string",
  "retention_days": 90
}
```

| Field | Type | Description |
| --- | --- | --- |
| `items` | array | Events in ascending order |
| `items[].id` | string | Stable event UUID (use to deduplicate webhook deliveries) |
| `items[].cursor` | string | Pass as `cursor` on the next request |
| `items[].type` | string | Event type (for example `agate.run.completed`) |
| `items[].schema_version` | integer | Envelope version |
| `items[].occurred_at` | string | ISO 8601 timestamp |
| `items[].flow` | object | Flow id and name when the event is flow-scoped |
| `items[].run` | object | Run id, attempt, and URL when the event is run-scoped |
| `items[].article_id` | integer \| null | Article id for article events |
| `items[].entity` | object | Canonical entity type and id for Stylebook events |
| `items[].data` | object | Type-specific payload |
| `items[].links` | object | Public API URLs for related run, article, or canonical resources |
| `next_cursor` | string \| null | Cursor of the last item when more results may exist |
| `retention_days` | integer | How long events are kept (currently 90) |

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/events?limit=25" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Continue from a previous page:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/events?cursor=opaque-cursor-string" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Malformed `cursor` or unknown `type` filter |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` or project outside caller scope |
| `410` | `cursor` predates the retention window — restart without a cursor |

## Related

- [Projects overview](index.md)
- [Webhooks](../../platform/settings/webhooks.md)
- [Authentication](../authentication.md)
