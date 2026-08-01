# Query project data

Retrieve articles, article entities, canonicals, mentions, custom records, and
connections while preserving their distinct meanings.

!!! note "Tutorial outline"
    Detailed examples in cURL, Python, and JavaScript are still to come.

## You'll learn

- How project API keys establish the project boundary.
- When to query article entities, canonicals, mentions, or custom records.
- How to paginate list endpoints reliably.
- How to follow identifiers between related resources.

## Before you begin

Use a project with Backfield Output data and a key stored in an environment
variable. Identify one article that contains canonical entities and custom
records.

## Planned walkthrough

1. Confirm the authenticated project.
2. List articles and follow the next-page cursor.
3. Retrieve one article and its people, organizations, locations, and metadata.
4. Follow an article entity to its canonical record.
5. List the canonical's mentions and connections.
6. Retrieve custom records by type.
7. Compare original article context with shared canonical knowledge.
8. Handle an unknown identifier and an invalid cursor.

## Related concepts

- [Articles API](../../api/articles/index.md)
- [Canonical entities API](../../api/entities/index.md)
- [Custom records API](../../api/custom-records/index.md)
