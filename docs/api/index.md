# API Reference

Use the Backfield Public API to search and retrieve data that is created and managed by Agate and Stylebook.

The API is served over HTTPS, accepts JSON, and uses project API keys for authentication.

## Base URL

```text
https://api.{organization_slug}.backfield.news/public/v1
```

Local development environments may use:

```text
http://localhost:8004/public/v1
```

## Project-scoped URLs

Most endpoints retrieve data at the project level and therefore require a project slug.

```text
/projects/{project_slug}/…
```

The slug identifies the project you want to query. Your API key must have access to that project.

## Quick start

1. **Find your project slug.** API keys are scoped to a project. Use the slug from your Backfield project settings, or confirm access with [Get project](projects/get-project.md):
  ```bash
    curl "https://api.{organization_slug}.backfield.news/public/v1/projects/YOUR_PROJECT_SLUG" \
      -H "Authorization: Bearer bfk_your_project_api_key"
  ```
    A `200` response confirms the slug and returns project metadata. A `404` means the slug is wrong or your key cannot access that project.
2. **Call an endpoint** using that slug. Examples in these docs use `general` as a placeholder:
  ```bash
    curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general" \
      -H "Authorization: Bearer bfk_your_project_api_key"
  ```

## Browser clients and CORS

The Public API is generally intended for **server-side** integrations, not client-side interactions. For most applications you should send your project API key from a backend service, not from JavaScript.

The API applies CORS rules for Backfield product UIs (for example, local Agate and Stylebook on ports 5173 and 5175). Arbitrary third-party web origins are not allowed by default. If you need to call the API from a frontend app, route requests through your own backend (BFF or proxy) and keep the API key on the server.

See [Authentication](authentication.md) for key handling guidance.

## How these docs are organized

The API reference is organized by resource:


| Section                                  | Use it for                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------- |
| [Authentication](authentication.md)      | API keys and authorization headers                                        |
| [Examples](examples.md)                  | Common search and retrieval patterns with example requests                |
| [Conventions](conventions/pagination.md) | Pagination, [errors](conventions/errors.md), and shared response patterns |
| [Metadata](taxonomy/index.md)            | Article Meta, Mention Meta, Entity Meta, and filter value catalogs       |
| [Projects](projects/index.md)            | Checking project metadata and access                                      |
| [Articles](articles/index.md)            | Searching articles and retrieving article context                         |
| [Mentions](mentions/index.md)            | Querying mention evidence across articles and entities                    |
| [Entities](entities/index.md)            | Searching people, locations, and organizations                            |
| [Other](other/index.md)                  | Map aggregations, custom records, and [run trigger](runs/index.md)        |


