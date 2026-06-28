# Organizations

Organizations are canonical records for companies, agencies, nonprofits, and other groups identified across project articles. Use organization endpoints to browse and search the organization catalog, retrieve organization detail, and explore mention evidence and Stylebook connections.

Each organization record includes a display label, organization type, and project-scoped **`counts`** (`mentions`, `stories`).

## Endpoints

| Method | Path | Use when | Doc |
| --- | --- | --- | --- |
| `GET` | `…/organizations/{organization_id}` | Show one organization's canonical fields | [Get organization](get-organization.md) |
| `GET` | `…/organizations` | Find organizations by name, type, or filters | [List and search](search.md) |
| `GET` | `…/organizations/search` | Find organizations by name, type, or filters | [List and search](search.md) |
| `GET` | `…/organizations/{organization_id}/articles` | Load paginated stories mentioning an organization | [List articles](list-articles.md) |
| `GET` | `…/organizations/{organization_id}/mentions` | Load paginated mention evidence per article | [List mentions](mentions.md) |
| `GET` | `…/organizations/{organization_id}/mentions/timeline` | Chart mention counts by publication date | [Get timeline](../other/mention-timeline/get-timeline.md) |
| `GET` | `…/organizations/{organization_id}/connections` | Load Stylebook relationships involving an organization | [List connections](connections.md) |

## Related

- [Entities overview](../entities/index.md) — shared entity-first pattern
- [People](../people/index.md) — similar entity routes
- [Entity Meta → Organizations](../taxonomy/entity-meta/organizations.md) — `organization_type` catalog
- [Organization types](types.md) — discover `organization_type` values in your project
