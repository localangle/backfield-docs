# Build a custom extraction

Extract structured records that do not belong in the canonical people,
organization, or location catalogs.

!!! note "Tutorial outline"
    Detailed steps, sample schemas, and screenshots are still to come.

## You'll learn

- When to use Custom Extract instead of a canonical entity extractor.
- How to define clear fields and useful record types.
- How custom records retain article context and mention evidence.
- How editors review and correct typed custom values.

## Before you begin

Choose one concrete use case, such as public meetings, restaurant inspections,
obituaries, recipes, or events. Prepare two sample articles and a short list of
fields that can be verified from the source.

## Planned walkthrough

1. Add **Custom Extract** to a flow.
2. Name the record type and define string, list, numeric, or date-like fields.
3. Write focused extraction instructions and select a model.
4. Run the flow on the sample articles.
5. Review records and evidence on the processed item's **Custom** tab.
6. Add a missing record, correct a field, and remove an unsupported result.
7. Inspect the reviewed JSON and query saved custom records.

## Related concepts

- [Extractor nodes](../../platform/agate/nodes/extractors.md#custom-extract)
- [Custom records API](../../api/custom-records/index.md)
