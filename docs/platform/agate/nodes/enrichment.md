# Enrichment nodes

**Enrichment nodes** refine or look up the entities identified by an [extractor](extractors.md) or assign metadata to the article text itself.

| Node | What it adds |
| --- | --- |
| **Article metadata** | Tags for the article as a whole, such as format, topic, subject, or other configured metadata categories |
| **Geocode** | Turns a place name into map coordinates and a normalized address, so locations can be plotted and searched geographically |

## Article metadata

The **Article Metadata** node classifies the full article, rather than one extracted entity. Use it when you want each processed item to carry tags that can later power search, filtering, dashboards, or downstream analysis.

You can choose from preset tag categories or define project-specific metadata types. The selectable categories include:

| Category | What it describes | Taxonomy |
| --- | --- | --- |
| **Critical information need** | Civic information needs the story helps answer | [Critical Information Need](../../../api/taxonomy/article-meta/critical-information-need.md) |
| **Custom** | Project-specific metadata defined by your team | [Custom](../../../api/taxonomy/article-meta/custom.md) |
| **Format** | How the story is structured, such as news story, profile, obituary, or opinion | [Format](../../../api/taxonomy/article-meta/format.md) |
| **Scope** | The story's geographic, civic, or editorial scope | [Scope](../../../api/taxonomy/article-meta/scope.md) |
| **Subject** | The concrete thing the story is primarily about, such as a legal case, public meeting, traffic crash, or development project | [Subject](../../../api/taxonomy/article-meta/subject.md) |
| **Timeframe** | The time horizon the story concerns, such as breaking, recent, ongoing, or historical coverage | [Timeframe](../../../api/taxonomy/article-meta/timeframe.md) |
| **Topic** | Broad coverage areas, such as local government, public safety, sports, or education | [Topic](../../../api/taxonomy/article-meta/topic.md) |
| **User need** | The audience need the story serves, such as explaining, updating, guiding, or contextualizing | [User Need](../../../api/taxonomy/article-meta/user-need.md) |

Article metadata becomes available to
[Backfield API](../../../api/taxonomy/article-meta/index.md#querying-with-meta),
where applications can use it for filtering and analysis.

The node records the selected value, a rationale, and confidence information
that editors can inspect on the processed item's **Meta** tab. Reviewers can
correct, add, or remove tags without changing the original model output.

Choose categories that serve a real downstream question. A small, consistently
applied taxonomy is usually more useful than many overlapping tags.

## Geocoding places

The **Geocode** node consumes the locations produced by Place Extract. It uses
the extracted name, type, address components, jurisdiction, and contextual
hints to look for a defensible map result.

A location can finish with:

- accepted point, line, or area geography;
- a match to known Stylebook geography;
- identity information but no safe geometry;
- a review-required result explaining why the lookup was uncertain.

Backfield does not force every place onto a map. Keeping “no geography” is
safer than attaching a story to the wrong city, address, district, or venue.
Editors can inspect and adjust results on the processed item's **Places** tab.

Geocoding uses the services configured under
[Integrations](../../settings/integrations.md). Missing credentials, ambiguous
names, conflicting jurisdictions, or incomplete addresses can all affect the
result without invalidating the extracted mention itself.

## Enrichment and provenance

Enrichment adds information to an existing article or entity result; it does
not replace the source evidence. The original mention remains available so an
editor can judge whether the added tag or geography is supported.