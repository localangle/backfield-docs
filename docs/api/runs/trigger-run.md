# Trigger run

```
POST /public/v1/projects/{project_slug}/runs
```

Start an Agate run for a graph that belongs to the project and is enabled for public API trigger. The response returns immediately with a run handle; poll [Get run](get-run.md) for progress.

Requires a **service** project API key with the **`runs:trigger`** scope. Read-only user keys receive **403**.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Request body

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `graph_id` | string | yes | Agate graph id (must belong to the project in the URL) |
| `inputs` | object | no | Per-alias ingress overrides. Omitted → use saved graph ingress params (same as a UI run). |

```json
{
  "graph_id": "550e8400-e29b-41d4-a716-446655440000",
  "inputs": {
    "article": {
      "text": "Body text to process."
    }
  }
}
```

## Idempotent retries

Send `Idempotency-Key` when a client might retry a trigger after a timeout or
lost response:

```http
Idempotency-Key: import-2026-07-18-001
```

The key must be 1–128 characters, start with a letter or number, and contain
only letters, numbers, `.`, `_`, `~`, `:`, `/`, `=`, `+`, or `-`. Keys are
scoped to the project and retained for seven days.

- The first request creates a run.
- Repeating the key with the same canonical JSON body returns the current
  snapshot of the original run and adds `Idempotency-Replayed: true`.
- Reusing the key with a different body returns `409`.
- If an identical concurrent request is still creating the original run, the
  API returns `409` with `Retry-After`; retry after that delay.

Only a SHA-256 hash of the canonical request body is retained with the key. The
request body and credentials are not stored in the idempotency record.

### Ingress aliases

Each ingress node declares a stable **`public_alias`** in its graph params. When **Enable API runs** is on, Agate sets this from the node name (for example **Text Input** → `text_input`). When `inputs` is provided, it must contain **exactly one** key matching that alias.

Supported ingress types (one per graph):

| Node type | `inputs[alias]` shape | Notes |
| --- | --- | --- |
| **TextInput** | `{ "text": "<non-empty string>" }` | Replaces saved `params.text` |
| **JSONInput** | JSON object with a resolvable article body | Same keys as the node panel (`text`, `headline`, …); normalized at run time |
| **S3Input** | `{ "bucket"?, "prefix"?, "max_files"? }` | Merged over saved node params; `prefix` maps to `folder_path`; `max_files` capped server-side (max 10,000) |

At trigger time the API computes an effective graph spec (saved params merged with `inputs`) and pins it on the run. Text and JSON payloads become processed-item input; S3 location params are read from the pinned spec during batch setup.

## Response `202`

The API returns `202 Accepted` with:

| Header | Description |
| --- | --- |
| `Location` | Relative URL for [Get run](get-run.md) |
| `Retry-After` | Initial polling delay in seconds |
| `Idempotency-Replayed` | Present as `true` only when returning an existing run |

```json
{
  "run_id": "660e8400-e29b-41d4-a716-446655440001",
  "status": "running",
  "counts": {
    "total": 1,
    "pending": 0,
    "running": 1,
    "succeeded": 0,
    "failed": 0
  },
  "created_at": "2026-06-25T12:00:00Z",
  "updated_at": "2026-06-25T12:00:00Z",
  "error_message": null
}
```

### Response fields

| Field | Type | Description |
| --- | --- | --- |
| `run_id` | string | Agate run UUID |
| `status` | string | Run status — `pending`, `running`, `succeeded`, or `failed` |
| `counts` | object | Processed-item counts (see below) |
| `counts.total` | integer | Total processed items |
| `counts.pending` | integer | Items not yet started |
| `counts.running` | integer | Items currently executing |
| `counts.succeeded` | integer | Items that finished successfully |
| `counts.failed` | integer | Items that failed or timed out |
| `created_at` | string | ISO 8601 timestamp |
| `updated_at` | string | ISO 8601 timestamp |
| `error_message` | string \| null | Run-level error when `status` is `failed` |

S3 batch runs often return `status: "pending"` with all counts zero until batch setup lists objects and creates processed items.

## Example

```bash
curl -X POST "https://api.{organization_slug}.backfield.news/public/v1/projects/general/runs" \
  -H "Authorization: Bearer bfk_your_service_api_key" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: article-2026-07-18-001" \
  -d '{
    "graph_id": "550e8400-e29b-41d4-a716-446655440000",
    "inputs": {
      "article": { "text": "City council approved the budget last night." }
    }
  }'
```

## Errors

| Status | When |
| --- | --- |
| `400` | Invalid `inputs` — unknown alias, empty text, bad shape |
| `401` | Missing or invalid API key |
| `403` | Missing `runs:trigger` scope; graph not enabled for public API runs |
| `404` | Unknown project or `graph_id` not in this project |
| `409` | Idempotency key is in progress, refers to a missing run, or was reused with a different body |
| `422` | Invalid request body or `Idempotency-Key` format |
| `429` | Run-trigger rate limit exceeded; wait for `Retry-After` |

## Related

- [Get run](get-run.md) — poll status after trigger
- [Runs overview](index.md)
- [Authentication](../authentication.md) — service keys and scopes
