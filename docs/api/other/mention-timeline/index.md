# Mention timeline

Timeline endpoints return mention counts grouped by article publication date for one canonical person, organization, or location. Use them to chart how often an entity appears in coverage over time without paginating through individual mention rows.

Each day bucket counts mentions in articles with a non-null `pub_date`. Items are ordered chronologically by `pub_date` ascending. Articles without a publication date are omitted.

## Endpoints


| Method | Path                                                  | Use when                                            | Doc                             |
| ------ | ----------------------------------------------------- | --------------------------------------------------- | ------------------------------- |
| `GET`  | `…/people/{person_id}/mentions/timeline`              | Chart mention volume for one person over time       | [Get timeline](get-timeline.md) |
| `GET`  | `…/organizations/{organization_id}/mentions/timeline` | Chart mention volume for one organization over time | [Get timeline](get-timeline.md) |
| `GET`  | `…/locations/{location_id}/mentions/timeline`         | Chart mention volume for one location over time     | [Get timeline](get-timeline.md) |


All three routes share the same query parameters and `items` shape. The response echoes the entity id and label (`person_id`, `organization_id`, or `location_id`).

## Related

- [List mentions](../../people/mentions.md) — paginated mention evidence with full filter vocabulary
- [Mentions overview](../../mentions/index.md) — how mention queries are organized
- [Other overview](../index.md)

