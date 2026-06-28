# Users & access

People sign in to Backfield as **users**. A user is invited to an [organization](organizations.md) and then given access to the projects they need.

## How access works

- **Organization membership** is the starting point — a person must belong to your organization before they can do anything.
- **Project access** determines which projects a member can open and what they can do inside them.
- **Permission levels** separate everyday work (building flows, reviewing items, editing the catalog) from administrative actions (managing members, defining shared [AI models](../settings/ai-models.md) and [integrations](../settings/integrations.md), and managing [Stylebook catalogs](../stylebook/stylebooks.md)).

In general:

- **Editors** do the hands-on work — build and run [flows](../agate/flows.md), review and correct [processed items](../agate/processed-items.md), and curate the [Stylebook catalog](../stylebook/index.md).
- **Viewers** can see results without changing them.
- **Administrators** manage organization-wide settings and who has access.

## Why this matters for security

Some settings involve sensitive credentials — provider keys for AI models, geocoding services, or cloud storage. These are restricted to administrators so that keys and billing boundaries stay protected. Everyday editors can use the configured services without ever seeing the underlying secrets.

For programmatic access (your own scripts and applications), you don't use a person's login — you use a project [API key](../settings/api-keys.md) instead.

!!! note "Work in progress"
    A detailed role-and-permission matrix will be documented here as the access model is finalized.
