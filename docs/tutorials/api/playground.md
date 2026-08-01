# Use the API Playground

Explore project-scoped endpoints interactively before writing application code.

!!! note "Tutorial outline"
    Detailed requests, responses, and screenshots are still to come.

## You'll learn

- How to authorize the Playground with a project API key.
- How path, query, and request-body fields are represented.
- How to read response status, headers, and JSON.
- How to translate a successful request into code without copying secrets.

## Before you begin

Create a temporary personal key by following
[Create and protect an API key](create-api-key.md). Use a project that already
contains at least one processed article.

## Planned walkthrough

1. Open the API Playground and authorize with the temporary key.
2. Request the current project and inspect its identity.
3. List recent articles with a small page size.
4. Open one article and compare its API fields with Agate.
5. Add a filter and observe validation for an invalid value.
6. Copy the generated request into a local client while keeping the key in an
   environment variable.
7. Clear authorization and revoke the tutorial key.

## Related concepts

- [API Playground](../../api/playground.md)
- [Pagination](../../api/conventions/pagination.md)
- [Errors](../../api/conventions/errors.md)
