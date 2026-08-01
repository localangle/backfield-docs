# Output nodes

**Output nodes** decide what happens to a [flow](../flows.md)'s results. Every flow ends with one.

| Node | What it does |
| --- | --- |
| **Output** | Presents the combined results as JSON for viewing — useful for inspection and testing |
| **Backfield Output** | Saves results into your project, including matching people and places into your [Stylebook](../../stylebook/index.md) catalog |
| **S3 Output** | Writes the results back to Amazon S3 cloud storage as files |

## JSON Output

**JSON Output** keeps the combined result available for inspection in the run
and processed item's JSON views. It is useful while designing a flow or when
another system will consume the result without saving Backfield articles and
entities.

## Backfield Output

**Backfield Output** is the bridge into the rest of the Backfield platform. It
saves article content, metadata, images, custom records, and entity evidence in
the project. People, organizations, and locations are matched against the
project's assigned Stylebook.

As it saves, canonicalization may link an existing record, create a new record
when policy allows, or send an uncertain candidate to editors. See
[Canonicalization](../../stylebook/canonicalization.md).

Its settings can also enable supported semantic indexing and automatic
connection inference. These features depend on compatible project models and
the corresponding upstream data. Connection status may appear in Agate, while
the canonical Stylebook record remains the place to edit a saved connection.

The output also defines how a rerun reconciles machine-generated evidence that
was already saved:

| Policy | Conceptual effect |
| --- | --- |
| **Add Only** | Add new results without treating omissions as removals |
| **Smart Merge** | Update compatible machine output while retaining prior data where appropriate |
| **Replace** | Treat the newly emitted machine domains as authoritative, including empty results |

Replace can retire prior machine-generated associations that the new run no
longer emits. Editor-added and editor-modified evidence is preserved.

The Stylebook is inherited from the project and is not selected on an
individual output node.

## S3 Output

**S3 Output** writes the structured result to an Amazon S3 bucket and prefix.
It is useful for downstream data pipelines or archives that consume files
instead of the Backfield database.

The node needs S3 credentials from [Integrations](../../settings/integrations.md).
After review, the processed item's JSON tools can synchronize reviewed output
back to the configured object when that output path is available.

## Choosing an output

Use JSON Output for inspection, Backfield Output for the full editorial and
Stylebook workflow, and S3 Output for file-based delivery. A flow's output
choice determines which review and downstream features are available; merely
extracting an entity does not save it into Stylebook.