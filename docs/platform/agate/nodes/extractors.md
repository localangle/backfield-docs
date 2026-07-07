# Extractor nodes

**Extractor nodes** read text and pull out structured data. Most extractors use an AI model (see [AI models](../../settings/ai-models.md)) to identify, filter or classify entities. They also capture the exact passage each detail came from so results can be verified later.

| Node | What it finds |
| --- | --- |
| **Place extract** | Locations mentioned in the text |
| **Person extract** | People |
| **Organization extract** | Companies, agencies, and other organizations |
| **Custom extract** | Capture types you define yourself, with your own fields |

Extracted people, places, and organizations can optionally flow into your [Stylebook](../../stylebook/index.md) when the flow saves its results. See [Canonicalization](../../stylebook/canonicalization.md).
