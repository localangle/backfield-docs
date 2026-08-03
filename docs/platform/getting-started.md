# Getting Started

Backfield helps a news organization turn reporting into structured information
that can be reviewed, maintained, searched, and reused. This page introduces
the platform from the perspective of someone signing in for the first time.

You do not need to understand every part of Backfield before you begin. Most
people work in only the parts relevant to their role.

## What your newsroom uses Backfield for

A story contains more than text. It refers to people, organizations, places,
events, topics, and relationships. Backfield helps your newsroom:

- identify and organize those details consistently;
- let editors verify what automated processing found;
- connect repeated references to the same real-world person, place, or
  organization;
- build a shared body of structured editorial knowledge;
- make that data available to newsroom products and other systems.

The original reporting remains the evidence behind the structured data.
Backfield does not replace editorial judgment: automated results can be
reviewed and corrected by people.

## Before your first visit

An organization administrator normally prepares:

- your account and initial password;
- access to the workspaces where your team works;
- access to any Stylebooks you help maintain;
- the projects and processing tools needed for your role.

There is no public self-registration screen. If you cannot see an expected
workspace, project, or Stylebook, ask an organization administrator to check
your access.

If an administrator gave you an initial password, change it promptly from your
account menu and store the replacement in your password manager.

## Sign in and choose your organization

Sign in with your Backfield email and password. If your account belongs to more
than one organization, choose the one you want to work in. You can switch
organizations later from the account menu.

Everything you see after choosing an organization—people, settings,
workspaces, projects, and Stylebooks—belongs to that organization.

## Find your team's work

Backfield is organized in three levels:

- Your **organization** is usually your newsroom, publication group, or
  company.
- A **workspace** groups related work, often by publication, desk, beat, or
  initiative.
- A **project** contains the flows, processing runs, and article-level results
  for a particular body of work.

Agate opens with the workspaces you are allowed to use. Open the workspace
named by your team, then select the appropriate project. It is normal for
different people in the same organization to see different workspaces and
Stylebooks.

## Know the three parts of Backfield

The platform has three connected applications. They serve different purposes,
but they work with the same underlying information.

### Agate: process and review reporting

Use **Agate** when the question is about a particular article or processing
job:

- run or inspect a reusable processing flow;
- monitor its progress;
- review extracted people, organizations, places, and article metadata;
- correct a result that applies to one story.

Depending on your role, you may run existing flows, review completed work, or
design the flows your newsroom uses.

### Stylebook: maintain shared knowledge

Use **Stylebook** when the question is about shared reference knowledge:

- decide whether an extracted item matches an existing canonical record;
- create or merge canonical people, organizations, and locations;
- maintain newsroom-wide metadata, geography, and connections;
- review possible duplicates or other catalog-quality issues.

For example, each article mentioning a mayor contains its own evidence, while
the mayor can have one shared Stylebook record used across many articles.

### Backfield API: use the data in other systems

Use **Backfield API** when a product, service, tool, or analysis needs to use
the structured data:

- retrieve articles and their extracted details;
- search by keyword, meaning, entity, metadata, or geography;
- follow mentions and connections across reporting;
- trigger approved flows from trusted automation.

The API is primarily used by developers, data teams, and newsroom applications.
You do not need to use it to review articles or maintain Stylebook records.

## Make changes in the right place

Before editing, ask whether the change belongs to one story or to the shared
record:

- Fix a wrong extraction, quote attribution, article tag, or story-specific
  place in the Agate processed item.
- Fix a canonical name, alias, maintained geography, metadata value, or
  relationship in Stylebook.

The [Data model](concepts/content-model.md) explains this distinction in more
detail.

## A good first tour

If you are exploring rather than completing an assigned task:

1. Open the workspace and project your team uses.
2. Look at the project's **Flows** to see what information your newsroom
   extracts or adds.
3. Open a completed **Run**, then select a processed item to see the source
   article beside its structured results.
4. Open **Stylebook** and inspect a familiar person, organization, or location.
   Notice how mentions from individual articles support one shared record.
5. Ask your team which actions are part of your role before changing a flow,
   canonical record, model, or integration.

## Learn more

- Follow a sample story through the platform in the
  [Simple Example](simple-example.md).
- Understand access and navigation in
  [Organizations & workspaces](concepts/organizations.md).
- Learn what a [Project](concepts/projects.md) contains.
- Learn how article processing works in [Agate](agate/index.md), or how shared
  records are curated in [Stylebook](stylebook/index.md).
- Explore project data through the [Backfield API](../api/index.md).
