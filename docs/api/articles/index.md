# Articles

Articles are a first-class resource in Backfield. Use article endpoints to find stories, retrieve article summaries, and explore the people, organizations, locations, and images connected to a story.

Article responses include headline, source information, publication date, metadata tags, and a truncated preview (max 280 characters).

## How article data is structured

Each article has a detail endpoint, search endpoints, and separate detail endpoints for larger related data.


| Endpoint type         | Use when                                                                                                          |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Detail**            | Show one article's summary data, inline images (up to 10), optional counts, optional full body via `include=text` |
| **List and search**   | Find articles by exact terms, metadata, or date                                                                   |
| **Article facets**    | Convenience wrapper to populate article search filter controls in one call — see [Metadata](../taxonomy/index.md) |
| **Semantic search**   | Find conceptually related articles with natural language; optional `include=counts` on each result |
| **Geographic search** | Find articles that mention places near a point or inside a bounding box; optional `include=counts` on each result |
| **Geo cells**         | H3 hex coverage map with distinct-article counts per cell; batch drill-down for multi-cell selections             |
| **Detail endpoints**  | Load related mentions, people, organizations, locations, custom records, or images                                |


This keeps article detail responses fast and predictable. If you need related data beyond inline images and counts, request the slice you need from [detail endpoints](hub/index.md).

## Endpoints


| Method | Path                                           | Doc                                                  |
| ------ | ---------------------------------------------- | ---------------------------------------------------- |
| `GET`  | `…/articles/{article_id}`                      | [Get article](get-article.md)                        |
| `GET`  | `…/articles/search`                            | [List and search](search.md)                         |
| `GET`  | `…/articles/facets`                            | [Article facets](facets.md)                          |
| `GET`  | `…/articles/metadata/types`                    | [List metadata types](metadata-types.md)             |
| `GET`  | `…/articles/metadata/types/{meta_type}/values` | [List metadata values](metadata-values.md)           |
| `GET`  | `…/articles/{article_id}/metadata`             | [Get article metadata](get-metadata.md)              |
| `POST` | `…/articles/semantic-search`                   | [Semantic search](semantic-search.md)                |
| `GET`  | `…/articles/geo-search`                        | [Geographic search](geo-search.md)                   |
| `GET`  | `…/articles/geo-cells`                         | [Coverage](../other/geo-cells/coverage.md)           |
| `GET`  | `…/articles/geo-cells/{h3_cell}`               | [List articles](../other/geo-cells/list-articles.md) |
| `POST` | `…/articles/geo-cells/query`                   | [Batch query](../other/geo-cells/query.md)           |
| `GET`  | `…/articles/{article_id}/mentions`             | [List mentions](hub/mentions.md)                     |
| `GET`  | `…/articles/{article_id}/people`               | [List people](hub/people.md)                         |
| `GET`  | `…/articles/{article_id}/organizations`        | [List organizations](hub/organizations.md)           |
| `GET`  | `…/articles/{article_id}/locations`            | [List locations](hub/locations.md)                   |
| `GET`  | `…/articles/{article_id}/custom-records`       | [List custom records](hub/custom-records.md)         |
| `GET`  | `…/articles/{article_id}/images`               | [List images](hub/images.md)                         |


## Article object

The article list shape is shared across [List and search](search.md), [Semantic search](semantic-search.md), and [Geographic search](geo-search.md) results (geo search adds `matching_locations` on each item). See [Get article](get-article.md) for the full field reference.

Core fields (list and detail):

- `id`, `headline`, `url`, `author`, `pub_date`
- `source` — publication or outlet (`id`, `name`) when known; `null` otherwise
- `metadata` — tags from article meta (`meta_type`, `category`, `confidence`)
- `preview` — truncated body snippet (max 280 characters)

Detail-only:

- `images` — up to 10 inline image rows on [Get article](get-article.md)

Optional embeds on [Get article](get-article.md):

- `include=counts` — populates `counts` (mention and entity totals, image count, custom record counts) and `embedded`; both are otherwise `null`
- `include=text` — adds `text` (full article body; `preview` is always included)

Optional embeds on list/search routes ([List and search](search.md), [Semantic search](semantic-search.md), [Geographic search](geo-search.md)):

- `include=counts` (or `"include": ["counts"]` on POST semantic search) — populates `counts` and `embedded`; they are otherwise `null`

Topic categories appear in `metadata[]` with `meta_type=topic`. Filter with `meta=topic:<category>` on any article-metadata filter endpoint — see [Article Meta](../taxonomy/article-meta/index.md#querying-with-meta).

## What article responses do not include

- Full article body on list/search routes (use [Get article](get-article.md) with `include=text`)
- Full mention, location, or image lists (use the [detail endpoints](hub/index.md); [Get article](get-article.md) includes up to 10 inline images)

