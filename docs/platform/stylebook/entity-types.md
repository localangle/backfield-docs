# Entity types

An **entity type** is a kind of thing you catalog in [Stylebook](index.md). Each type has its own records, its own way of matching mentions, and its own detail view.

| Type | What it catalogs | Status |
| --- | --- | --- |
| **Location** | Places — cities, neighborhoods, buildings, roads, districts | Fully supported, including maps |
| **Person** | Individual people | Fully supported |
| **Organization** | Companies, agencies, governments, schools, and other institutions | Fully supported |

Articles themselves are **content**, not an entity type — they carry mentions and metadata but aren't catalogued the same way. See [Data model](../concepts/content-model.md).

## What the types share

All three supported types have:

- a canonical list with search and filters;
- a candidate queue for unresolved article entities;
- manual create and bulk import;
- a canonical detail page with mentions, metadata, and connections;
- duplicate and quality checks in Stylebook Review.

The shared pattern makes the catalog predictable, while each type keeps fields
needed for its real-world identity.

## Type-specific information

**Locations** can store a location type, formatted address, coordinates, and
point, line, or area geometry. Their identity decisions consider name,
location type, jurisdiction, address, and available geography.

**People** can store title, affiliation, public-figure status, person type, and
aliases. Name alone may not be enough to distinguish two people, so
affiliation and evidence matter during matching.

**Organizations** can store organization type, aliases, and other
editor-maintained metadata. Acronyms may help find a possible match, but an
ambiguous acronym should not silently merge two organizations.

## Custom records are different

A [Custom Extract](../agate/nodes/extractors.md) can produce project-defined
records such as events or inspections. Those records remain attached to
articles and are reviewed in Agate; they do not become a fourth canonical
Stylebook type.

Named works are reserved for future development but do not currently have a
functional catalog or editorial workflow.
