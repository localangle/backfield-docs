# Canonicalization

**Canonicalization** is the process of deciding whether a person, organization,
or place found in an article is already in the Stylebook, is genuinely new, or
needs an editor's judgment. It connects article evidence to durable identities
without treating every extracted name as a new record.

This happens when an Agate flow saves its results (the **Backfield Output** step — see [Output nodes](../agate/nodes/outputs.md)). For each extracted entity, the result is one of:

| Outcome | What it means |
| --- | --- |
| **Link** | The entity confidently matches an existing canonical record, so the mention is attached to it |
| **Create** | No good match exists, so a new canonical record is created |
| **Set aside for review** | The match is uncertain, so the item waits in a **candidate** queue for an editor to decide |

Linking to an existing canonical does not overwrite its editorial fields with
the latest article extraction. The article-specific record and evidence are
attached while the canonical remains the newsroom's authoritative identity.

## What matching considers

Matching rules differ by entity type:

- **People** use normalized names, aliases, and affiliation signals. Similar
  names are not enough when evidence suggests different people.
- **Organizations** use names, aliases, acronyms, and organization types.
  Ambiguous acronym matches are held for review.
- **Locations** use names, location types, address and jurisdiction
  information, and available geography. Missing geography is not automatically
  an identity conflict.

Inactive records are excluded from automatic linking. Final safeguards can
reject a proposed link when type, name, address, or jurisdiction evidence
conflicts.

## Rules and AI assistance

You can run canonicalization in two modes:

- **Rules** — match using fixed, predictable logic only.
- **AI-assisted** — when the rules are unsure, an AI model helps judge whether two records are really the same real-world thing, within careful guardrails.

AI assistance considers only a limited set of recalled candidates and must
return a structured, sufficiently confident decision. It cannot bypass the
same final identity safeguards. Uncertain or contradictory results remain for
editorial review.

## Candidate queues

Items set aside for review appear in a candidate queue for their entity type.
The queue spans accessible projects assigned to the current Stylebook and shows
project provenance when several projects contribute.

For each candidate, an editor can:

- **link** it to an existing canonical;
- **create** a new canonical from the article record;
- **defer** it, moving it out of the active linking queue;
- inspect review reasons, evidence, suggested matches, and similar records.

The queue separates **For review** and **Deferred** work. Deferral is useful
when a record should not be resolved now; it is not the same as linking or
deleting the article evidence.

AI review can suggest link, create, or defer actions, and editors can accept
suggestions individually or in supported bulk workflows. The accepted action
uses the normal editorial operation and remains attributable as a decision.

## Canonical cleanup

Canonicalization handles incoming article records. **Stylebook Review** checks
the catalog after records exist. Its checks can flag duplicates, mismatched
records, questionable canonicals, and location geography concerns. Editors can
merge, keep separate, delete an empty record, or dismiss an issue; dismissals
remain in place until new evidence warrants another review.
