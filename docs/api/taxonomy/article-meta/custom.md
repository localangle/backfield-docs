# Custom

Custom article metadata uses a project-defined `meta_type` and project-defined categories. Use it when the preset article metadata dimensions do not fit the classification you want a flow to produce.

## Filter

For a custom metadata type named `audience_segment`:

```text
?meta=audience_segment:parents
```

The exact `meta_type` and category values depend on how your Article Metadata node is configured.

## Categories

Custom metadata does not have a fixed global taxonomy. Discover available custom types and values in your project with [Article facets](../../articles/facets.md) or the metadata type routes:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/metadata/types" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Then list values for a custom type:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/articles/metadata/types/audience_segment/values" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

## Related

- [Article Meta overview](index.md)
- [Article facets](../../articles/facets.md)
