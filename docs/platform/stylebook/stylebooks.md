# Managing Stylebooks

An organization can have more than one **Stylebook**. Each is a separate
catalog of people, organizations, and locations.

## Share or separate?

Projects should share a Stylebook when they cover the same people, institutions,
and places. This lets them reuse identities, aliases, metadata, and
connections.

Use separate Stylebooks only when the records should remain independent—for
example, for publications or datasets with different editorial standards. A
second Stylebook is not a folder or filtered view. It creates a separate set of
canonical records.

## Assigning a Stylebook to a project

Each project uses one Stylebook. The choice is made when the project is created
and applies to every flow and article in that project. Individual flows cannot
choose a different Stylebook.

Every organization has at least one Stylebook and exactly one organization
default. A workspace can supply the initial choice when a project is created,
and the person creating the project can choose another Stylebook in the same
organization. Changing a default does not move existing projects.

## Create, rename, copy, or remove a Stylebook

Organization administrators manage Stylebooks in Agate. They can:

- create and rename Stylebooks;
- choose the organization default;
- export a Stylebook bundle or import one as a new Stylebook;
- review the impact before deleting a Stylebook.

!!! warning "Deleting a Stylebook cannot be undone"
    Deletion removes its canonical records and editorial context. Projects and
    workspaces that used it are reassigned to the organization default, or to a
    replacement chosen when deleting the default Stylebook. Existing article
    entities may need to be matched again.

    Review the impact screen, export anything you need to retain, and update
    dependencies before continuing. The last Stylebook in an organization
    cannot be deleted.

For the complete administration workflow, see
[Create and manage Stylebooks](../../tutorials/agate/manage-stylebooks.md).

## Who may edit

Organization administrators can edit every Stylebook. Other members receive
editing access per Stylebook. Project/workspace access and Stylebook editing
access are separate: someone may need to review project runs without being
allowed to change newsroom-wide canonical records.
