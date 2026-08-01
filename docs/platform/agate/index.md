# Agate

Agate is Backfield's processing workspace. It is where teams define how an
article should be read, enriched, and saved; run that process on one article or
a batch; and review the result against the source text.

![Demo flow showing a text input, metadata and embedding nodes, entity extraction, geocoding, and JSON output](../images/simple-example/qs2.png)

## Three concepts to know

Agate executions revolve around three connected concepts:

| Concept | Definition |
| --- | --- |
| **[Flows](flows.md)** | A series of steps composed of nodes that are wired together. You build it once and reuse it. |
| **[Runs](runs.md)** | A single execution of a flow over one or more articles. |
| **[Processed items](processed-items.md)** | A flow's output for one article: the people, places, metadata and other information extracted by the flow — which you can review and correct. |

## Building flows

A flow is built from **[nodes](nodes/index.md)**. Each node does one job, such
as assigning a topic, extracting people, or geocoding places. Agate's guided
builder starts by asking for an input and an output, then offers compatible
steps that can be inserted between them. Connections are created
automatically; flow builders do not have to wire technical ports by hand.

Nodes come in a variety of flavors, and developers can create new ones for specific tasks. See the [Nodes overview](nodes/index.md) for the full catalog.

## Running and reviewing

A flow is a reusable definition, not a result. Starting it creates a
[run](runs.md). Each article in that run becomes a
[processed item](processed-items.md), where an editor can:

- compare extracted data with highlighted passages in the story;
- correct fields, remove mistakes, or add something the model missed;
- inspect geography and article metadata;
- compare original model output with reviewed output.

Completed runs keep their own snapshot of what executed. Editing the flow
affects later runs rather than silently changing past results.

## How Agate works with Stylebook

Agate either produces raw JSON (via JSON or S3 Output nodes) or sends its output into a shared Backfield database.

The **Backfield Output** node saves articles and structured results into the
Backfield ecosystem. It always uses the Stylebook assigned to the project. As
it saves, it can match each extracted person, organization, or place against
that [Stylebook](../stylebook/index.md), propose new records, and form supported
connections.

This identity-matching process is known as
**[canonicalization](../stylebook/canonicalization.md)**. The output step also
controls how a rerun reconciles new machine output with data already saved for
an article: add only, smart merge, or replace. Editor-created and
editor-modified evidence is protected from automatic replacement.

Canonical matching can use deterministic rules and, when configured, guarded
AI assistance. Uncertain decisions go to Stylebook for editorial review.

## In this section

| Page | What it covers |
| --- | --- |
| [Flows](flows.md) | Building and executing pipelines |
| [Nodes](nodes/index.md) | The building blocks, grouped by what they do |
| [Runs](runs.md) | Running flows on one item or a batch, and tracking progress |
| [Processed items](processed-items.md) | Reviewing and correcting results article by article |
