# FAQ

## General

??? question "What is Backfield?"
    Backfield turns unstructured news stories into durable, structured data. It extracts and enriches people, places, organizations, article metadata, and custom records; supports editorial review; and exposes the resulting data through a Public API.

??? question "What can I build with Backfield data?"
    Examples include geographically targeted news feeds, coverage and sourcing audits, knowledge graphs, semantic search, analytics enriched with editorial taxonomies, and products built from structured recipes, obituaries, events, or other custom records.

??? question "Can I run Backfield locally?"
    Yes. The public repository supports local development and source inspection. Follow the [Backfield quickstart](https://github.com/localangle/backfield#quickstart). The initial setup uses `make bootstrap` followed by `backfield init`.

??? question "Can I self-host Backfield in production from the public repository?"
    Not as a supported deployment path today. The repository includes local development tooling, but does not supply the production infrastructure and image-delivery setup needed for supported self-hosting. [Contact Local Angle](https://localangle.co) to discuss deployment.

## API

??? question "How do I get an API key?"
    Open your project in Agate, select the **API** tab, and choose **New access key**. The secret is shown only once, so copy it to a password manager or secret store before closing the dialog. See [Authentication](../api/authentication.md).

??? question "Are there rate limits?"
    Yes. Limits apply per API key and to the project in one-minute windows. Responses include standard rate-limit headers; a `429` response includes `Retry-After`. See [Rate limits](../api/conventions/rate-limits.md).

??? question "Where can I try the API?"
    Use the hosted [API Playground](https://playground.backfield.news). It loads your tenant's public OpenAPI contract and keeps an entered key in browser memory only; reloading or closing the page clears it.

??? question "Where is the OpenAPI schema?"
    Each tenant exposes its public schema without authentication:

    ```text
    https://api.{organization_slug}.backfield.news/public/v1/openapi.json
    ```

??? question "What should I include when asking about a failed API request?"
    Include the endpoint, HTTP method and status, a sanitized response body, and the `X-Request-ID` response header (or matching `request_id` in the error body). Never include the API key or sensitive article data.

??? question "Why do I get a 404 for a project or resource that exists?"
    API keys are scoped to a project. A resource outside the key's project may appear as not found. Confirm that `{project_slug}` matches the project that issued the key and test access with [Get project](../api/projects/get-project.md).

## Contributions and security

??? question "How do I report a bug or request a feature?"
    Search the [Backfield issues](https://github.com/localangle/backfield/issues) first. Then use the [bug report](https://github.com/localangle/backfield/issues/new?template=bug_report.yml) or [feature request](https://github.com/localangle/backfield/issues/new?template=feature_request.yml) form. See [Support](index.md) for what to include.

??? question "How do I contribute code?"
    Start with [CONTRIBUTING.md](https://github.com/localangle/backfield/blob/main/CONTRIBUTING.md). Keep changes focused and run `make lint` and `make test` before opening a pull request.

??? question "How do I report a security vulnerability?"
    Do not open a public issue. Use [GitHub private vulnerability reporting](https://github.com/localangle/backfield/security/advisories/new). If that is unavailable, email [opensource@localangle.co](mailto:opensource@localangle.co) with the subject `Security report: Backfield`.
