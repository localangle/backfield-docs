# Get run

```
GET /public/v1/projects/{project_slug}/runs/{run_id}
```

Return run status, processed-item counts, and timestamps for one run in the project. Use this to poll after [Trigger run](trigger-run.md).

Any valid project API key may call this route. Triggering a run requires **`runs:trigger`**; polling does not.

The response does not include per-item bodies, AI costs, or review overlays.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |
| `run_id` | string | Run UUID from [Trigger run](trigger-run.md) |

## Response `200`

Same body shape as [Trigger run](trigger-run.md#response-202):

```json
{
  "run_id": "660e8400-e29b-41d4-a716-446655440001",
  "status": "succeeded",
  "counts": {
    "total": 1,
    "pending": 0,
    "running": 0,
    "succeeded": 1,
    "failed": 0
  },
  "created_at": "2026-06-25T12:00:00Z",
  "updated_at": "2026-06-25T12:05:00Z",
  "error_message": null
}
```

`counts` reflect processed-item row statuses when items exist. For single-item text/JSON runs before items are materialized, counts may be inferred from run status.

When `status` is `pending` or `running`, the response includes `Retry-After`
with the recommended polling delay in seconds. Terminal responses omit it.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/runs/660e8400-e29b-41d4-a716-446655440001" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project or run not belonging to this project |
| `429` | Read rate limit exceeded; wait for `Retry-After` |

## Related

- [Trigger run](trigger-run.md)
- [Runs overview](index.md)
