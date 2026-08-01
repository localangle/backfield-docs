# Rerun processed items safely

Rerun one or more items after changing a flow while accounting for review
overlays and Backfield Output reconciliation.

!!! note "Tutorial outline"
    Detailed steps and screenshots are still to come.

## You'll learn

- Why reruns use the current saved flow rather than the historical snapshot.
- When run-local review changes are cleared.
- How Add Only, Smart Merge, and Replace affect machine-generated evidence.
- Which editor-created and canonical changes are protected.

## Before you begin

Use a completed run with a Backfield Output node and at least one reviewed item.
Record the current reconciliation policy and the correction you expect to
change.

## Planned walkthrough

1. Compare the run snapshot with the current flow.
2. Make and save a small prompt or model change.
3. Start a rerun and read the full confirmation warning.
4. Verify editing is locked while regeneration is active.
5. Compare the new original output with the previous reviewed result.
6. Repeat with a selected failed-item batch.
7. Review how each reconciliation policy would treat omitted machine evidence.

## Related concepts

- [Runs](../../platform/agate/runs.md#cancellation-failures-and-reruns)
- [Output nodes](../../platform/agate/nodes/outputs.md#backfield-output)
