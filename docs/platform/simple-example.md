# Simple Example

The easiest way to understand Backfield is by example. This page follows a short (fake) news article from raw text to structured, queryable data — the same path every story takes through the platform.

## The story

Imagine your newsroom publishes this brief:

> **Riverside Bridge repairs approved after months of delay**
>
> SPRINGFIELD, Ill. — The Springfield City Council voted 6–1 on Tuesday to approve a $2.4 million contract with Harlan Construction Co. to repair the aging Riverside Bridge, closed to trucks since a February inspection found cracks in two support beams.
>
> "We can't ask people on the east side to detour around the river for another winter," said Mayor Jane Doe, who pushed for the expedited timeline.
>
> Councilmember Marcus Webb cast the lone dissenting vote, citing concerns about the no-bid process. Work is expected to begin near Riverside Park in March.

To a reader, this presents as a 100-word brief. To Backfield, it's a bundle of structured facts: two named officials (one quoted), a government body, a construction company, several places, and some metadata.

## Step 1: Build and run a flow

We'll start by building an [Agate flow](agate/flows.md) to process the article. We'll paste our text into the input.

![Text input node with the sample Riverside Bridge story pasted into Agate](images/simple-example/qs1.png)

And then we will construct a pipeline of interconnected [nodes](agate/nodes/index.md) — in this case, assigning some topical metadata; creating a semantic embedding of the article; extracting people, places and organizations; and geocoding the locations so they can be plotted on a map.

![Demo flow with text input, metadata, embedding, person, organization, place, geocoding, and JSON output nodes](images/simple-example/qs2.png)

Executing the flow creates [Run](agate/runs.md), which processes the article in a matter of seconds.

The run details drawer confirms that the flow has started, and the run page shows each processed item's status with a link to review the story.

=== "Start a run"

    ![Run details drawer showing the demo flow running](images/simple-example/qs3.png)

=== "Run details"

    ![Run page showing a single processed item for the Springfield story](images/simple-example/qs4.png)

## Step 2: Review the output

Once the run finishes, the story becomes a [processed item](agate/processed-items.md) — a review page with one tab for each type of data extracted by the flow.

Editors can review and change each canonical type of data extracted from the story, as well as metadata we assign to the story itself.

=== "Places"

    ![Places tab showing highlighted location mentions, a map, and geocoded places](images/simple-example/qs5-1.png)

=== "People"

    ![People tab showing highlighted people mentions and extracted person rows](images/simple-example/qs5-2.png)

=== "Organizations"

    ![Organizations tab showing organization mentions and extracted organization rows](images/simple-example/qs5-3.png)

=== "Meta"

    ![Meta tab showing topic tags, rationale, and confidence](images/simple-example/qs5-4.png)

Every piece of extracted data is tied to **evidence** — the exact, word-for-word passages within an article that reference the data. Select a person, organization or location and the source material for each will be highlighted in the review interface.

## Step 3: Correct any mistakes

Models make mistakes, so Agate is built for verification. When reviewing a processed item, an editor can:

- Fix incorrect metadata
- Remove a spurious extraction
- Add something the model missed, anchored to a passage in the story
- Adjust map coordinates for a place

Corrections are saved as a **review layer** on top of the original model output, and you always recover the original extraction if you need it. See [Processed items](agate/processed-items.md).

=== "Adjust geography"

    ![Places review screen showing an editable map shape for a geocoded place](images/simple-example/qs6-1.png)

=== "Edit place details"

    ![Places review screen showing editable place label, type, mentions, and role in story](images/simple-example/qs6-2.png)

## Step 4: Curate Stylebook records

Suppose your newsroom has written 50 stories about Mayor Jane Doe. Backfield treats each as a separate **mention** — all tied to a single canonical person.

When a flow saves its results, [Stylebook](stylebook/index.md) matches each extracted person, place, and organization against your catalog of **canonical records**. This story's "Mayor Jane Doe" links to the same canonical Jane Doe as every previous story, through a process called [canonicalization](stylebook/canonicalization.md).

The canonical record accumulates everything the newsroom knows: every variation of a source's name; each mention with its evidence, [connections](stylebook/connections.md) to other entities (Jane Doe *works at* City Hall), and any metadata your editors choose to add. See [The content model](concepts/content-model.md) for how mentions and entities fit together.

=== "Canonical details"

    ![Stylebook canonical location page showing details and map geometry for Springfield, IL](images/simple-example/qs7-1.png)

=== "Mentions"

    ![Stylebook canonical location page showing article mentions grouped under Springfield, IL](images/simple-example/qs7-2.png)

=== "Connections"

    ![Stylebook canonical location page showing metadata and connections to other canonical records](images/simple-example/qs7-3.png)

## Step 5: Query data via the API

Everything above is now available through the [Public API](../api/index.md). A few things you could ask for:

Every story that mentions Jane Doe:

```bash
curl "http://localhost:8004/public/v1/projects/general/people/{jane_doe_id}/articles" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Every source your organization has quoted in local-government coverage:

```bash
curl "http://localhost:8004/public/v1/projects/general/mentions/search?entity_type=person&quote=true&meta=topic:local_government_politics" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

Articles that mention places near the bridge:

```bash
curl "http://localhost:8004/public/v1/projects/general/articles/geo-search?center_lng=-89.65&center_lat=39.80&radius_miles=2" \
  -H "Authorization: Bearer bfk_your_project_api_key"
```

And much more. See the [API Reference](../api/index.md) for more examples of what data can be queried and how.

## Where to go next

- Set up the stack locally in [Getting Started](getting-started.md)
- Build the pipeline in [Agate → Flows](agate/flows.md)
- Understand the catalog in [Stylebook](stylebook/index.md)
- Query your data in the [API Reference](../api/index.md)