# API keys

**API keys** let your own applications and scripts use a project's
[Backfield API](../../api/index.md). Editorial users do not need a key to work in
Agate or Stylebook. A key is for software and is tied to one project.

Open the project in **Agate**, select the **API** tab, and choose **New access key**. Keys begin with the prefix `bfk_` and are sent with each request in an authorization header.

The full secret is shown only once. Copy it to a password manager or secret store before closing the dialog.

Treat API keys like passwords:

- Keep them on a server, not in browser code or a public repository.
- Share them only with the systems that need them.
- Replace a key if you suspect it's been exposed.

## Personal and service keys

| Type | Use it for | Who manages it |
| --- | --- | --- |
| **Personal** | A script or tool operated on behalf of one user | The owner can rotate or revoke it; an organization administrator can revoke it |
| **Service** | Shared, trusted automation that should not depend on one person's account | Organization administrators |

Backfield rechecks a personal key owner's account, organization membership,
and project access on every request. Removing required access therefore
invalidates the key on its next request.

All keys can read the project. A service key can optionally receive the
`runs:trigger` scope when trusted automation must start a configured flow.

## Rotation and revocation

To rotate safely, create a replacement, update and test every client, then revoke the old key. Do not revoke the old key until the replacement is in use.

For bearer authentication, scopes, and request examples, see
[Authentication](../../api/authentication.md) in the API reference.
