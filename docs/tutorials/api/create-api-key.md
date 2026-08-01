# Create and protect an API key

Create a project-scoped personal or service key, test it, and rotate or revoke
it without exposing the secret.

!!! note "Tutorial outline"
    Detailed requests, responses, and screenshots are still to come.

## You'll learn

- When to use a personal key and when to use a service key.
- How project access, user status, and key status affect authorization.
- Why the full secret appears only once.
- How to rotate a key without interrupting a consuming application.

## Before you begin

You need access to the target project. For a service key, decide its purpose,
owner, storage location, and rotation process before creating it.

## Planned walkthrough

1. Open the project's **API** tab.
2. Create a temporary personal key for interactive work.
3. Copy the secret into an approved credential store.
4. Send an authenticated request to the current-project endpoint.
5. Inspect last-used information and key ownership.
6. Create a replacement, update the consumer, and verify the new key.
7. Revoke the old key.
8. Repeat with a purpose-specific service key.

## Related concepts

- [Authentication](../../api/authentication.md)
