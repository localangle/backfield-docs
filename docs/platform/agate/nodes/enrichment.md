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

Article metadata appears in article `metadata[]` and can be queried with `meta` filters in the [Public API](../../../api/taxonomy/article-meta/index.md#querying-with-meta).