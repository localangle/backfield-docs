# Build a first flow

Build a reusable article-processing flow with an input, extraction steps, and
an output.

!!! note "Tutorial outline"
    Detailed steps, sample text, and screenshots are still to come.

## You'll learn

- How the guided builder adds compatible steps and automatic connections.
- When to use sequential steps, parallel branches, and Gather.
- How node settings, prompts, models, and output tabs differ.
- Why JSON Output and Backfield Output lead to different downstream behavior.

## Before you begin

You need a project with an enabled generative model. Use a short sample article
that contains at least one person, organization, and location.

## Planned walkthrough

1. Create a flow and choose **Text Input**.
2. Choose **JSON Output** while testing the shape.
3. Add parallel Person Extract, Organization Extract, and Place Extract steps.
4. Add Geocode after Place Extract.
5. Open each node panel and review its model and prompt.
6. Resolve validation messages and save the flow.
7. Run the sample and inspect per-node output.
8. Duplicate the flow and replace JSON Output with Backfield Output for
   persistent article and Stylebook data.

## Related concepts

- [Flows](../../platform/agate/flows.md)
- [Nodes](../../platform/agate/nodes/index.md)
- [Output nodes](../../platform/agate/nodes/outputs.md)
