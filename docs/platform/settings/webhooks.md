# Webhooks

**Webhooks** let another application learn when important things happen in a
project — a flow run finishes, an article is saved, or a Stylebook canonical
record changes — without polling Backfield constantly.

Organization administrators configure webhooks in **Settings → Webhooks**. Each
endpoint belongs to one project, chooses which event types to receive, and can
listen to selected flows or every flow in the project.

## Signed delivery

Each notification is an HTTP POST with a signed payload. Your receiver can
verify the signature using the endpoint's signing secret before acting on the
event. Secrets are shown only when an endpoint is created or its signing secret
is rotated.

New endpoints stay inactive until a successful test delivery confirms that your
receiver accepts signed requests.

## What you can subscribe to

| Area | Examples |
| --- | --- |
| **Agate runs** | A run attempt reaches a finished state (succeeded or failed) |
| **Articles** | A new article is saved, an article is reprocessed, or review metadata changes |
| **Stylebook canonicals** | A canonical person, organization, or location is created, updated, merged, deleted, or gains or loses evidence |

Webhook bodies are intentionally thin. They identify what changed and include
links you can follow with a project [API key](api-keys.md) to load full run,
article, or canonical details through [Backfield API](../../api/index.md).

Stylebook canonicals can be shared across projects. When one canonical change
applies to several projects, each subscribed project receives its own
notification.

## Recovering missed events

Backfield keeps an immutable project event feed for 90 days. If your receiver
was down or an endpoint was paused, you can replay the feed from your last
processed position instead of relying on redelivered webhooks alone. See
[List project events](../../api/projects/list-events.md) in the API reference.

## Related

- [API keys](api-keys.md) — credentials your receiver uses to fetch full records
- [Settings overview](index.md) — how organization and project settings fit together
- [Projects](../concepts/projects.md) — what a project contains
