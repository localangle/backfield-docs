# Settings

Settings are where administrators configure the shared services and access
controls that projects rely on. Project pages also contain settings that apply
only to that project.

## How settings are layered

AI model and integration settings use an **organization** configuration with
project choices or overrides where a particular team needs something
different. API keys, user access, and Stylebook assignments follow their own
scopes rather than this inheritance pattern.

This means an administrator can configure shared, approved services once, and individual projects can adjust them without exposing sensitive credentials to everyone.

### Organization settings

Organization administrators manage:

- approved [AI models](ai-models.md) and their credentials;
- [integrations](integrations.md) for geocoding, web search, and S3;
- users, workspace access, and Stylebook editing rights;
- the organization's Stylebooks and default Stylebook.

Secrets are write-only after they are saved: the interface can show that a
credential exists, but does not display its value again.

### Project settings

A project can select among approved models and provide supported project-level
credentials or integration overrides. Project settings also show the
project's fixed Stylebook assignment and manage project
[API keys](api-keys.md).

An override affects only that project. Removing it returns the project to the
organization setting where fallback is supported.

## In this section

| Page | What it covers |
| --- | --- |
| [AI models](ai-models.md) | The approved AI models flows can use, and how cost is tracked |
| [Integrations](integrations.md) | Outside services for geocoding, web search, and file storage |
| [API keys](api-keys.md) | Keys that let your own applications use [Backfield API](../../api/index.md) |

!!! note "Who can change settings"
    Sensitive settings — especially provider credentials — are limited to administrators. See [Users & access](../concepts/users.md).
