# Search project data

Use text, semantic, metadata, and geographic query tools to answer different
questions about a project's processed content.

## You'll learn

- When direct filters are more appropriate than semantic search.
- How to check whether semantic search is ready.
- How metadata and geographic constraints narrow article sets.
- Why an empty result can be correct rather than an API failure.

## Before you begin

Complete [Query project data](query-data.md). Keep these variables in your
terminal:

```bash
export BACKFIELD_PROJECT_API_KEY="paste-the-key-here"
export BACKFIELD_API_ORIGIN="http://localhost:8004"
export PROJECT_SLUG="tutorial-project"
export BASE="$BACKFIELD_API_ORIGIN/public/v1/projects/$PROJECT_SLUG"
```

## 1. Choose the search method

Use the simplest method that answers the question:

| Question | Method |
| --- | --- |
| Does the article contain a known word or phrase? | Keyword search |
| Which articles have a selected editorial classification? | Metadata filter |
| Which stories mention one known canonical? | Canonical articles endpoint |
| Which stories mention places in an area? | Geographic search |
| Which stories discuss a concept in different words? | Semantic search |

## 2. Search by keyword

The `q` field searches headline, body text, and URL. Search for `Duluth`:

```bash
curl "$BASE/articles/search?q=Duluth&limit=10&include=counts" \
  -H "Authorization: Bearer $BACKFIELD_PROJECT_API_KEY"
```

The current tutorial data returns four matching articles. Keyword search is
appropriate because the word appears in the source text.

You can also use web-style syntax:

```text
"cooling center"
cooling OR heat
cooling -recipe
```

Quoted words must appear together. `OR` accepts either term. A leading `-`
excludes a term.

## 3. Filter by article metadata

Discover metadata types and their available values before constructing a
filter:

```bash
curl "$BASE/articles/metadata/types" \
  -H "Authorization: Bearer $BACKFIELD_PROJECT_API_KEY"

curl "$BASE/articles/metadata/types/subject/values" \
  -H "Authorization: Bearer $BACKFIELD_PROJECT_API_KEY"
```

The tutorial project currently has these subject values:

```json
{
  "values": [
    "government_action",
    "other",
    "weather_event"
  ]
}
```

Filter for the government-action story:

```bash
curl "$BASE/articles/search?meta=subject%3Agovernment_action&limit=10" \
  -H "Authorization: Bearer $BACKFIELD_PROJECT_API_KEY"
```

This returns article `654`. Repeat `meta` to require more than one condition.
Within one condition, comma-separated categories act as alternatives. Use
values returned by the discovery endpoints instead of guessing category names.

## 4. Search through a canonical

The canonical for **Duluth, MN** has ID
`2662456f-a3b8-46f3-9ceb-2105684ff1cc`.

```bash
curl "$BASE/locations/2662456f-a3b8-46f3-9ceb-2105684ff1cc/articles?limit=10" \
  -H "Authorization: Bearer $BACKFIELD_PROJECT_API_KEY"
```

This asks which articles are connected to one known place. It is more precise
than searching all article text for the word `Duluth`.

## 5. Search geographically

Search within 25 miles of central Duluth:

```bash
curl "$BASE/articles/geo-search\
?center_lng=-92.1005&center_lat=46.7867&radius_miles=25&limit=10" \
  -H "Authorization: Bearer $BACKFIELD_PROJECT_API_KEY"
```

The tutorial data returns four articles. Each item includes
`matching_locations`, which explains why it met the geographic test. A large
region such as Minnesota can intersect the search radius, so inspect those
locations instead of assuming every match names a point inside Duluth.

Add a metadata condition to narrow the geographic results:

```bash
curl "$BASE/articles/geo-search\
?center_lng=-92.1005&center_lat=46.7867&radius_miles=25\
&meta=subject%3Agovernment_action&limit=10" \
  -H "Authorization: Bearer $BACKFIELD_PROJECT_API_KEY"
```

## 6. Check semantic-search readiness

First request the project:

```bash
curl "$BASE" \
  -H "Authorization: Bearer $BACKFIELD_PROJECT_API_KEY"
```

Compare `stats.articles.total` with `stats.articles.embedded`. The current
tutorial project reports five articles and zero embedded articles, so none are
eligible for semantic search yet.

Do not treat a zero-result semantic query as evidence that the concept is
absent when the articles have not been embedded. Add an **Embed Text** node to
the flow, configure an embedding provider, and process the articles before
using this request:

```bash
curl -X POST "$BASE/articles/semantic-search" \
  -H "Authorization: Bearer $BACKFIELD_PROJECT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "ways local officials protect residents from extreme heat",
    "limit": 10,
    "include": ["counts"]
  }'
```

Semantic results include a similarity `score`; higher scores are closer to the
query's meaning. Compare them within one result set rather than treating a
score as an absolute fact.

## 7. Interpret empty results

A valid search with no matches returns **200 OK**, an empty `items` array, and
`pagination.total: 0`. That is different from:

- **401** for a missing or invalid key.
- **422** for an invalid filter or geographic shape.
- **503** when the configured model provider is unavailable.

Check the status, the echoed filters, and the pagination object before changing
your search.

When finished, revoke the temporary key from **Tutorial Project → API**.

## Related concepts

- [Semantic search](../../api/articles/semantic-search.md)
- [Metadata discovery](../../api/taxonomy/article-meta/index.md)
- [Geo cells](../../api/other/geo-cells/index.md)
