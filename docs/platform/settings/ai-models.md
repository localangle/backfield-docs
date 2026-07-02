# AI models

Many Agate steps — especially [extractors](../agate/nodes/extractors.md) — use AI models to read text and identify details. The **AI models** settings control which models are available and keep your team using approved, vetted options rather than arbitrary choices.

How it works:

- **Administrators** define the catalog of approved models for the organization and supply the provider credentials once.
- **Projects** inherit that catalog, can turn individual models on or off, and can set their own defaults or bring their own provider keys.
- **Flow builders** pick from the approved models in node settings, filtered to those suitable for the step.

Backfield records the **estimated cost** of each [run](../agate/runs.md), broken down by step, so teams can see what their pipelines cost. Cost records don't store the content of your prompts or the model's responses.
