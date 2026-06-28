# Agate

Agate is where you build and run the pipelines that read your text and pull out structured information. If you've ever sketched a process on a whiteboard as a series of connected boxes, Agate will feel familiar — you assemble a pipeline visually, then run your articles through it.

## The three ideas to know

Everything in Agate revolves around three connected concepts:

| Concept | Plain-English meaning |
| --- | --- |
| **[Flow](flows.md)** | The pipeline itself — a series of steps wired together. You build it once and reuse it. |
| **[Run](runs.md)** | What happens when you execute a flow on some text. One run can process a single article or a whole batch. |
| **[Processed item](processed-items.md)** | The result for one article: the people, places, and details the flow found — which you can review and correct. |

## What a flow is made of

A flow is built from **[nodes](nodes/index.md)** — the individual steps. Each node does one job, and you connect them so the output of one becomes the input of the next. A typical flow brings text in, extracts details, optionally enriches them, then saves the results.

Nodes come in a handful of families — bringing text in, pulling details out, enriching them, and saving the results. See the [Nodes overview](nodes/index.md) for the full picture.

## From Agate into Stylebook

Agate doesn't just produce a report — it can feed your reference catalog. The **output** step that saves results (called **Backfield Output**) is the handoff point into [Stylebook](../stylebook/index.md): as it saves, it can match each extracted person or place against your existing catalog, linking to a known record or proposing a new one. How aggressively it does this is a setting called **[canonicalization](../stylebook/canonicalization.md)**, which you can run by fixed rules or with AI assistance.

This is why the same place mentioned across many articles can end up as a single, clean entry in your catalog rather than dozens of duplicates.

## In this section

| Page | What it covers |
| --- | --- |
| [Flows](flows.md) | Building pipelines, reusing them, and starter templates |
| [Nodes](nodes/index.md) | The building blocks, grouped by what they do |
| [Runs](runs.md) | Running flows on one item or a batch, and tracking progress |
| [Processed items](processed-items.md) | Reviewing and correcting results article by article |

!!! note "Work in progress"
    These pages introduce the concepts. Step-by-step builder guides will follow.
