# Projects

Most public API routes are scoped to a project. Use project endpoints to
confirm access, read project metadata and summary stats, and discover the
Stylebook assigned to the project.

## Endpoints

| Method | Path | Doc |
| --- | --- | --- |
| `GET` | `…/projects/{project_slug}` | [Get project](get-project.md) |

## Project-scoped URLs

Once you know the project slug, other resources live under:

```text
/projects/{project_slug}/articles/…
/projects/{project_slug}/people/…
/projects/{project_slug}/locations/…
/projects/{project_slug}/organizations/…
```

Project slugs are unique within a Backfield organization. Your organization is
selected by the API host, and a project API key resolves its bound project
before Backfield validates `{project_slug}`. The slug must match the key's
project even if another organization has a project with the same slug.

## Related

- [API overview](../index.md)
- [Authentication](../authentication.md)
