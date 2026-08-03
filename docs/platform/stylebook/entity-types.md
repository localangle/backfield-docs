# Entity types

Stylebook catalogs three kinds of real-world entities:

| Type | Examples |
| --- | --- |
| **People** | Officials, sources, candidates, experts, and other individuals |
| **Organizations** | Companies, agencies, governments, schools, and other institutions |
| **Locations** | Cities, neighborhoods, buildings, roads, parks, and districts |

Articles carry mentions and metadata, but they are not canonical entities. See
the [Data model](../concepts/content-model.md).

## What every entity has

Each type has:

- a canonical list with search and filters;
- a candidate queue for unresolved article entities;
- tools for creating and importing records;
- a canonical detail page with mentions, metadata, and connections;
- duplicate and quality checks.

Canonical records use a preferred name or label. **Aliases** record other names
that refer to the same entity and can improve search and matching. An
**inactive** record remains in the catalog for reference but is excluded from
automatic linking.

## What differs by type

**Locations** can store a location type, formatted address, coordinates, and
point, line, or area geography. Name, jurisdiction, address, and geography all
help distinguish one place from another.

**People** can store title, affiliation, public-figure status, person type, and
aliases. A name alone may not distinguish two people, so affiliation and
article evidence also matter.

**Organizations** can store organization type, aliases, and other
editor-maintained metadata. Names and acronyms may suggest a match, but an
ambiguous acronym should not join two different organizations.

## Custom records are different

A [Custom Extract](../agate/nodes/extractors.md) can produce project-defined
records such as events or inspections. Those records remain attached to
articles and are reviewed in Agate; they do not become a fourth canonical
Stylebook type.
