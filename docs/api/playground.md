# API Playground

Use the hosted [Backfield API Playground](https://playground.backfield.news) to
explore the public OpenAPI contract, inspect endpoint parameters and schemas,
and send requests to your Backfield tenant.

The Playground loads the public contract from:

```text
https://api.{organization_slug}.backfield.news/public/v1/openapi.json
```

The schema endpoint is public and does not require an API key. It contains only
the `/public/v1` consumer surface and declares project API keys as Bearer
authentication.

## Key handling

Project API keys entered in the Playground are held in browser memory only.
They are not written to local storage, session storage, cookies, or the
Playground server. Reloading or closing the page clears the key.

Use a key scoped to the project you are exploring. Because the key is still
present in the active browser tab while you use it:

- use the Playground only on a trusted device;
- do not paste keys into screenshots, support messages, or shared recordings;
- clear the key or close the tab when finished;
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
