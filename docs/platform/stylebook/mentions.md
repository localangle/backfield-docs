# Mentions & evidence

A **mention** is one reference to a person, organization, or location in an
article. A canonical record in [Stylebook](index.md) brings together the
mentions that refer to the same real-world entity.

Each mention retains its **evidence**: the passage from which it came. This
lets editors trace a record back to the reporting that supports it. A mention
can also record the entity's role in that story.

See the [Data model](../concepts/content-model.md) for how mentions relate to
articles and canonical records.

![Canonical location mentions grouped with their source articles](../images/simple-example/qs7-2.png)

## One entity can have several mentions

A person might be named in the opening paragraph, referred to by surname later,
and quoted near the end. These are separate mentions of one article entity.
Stylebook groups them under the linked canonical person and preserves the
passages needed for review.

## Story context belongs to the mention

A mention can describe the entity's role in that story—for example,
whether a person is a subject, source, or quoted speaker. That context does not
become a permanent property of the canonical person.

This is why “Jane Doe was quoted in this story” belongs to article evidence,
while “Jane Doe is the mayor” may belong in canonical metadata.

## Project scope

Mentions remain tied to their project and article even when several projects
share a Stylebook. A project filter narrows the evidence shown on a canonical
record; it does not create a separate version of the record.

## Correcting a link

Editors can move or unlink evidence when it points to the wrong canonical
record. This corrects the link without rewriting the source article or merging
the canonical records.

When the final piece of evidence is removed from an otherwise empty canonical,
Stylebook may offer to delete the empty record. Records with useful editorial
metadata or other evidence should be reviewed before removal.
