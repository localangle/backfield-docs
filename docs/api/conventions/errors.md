# Errors

Every Public API error uses the same envelope:

```json
{
  "error": {
    "code": "bad_request",
    "message": "Invalid pub_date_from. Use YYYY-MM-DD.",
    "details": null
  },
  "request_id": "req_01J..."
}
```

`error.code` is a stable, machine-readable identifier. `error.message` is for
people. `error.details` is `null` for simple errors and contains structured
context when available. `request_id` matches the `X-Request-ID` response header.

## Status codes

| Status | Meaning |
| --- | --- |
| `400` | Malformed request or invalid parameter (e.g. bad date format) |
| `401` | Missing or invalid API key |
| `403` | API key lacks access to the requested project |
| `404` | Project, article, or canonical not found — or outside caller scope |
| `409` | Request conflicts with existing state, including an idempotency-key conflict |
| `422` | Path, query, header, or JSON body validation failed |
| `429` | A per-key or project rate limit was exceeded |
| `503` | Requested capability is temporarily unavailable |

## Not found responses

For privacy and security, **404** can mean either "does not exist" or "not accessible with this API key."

Treat it as "not found in this project for this key."

## Validation examples

Invalid date on article search:

```json
{
  "error": {
    "code": "bad_request",
    "message": "Invalid pub_date_from. Use YYYY-MM-DD.",
    "details": null
  },
  "request_id": "req_01J..."
}
```

## Request validation (`422`)

Validation failures retain the shared envelope. The individual validation
issues appear in `error.details`:

```json
{
  "error": {
    "code": "validation_error",
    "message": "Request validation failed.",
    "details": [
      {
        "type": "missing",
        "loc": ["body", "query"],
        "msg": "Field required",
        "input": {}
      }
    ]
  },
  "request_id": "req_01J..."
}
```

Each item identifies the invalid input location and validation message. Clients
can parse one envelope for both application errors and request validation.

## Error codes

| Code | Typical status |
| --- | --- |
| `bad_request` | `400` |
| `unauthorized` | `401` |
| `forbidden` | `403` |
| `not_found` | `404` |
| `conflict` | `409` |
| `validation_error` | `422` |
| `rate_limit_exceeded` | `429` |
| `service_unavailable` | `503` |

See [Rate limits](rate-limits.md) for retry headers on `429` responses.
