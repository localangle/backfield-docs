# Input nodes

**Input nodes** bring text into a [flow](../flows.md). Every flow starts with one. You choose an input based on where your text is coming from.

| Node | Use it when… |
| --- | --- |
| **Text input** | You want to paste or type text directly |
| **JSON input** | Your content comes as a structured JSON document |
| **S3 input** | You want to process a batch of files stored in Amazon S3 cloud storage |

The text or document an input provides becomes the starting material that [extractor nodes](extractors.md) work on.

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
