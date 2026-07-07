# Nodes

A **node** is a single step in an Agate [flow](../flows.md). Each node does one job, and you connect nodes together so that the output of one becomes the input of the next. You build a pipeline by dragging nodes onto a canvas and connecting them to each other.

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

## How nodes use AI

Many extractors and enrichment steps use AI models to read text and identify details. You choose which model a node uses from a list your administrators have approved, and Backfield tracks the estimated cost of each run. See [AI models](../../settings/ai-models.md).

## In this section

- **[Inputs](inputs.md)** — getting text into a flow
- **[Extractors](extractors.md)** — finding places, people, organizations, topics, and custom records
- **[Enrichment](enrichment.md)** — refining extracted details, such as geocoding
- **[Embedding](embedding.md)** — preparing content for semantic search
- **[Outputs](outputs.md)** — saving results and exporting
- **[Flow control](flow-control.md)** — combining branches
