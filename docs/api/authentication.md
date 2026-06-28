# Authentication

All API requests require a **project API key**. Send the key as a Bearer token in the `Authorization` header.

## Header

```http
Authorization: Bearer bfk_<project_api_key>
```

Keys are created in Agate, under a project's API settings. Each request must target a project the key may access.

## Key types and scopes

| Key type | Scopes | Use when |
| --- | --- | --- |
| **User** | `read` (always) | Read-only integrations from a user account |
| **Service** | `read` (always) plus optional `runs:trigger` | Server-side automation; required to [trigger runs](runs/trigger-run.md) |

- **`read`** — query articles, mentions, entities, and other read routes.
- **`runs:trigger`** — call `POST …/runs`. May only be minted on **service** keys (org-admin gated). [Get run](runs/get-run.md) works with any project key that can access the project.

Do not expose API keys in browser code, mobile apps, logs, or public repositories. Rotate keys if they are shared accidentally.

Every request is scoped to a project by `{project_slug}` in the URL. The API key must have access to that project.

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