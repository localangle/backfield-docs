# Settings

Settings are where you configure the shared services your projects rely on — the AI models that read your text, the outside services that geocode places and store files, and the keys that let your own applications reach your data.

## How settings are layered

Most settings follow the same pattern: an **organization** default that applies everywhere, with optional **project** overrides where a particular team needs something different.

This means an administrator can configure shared, approved services once, and individual projects can adjust them without exposing sensitive credentials to everyone.

## In this section

| Page | What it covers |
| --- | --- |
| [AI models](ai-models.md) | The approved AI models flows can use, and how cost is tracked |
| [Integrations](integrations.md) | Outside services for geocoding, web search, and file storage |
| [API keys](api-keys.md) | Keys that let your own applications query the [Public API](../../api/index.md) |

!!! note "Who can change settings"
    Sensitive settings — especially provider credentials — are limited to administrators. See [Users & access](../concepts/users.md).
