# Extract people, organizations, and places

Configure entity extractors that produce structured, evidence-backed results
from article text.

!!! note "Tutorial outline"
    Detailed steps, sample output, and screenshots are still to come.

## You'll learn

- What Person Extract, Organization Extract, and Place Extract produce.
- How article entities, mentions, and canonical records differ.
- How evidence supports later editorial review.
- Why Place Extract should feed Geocode on the same branch.

## Before you begin

Complete [Build a first flow](build-flow.md) or open a flow with Text or JSON
Input and an output node. Enable a compatible generative model.

## Planned walkthrough

1. Add the three entity extractors on parallel branches.
2. Review their default prompts and structured output formats.
3. Select a project-approved model.
4. Add Geocode after Place Extract and review its dependencies.
5. Run an article containing names, quotes, institutions, and ambiguous places.
6. Inspect evidence and entity fields on the processed item.
7. Identify one uncertain result that should remain for editorial review.

## Related concepts

- [Extractor nodes](../../platform/agate/nodes/extractors.md)
- [Data model](../../platform/concepts/content-model.md)
- [Canonicalization](../../platform/stylebook/canonicalization.md)
