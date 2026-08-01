# API keys

**API keys** let your own applications and scripts read a project's data through the [Public API](../../api/index.md). Unlike a personal login, an API key is tied to one project and is meant to be used by software. Project keys authenticate `/public/v1` only, not Backfield's internal APIs.

Open the project in **Agate**, select the **API** tab, and choose **New access key**. Keys begin with the prefix `bfk_` and are sent with each request in an authorization header.

The full secret is shown only once. Copy it to a password manager or secret store before closing the dialog.

Treat API keys like passwords:

- Keep them on a server, not in browser code or a public repository.
- Share them only with the systems that need them.
- Replace a key if you suspect it's been exposed.

Personal keys belong to the user who created them; that user can rotate or
revoke the key, and organization administrators can revoke it. Backfield
rechecks the owner's account, organization membership, and project access on
every request, so removing any required access invalidates the key immediately.
Legacy personal keys without an owner are rejected.

Service keys are ownerless credentials managed by organization administrators
for trusted automation. They can optionally receive the `runs:trigger` scope.

To rotate safely, create a replacement, update and test every client, then revoke the old key. Do not revoke the old key until the replacement is in use.

For the full request format and examples, see [Authentication](../../api/authentication.md) in the API reference.
