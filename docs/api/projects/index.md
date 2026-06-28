# Projects

Most public API routes are scoped to a project. Use project endpoints to confirm access, read project metadata and summary stats, and discover the catalog used for entity data.

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

Your API key must have access to the project you query.

## Related

- [API overview](../index.md)
- [Authentication](../authentication.md)
