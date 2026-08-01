# AI models

Many Agate steps — especially
[extractors](../agate/nodes/extractors.md) — use AI models to read text,
identify details, or create semantic embeddings. The **AI models** settings
create an approved catalog so flow builders choose named configurations rather
than entering provider and billing details on every node.

## The model catalog

An organization administrator can add a curated preset or define a custom model
configuration. A catalog entry records:

- a readable name shown to flow builders;
- the provider model identifier;
- whether it is generative or embedding-oriented;
- capabilities that determine which nodes may use it;
- the saved provider credential or endpoint;
- optional input and output prices used for estimates;
- whether the configuration is active or disabled.

Disabling a configuration removes it from new choices without erasing the
history of runs that used it.

## Organization and project choices

- **Administrators** define the organization catalog and save provider
  credentials.
- **Projects** inherit approved models, can enable the subset they use, and can
  choose defaults for supported roles.
- **Flow builders** see only compatible, enabled choices in each node's settings.

Some deployments allow project-specific provider credentials. These let a
project use its own billing boundary while keeping the model configuration
under organization control.

## Testing and credentials

Saved credentials are not displayed after entry. Administrators can see whether
a credential is configured, replace or remove it, and test a model connection
before teams depend on it in a flow.

Removing a credential can affect every model linked to it, so check the linked
model list before changing a shared credential.

## Cost estimates

Backfield records the **estimated cost** of each [run](../agate/runs.md),
broken down by step, so teams can compare the estimated model cost of their
flows.

Estimates use the prices stored with the model configuration and the usage
reported during execution. They are useful for comparison and monitoring, but
the provider's invoice remains the billing record.
