# Import & export

Besides building your catalog from reporting, you can bring records into [Stylebook](index.md) in bulk and move catalogs between organizations.

| Method | Use it for |
| --- | --- |
| **Spreadsheet import (CSV)** | Loading lists of people or organizations you already maintain |
| **Geographic import (GeoJSON)** | Loading locations with map geometry |
| **Stylebook copy** | Copying supported canonical records into a new Stylebook |

## Spreadsheet and geographic imports

CSV import creates canonical people or organizations from rows in a
spreadsheet. GeoJSON import creates canonical locations and can preserve point,
line, or area geometry from each feature.

These imports are best for reference lists your newsroom already maintains.
They create canonical records directly; they do not pretend that the records
were extracted from an article and therefore do not create article mentions.

Prepare one clear real-world identity per row or feature. Consistent names,
types, affiliations, addresses, and identifiers make later matching more
reliable.

## Stylebook copies

Organization administrators can download a Stylebook file and upload it to
create a new Stylebook. The current copy workflow includes canonical locations
and people and assigns them new internal identifiers in the destination.

It is not a complete backup or clone. The current workflow does **not** include:

- canonical organizations;
- aliases, metadata, or connections;
- source articles, article entities, or mentions;
- candidate and review queues;
- semantic embeddings, geocoding caches, or activity history.

Those exclusions matter: copied records carry a starting set of canonical
people and locations, not the full evidence and editorial context of the
source Stylebook.

The import screen previews the package before creating the new Stylebook.

## Before importing

Review the destination Stylebook and the import preview. Imports can introduce
records that resemble existing canonicals, so run the relevant Stylebook
Review checks afterward rather than assuming every imported name is unique.
