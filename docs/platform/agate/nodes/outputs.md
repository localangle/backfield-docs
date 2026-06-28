# Output nodes

**Output nodes** decide what happens to a [flow](../flows.md)'s results. Every flow ends with one.

| Node | What it does |
| --- | --- |
| **Output** | Presents the combined results as JSON for viewing — useful for inspection and testing |
| **Backfield Output** | Saves results into your project, including matching people and places into your [Stylebook](../../stylebook/index.md) catalog |
| **S3 Output** | Writes the results back to Amazon S3 cloud storage as files |

**Backfield Output** is the most important one to understand: it's the bridge into your catalog. As it saves, it can match each extracted person or place against existing records — linking, proposing a new record, or setting an item aside for review. That matching behavior is controlled by [canonicalization](../../stylebook/canonicalization.md) settings, which you can run by fixed rules or with AI assistance.

!!! note "Coming soon"
    This page will cover each output's options, including catalog matching settings and file naming for cloud exports.
