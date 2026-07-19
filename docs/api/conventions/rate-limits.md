# Rate limits

The Public API uses one-minute fixed windows. Limits apply both to each API key
and to the project as a whole.

## Default limits

| Request class | Per key | Project aggregate |
| --- | ---: | ---: |
| Standard reads | 600/minute | 2,400/minute |
| Semantic, geographic, and geo-cell searches | 60/minute | 240/minute |
| Run triggers | 5/minute | 20/minute |

Successful responses include:

| Header | Meaning |
| --- | --- |
| `RateLimit-Limit` | Per-key limit for this request class |
| `RateLimit-Remaining` | Requests remaining, accounting for both key and project usage |
| `RateLimit-Reset` | Seconds until the current window resets |

When either limit is exceeded, the API returns `429` with the shared
[error envelope](errors.md), the three rate-limit headers, and `Retry-After`.
Wait at least that many seconds before retrying.

```http
HTTP/1.1 429 Too Many Requests
RateLimit-Limit: 60
RateLimit-Remaining: 0
RateLimit-Reset: 18
Retry-After: 18
X-Request-ID: req_01J...
```

```json
{
  "error": {
    "code": "rate_limit_exceeded",
    "message": "Public API rate limit exceeded.",
    "details": null
  },
  "request_id": "req_01J..."
}
```

Backfield may adjust limits by deployment. Use the response headers rather than
hard-coding retry timing. If the rate-limit service is temporarily unavailable,
requests are allowed through rather than failing authentication or API access.
