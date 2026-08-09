# Mention Meta

Mentions are specific instances of a person, organization or location appearing in the story. Each mention carries a fixed piece of metadata, known as its `nature`, which describes **the role of the entity in the story**.


| Field        | Controlled vocabulary?               | Purpose                               |
| ------------ | ------------------------------------ | ------------------------------------- |
| `**nature`** | Yes — values depend on `entity_type` | Primary editorial role of the mention |


## Nature by entity type

Different canonical types carry different natures for their mentions.


| Entity        | Reference                         |
| ------------- | --------------------------------- |
| People        | [People](people.md)               |
| Organizations | [Organizations](organizations.md) |
| Locations     | [Locations](locations.md)         |


## Discover values in your project

Call [Mention facets](../../mentions/facets.md) for distinct `natures` and type values on mention rows in your project — a convenience wrapper for frontend search UI:

```bash
curl "https://api.{organization_slug}.backfield.news/public/v1/projects/general/mentions/facets" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

The `natures` array merges values from all entity types. Use the entity pages above to interpret which entity type each value applies to.

## Filtering by nature in API requests

Many public routes accept a repeatable `nature` query parameter. Repeat the
parameter to match any listed value (OR). For example,
`?nature=subject&nature=official` on a person mention list returns mentions
tagged with either role.

Connection lists use the same repeatable pattern for relationship `nature`
values.

## Related

- [Metadata overview](../index.md)
- [Entity Meta](../entity-meta/index.md)
- [Mention facets](../../mentions/facets.md)
- [List and search mentions](../../mentions/search.md)

