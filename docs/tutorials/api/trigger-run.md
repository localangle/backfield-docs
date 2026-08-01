# Trigger and monitor a run

Start an approved Agate flow from trusted automation and monitor the resulting
run without reproducing flow logic in the calling application.

!!! note "Tutorial outline"
    Detailed payloads, polling code, and failure examples are still to come.

## You'll learn

- How API-triggered runs use saved project flows.
- How input type determines the request payload.
- How to poll run state without creating duplicate work.
- How to surface run and item errors to operators.

## Before you begin

Use a valid saved flow and a purpose-specific service key. Test the flow in
Agate first, including its models, integrations, and output behavior.

## Planned walkthrough

1. Identify the saved flow and its expected input.
2. Trigger a small run with a unique source identity.
3. Store the returned run identifier.
4. Poll the run with bounded backoff until it reaches a terminal status.
5. Inspect completed, failed, and completed-with-errors outcomes.
6. Link operators back to the Agate run and processed items.
7. Retry only when the input identity and desired update behavior are clear.
8. Revoke the tutorial service key.

## Related concepts

- [Trigger run](../../api/runs/trigger-run.md)
- [Get run](../../api/runs/get-run.md)
