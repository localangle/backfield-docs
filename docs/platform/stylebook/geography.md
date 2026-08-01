# Geography

For **location** records, Stylebook keeps geographic information: map coordinates and, where available, the shape of a place (a point, a line such as a road, or an area such as a neighborhood). This is what makes map views and location-based search possible.

Geography is added mainly through the [Geocode](../agate/nodes/enrichment.md) step in an Agate flow, which turns place names into coordinates, and can be reviewed and corrected on the [processed item](../agate/processed-items.md) map.

![Canonical location detail showing Springfield's maintained boundary](../images/simple-example/qs7-1.png)

## Geometry types

Stylebook can represent several kinds of geography:

- a **point** for a venue, address, or other specific position;
- a **line** for a road or similar feature;
- an **area** for a neighborhood, district, city, park, or other boundary.

The right geometry depends on what the canonical record represents. A city
center point may be useful for display, but it is not equivalent to the city's
boundary for containment search.

## Article geography and canonical geography

Geocoding first produces geography for the location found in an article. That
article-specific result can help match a known canonical, but it does not
automatically overwrite the canonical's editor-maintained geometry.

On a location detail page, editors can review article evidence and, when
appropriate, adopt useful saved-story geometry for the canonical. This keeps a
single questionable run from silently changing a shared map record.

## No geography is a valid result

Some identities are clear even when a safe map result is not. Backfield can
retain the place name, type, jurisdiction, evidence, and canonical link while
showing **No geography**.

This commonly happens when:

- a place name is ambiguous;
- an address is incomplete;
- a geocoder returns a conflicting jurisdiction or wrong kind of feature;
- a country or administrative identity is known but no appropriate boundary
  is available.

Editors should prefer no geometry over a confident-looking but incorrect point.

## Review and cleanup

The processed item's Places tab is where an editor fixes geography for one
article. The Stylebook location page is where an editor maintains the shared
canonical geometry. Stylebook Review can flag geography-quality concerns and
possible duplicate locations for broader catalog cleanup.

Canonical geography supports map display and geographic API search. Changes
therefore affect every project using that Stylebook and should be treated as
shared reference edits.
