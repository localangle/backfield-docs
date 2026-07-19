# Examples

These recipes walk through common Public API workflows. Each example uses `general` as the project slug and assumes you have a project API key — see [Authentication](authentication.md) for how to send it.

Replace `general` with your project slug and `bfk_your_project_api_key` with your key. Confirm access with [Get project](projects/get-project.md) if needed.

```bash
export BACKFIELD_API_KEY="bfk_your_project_api_key"
export BACKFIELD_SERVICE_API_KEY="bfk_your_service_api_key"
export PROJECT="general"
export BASE="https://api.{organization_slug}.backfield.news/public/v1/projects/${PROJECT}"
```

By default, local development will use `http://localhost:8004/public/v1/projects/${PROJECT}` instead.

Examples that pass IDs between requests use [`jq`](https://jqlang.github.io/jq/) to read JSON responses.

## Search articles by keyword

Use [List and search articles](articles/search.md) with the `q` parameter. Keyword search matches headline, body text, and URL.

```bash
curl "${BASE}/articles/search?q=city%20council" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

Results are paginated. Use `limit` and `offset` to page through matches. Each item includes a truncated preview (max 280 characters). See [Pagination](conventions/pagination.md).

For meaning-based search instead of keywords, see [Semantic search](articles/semantic-search.md).

## Discover metadata and search

Agate can generate arbitrary metadata about articles, expressed as `meta_type` and `category` pairs. Before filtering, discover which types and values appear in your project — see [Metadata](taxonomy/index.md).

**1. List metadata types**

```bash
curl "${BASE}/articles/metadata/types" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

The response lists types such as `format`, `topic`, and `subject`:

```json
{
  "meta_types": ["format", "subject", "topic"]
}
```

**2. List category values for one type**

Pick a type from the response — for example, `topic` — and fetch the values used in your project:

```bash
curl "${BASE}/articles/metadata/types/topic/values" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

```json
{
  "meta_type": "topic",
  "values": ["local_government_politics", "public_safety_crime"]
}
```

**3. Search using a discovered value**

Use a `meta` clause on any article-metadata filter endpoint. For example, on [List and search](articles/search.md):

```bash
curl "${BASE}/articles/search?meta=topic:local_government_politics" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

Combine metadata filters with keyword search or date bounds:

```bash
curl "${BASE}/articles/search?q=development&meta=subject:development_project&pub_date_from=2024-01-01" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

**4. Advanced multi-clause metadata filter**

Repeat `meta` to AND clauses together. Use `|` for OR within one type, and `!` to negate. This example targets factual game previews and recaps — pro sports, a specific contest, without explainer/analysis pieces:

```bash
curl "${BASE}/articles/search\
?meta=topic:pro_sports\
&meta=subject:sports_contest\
&meta=%21format:explainer_analysis" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

Standard category catalogs, clause grammar, transport rules, and display labels are under [Article Meta](taxonomy/article-meta/index.md).

**5. Filter mentions by article metadata**

Use `meta` on [List and search mentions](mentions/search.md) to filter by the parent article's metadata:

```bash
curl "${BASE}/mentions/search?entity_type=person&meta=topic:local_government_politics" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

Quoted mentions only:

```bash
curl "${BASE}/mentions/search?entity_type=person&quote=true" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

**6. Semantic search with metadata filters**

Pass `meta` as a JSON array on [Semantic search](articles/semantic-search.md):

```bash
curl "${BASE}/articles/semantic-search" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "playoff game preview",
    "meta": ["topic:pro_sports", "subject:sports_contest", "!format:explainer_analysis"],
    "include": ["counts"],
    "limit": 10
  }'
```

Use the same JSON array form on [Geo cells batch query](other/geo-cells/query.md). GET routes such as [Geographic search](articles/geo-search.md), [Geo cells coverage](other/geo-cells/coverage.md), and [List and search mentions](mentions/search.md) use repeatable query parameters instead.

## Get an article and list its entities

Start from search (or any source of article ids), then load detail and related entities in separate requests.

**1. Find an article**

```bash
ARTICLE_ID="$(
  curl -sS "${BASE}/articles/search?q=budget&limit=1" \
    -H "Authorization: Bearer ${BACKFIELD_API_KEY}" |
    jq -r '.items[0].id'
)"
```

This stores the first result's `id` in `ARTICLE_ID`.

**2. Load the article**

```bash
curl "${BASE}/articles/${ARTICLE_ID}?include=counts&include=text" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

Omit `include=text` when you only need the truncated `preview`.

**3. List entities mentioned in the story**

One mixed list of people, organizations, and locations — returns every matching mention in one array:

```bash
curl "${BASE}/articles/${ARTICLE_ID}/mentions" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

Filter to quoted mentions with `?quote=true`, or combine `entity_type` and `nature` — see [List mentions](articles/hub/mentions.md).

Or load entity-type-specific lists when you need richer fields — for example, map-ready geometry from [List locations](articles/hub/locations.md), or person title and affiliation from [List people](articles/hub/people.md).

See [Detail endpoints](articles/hub/index.md) for the full set of per-article routes.

## Get an entity and list its articles

Canonical people, organizations, and locations live in the entity catalog. Search for a record, then fetch the articles that mention it.

**1. Find a person**

```bash
PERSON_ID="$(
  curl -sS "${BASE}/people/search?q=Jane%20Doe&limit=1" \
    -H "Authorization: Bearer ${BACKFIELD_API_KEY}" |
    jq -r '.items[0].id'
)"
```

This stores the person's UUID in `PERSON_ID`.

**2. List articles that mention them**

```bash
curl "${BASE}/people/${PERSON_ID}/articles?pub_date_from=2024-01-01&pub_date_to=2024-12-31" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

The same pattern applies to organizations and locations. All three entity
article routes accept `nature`, `author`, `external_source`, repeatable `meta`,
`pub_date_from`, `pub_date_to`, and repeatable `include=counts`:


| Entity       | Search                                                   | List articles                                   |
| ------------ | -------------------------------------------------------- | ----------------------------------------------- |
| Person       | [List and search people](people/search.md)               | [List articles](people/list-articles.md)        |
| Organization | [List and search organizations](organizations/search.md) | [List articles](organizations/list-articles.md) |
| Location     | [List and search locations](locations/search.md)         | [List articles](locations/list-articles.md)     |


Use the entity's `…/mentions` routes when you need mention-level evidence (nature, quote spans, article metadata filters) rather than a deduplicated article feed. Entity mention routes share the same filter vocabulary as [List and search mentions](mentions/search.md), plus `sort` and `sort_direction`.

```bash
curl "${BASE}/people/${PERSON_ID}/mentions?nature=subject&meta=topic:local_government_politics&quote=true" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

## Geographic search

Use [Geographic search](articles/geo-search.md) to find articles that mention locations near a point or inside a bounding box. Each item uses the standard article list shape plus `matching_locations`, and the response echoes the geo query at the top level.

**Point and radius** — search within five miles of a coordinate:

```bash
curl "${BASE}/articles/geo-search?center_lng=-93.265&center_lat=44.977&radius_miles=5" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

**Bounding box** — search inside a map viewport (`min_lng,min_lat,max_lng,max_lat`):

```bash
curl "${BASE}/articles/geo-search?bbox=-93.3,44.9,-93.2,45.0" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

Narrow results by location type or mention role:

```bash
curl "${BASE}/articles/geo-search?center_lng=-93.265&center_lat=44.977&radius_miles=5&nature=primary&location_type=place&location_type=address" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

Combine with article metadata filters:

```bash
curl "${BASE}/articles/geo-search?bbox=-93.3,44.9,-93.2,45.0&meta=topic:local_government_politics" \
  -H "Authorization: Bearer ${BACKFIELD_API_KEY}"
```

The same `meta` grammar applies on [Geo cells](other/geo-cells/index.md) coverage and drill-down routes.

## Trigger a run and poll status

Requires a **service** API key with **`runs:trigger`**. The target Agate graph must have **Enable API runs** turned on.

**1. Start a run**

```bash
RUN_ID="$(
  curl -sS -X POST "${BASE}/runs" \
    -H "Authorization: Bearer ${BACKFIELD_SERVICE_API_KEY}" \
    -H "Content-Type: application/json" \
    -H "Idempotency-Key: article-import-001" \
    -d '{
      "graph_id": "YOUR_GRAPH_ID",
      "inputs": {
        "article": { "text": "Story body to process." }
      }
    }' |
    jq -r '.run_id'
)"
```

The trigger returns `202 Accepted`, `Location`, and `Retry-After`. This stores
the returned run id in `RUN_ID`. Repeating the same idempotency key and body
within seven days returns the original run with `Idempotency-Replayed: true`;
reusing the key with a different body returns `409`.

**2. Poll until finished**

```bash
curl "${BASE}/runs/${RUN_ID}" \
  -H "Authorization: Bearer ${BACKFIELD_SERVICE_API_KEY}"
```

See [Trigger run](runs/trigger-run.md) for ingress alias and idempotency rules,
and [Get run](runs/get-run.md) for the response shape and polling headers.

## More examples

These recipes cover several common use cases. The rest of the API reference goes deeper:


| Topic                                    | Start here                                     |
| ---------------------------------------- | ---------------------------------------------- |
| All article search and filter parameters | [List and search articles](articles/search.md) |
| Mention-level queries across the project | [List and search mentions](mentions/search.md) |
| Entity catalog search and filters        | [Entities overview](entities/index.md)         |
| Map hex aggregations                     | [Geo cells](other/geo-cells/index.md)          |
| Trigger an Agate graph run               | [Runs](runs/index.md)                          |
| Metadata filters and value discovery     | [Metadata](taxonomy/index.md)                  |
| Pagination, errors, and rate limits      | [Conventions](conventions/pagination.md)       |


Browse the sidebar under **API Reference** for every endpoint, request parameter, and response shape.