# Quickstart

Follow one sample article through all three Backfield applications. You will
process and review it in Agate, inspect its canonical records in Stylebook, and
retrieve the saved result through Backfield API.

!!! note "Tutorial outline"
    This page defines the planned walkthrough. Detailed instructions,
    screenshots, and sample files will be added in a later pass.

## What you'll learn

- How a project, flow, run, and processed item relate.
- Why Backfield Output is required to save data into the platform.
- Where to correct article evidence and where to edit canonical knowledge.
- How a project API key exposes the saved result to another application.

## Before you begin

- A Backfield account with access to a project.
- At least one approved generative model and embedding model.
- Geocoding credentials if the sample flow will resolve locations.
- Permission to run flows and edit the project's Stylebook.

## Planned walkthrough

1. Open an existing project or create a project for the walkthrough.
2. Build a flow with Text Input, article metadata, people, organization and
   place extraction, Geocode, and Backfield Output.
3. Run the flow on the sample article and monitor its processed item.
4. Review evidence, correct one article-level result, and compare original with
   reviewed output.
5. Open a linked canonical record in Stylebook and inspect its mentions,
   metadata, geography, and connections.
6. Resolve any candidate created by the run.
7. Create a personal project API key and retrieve the saved article in the API
   Playground.
8. Revoke the temporary key when the walkthrough is complete.

## Where to go next

- [Build a first flow](agate/build-flow.md)
- [Correct processed items](agate/review-processed-items.md)
- [Review candidate queues](stylebook/review-candidates.md)
- [Use the API Playground](api/playground.md)
