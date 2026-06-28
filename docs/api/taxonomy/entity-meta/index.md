# Entity Meta

Entity Meta classifies **canonical** people, organizations, and locations in Stylebook. Types appear on mention rows and entity search filters as `person_type`, `organization_type`, and `location_type`.

This is **Entity Meta**, not Article Meta's `meta_type=subject` (what the story is about) or Mention Meta's `nature=subject` (when a person or place is the central focus of the narrative).

Extractors assign types when stories are processed; unmatched free text normalizes to `other`.

## Type fields

| Entity | Field | Reference |
| --- | --- | --- |
| People | `person_type` | [People](people.md) |
| Organizations | `organization_type` | [Organizations](organizations.md) |
| Locations | `location_type` | [Locations](locations.md) |

## Discover values in your project

Catalog tables on each page list **allowed** slugs. Call the types endpoint for each entity to see defaults plus types stored on active canonical records in your project:

| Entity | Endpoint | Doc |
| --- | --- | --- |
| People | `GET …/people/types` | [People types](../../people/types.md) |
| Organizations | `GET …/organizations/types` | [Organizations types](../../organizations/types.md) |
| Locations | `GET …/locations/types` | [Locations types](../../locations/types.md) |

[Mention facets](../../mentions/facets.md) also returns distinct `person_types`, `organization_types`, and `location_types` seen on mention rows.

## Related

- [Metadata overview](../index.md)
- [Mention Meta](../mention-meta/index.md) — editorial `nature` on mentions (separate from entity type)
- [Entities overview](../../entities/index.md)
