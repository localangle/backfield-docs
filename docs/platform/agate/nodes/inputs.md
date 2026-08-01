# Input nodes

**Input nodes** bring text into a [flow](../flows.md). Every flow starts with one. You choose an input based on where your text is coming from.

| Node | Use it when… |
| --- | --- |
| **Text input** | You want to paste or type text directly |
| **JSON input** | Your content comes as a structured JSON document |
| **S3 input** | You want to process a batch of files stored in Amazon S3 cloud storage |

The text or document an input provides becomes the starting material that [extractor nodes](extractors.md) work on.

## Choosing an input

**Text Input** is the quickest way to test a flow. The article is entered when
you run it, so the same flow can be tried with different sample stories.

**JSON Input** is useful when you have one structured article and want to keep
fields such as headline, URL, author, publication date, and images alongside
the text.

**S3 Input** is designed for repeatable batches. It scans a bucket and prefix
for article JSON files, creates one processed item per accepted file, and keeps
an ingestion ledger so unchanged object versions are not processed again by
later runs. Use **Process files again** only when a deliberate rerun should
ignore that protection.

## JSON format

JSON and S3 inputs expect each article as a JSON object. The only required field is `text`; the other fields are optional metadata that make processed items easier to identify and review.

```json
{
  "publication": "Example Daily",
  "headline": "City council approves bridge repairs",
  "url": "https://example.com/news/bridge-repairs",
  "author": "Riley Chen",
  "pub_date": "2024-05-14",
  "updated": "2024-05-14T18:15:18.425000-05:00",
  "text": "The city council approved emergency repairs to the Riverside Bridge on Tuesday.\n\nMayor Jane Doe said the work will begin next month and is expected to take six weeks.\n\nThe project will be managed by the Department of Transportation.",
  "images": [
    {
      "id": "image:bridge-repairs-001",
      "url": "https://example.com/images/bridge-repairs.jpg",
      "caption": "The Riverside Bridge will close for repairs next month."
    }
  ],
  "entry_id": "https://example.com/news/bridge-repairs"
}
```

For **JSON input**, paste or provide one object in this shape. For **S3 input**, store each article as a `.json` file with this shape, then point the node at the bucket and prefix that contain those files.

## Identity and updates

The optional `entry_id` gives an article a stable source identity. A durable
CMS URL or source-system ID works well. Stable identity helps Backfield
recognize that a later run refers to an article it has seen before, rather than
creating an unrelated duplicate.

For S3, object version information also controls whether a file is considered
unchanged. Moving or rewriting source files can therefore affect what a later
scan sees.

## Images

Each image may include a source ID, URL, and caption. Image-aware nodes can
describe or embed these images, and the processed item keeps them with the
article. The image file still needs to be reachable by the services performing
that work.

## Before a run

The input panel shows the fields required by the selected input. S3 also needs
configured [AWS integration credentials](../../settings/integrations.md).
Input nodes bring content into Agate; collecting stories from a CMS, feed, or
scraper happens outside the flow.
