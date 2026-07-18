# Output nodes

**Output nodes** decide what happens to a [flow](../flows.md)'s results. Every flow ends with one.

| Node | What it does |
| --- | --- |
| **Output** | Presents the combined results as JSON for viewing — useful for inspection and testing |
| **Backfield Output** | Saves results into your project, including matching people and places into your [Stylebook](../../stylebook/index.md) catalog |
| **S3 Output** | Writes the results back to Amazon S3 cloud storage as files |

**Backfield Output** is the most important one to understand: it's the bridge into other parts of the Backfield ecosystem, including the Stylebook.

As it saves, it can match each extracted entity against existing records, create new ones, and connect them to each other. This matching behavior is controlled by [canonicalization](../../stylebook/canonicalization.md) settings, which you can run by fixed rules or with AI assistance.