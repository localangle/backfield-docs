# Locations

`location_type` classifies canonical locations, location mentions, location/geo search filters, and geo-cells mention filters.

Discover values in your project with `GET …/locations/types` — see [Locations types](../../locations/types.md).

## Categories

| Value | Typical use |
| --- | --- |
| `place` | Named point of interest or venue |
| `address` | Street address |
| `intersection_road` | Road intersection |
| `intersection_highway` | Highway interchange |
| `street_road` | Named street or road segment |
| `span` | Stretch between two points |
| `political_district` | Legislative or political district |
| `neighborhood` | Neighborhood |
| `region_city` | City region or sub-area |
| `city` | City |
| `county` | County |
| `region_state` | State region |
| `state` | State or province |
| `region_national` | National region |
| `country` | Country |
| `natural` | Natural feature |
| `other` | Does not fit another category |

Address-like types (`address`, `intersection_*`, `street_road`, `span`) may carry an `address_place_kind` in extraction output (`public_named`, `private_residence`, `unknown`).

## Related

- [Entity Meta overview](index.md)
- [People](people.md)
- [Organizations](organizations.md)
