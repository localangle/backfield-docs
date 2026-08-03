# AI Disclosure

## How AI is used in Backfield

Backfield primarily uses generative AI models to perform a variety of
extraction, enrichment, and data-cleaning tasks. Among them:

- Identifying people, places, and organizations present in stories and
  structuring them for processing.
- Choosing the most effective strategy for geocoding locations and identifying
  the most relevant results from external services such as search.
- Connecting new data from articles to existing canonical Stylebook entries,
  or surfacing situations where a connection is unclear.
- Enriching articles and entities with metadata, such as classifying articles
  by type or describing the nature and importance of entities relative to the
  documents that contain them.

Prompts for many of these tasks can be modified in the Agate interface through
individual nodes when flows are created. When AI models are used to extract
entities from articles, the specific text from each mention is retained as
evidence for review.

## How AI was used to build Backfield

In addition to AI use within the platform, generative AI was also used to
engineer and document Backfield.

Early versions of Backfield were written largely by hand. Those pieces
continue to inform the broad architecture of the application, as well as many
of its core concepts and workflows.

The code for this version of Backfield was written almost entirely by coding
agents, following architectural guidelines and best practices documented in
the repository.

This documentation was written largely by AI agents and was edited by humans.
