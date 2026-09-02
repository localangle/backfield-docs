# AI Disclosure

## How AI is used in Backfield

Backfield uses generative AI models to perform a variety of
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
individual nodes when flows are created.

## Human review

One important principle of Backfield is that AI judgments should be transparent
and reviewable.

To that end, AI-based extractions (of people, places, organizations and custom
data) are designed to be clearly connected to their source text, which users can
see when they view processed items.

Connections between structured information and its source passages are made
using deterministic logic, which ensures large language models cannot hallucinate
erroneous results.

Most information that is extracted from or enriched by a LLM can be overridden
by a human, except (for now) for some small secondary pieces of metadata, such as
that explaning the relationship between an entity and the article the entity is
referenced within.

## How AI was used to build Backfield

In addition to AI use within the platform, generative AI is also used to
write code and documentation for Backfield.

Early versions of Backfield were written mostly by hand. Those core pieces
continue to guide the broad architecture of the application, as well as many
of its concepts and workflows.

The code for the current version of Backfield was written almost entirely by coding
agents and reviewed by humans. It follows architectural guidelines and best practices
documented in the repository.

With the exception of this page and several others, this documentation is written 
and maintained by generative AI systems that update it automatically whenever the
code is meaningfully changed. These changes are reviewed by humans in the form of
pull requests.
