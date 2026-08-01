# Configure AI models

Add approved generative and embedding models at the organization level, then
choose which models a project can use.

!!! note "Tutorial outline"
    Detailed steps, provider examples, and screenshots are still to come.

## You'll learn

- How credentials, catalog models, capabilities, and project defaults differ.
- When to use a curated preset or a custom LiteLLM model identifier.
- How pricing fields feed run cost estimates.
- How project-specific provider credentials override an organization credential.

## Before you begin

You need organization-administrator access and a provider credential. Confirm
whether the model is generative or embedding-oriented and which capabilities
its nodes require.

## Planned walkthrough

1. Open **Settings → AI models**.
2. Save a write-only provider credential.
3. Add a curated or custom model and review its capabilities and prices.
4. Test the model connection.
5. Open a project and enable the model on its **Models** tab.
6. Choose generative and semantic-embedding defaults.
7. Select the model in a compatible flow node.
8. Disable a model and clear a project credential override safely.

## Related concepts

- [AI models](../../platform/settings/ai-models.md)
- [Nodes](../../platform/agate/nodes/index.md)
