# Runs

Run endpoints let approved API clients trigger Agate graph runs and poll their status. Use them to send text or batch inputs into a configured flow and track progress until items finish.

Runs are **opt-in**: only graphs with **Enable API runs** turned on in Agate (`public_run_enabled: true`) can be triggered. Triggering requires a **service** project API key with the **`runs:trigger`** scope. Polling status uses the same project key (read access is sufficient).

The public API returns a minimal run summary — status, item counts, and timestamps. It does not expose per-item bodies, AI cost breakdowns, cancel/rerun, or review overlays (those remain on the Agate API).

## Endpoints

| Method | Path | Use when | Doc |
| --- | --- | --- | --- |
| `POST` | `…/runs` | Start a run for an enabled graph | [Trigger run](trigger-run.md) |
| `GET` | `…/runs/{run_id}` | Poll run status and item counts | [Get run](get-run.md) |

## How to use

1. Enable **Enable API runs** on the graph's content-source node in Agate (or set `public_run_enabled: true` via the Agate API).
2. Mint a **service** API key with the **`runs:trigger`** scope.
3. Call [Trigger run](trigger-run.md) with `graph_id`, optional `inputs`, and an
   `Idempotency-Key` when the request may be retried.
4. Follow the `Location` header and honor `Retry-After` while polling [Get
   run](get-run.md) until `status` is terminal (`succeeded` or `failed`) or
   `counts` show all items finished.

Text and JSON ingress runs usually return `status: "running"` with `counts.total: 1` immediately. S3 batch runs start as `pending` with zero counts until batch setup creates processed items.

Trigger responses use `202 Accepted`. Idempotency keys can safely replay the
same request for seven days; using a retained key with a different body returns
`409`. See [Trigger run](trigger-run.md#idempotent-retries).

## Related

- [Authentication](../authentication.md) — API keys and `runs:trigger` scope
- [Other overview](../other/index.md)
- [API overview](../index.md)
