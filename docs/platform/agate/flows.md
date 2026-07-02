# Flows

A **flow** is the pipeline you build in Agate — a series of connected [nodes](nodes/index.md) that read your text and produce structured results. You build a flow once and reuse it across as many [runs](runs.md) as you like.

Every flow begins with a step that brings text **in** and ends with a step that sends results **out**, with extraction and enrichment steps in between.

## What a flow does

Flows turn unstructured text into reusable data. A simple flow might take article text, identify people and places, geocode the places, and save the results for review. A more advanced flow can branch into several extraction tasks, gather results back together, and write structured JSON or custom records.

Most flows follow the same pattern:

1. **Input** — bring text into the flow.
2. **Extract** — find the entities, metadata, or custom records you care about.
3. **Enrich** — add useful context, such as coordinates for locations or embeddings for search.
4. **Output** — save the results to Backfield or export them elsewhere.

The demo flow below starts with JSON input, sends the same article text through embedding and article-metadata extractors, gathers those results, then extracts people and places. Places pass through geocoding before the flow writes JSON output.

![Demo flow showing JSON input, metadata extraction, embedding, people and place extraction, geocoding, and JSON output](/platform/agate/images/flow-builder.png)

## The flow builder

The builder is a canvas. Nodes sit on the canvas, and connections show how data moves from one node to the next. Build left to right: start with an input, add the processing steps, then finish with an output.

In edit mode, Agate shows controls for adding paths, inserting steps between existing nodes, changing a node's source or destination, and tidying the layout. The underlying shape stays visible, so you can adjust the flow without losing sight of how data moves through it.

![Agate flow builder in edit mode with controls for adding paths and inserting steps](/platform/agate/images/flow-edit-builder.png)

Each node has its own settings panel. Use it to choose a model, write extraction instructions, map fields, or configure where results should go. When a node depends on another node's output, connect them on the canvas instead of duplicating work.

![Place Extract node settings panel showing the model selector and node tabs](/platform/agate/images/flow-node-settings.png)

## Inputs and outputs

Every runnable flow needs at least one input and one output.

| Node type | What it does |
| --- | --- |
| **Input** | Defines what text or data the run receives, such as pasted text, JSON, or files from cloud storage |
| **Output** | Defines where the flow sends results, such as Backfield, JSON, or cloud storage |

The input and output are the bookends of the flow. Everything between them should transform, extract, enrich, or route the data.

## Branches and gathering

A flow does not have to be a single straight line. You can branch when several steps should read from the same input — for example, one branch extracts people while another extracts locations. Use flow-control nodes to gather branches when a later step needs their combined output.

Branching keeps each node focused. It also makes runs easier to debug because each extraction or enrichment step has its own output.

## Validation

Before you run a flow, check that it is complete:

- The flow has an input node and an output node.
- Required node settings are filled in.
- Each node that needs upstream data is connected.
- Model-backed nodes use an approved model configuration.
- Output nodes receive the fields they expect.

Agate surfaces validation issues in the builder so you can fix missing settings or broken connections before starting a run.

## Starter templates

Starter templates give you a working flow shape for common jobs. Use them when you want to begin from a known pattern, then adjust the nodes, instructions, and outputs for your project.

Templates are especially useful for:

- Extracting people, organizations, and locations from articles
- Geocoding places for maps and geographic search
- Tagging articles with topics, subjects, or formats
- Creating custom records from recurring story types

## From flow to run

Building a flow defines the pipeline. A [run](runs.md) executes that pipeline on one item or a batch. After a run finishes, each article becomes a [processed item](processed-items.md), where you can inspect node outputs, review extracted entities, and correct article-level results before they feed the rest of Backfield.

## Related

- [Nodes](nodes/index.md) — the building blocks of a flow
- [Runs](runs.md) — executing a flow and tracking progress
- [Processed items](processed-items.md) — reviewing run results
- [Backfield Output](nodes/outputs.md) — saving flow results into Backfield
