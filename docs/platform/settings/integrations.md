# Integrations

**Integrations** are the outside services Backfield uses while running flows — separate from the [AI models](ai-models.md) that read your text. They're configured in one place so credentials stay organized and secure.

| Integration | Used for |
| --- | --- |
| **Geocoding** | Turning place names into map coordinates (used by the [Geocode](../agate/nodes/enrichment.md) step) |
| **Web search** | Looking up information on the web where a flow needs it |
| **Object storage (Amazon S3)** | Reading batches of files and writing results back |

Like other [settings](index.md), integrations have organization defaults with optional project overrides. Some helper services are always built in and need no setup; the settings screen still lists them so you can see the full picture of what's in use.
