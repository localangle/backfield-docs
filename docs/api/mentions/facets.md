# Mention facets

Mention facets is a **convenience endpoint** for frontend applications. It returns the distinct filter values commonly needed to populate mention search controls — entity types, mention natures, and entity types on mention rows — in a single response.

The same values can be assembled from [Mention Meta](../taxonomy/mention-meta/index.md), [Entity Meta](../taxonomy/entity-meta/index.md), and entity types endpoints, but facets avoid multiple round trips when you are building search UI.

```text
GET /public/v1/projects/{project_slug}/mentions/facets
```

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Response `200`

```json
{
  "entity_types": ["location", "person", "organization"],
  "natures": ["actor", "primary", "subject"],
  "location_types": ["place"],
  "person_types": ["elected_official"],
  "organization_types": ["government"]
}
```

## Response fields

| Field | Type | Description |
| --- | --- | --- |
| `entity_types` | array of strings | Entity types that have at least one mention in the project |
| `natures` | array of strings | Distinct mention `nature` values across all entity types |
| `location_types` | array of strings | Distinct location types on location mentions |
| `person_types` | array of strings | Distinct person types on person mentions |
| `organization_types` | array of strings | Distinct organization types on organization mentions |

Values are returned alphabetically and omit blank values.

## Using facets with search

Pair facet values with the corresponding [List and search](search.md) parameters:

| Facet field | Search parameter |
| --- | --- |
| `entity_types` | `entity_type` |
| `natures` | `nature` |
| `location_types` | `location_type` |
| `person_types` | `person_type` |
| `organization_types` | `organization_type` |

For article metadata filters, use [Article facets](../articles/facets.md). See [Metadata](../taxonomy/index.md) for full vocabularies.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/mentions/facets" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown `project_slug` |

## Related

- [Metadata overview](../taxonomy/index.md)
- [List and search mentions](search.md)
- [Article facets](../articles/facets.md)
- [Mentions overview](index.md)
