# Extractor nodes

**Extractor nodes** are the heart of a [flow](../flows.md): they read the text and pull out the structured details you care about. Most extractors use an AI model (see [AI models](../../settings/ai-models.md)) and capture the exact passage each detail came from, so results can be verified later.

| Node | What it finds |
| --- | --- |
| **Place extract** | Locations mentioned in the text |
| **Person extract** | People |
| **Organization extract** | Companies, agencies, and other organizations |
| **Custom extract** | Record types you define yourself, with your own fields |
| **Article metadata** | Topic and format tags for the article as a whole |

Extracted people, places, and organizations can flow into your [Stylebook](../../stylebook/index.md) catalog when the flow saves its results. See [Canonicalization](../../stylebook/canonicalization.md).

!!! note "Coming soon"
    This page will cover writing extraction instructions, defining custom record types, and how grounding passages are captured for review.
