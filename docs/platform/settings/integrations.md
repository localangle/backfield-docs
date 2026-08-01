# Integrations

**Integrations** are the outside services Backfield uses while running flows — separate from the [AI models](ai-models.md) that read your text. They're configured in one place so credentials stay organized and secure.

| Integration | Used for |
| --- | --- |
| **Geocode Earth** | Primary place lookup for the [Geocode](../agate/nodes/enrichment.md) step |
| **Geocodio** | Additional address and place lookup |
| **Nominatim** | Built-in fallback geocoding service; no saved key is required |
| **Brave Search** | Web and place search used when a location needs more context before it can be resolved |
| **Object storage (Amazon S3)** | Reading batches of files and writing results back |

## Organization defaults and project overrides

Organization administrators save the normal credentials once. Projects inherit
them and can provide supported overrides from the project's Integrations tab.
This is useful when a desk has a separate service account, bucket, or billing
boundary.

The interface shows whether each secret is configured but never reveals a
saved value. Pasting a new value replaces the old one; removing an override
returns the project to the organization default.

## How integrations affect flows

An integration is used only when a flow contains a node that needs it:

- **Geocode** uses configured geocoding and search services to turn extracted
  place descriptions into reviewed geography.
- **S3 Input** reads article JSON from a bucket and prefix.
- **S3 Output** writes structured results back to storage.

Missing credentials therefore do not prevent every flow from running, but the
affected node may fail or be unable to complete its enrichment.

## S3 credentials

Amazon S3 normally requires an access-key ID and secret access key; temporary
credentials may also include a session token. Treat all three as secrets.
Bucket names and prefixes are configured on the S3 nodes because they describe
what a particular flow reads or writes, while credentials belong in settings.
