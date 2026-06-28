# Errors

Errors use a consistent JSON body:

```json
{
  "detail": "Human-readable message"
}
```

## Status codes

| Status | Meaning |
| --- | --- |
| `400` | Malformed request or invalid parameter (e.g. bad date format) |
| `401` | Missing or invalid API key |
| `403` | API key lacks access to the requested project |
| `404` | Project, article, or canonical not found — or outside caller scope |
| `503` | Requested capability is temporarily unavailable |

## Not found responses

For privacy and security, **404** can mean either "does not exist" or "not accessible with this API key."

Treat it as "not found in this project for this key."

## Validation examples

Invalid date on article search:

```json
{
  "detail": "Invalid pub_date_from. Use YYYY-MM-DD."
}
```

Invalid `entity_type` filter on article mentions:

```json
{
  "detail": "Invalid entity_type. Use location, person, or organization."
}
```
