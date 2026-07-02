# API keys

**API keys** let your own applications and scripts read a project's data through the [Public API](../../api/index.md). Unlike a personal login, an API key is tied to a project and is meant to be used by software.

Keys begin with the prefix `bfk_` and are sent with each request in an authorization header. Each key is scoped to the project (or projects) it's allowed to access.

Treat API keys like passwords:

- Keep them on a server, not in browser code or a public repository.
- Share them only with the systems that need them.
- Replace a key if you suspect it's been exposed.

For the full request format and examples, see [Authentication](../../api/authentication.md) in the API reference.
