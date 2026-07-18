# Get article

```http
GET /public/v1/projects/{project_slug}/articles/{article_id}
```

Return one article by id. The response includes article summary fields, metadata tags, a short preview, and attached images.

Use optional **`include`** tokens on detail only:

- `include=counts` — mention and entity totals, custom record counts, and the article `embedded` flag
- `include=text` — full article body in `text` (in addition to the always-included `preview`)

## Path parameters


| Name           | Type    | Description  |
| -------------- | ------- | ------------ |
| `project_slug` | string  | Project slug |
| `article_id`   | integer | Article id   |


## Query parameters


| Name      | Type   | Default | Description                                                                 |
| --------- | ------ | ------- | --------------------------------------------------------------------------- |
| `include` | string | —       | Repeatable include token. Supported: `counts`, `text`                       |


## Response `200`

Detail responses use the same core article shape as [List and search](search.md), plus an `images` array (up to 10 rows). Without `include=counts`, `counts` and `embedded` are present as `null`. Without `include=text`, `text` is omitted — only `preview` is returned for body content.

```json
{
  "id": 1,
  "headline": "City council votes on budget",
  "url": "https://example.com/budget",
  "author": "Jane Doe",
  "pub_date": "2024-03-01",
  "source": {
    "id": "example.com",
    "name": "example.com"
  },
  "preview": "The city council approved a revised budget after…",
  "metadata": [
    {
      "meta_type": "topic",
      "category": "local_government_politics",
      "confidence": 0.92
    }
  ],
  "images": [
    {
      "id": 10,
      "image_id": "img-1",
      "url": "https://example.com/photo.jpg",
      "caption": "Council chamber"
    }
  ],
  "embedded": true,
  "counts": {
    "mentions": {
      "locations": 1,
      "people": 1,
      "organizations": 1,
      "total": 3
    },
    "entities": {
      "locations": 1,
      "people": 1,
      "organizations": 1,
      "total": 3
    },
    "images": 1,
    "custom_records": {
      "contracts": 1
    }
  }
}
```

The example above includes `embedded` and `counts` because the request used `?include=counts`.

### Article fields


| Field                   | Type           | Description                                                                                                     |
| ----------------------- | -------------- | --------------------------------------------------------------------------------------------------------------- |
| `id`                    | integer        | Article id                                                                                                      |
| `headline`              | string         | Headline                                                                                                        |
| `url`                   | string \| null  | Source URL                                                                                                      |
| `author`                | string \| null  | Author                                                                                                          |
| `pub_date`              | string \| null  | Publication date (`YYYY-MM-DD`)                                                                                 |
| `source`                | object \| null  | Publication or outlet when known                                                                                |
| `source.id`             | string         | Stable source identifier — stored external source when set, otherwise the article URL hostname (without `www.`) |
| `source.name`           | string         | Display label for the outlet                                                                                    |
| `preview`               | string \| null  | Truncated body snippet (max 280 characters); always included on detail        |
| `text`                  | string \| null  | Present with `include=text` — full article body (alongside `preview`)       |
| `metadata`              | array           | Metadata tags                                                                 |
| `metadata[].meta_type`  | string         | Tag type (`format`, `topic`, `subject`, …)                                                                      |
| `metadata[].category`   | string         | Tag category value                                                                                              |
| `metadata[].confidence` | number         | Classifier confidence                                                                                           |
| `images`                | array          | Up to 10 inline images on detail responses                                                                      |
| `images[].id`           | integer        | Image record id                                                                                                 |
| `images[].image_id`     | string         | Stable image identifier                                                                                         |
| `images[].url`          | string         | Image URL                                                                                                       |
| `images[].caption`      | string \| null  | Caption when set                                                                                                |
| `embedded`              | boolean \| null | `null` unless `include=counts` is requested; then indicates whether the article has an embedding row           |
| `counts`                | object \| null  | `null` unless `include=counts` is requested — see below                                                        |


Read Article Meta tags, such as topic, subject, format, scope, timeframe, and user need, from `metadata[]`.

### Article metadata only

```http
GET …/articles/{article_id}/metadata
```

Returns metadata rows and distinct types for one article without the full article object or related lists:

```json
{
  "article_id": 1,
  "meta_types": ["format", "topic"],
  "metadata": [
    {
      "meta_type": "topic",
      "category": "local_government_politics",
      "confidence": 0.92
    }
  ]
}
```

### Full text embed (`include=text`)

Adds the complete article body in **`text`**. **`preview`** is still included — use it for list-style snippets and `text` when you need the full story for display, analysis, or downstream processing.

```json
{
  "id": 1,
  "headline": "City council votes on budget",
  "preview": "The city council approved a revised budget after…",
  "text": "The city council approved a revised budget after weeks of debate…"
}
```

List and search endpoints never return `text`. Request it from this detail route only.

### Counts embed (`include=counts`)

Adds summary counts and `embedded` without loading full related records:


| Field                   | Description                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `counts.mentions`       | Non-deleted mention rows by type (`locations`, `people`, `organizations`, `total`)                                                         |
| `counts.entities`       | Distinct Stylebook canonical records linked to mentions (`locations`, `people`, `organizations`, `total`). Unlinked mentions are excluded. |
| `counts.images`         | Images attached to the article                                                                                                             |
| `counts.custom_records` | Map of record type → count (for example `{ "contracts": 3 }`)                                                                              |


Use [detail endpoints](hub/index.md) to fetch the actual mention, location, image, or custom record rows. Use [List images](hub/images.md) when you need more than the 10 inline images on detail.

## Example

Fetch detail with counts and full body:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1?include=counts&include=text" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Preview only (default):

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/1" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Errors


| Status | When                                                        |
| ------ | ----------------------------------------------------------- |
| `400`  | Unknown `include` token                                     |
| `401`  | Missing or invalid API key                                  |
| `403`  | API key not valid for this project                          |
| `404`  | Unknown project, unknown article, or article not in project |


## Related

- [List and search](search.md) — find articles
- [Metadata](../taxonomy/index.md) — metadata types, values, and catalogs
- [List mentions](hub/mentions.md)
- [List people](hub/people.md)
- [List organizations](hub/organizations.md)
- [List locations](hub/locations.md)
- [List custom records](hub/custom-records.md)
- [List images](hub/images.md)

