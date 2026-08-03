# Organizations & workspaces

Backfield is organized in a simple hierarchy. Understanding it helps you know
where settings live and who can see or change what.

## Organization

An **organization** generally corresponds to your news organization or
company. It is the top-level account and owns everything else: the people who
have access, shared settings such as AI models and integrations, Stylebooks,
and projects. Backfield can host several organizations while keeping their data
separate; users with several memberships choose an organization when signing
in and can switch afterward.

Changing organizations changes the whole working context. The workspaces,
projects, Stylebooks, users, and settings shown in the interface all belong to
the selected organization.

## Workspace

A **workspace** groups related projects under an organization — for example, by
desk, publication, beat, or initiative. The Agate home page is organized around
workspaces, making them the main way people find the projects they can access.

A workspace also sets defaults used when projects are created, such as the
[Stylebook](../stylebook/stylebooks.md). Each project then keeps one
authoritative Stylebook assignment.

Workspace access is also an access shortcut: an organization administrator can
give a member access to a workspace and therefore its projects. Organization
administrators can see every workspace and project.

## Project

A **project** is where day-to-day processing happens — the flows you build, the
runs you execute, and the article evidence those runs produce. A project is
assigned one Stylebook, but the Stylebook itself may collect canonical records
from several projects.

Projects are covered in detail in [Projects](projects.md).

## The hierarchy at a glance

```text
Organization
├── Workspace
│   ├── Project
│   └── Project
├── Workspace
│   └── Project
└── Stylebooks and shared settings
```

Workspaces group projects; they do not own a separate copy of the content.
Stylebooks belong to the organization and sit alongside the workspace
hierarchy.

## How this affects access and settings

- **People** are created in the **organization**, then given workspace access
  and, separately, editing rights for particular Stylebooks. See
  [Users & access](users.md).
- **Shared settings** like [AI models](../settings/ai-models.md) and
  [integrations](../settings/integrations.md) are defined once at the
  organization level. Projects can override supported settings where a team
  needs a different model or service.
- **Stylebooks** belong to the organization and can be shared by projects, but
  each project uses only the Stylebook chosen when that project was created.
