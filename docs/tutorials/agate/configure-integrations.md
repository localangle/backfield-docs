# Configure integrations

Configure the outside services that flows use for geocoding, search, and S3
storage, then apply a project override where needed.

!!! note "Tutorial outline"
    Detailed steps and screenshots are still to come.

## You'll learn

- Which flow nodes use Geocode Earth, Geocodio, Brave Search, and Amazon S3.
- How organization defaults and project overrides interact.
- Why saved secret values are never displayed again.
- How to diagnose a node that is missing a required integration.

## Before you begin

You need organization-administrator access and the credentials your
organization intends to use. For S3, collect the access-key ID, secret key, and
optional session token.

## Planned walkthrough

1. Open **Settings → Integrations**.
2. Add organization credentials for geocoding and search.
3. Add a complete S3 credential set.
4. Confirm the configured status without exposing the saved secret.
5. Open a project and inspect its **Integrations** tab.
6. Add and remove one project-specific override.
7. Run a small flow that exercises the configured service.

## Related concepts

- [Integrations](../../platform/settings/integrations.md)
- [Enrichment nodes](../../platform/agate/nodes/enrichment.md)
- [Input nodes](../../platform/agate/nodes/inputs.md)
