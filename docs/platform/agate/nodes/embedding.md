# Embedding nodes

**Embedding nodes** prepare your content for **semantic search** — finding articles by meaning rather than exact keywords. They create a numerical "fingerprint" of text or images that powers meaning-based matching.

| Node | What it indexes |
| --- | --- |
| **Embed text** | Article text, so stories can be found by concept |
| **Embed images** | Images associated with articles |

Semantic search built on these embeddings is available through the API — see [Semantic search](../../../api/articles/semantic-search.md).

## What an embedding is

An embedding is a long list of numbers that represents patterns in content.
Backfield stores that representation for comparison; it is not a summary that
people read. Items with similar meaning can be close even when they do not use
the same words.

This makes embeddings useful for questions such as “find stories about barriers
to public transit” when those exact words may not appear in the articles.

## Text and image embeddings

**Embed Text** indexes article text for semantic article search. **Embed
Images** works on associated images so image-aware features can compare visual
content. They are separate because a model capable of embedding text may not
support images.

The node uses an approved embedding configuration from
[AI models](../../settings/ai-models.md). If a project changes models, new runs
may produce vectors that are not directly comparable with vectors from a
different model. Treat the selected embedding configuration as part of the
search index design.

## What embeddings do not do

An embedding does not verify a fact, identify a person, or replace editorial
metadata. It adds a meaning-based retrieval signal. Keep structured extraction,
taxonomy tags, and source evidence when users need exact filtering or an
explainable reason that an item matched.

The project overview and API expose whether articles have an embedding, which
helps teams see how much content is eligible for semantic search.
