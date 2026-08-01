# Run and monitor a flow

Start a single-item or batch run, understand its status, and locate items that
need attention.

!!! note "Tutorial outline"
    Detailed steps and screenshots are still to come.

## You'll learn

- How Text, JSON, and S3 inputs change the launch experience.
- How run-level and item-level statuses differ.
- Where to find per-step progress, errors, duration, and estimated model cost.
- How stopping, replaying, and rerunning selected items differ.

## Before you begin

Use a saved, valid flow with enabled models and integrations. For an S3 batch,
prepare the bucket, prefix, credentials, and correctly shaped article files.

## Planned walkthrough

1. Start a Text Input run and follow it from pending to completed.
2. Open the run detail and inspect its saved flow snapshot.
3. Review item counts, per-step cost, duration, and errors.
4. Filter and sort the processed-item table.
5. Compare a normal S3 scan with replay and **Process files again**.
6. Stop an active test run and observe bounded cancellation.
7. Select failed items on a page and prepare a bulk rerun.

## Related concepts

- [Runs](../../platform/agate/runs.md)
- [Input nodes](../../platform/agate/nodes/inputs.md)
