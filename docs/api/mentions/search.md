# List and search mentions

```
GET /public/v1/projects/{project_slug}/mentions/search
```

Search mentions across a project. Results span location, person, and organization mentions from all articles, with entity labels, mention nature, type-specific fields, optional canonical links, first-occurrence evidence, and nested article context.

Use this route when you need a project-wide mention feed — for example, monitoring who appears in local-government stories, or finding unlinked mentions that need review.

Entity-first routes ([List mentions for people](../people/mentions.md), [organizations](../organizations/mentions.md), [locations](../locations/mentions.md)) share the same **`nature`**, article metadata, publication date, and **`quote`** filters, plus entity-specific **`sort`** and **`sort_direction`**. They omit project-wide-only params such as `entity_type`, `q`, and `has_canonical`.

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Query parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `entity_type` | string | — | Filter to `location`, `person`, or `organization` |
| `q` | string | — | Keyword match on entity name (case-insensitive) |
| `nature` | string | — | Filter by mention `nature` (exact match) |
| `has_canonical` | boolean | — | When `true`, only mentions linked to a canonical record; when `false`, only unlinked |
| `author` | string | — | Filter by article byline (case-insensitive exact match) |
| `meta` | string | — | Repeatable metadata filter clause on the parent article (AND across clauses). Same grammar as [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta) |
| `location_type` | string | — | Filter location mentions by location type |
| `person_type` | string | — | Filter person mentions by person type |
| `organization_type` | string | — | Filter organization mentions by organization type |
| `public_figure` | boolean | — | Filter person mentions by public-figure flag |
| `quote` | boolean | — | When `true`, return only mentions whose first evidence span is a quote |
| `pub_date_from` | string | — | ISO date `YYYY-MM-DD`, inclusive lower bound on article `pub_date` |
| `pub_date_to` | string | — | ISO date `YYYY-MM-DD`, inclusive upper bound on article `pub_date` |
| `limit` | integer | `25` | Page size (1–100) |
| `offset` | integer | `0` | Offset for pagination |

See [Pagination](../conventions/pagination.md) for the list response envelope.

## Metadata filters

Article metadata filters apply to the **article** that contains each mention, not to the mention itself. Use the repeatable **`meta`** query parameter — see [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta) for clause grammar.

Use [Mention facets](facets.md) to discover mention-level values, or [Metadata](../taxonomy/index.md) for article metadata and full catalogs.

Example — people mentioned in local-government stories:

```text
?entity_type=person&meta=topic:local_government_politics
```

Example — unlinked location mentions:

```text
?entity_type=location&has_canonical=false
```

Example — quoted person mentions:

```text
?entity_type=person&quote=true
```

## Sort order

Results are ordered by article `pub_date` descending (nulls last), then `mention_id` descending.

## Response `200`

```json
{
  "items": [
    {
      "entity_type": "person",
      "mention_id": 2,
      "substrate_entity_id": 1,
      "label": "Jane Doe",
      "nature": "subject",
      "role_in_story": null,
      "location_type": null,
      "person_type": "elected_official",
      "organization_type": null,
      "title": "Mayor",
      "affiliation": "City Hall",
      "public_figure": true,
      "canonical": {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "slug": "jane-doe",
        "label": "Jane Doe",
        "stylebook_slug": "default"
      },
      "evidence": {
        "mention_text": "Jane Doe",
        "quote_text": null,
        "start_char": null,
        "end_char": null
      },
      "article": {
        "id": 1,
        "headline": "City council votes on budget",
        "url": "https://example.com/budget",
        "pub_date": "2024-03-01"
      }
    }
  ],
  "pagination": {
    "limit": 25,
    "offset": 0,
    "total": 3
  }
}
```

### Item fields

| Field | Type | Description |
| --- | --- | --- |
| `entity_type` | string | `location`, `person`, or `organization` |
| `mention_id` | integer | Mention id |
| `substrate_entity_id` | integer | Backfield entity id for this mention type |
| `label` | string | Display label |
| `nature` | string \| null | Mention nature when set |
| `role_in_story` | string \| null | Role in story when set |
| `location_type` | string \| null | Present on location mentions |
| `person_type` | string \| null | Present on person mentions |
| `organization_type` | string \| null | Present on organization mentions |
| `title` | string \| null | Present on person mentions |
| `affiliation` | string \| null | Present on person mentions |
| `public_figure` | boolean \| null | Present on person mentions |
| `canonical` | object \| null | Linked canonical record, when available |
| `evidence` | object \| null | First non-suppressed occurrence span |
| `article` | object | Article summary (`id`, `headline`, `url`, `pub_date`) |

Type-specific fields are `null` when they do not apply to the mention's entity type.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/mentions/search\
?entity_type=person&nature=subject&quote=true&meta=topic:local_government_politics&pub_date_from=2024-01-01&limit=10" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `400` | Invalid `entity_type`, invalid `pub_date_from` / `pub_date_to`, malformed `meta` clause, or more than 25 `meta` clauses |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` |

## Related

- [Mention facets](facets.md) — discover filter values for search UI
- [Article Meta](../taxonomy/article-meta/index.md) — `meta` clause grammar
- [Get mention](get-mention.md) — full occurrence evidence for one mention
- [List mentions (people)](../people/mentions.md) — mention evidence for one canonical person
- [Mentions overview](index.md)
