# Geography

Location records can keep coordinates and map shapes. This supports map views
and location-based search.

The [Geocode](../agate/nodes/enrichment.md) step in an Agate flow can turn place
names into geography. Editors can review the result on the
[processed item](../agate/processed-items.md) map.

![Canonical location detail showing Springfield's maintained boundary](../images/simple-example/qs7-1.png)

## Geometry types

Stylebook can represent several kinds of geography:

- a **point** for a venue, address, or other specific position;
- a **line** for a road or similar feature;
- an **area** for a neighborhood, district, city, park, or other boundary.

The right shape depends on the place. A city-center point may work for display,
but it cannot answer whether another point falls inside the city boundary.

## Article geography and canonical geography

Geocoding first produces a result for the location found in one article. It can
help match a canonical record, but it does not automatically replace that
record's maintained geography.

Editors can review article evidence and adopt useful geography for the
canonical record when appropriate. This prevents one questionable run from
silently changing a shared map record.

## No geography is a valid result

Some places can be identified even when no reliable map result is available.
Backfield can keep the name, type, jurisdiction, evidence, and canonical link
while showing **No geography**.

This commonly happens when:

- a place name is ambiguous;
- an address is incomplete;
- a geocoder returns the wrong jurisdiction or kind of place;
- no suitable boundary is available.

Editors should prefer no geometry over a confident-looking but incorrect point.

Use editorial judgment for disputed boundaries and sensitive locations. A
technically available boundary or precise point may not be the most accurate or
responsible representation for publication.

## Review and cleanup

The processed item's Places tab is where an editor fixes geography for one
article. The Stylebook location page is where an editor maintains the shared
canonical geometry. Stylebook Review can flag geography-quality concerns and
possible duplicate locations for broader catalog cleanup.

Canonical geography supports map display and geographic API search. A change
affects every project using that Stylebook and requires Stylebook editing
access.
