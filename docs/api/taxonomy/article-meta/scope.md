# Scope

Scope metadata (`meta_type=geographic_scope`) describes the primary geographic level at which the story's events, decisions, or effects matter. Scope is about who is affected, not every place mentioned.

## Filter

```text
?meta=geographic_scope:city_municipality
```

Discover values in your project with `geographic_scope_categories` from [Article facets](../../articles/facets.md) or `GET …/articles/metadata/types/geographic_scope/values`.

## Categories

| API value | Meaning |
| --- | --- |
| `neighborhood_community` | Impacts a single neighborhood, district, school, or hyperlocal community |
| `city_municipality` | Impacts residents of an entire city or town |
| `regional` | Impacts multiple communities or counties within a broader geographic area, including metro areas, non-metro regions, tribal nations, and multi-state regions |
| `statewide` | Impacts residents across the entire state |
| `national` | Impacts people across the United States, with no specific local or state focus |
| `international` | Impacts multiple countries or deals with global affairs, with no specific U.S. or local focus |
| `elsewhere_to_local` | A national or global trend, policy, or event that directly affects the local area |
| `local_to_elsewhere` | A local action, innovation, discovery, or event with impact beyond the local area |
| `other` | Does not clearly fit any scope category |

## Related

- [Article Meta overview](index.md)
- [Topic](topic.md)
- [Timeframe](timeframe.md)
