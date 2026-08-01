# API Reference

Use the Backfield Public API to search and retrieve data that is created and managed by Agate and Stylebook.

The API is served over HTTPS, accepts JSON, and uses project API keys for authentication.

Explore the contract interactively in your organization's
[API Playground](playground.md). The Playground keeps API keys in tab-scoped
session storage so they survive a reload without persisting as long-term
browser data.

## Base URL

```text
https://api.{organization_slug}.backfield.news/public/v1
```

Replace `{organization_slug}` with your Backfield organization slug. The host
selects your organization; project slugs are unique within an organization, not
across all Backfield clients.

Local development environments may use:

```text
http://localhost:8004/public/v1
```

## Project-scoped URLs

Most endpoints retrieve data at the project level and therefore require a project slug.

```text
/projects/{project_slug}/…
```

The slug identifies the project you want to query. A project API key is bound
to one project, and the path slug must match that project. The organization and
project context come from the validated key; request headers cannot redirect a
project key to another tenant or project.

## Quick start

1. **Find your project slug.** API keys are scoped to a project. Use the slug from your Backfield project settings, or confirm access with [Get project](projects/get-project.md):
  ```bash
    curl "https://api.{organization_slug}.backfield.news/public/v1/projects/YOUR_PROJECT_SLUG" \
      -H "Authorization: Bearer bfk_your_project_api_key"
  ```
    A `200` response confirms the slug and returns project metadata. A `403`
    means the key is bound to a different project; a `404` means the project or
    resource is not found in the resolved scope.
2. **Call an endpoint** using that slug. Examples in these docs use `general` as a placeholder:
  ```bash
    curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general" \
      -H "Authorization: Bearer bfk_your_project_api_key"
  ```

## Browser clients and CORS

The Public API is generally intended for **server-side** integrations, not client-side interactions. For most applications you should send your project API key from a backend service, not from JavaScript.

The API applies CORS rules for Backfield product UIs (for example, local Agate and Stylebook on ports 5173 and 5175). Arbitrary third-party web origins are not allowed by default. If you need to call the API from a frontend app, route requests through your own backend (BFF or proxy) and keep the API key on the server.

See [Authentication](authentication.md) for key handling guidance.

## OpenAPI

Each tenant serves the public-only OpenAPI 3.1 contract without authentication:

```text
https://api.{organization_slug}.backfield.news/public/v1/openapi.json
```

The document uses the tenant host as its server and keeps `/public/v1` in every
path. It declares project API keys as HTTP Bearer authentication. See
[API Playground](playground.md) for interactive use.

## How these docs are organized

The API reference is organized by resource:


| Section                                  | Use it for                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------- |
| [Authentication](authentication.md)      | API keys and authorization headers                                        |
| [API Playground](playground.md)          | Explore the OpenAPI contract and try requests safely                       |
| [Examples](examples.md)                  | Common search and retrieval patterns with example requests                |
| [Conventions](conventions/pagination.md) | Pagination, [errors](conventions/errors.md), [rate limits](conventions/rate-limits.md), and shared response patterns |
| [Metadata](taxonomy/index.md)            | Article Meta, Mention Meta, Entity Meta, and filter value catalogs       |
| [Projects](projects/index.md)            | Checking project metadata and access                                      |
| [Articles](articles/index.md)            | Searching articles and retrieving article context                         |
| [Mentions](mentions/index.md)            | Querying mention evidence across articles and entities                    |
| [Entities](entities/index.md)            | Searching people, locations, and organizations                            |
| [Other](other/index.md)                  | Map aggregations, custom records, and [run trigger](runs/index.md)        |


