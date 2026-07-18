# Mentions

Mentions are evidence rows that link articles to people, organizations, and locations. Each mention includes a display label, optional link to a canonical record, mention nature, and text spans showing where the reference appears in the story.

## How mention queries are organized

Mentions can be reached from several starting points:


| Starting point                   | Use when                                                            | Doc                                                                                               |
| -------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Project-wide**                 | Search mentions across all articles in a project                    | [List and search](search.md)                                                                      |
| **Article-first**                | You have an article and want its mentions                           | [Detail endpoints](../articles/hub/index.md)                                                      |
| **Entity-first (people)**        | You have a person and want their stories or mention evidence        | [List articles](../people/list-articles.md), [List mentions](../people/mentions.md)               |
| **Entity-first (organizations)** | You have an organization and want their stories or mention evidence | [List articles](../organizations/list-articles.md), [List mentions](../organizations/mentions.md) |
| **Entity-first (locations)**     | You have a place and want its stories or mention evidence           | [List articles](../locations/list-articles.md), [List mentions](../locations/mentions.md)         |
| **Entity mention timeline**      | You want mention counts by publication date for one entity          | [Mention timeline](../other/mention-timeline/index.md)                                              |


Project-wide routes search across articles. Article-first routes return mentions for one story. Entity-first routes return mentions for one canonical record across the project, using the same **`nature`**, article metadata, publication date, and **`quote`** filters as [List and search](search.md), plus entity-specific **`sort`** and **`sort_direction`**.

## Mention object (shared fields)

Mention responses vary slightly by route, but commonly include:

- `mention_id` — mention id (not on [List mentions](../articles/hub/mentions.md); present on typed and entity-first routes)
- `label` — display label for the reference
- `entity_type` — `person`, `organization`, or `location` (project-wide search only; omitted on entity-first routes)
- `nature` — editorial role when set — values depend on entity type; see [Mention Meta](../taxonomy/mention-meta/index.md)
- `canonical` — linked canonical record (`id`, `slug`, `label`) when available (project-wide search only)
- `evidence` — first occurrence text span on list routes: `mention_text`, `quote`, `start_char`, and `end_char`
- `occurrences` — all non-suppressed spans on [Get mention](get-mention.md)
- `article` — article summary (`id`, `headline`, `url`, `pub_date`) on project-wide and entity-first routes

Several list routes accept **`quote=true`** to return only mentions whose first evidence span is a quote — [List mentions](../articles/hub/mentions.md), [List and search](search.md), and entity-first [List mentions](../people/mentions.md) routes.

Entity-first mention lists ([people](../people/mentions.md), [organizations](../organizations/mentions.md), [locations](../locations/mentions.md)) share the article and mention filter vocabulary with project-wide search. They add **`sort`** / **`sort_direction`**, echo the canonical `{type}_id` and `label`, and omit redundant fields such as `entity_type` and `canonical` on each item.

## Endpoints

### Project-wide


| Method | Path                                    | Doc                           |
| ------ | --------------------------------------- | ----------------------------- |
| `GET`  | `…/mentions/{entity_type}/{mention_id}` | [Get mention](get-mention.md) |
| `GET`  | `…/mentions/search`                     | [List and search](search.md)  |
| `GET`  | `…/mentions/facets`                     | [Mention facets](facets.md)   |


### Article-first


| Method | Path                                    | Doc                                                    |
| ------ | --------------------------------------- | ------------------------------------------------------ |
| `GET`  | `…/articles/{article_id}/mentions`      | [List mentions](../articles/hub/mentions.md)           |
| `GET`  | `…/articles/{article_id}/people`        | [List people](../articles/hub/people.md)               |
| `GET`  | `…/articles/{article_id}/organizations` | [List organizations](../articles/hub/organizations.md) |
| `GET`  | `…/articles/{article_id}/locations`     | [List locations](../articles/hub/locations.md)         |


### Entity-first


| Method | Path                                         | Doc                                                |
| ------ | -------------------------------------------- | -------------------------------------------------- |
| `GET`  | `…/people/{person_id}/articles`              | [List articles](../people/list-articles.md)        |
| `GET`  | `…/people/{person_id}/mentions`              | [List mentions](../people/mentions.md)             |
| `GET`  | `…/organizations/{organization_id}/articles` | [List articles](../organizations/list-articles.md) |
| `GET`  | `…/organizations/{organization_id}/mentions` | [List mentions](../organizations/mentions.md)      |
| `GET`  | `…/locations/{location_id}/articles`         | [List articles](../locations/list-articles.md)     |
| `GET`  | `…/locations/{location_id}/mentions`         | [List mentions](../locations/mentions.md)          |


### Planned


| Method | Path                         | Purpose                         |
| ------ | ---------------------------- | ------------------------------- |
| `POST` | `…/mentions/semantic-search` | Natural-language mention search |


## Related

- [Articles](../articles/index.md) — article search and [detail endpoints](../articles/hub/index.md)
- [Entities](../entities/index.md) — canonical people, locations, and organizations
- [Pagination](../conventions/pagination.md) — list response envelope

