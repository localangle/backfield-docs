# Stylebooks & the library

An organization can keep more than one **Stylebook** — each a separate catalog of people, places, and organizations. This is useful when different desks or projects need parallel reference sets that shouldn't mix.

A few ground rules keep this predictable:

- Every organization always has **at least one** Stylebook, with **exactly one** marked as the **default**.
- Each project is assigned exactly one Stylebook from its organization. New
  projects use the selected Stylebook (the organization or workspace default
  when no other choice is made), and every flow in that project uses that
  assignment. Individual flow steps cannot select a different Stylebook.
- Stylebooks have readable names and stable URL slugs for navigation.

## Why use more than one?

Sharing one Stylebook lets projects reuse the same identities and aliases. That
is useful when several desks cover the same people and institutions.

Separate Stylebooks are appropriate when two catalogs intentionally should not
share identity—for example, different publications, clients, or datasets with
independent editorial standards. Creating a second Stylebook is not merely a
visual folder; it creates a separate canonical namespace.

## Project assignment

When a project is created, Backfield offers the Stylebooks in its organization.
If no other selection is made, the workspace or organization default is used.
The chosen Stylebook is then authoritative for every flow and entity operation
in that project and appears read-only in project settings.

This fixed assignment prevents different runs in one project from sending
people and places into unrelated catalogs. Choose deliberately when creating a
project.

## The default Stylebook

The organization must always have at least one Stylebook and exactly one
default. Changing the default affects future project creation; it does not
silently move existing projects.

## Managing the library

Organization administrators manage the library in Agate. They can:

- create and rename Stylebooks;
- choose the organization default;
- export a Stylebook bundle or import one as a new Stylebook;
- review the impact before deleting a Stylebook.

Deletion is guarded because projects, editor assignments, and canonical data
may depend on the Stylebook. The interface shows an impact preview and may
require a replacement. The last Stylebook in an organization cannot be
deleted.

## Who may edit

Organization administrators can edit every Stylebook. Other members receive
editing access per Stylebook. Project/workspace access and Stylebook editing
access are separate: someone may need to review project runs without being
allowed to change newsroom-wide canonical records.
