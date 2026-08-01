# Changelog

Highlights from recent changes merged into Backfield.

| Date | Changes |
| --- | --- |
| **July 31, 2026** | <ul><li>Added explicit organization sessions, organization-scoped routes, and trusted organization provisioning.</li><li>Made each project's Stylebook assignment authoritative, with a Stylebook choice during project creation.</li><li>Added a combined Stylebook candidate inbox across accessible projects.</li><li>Restricted project API keys to public endpoints and current user access.</li><li>Scoped S3 ingestion-ledger records by project.</li></ul> |
| **July 30, 2026** | <ul><li>Upgraded LiteLLM and refreshed curated model options.</li><li>Kept the Stylebook navigation current after catalog changes.</li></ul> |
| **July 29, 2026** | <ul><li>Added an S3 Input idempotency ledger so unchanged files are not processed again.</li><li>Added clearer already-processed states and a deliberate reprocess option.</li><li>Improved place-and-street co-mention handling.</li></ul> |
| **July 28, 2026** | <ul><li>Added CloudWatch application metrics for Backfield Cloud.</li></ul> |
| **July 26, 2026** | <ul><li>Improved multi-workspace behavior.</li><li>Improved geocoding recall and precision across place types.</li></ul> |
| **July 22, 2026** | <ul><li>Decoupled canonical location matching from geocode quality.</li><li>Improved API Playground execution controls.</li></ul> |
| **July 21, 2026** | <ul><li>Improved Stylebook Review status and table behavior.</li><li>Added friendly 404 pages across Backfield applications.</li><li>Improved geocoding for venues, countries, and named places.</li></ul> |
| **July 20, 2026** | <ul><li>Made large-run finalization and cancellation safer.</li><li>Fixed cleanup AI review credential resolution.</li><li>Required authentication before opening the API Playground.</li></ul> |
| **July 19, 2026** | <ul><li>Added the signed-in API Playground with endpoint navigation, parameter helpers, generated requests, and geographic selectors.</li><li>Fixed Playground staging-host and session routing.</li><li>Improved concurrent idempotency handling.</li></ul> |
| **July 17, 2026** | <ul><li>Hardened canonical identity and geocode persistence.</li><li>Refreshed repository and product documentation.</li></ul> |
| **July 16, 2026** | <ul><li>Derived sibling Agate and Stylebook hosts at runtime for more flexible deployments.</li></ul> |
| **July 15, 2026** | <ul><li>Improved the open-source setup experience and readiness checks.</li><li>Synchronized Agate node UI before build type-checking.</li></ul> |
| **July 14, 2026** | <ul><li>Published the first versioned artifact, <code>v0.0.1</code>.</li><li>Added immutable, retry-safe artifact publishing and container-image security scanning.</li><li>Reduced the size of production runtime packages.</li></ul> |
| **July 12, 2026** | <ul><li>Expanded canonical cleanup and Stylebook copy handling.</li><li>Allowed Stylebook S3 access through an IAM task role.</li><li>Allowed Geocode model steps to use configured catalog models.</li></ul> |
| **July 2, 2026** | <ul><li>Reduced batch-run latency and improved extraction performance.</li><li>Synchronized Organization Extract behavior with Agate UI defaults.</li></ul> |
| **July 1, 2026** | <ul><li>Prepared deployment with project-local commands, initialization fixes, and licensing.</li></ul> |
