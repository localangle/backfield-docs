# Canonicalization

**Canonicalization** is the process of deciding whether a person, organization,
or location found in an article matches a Stylebook record, is new, or needs an
editor's judgment.

This happens when an Agate flow saves results through
[Backfield Output](../agate/nodes/outputs.md). Each extracted entity has one of
three outcomes:

| Outcome | What it means |
| --- | --- |
| **Link** | Attach the article evidence to an existing canonical record |
| **Create** | No good match exists, so a new canonical record is created |
| **Review** | The match is uncertain, so the item enters a candidate queue |

Linking to an existing canonical does not overwrite its editorial fields with
the latest article extraction. The article-specific record and evidence are
attached while the canonical remains the newsroom's authoritative identity.

## How matching works

Matching rules differ by entity type:

- **People** use normalized names, aliases, and affiliation signals. Similar
  names are not enough when evidence suggests different people.
- **Organizations** use names, aliases, acronyms, and organization types.
  Ambiguous acronym matches are held for review.
- **Locations** use names, location types, addresses, jurisdictions, and
  available geography.

Inactive records are not linked automatically. Conflicting identity
information can prevent a proposed match.

## Rules and AI suggestions

You can run canonicalization in two modes:

- **Rules** uses fixed matching logic.
- **AI-assisted** asks a model for help when the rules are unsure.

AI assistance cannot bypass the identity safeguards. Uncertain or conflicting
results still go to an editor.

## Candidate queues

Unresolved people, organizations, and locations appear in separate candidate
queues. A queue can include work from several projects using the Stylebook and
shows which project produced each candidate.

For each candidate, an editor can:

- **link** it to an existing canonical;
- **create** a new canonical from the article record;
- **defer** it for later;
- inspect its evidence, suggested matches, and similar records.

Deferring a candidate moves it out of the active queue. It does not delete the
article evidence.

AI review can suggest link, create, or defer actions. Nothing changes until an
editor accepts a suggestion.

## Canonical cleanup

Canonicalization handles incoming article entities. **Stylebook Review** checks
records already in the catalog. It can flag duplicates, questionable links,
and location geography concerns. Editors can merge records, keep them
separate, delete an empty record, or dismiss the issue.

Merging moves the linked article records from the duplicate into the record
you choose to keep, then deletes the duplicate. Review both records before
confirming; Stylebook does not provide an undo action. The **Recent** view can
show that the merge occurred, but it cannot restore the deleted record.
