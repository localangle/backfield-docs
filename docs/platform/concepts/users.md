# Users & access

A Backfield **user** belongs to one or more
[organizations](organizations.md). Within each organization, access is built
from an organization role, workspace membership, and Stylebook editing rights.

If a person belongs to several organizations, they choose one when signing in
and can switch organizations from the account menu. Backfield keeps each
organization's projects and settings separate.

## How access works

- **Organization membership** is the starting point — a person must belong to your organization before they can do anything.
- **Organization role** is either member or organization administrator.
- **Workspace access** determines which grouped projects a member can open in
  Agate.
- **Stylebook editing access** determines which Stylebooks a member may curate.
  It is managed separately because one Stylebook can serve several projects or
  workspaces.

## Members and organization administrators

| Role | What it means |
| --- | --- |
| **Member** | Can work in assigned workspaces and projects, and can edit only the Stylebooks explicitly assigned to them |
| **Organization administrator** | Can access all projects and Stylebooks and manage users, Stylebooks, AI models, integrations, and other organization-wide settings |

A member's day-to-day work can include building and running
[flows](../agate/flows.md), reviewing
[processed items](../agate/processed-items.md), and curating an assigned
[Stylebook](../stylebook/index.md).

## When access changes

Administrators can change a user's role, workspace memberships, and Stylebook
editing access independently. They can also disable an account. Removing
organization or project access invalidates affected user-owned
[API keys](../settings/api-keys.md) on their next request, because those
credentials are checked against the owner's current access every time.

## Why this matters for security

Some settings involve sensitive credentials — provider keys for AI models, geocoding services, or cloud storage. These are restricted to administrators so that keys and billing boundaries stay protected. Everyday editors can use the configured services without ever seeing the underlying secrets.

Newly provisioned users may be required to replace a temporary password before
they can open other parts of the platform.

For programmatic access (your own scripts and applications), use a project
[API key](../settings/api-keys.md) instead of sharing a personal login.
