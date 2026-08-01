# Mentions & evidence

A **mention** is a single reference to an entity in a single article — for example, one place name appearing in one story. A canonical record in [Stylebook](index.md) gathers together all the mentions that refer to the same real-world person, organization, or place.

Each mention keeps its **evidence**: the exact passage it came from, so you can always trace a catalog entry back to the reporting that supports it. Mentions can also carry context such as the **role** the entity played in the story.

Mentions are part of Backfield's [data model](../concepts/content-model.md) and are queryable through the API — see [Mentions](../../api/mentions/index.md).

![Canonical location mentions grouped with their source articles](../images/simple-example/qs7-2.png)

## Evidence can appear more than once

One article-level entity may have several evidence occurrences. A person might
be named in the opening paragraph, referred to by surname later, and quoted
near the end. Stylebook groups those occurrences under the article evidence
linked to the canonical person.

Where exact character positions can be mapped safely, Backfield keeps them so
the interface can highlight the source text. When text normalization prevents
an exact offset, the evidence text can still be retained without pretending to
know a precise position.

## Story context belongs to the mention

A mention can describe the entity's role in that particular story—for example,
whether a person is a subject, source, or quoted speaker. That context does not
become a permanent property of the canonical person.

This is why “Jane Doe was quoted in this story” belongs to article evidence,
while “Jane Doe is the mayor” may belong in canonical metadata.

## Project scope

Mentions remain project-scoped even when several projects share a Stylebook.
Canonical detail pages can filter evidence by project, and candidate queues
show which project produced an unresolved item. Changing the project filter
does not change canonical metadata or connections.

## Correcting a link

Editors can move or unlink article evidence when it points to the wrong
canonical. That changes the relationship between the project record and the
Stylebook identity; it does not rewrite the source article or merge the two
canonicals.

When the final piece of evidence is removed from an otherwise empty canonical,
Stylebook may offer to delete the empty record. Records with useful editorial
metadata or other evidence should be reviewed before removal.
