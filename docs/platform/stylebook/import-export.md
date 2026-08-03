# Import & export

You can add records to [Stylebook](index.md) in bulk instead of creating them
one at a time.

| Method | Use it for |
| --- | --- |
| **Spreadsheet import (CSV)** | Loading lists of people or organizations you already maintain |
| **Geographic import (GeoJSON)** | Loading locations with map geometry |
| **Stylebook copy** | Starting a new Stylebook with supported records from another one |

## Spreadsheet and geographic imports

CSV import creates canonical people or organizations from spreadsheet rows.
GeoJSON import creates canonical locations and can preserve point, line, or
area geography.

These methods work well for reference lists your newsroom already maintains.
They create canonical records directly and do not create article mentions.

For CSV:

- include a header row and a name for every person or organization;
- map your columns to Stylebook fields before importing;
- review the parsed rows and remove any that should not be imported.

For GeoJSON:

- use a valid `FeatureCollection`;
- map a label and location type for each feature;
- review geography and any optional address or metadata fields.

Both importers accept files up to 25 MB and report records that could not be
created. Start with a small file, keep the source, and inspect the result before
loading a larger set. Imports do not guarantee that similarly named records
will be deduplicated.

## Stylebook copies

Organization administrators can export a Stylebook package and import it as a
new Stylebook. The current package includes canonical people and locations,
which receive new internal identifiers in the new Stylebook.

It is not a complete backup or clone. The current workflow does **not** include:

- canonical organizations;
- aliases, metadata, or connections;
- source articles, article entities, or mentions;
- candidate and review queues;
- semantic embeddings, geocoding caches, or activity history.

The result is a starting set of people and locations, not a backup or complete
copy of the source Stylebook.

## Before importing

Review the source file before importing. The current Stylebook copy dialog does
not provide a record-by-record preview.

After any import, inspect the new records and run the relevant Stylebook Review
checks. Imported records may resemble canonicals already in the catalog.
Correct imported records individually if the source mapping or values were
wrong; there is no one-click rollback for the completed import.
