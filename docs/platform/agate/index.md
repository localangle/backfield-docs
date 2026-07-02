# Agate

Agate is where you build and run the pipelines that pull structured data from your text and enrich it with arbitrary metadata. It does this through composable workflows that you construct from a library of nodes.

[SCREENSHOT]

## Three concepts to know

Agate executions revolve around three connected concepts:

| Concept | Definition |
| --- | --- |
| **[Flows](flows.md)** | The pipeline itself — a series of steps wired together. You build it once and reuse it. |
| **[Runs](runs.md)** | What happens when you execute a flow on some text. One run can process a single article or a whole batch. |
| **[Processed items](processed-items.md)** | The result for one article: the people, places, and details extracted by the flow — which you can review and correct. |

## Building flows

A flow is built from **[nodes](nodes/index.md)**. Each node does one job, and you connect them so the output of one becomes the input of the next. A typical flow brings text in, extracts details, optionally enriches them, then saves the results.

Nodes come in a variety of flavors, and developers can create new ones for specific tasks. See the [Nodes overview](nodes/index.md) for the full picture.

## From Agate into Stylebook

Generally, Agate either produces raw JSON (via JSON or S3 Output nodes) you can process on your own or feeds into the shared Backfield database that supports applications like Stylebook.

The **Backfield Output** node is responsible for saving data into the Backfield ecosystem. As it saves, it can match each extracted person or place against your [Stylebook](../stylebook/index.md), reconciling data with known records, proposing new ones and forming connections between them.

This process is known as **[canonicalization](../stylebook/canonicalization.md)** and can be performed fixed rules or with AI assistance.

## In this section

| Page | What it covers |
| --- | --- |
| [Flows](flows.md) | Building and executing pipelines |
| [Nodes](nodes/index.md) | The building blocks, grouped by what they do |
| [Runs](runs.md) | Running flows on one item or a batch, and tracking progress |
| [Processed items](processed-items.md) | Reviewing and correcting results article by article |
