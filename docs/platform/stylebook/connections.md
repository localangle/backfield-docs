# Connections

**Connections** are relationships between canonical records — the links that turn a list of people, places, and organizations into a knowledge graph. A connection captures something like *this person works for that organization* or *this organization is located in that place*.

Connections come from two sources:

- **Manual** — editors create relationships by hand and can describe them in their own words.
- **Automatic** — Backfield can infer certain relationships from your reporting after canonicalization, using a focused set of relationship kinds (such as person-to-organization). Inferred connections are backed by evidence from the text.

![Canonical record showing its advanced connections area](../images/simple-example/qs7-3.png)

## What a connection contains

A connection has a direction: one canonical is the **from** record and another
is the **to** record. It may include:

- a normalized relationship kind, or **nature**;
- a human-readable description;
- project and article evidence when the relationship was inferred from
  reporting.

Direction matters. “Jane Doe works for City Hall” and “City Hall works for Jane
Doe” do not mean the same thing, even though they contain the same two records.

## Supported relationships

Connections can link people, organizations, and locations in useful
combinations—for example:

- person → organization: works for, leads, represents;
- organization → location: based at, serves, located in;
- person → location: lives in, represents, associated with;
- person → person or organization → organization relationships.

The description can preserve nuance when a controlled nature alone would be
too broad.

## Manual and inferred connections

Manual connections are deliberate editorial knowledge. Automatic connections
are proposals derived from article evidence and written only when the
configured inference is sufficiently confident. Quote-backed evidence helps
editors inspect why a relationship was created.

Review the endpoints and wording before accepting or keeping a connection.
Two correct canonical records can still be connected in the wrong direction
or with an overbroad description.

## Stylebook-wide scope

Connections belong to the Stylebook identity graph. They remain visible when a
canonical detail page is filtered to one project. Evidence attached to an
inferred connection can still identify the project and article that supported
it.

The detail page shows both a list and a graph view so editors can understand
the immediate neighborhood around a canonical without treating the graph as an
independent source of truth.
