# People

People are canonical records for individuals identified across project articles. Use people endpoints to browse and search the person catalog, retrieve person detail, and explore mention evidence and Stylebook connections.

Each person record includes a display label, optional title and affiliation, person type, and project-scoped **`counts`** (`mentions`, `stories`).

## Endpoints

| Method | Path | Use when | Doc |
| --- | --- | --- | --- |
| `GET` | `…/people/{person_id}` | Show one person's canonical fields | [Get person](get-person.md) |
| `GET` | `…/people` | Find people by name, title, affiliation, or filters | [List and search](search.md) |
| `GET` | `…/people/search` | Find people by name, title, affiliation, or filters | [List and search](search.md) |
| `GET` | `…/people/{person_id}/articles` | Load paginated stories mentioning a person | [List articles](list-articles.md) |
| `GET` | `…/people/{person_id}/mentions` | Load paginated mention evidence per article | [List mentions](mentions.md) |
| `GET` | `…/people/{person_id}/mentions/timeline` | Chart mention counts by publication date | [Get timeline](../other/mention-timeline/get-timeline.md) |
| `GET` | `…/people/{person_id}/connections` | Load Stylebook relationships involving a person | [List connections](connections.md) |

## Related

- [Entities overview](../entities/index.md) — shared entity-first pattern
- [Organizations](../organizations/index.md) — similar entity routes
- [Entity Meta → People](../taxonomy/entity-meta/people.md) — `person_type` catalog
- [People types](types.md) — discover `person_type` values in your project
