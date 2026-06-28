# Article facets

Article facets is a **convenience endpoint** for frontend applications. It returns the distinct filter values commonly needed to populate article search controls — authors and preset metadata categories — in a single response.

The same values are available through `GET …/articles/metadata/types` and related routes, but facets avoid multiple round trips when you are building search UI. For the full metadata reference, see [Metadata](../taxonomy/index.md).

```text
GET /public/v1/projects/{project_slug}/articles/facets
```

## Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `project_slug` | string | Project slug |

## Response `200`

```json
{
  "authors": ["Jane Doe", "Sam Rivera"],
  "format_categories": ["news", "opinion"],
  "topic_categories": ["local_government_politics", "public_safety"],
  "subject_categories": ["government_action", "development_project"]
}
```

## Response fields

| Field | Type | Description |
| --- | --- | --- |
| `authors` | array of strings | Distinct article authors in the project |
| `format_categories` | array of strings | Distinct `format` metadata categories |
| `topic_categories` | array of strings | Distinct `topic` metadata categories (broad subject areas) |
| `subject_categories` | array of strings | Distinct `subject` metadata categories (concrete primary subjects) |

Values are returned alphabetically and omit blank values.

## Example

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/facets" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Using facets with article filters

Facets supply **values** for filter UI. On any article-metadata filter endpoint, use the repeatable **`meta`** parameter (or JSON `meta` array on POST routes) for **query syntax** — see [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta).

```text
?meta=topic:local_government_politics
?meta=subject:development_project
?meta=topic:local_government_politics&meta=!format:opinion
```

Mapping:

- `topic_categories` → `meta=topic:…`
- `subject_categories` → `meta=subject:…`
- `format_categories` → `meta=format:…`

See [Article Meta](../taxonomy/article-meta/index.md) for standard category values, display labels, and advanced patterns (OR within a type, negation, same-type AND).

## Errors

| Status | When |
| --- | --- |
| `401` | Missing or invalid API key |
| `403` | API key not valid for this project |
| `404` | Unknown project |

## Related

- [Metadata overview](../taxonomy/index.md)
- [List and search](search.md)
- [Mention facets](../mentions/facets.md)
