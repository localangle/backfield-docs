# API Playground

Use your organization's hosted API Playground to explore the public OpenAPI
contract, inspect endpoint parameters and schemas, and send requests to your
Backfield tenant. The Playground URL is client-specific; open it from Agate or
use the host provided for your organization.

Opening the Playground requires a signed-in Backfield session. If your account
belongs to more than one organization, select the organization whose project
you intend to query. The project API key still determines the API project
scope when you execute a request.

The Playground loads the public contract from:

```text
https://api.{organization_slug}.backfield.news/public/v1/openapi.json
```

The schema endpoint is public and does not require an API key. It contains only
the `/public/v1` consumer surface and declares project API keys as Bearer
authentication.

## Key handling

Project API keys entered in the Playground are written to tab-scoped browser
session storage. They are not written to long-lived local storage, cookies, or
the Playground server. A key survives a reload in the same tab and is removed
when you clear it, sign out, or close the tab under the browser's normal
session-storage lifecycle.

Use a key scoped to the project you are exploring. Because the key is still
present in the active browser tab while you use it:

- use the Playground only on a trusted device;
- do not paste keys into screenshots, support messages, or shared recordings;
- clear the key or sign out when finished;
- rotate the key if it may have been exposed.

For production applications, keep API keys in a server-side secret store and
call Backfield from your backend. See [Authentication](authentication.md).

## Tenant host

Set the server to your tenant host:

```text
https://api.YOUR_ORGANIZATION_SLUG.backfield.news
```

The paths in the OpenAPI document already include `/public/v1`; do not append
that prefix to the server URL a second time.
