# Canonicalization

**Canonicalization** is the process of deciding whether a person or place found in an article is one you already have in your catalog, a brand-new one, or something an editor should look at. It's how scattered [mentions](mentions.md) get tied to a single **canonical** record instead of creating duplicates.

This happens when an Agate flow saves its results (the **Backfield Output** step — see [Output nodes](../agate/nodes/outputs.md)). For each extracted entity, the result is one of:

| Outcome | What it means |
| --- | --- |
| **Link** | The entity confidently matches an existing canonical record, so the mention is attached to it |
| **Create** | No good match exists, so a new canonical record is created |
| **Set aside for review** | The match is uncertain, so the item waits in a **candidate** queue for an editor to decide |

You can run canonicalization in two modes:

- **Rules** — match using fixed, predictable logic only.
- **AI-assisted** — when the rules are unsure, an AI model helps judge whether two records are really the same real-world thing, within careful guardrails.

Items set aside for review appear in a **candidate queue**, where editors confirm matches, create records, or merge duplicates — with the original reasons and evidence shown to help them decide.

!!! note "Coming soon"
    This page will cover the candidate queue, suggested matches, linking and merging, and how the two modes differ in practice.
