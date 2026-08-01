# Nodes

A **node** is one step in an Agate [flow](../flows.md). Each node has a focused
job and declares what information it needs and what it produces. In the guided
builder, you add nodes with **+** controls; Agate creates compatible connections
automatically.

Every flow starts with an **input** step and ends with an **output** step. In between, you add steps that find and refine the details you care about.

## The node families

Nodes are grouped by what they do:

| Family | What it does | Examples |
| --- | --- | --- |
| **[Inputs](inputs.md)** | Bring text into the flow | Paste text, supply a JSON document, or pull a batch of files from cloud storage |
| **[Extractors](extractors.md)** | Pull structured details out of the text | Places, people, organizations, and custom record types you define |
| **[Enrichment](enrichment.md)** | Refine extracted details or assign article-level metadata | Geocoding places into map coordinates; adding Article Meta tags |
| **[Embedding](embedding.md)** | Prepare content for semantic ("meaning-based") search | Indexing article text and images |
| **[Outputs](outputs.md)** | Save or export the results | Save into your catalog, view as JSON, or write files back to cloud storage |
| **[Flow control](flow-control.md)** | Shape how data moves through the flow | Gathering multiple branches together |

## A typical flow

Most flows follow the same left-to-right shape: bring text in, extract details, optionally enrich them, then save the results.

For example, a flow that maps the places in your reporting might be:

> **Paste text → Find places → Geocode → Save to database**

## How data moves between nodes

The article supplied by the input remains available throughout the flow.
Specialized outputs travel along their branch: Place Extract produces places
that Geocode can enrich, while Person Extract produces people. A later Gather
step can collect several branches for an output that needs them together.

Agate uses these requirements to limit the add-step menu. If a node is not
offered at a particular point, its required upstream data is not available
there yet.

## Node panels

Selecting a node opens its panel. The available tabs depend on the node:

- **Settings** controls its normal behavior.
- **Prompt** shows configurable instructions for model-backed extraction.
- **Models** selects approved model roles where a step needs more than one.
- **Info** explains inputs, outputs, and other details.
- **Output** shows that node's result when viewing a completed run.

The names and choices shown in a panel belong to the node itself, but model and
integration options come from the current project's settings.

## How nodes use AI

Many extractors and enrichment steps use AI models to read text and identify details. You choose which model a node uses from a list your administrators have approved, and Backfield tracks the estimated cost of each run. See [AI models](../../settings/ai-models.md).

Not every node uses AI. Inputs, outputs, Gather, and some deterministic
enrichment work without a generative model. A model-backed node should still
produce structured output and evidence that editors can inspect later.

## In this section

- **[Inputs](inputs.md)** — getting text into a flow
- **[Extractors](extractors.md)** — finding places, people, organizations, topics, and custom records
- **[Enrichment](enrichment.md)** — refining extracted details, such as geocoding
- **[Embedding](embedding.md)** — preparing content for semantic search
- **[Outputs](outputs.md)** — saving results and exporting
- **[Flow control](flow-control.md)** — combining branches
