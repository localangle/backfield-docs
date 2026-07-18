# Authentication

All API requests require a **project API key**. Send the key as a Bearer token in the `Authorization` header.

## Header

```http
Authorization: Bearer bfk_<project_api_key>
```

Create keys in **Agate**: open the project, select its **API** tab, then choose **New access key**. A key belongs to that project only, so `{project_slug}` must identify the same project.

The full secret is displayed once, immediately after creation. Copy it to a password manager or secret store before closing the dialog; Backfield cannot show it again.

## Key types and scopes

| Key type | Scopes | Use when |
| --- | --- | --- |
| **User** | `read` (always) | Read-only integrations from a user account |
| **Service** | `read` (always) plus optional `runs:trigger` | Server-side automation; required to [trigger runs](runs/trigger-run.md) |

- **`read`** — query articles, mentions, entities, and other read routes.
- **`runs:trigger`** — call `POST …/runs`. May only be minted on **service** keys (org-admin gated). [Get run](runs/get-run.md) works with any project key that can access the project.

Do not expose API keys in browser code, mobile apps, logs, or public repositories. Rotate keys if they are shared accidentally.

Personal keys are owned by the user who created them. Their owner can rotate or revoke them; organization administrators can also revoke them. Service keys are managed by organization administrators.

For a safe rotation, create a replacement key, update every client and verify requests with the replacement, then revoke the old key. Revoking first causes clients using the old key to receive `401` responses.

## Request IDs

Every Public API response includes an `X-Request-ID` header. You may send your own `X-Request-ID`; otherwise Backfield generates one and returns it. Record this value when troubleshooting and include it with a support request so the server-side request can be traced.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/search?q=budget" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors


| Status | When                                                      |
| ------ | --------------------------------------------------------- |
| `401`  | Missing or invalid API key                                |
| `403`  | Key is valid but not authorized for the requested project |


If a project or resource cannot be found for your key, the API may return **404**. See [Errors](conventions/errors.md).

For unexpected errors, inspect the response's `X-Request-ID` header and retain it with the status code and response body.