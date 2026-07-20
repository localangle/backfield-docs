# Support

Use the channel that matches your question. Backfield's public repository supports local development, source inspection, and external contributions. Production self-hosting from that checkout is not currently supported.

## API questions

Start with these resources:

- [API overview](../api/index.md) — base URLs, project scoping, OpenAPI, and available resources
- [Authentication](../api/authentication.md) — creating and protecting project API keys
- [API Playground](../api/playground.md) — inspect the public contract and try requests interactively
- [Errors](../api/conventions/errors.md) — error envelopes, status codes, and request IDs
- [FAQ](faq.md) — common setup and usage questions

The hosted API Playground is available at [playground.backfield.news](https://playground.backfield.news).

## Bugs and feature requests

Use the public [Backfield issue tracker](https://github.com/localangle/backfield/issues) for non-security defects:

- [Report a bug](https://github.com/localangle/backfield/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/localangle/backfield/issues/new?template=feature_request.yml)

Search existing issues first. For a bug, include:

1. What you were trying to do
2. Steps to reproduce the problem
3. What you expected and what happened instead
4. Relevant versions or commit SHA
5. Error status and response body, with secrets removed
6. The `X-Request-ID` response header or matching `request_id` from the API error body

Never include API keys, credentials, private article content, or unnecessary personal data in a public issue.

## Local development

The public [Backfield repository](https://github.com/localangle/backfield) includes the application source and local development tooling. Start with its [README](https://github.com/localangle/backfield#quickstart) and [contribution guide](https://github.com/localangle/backfield/blob/main/CONTRIBUTING.md).

Local setup requires Python 3.11, Docker with Compose v2, `uv`, Node.js 20, and Git. The standard bootstrap is:

```bash
git clone https://github.com/localangle/backfield.git
cd backfield
make bootstrap
source .venv/bin/activate
backfield init
```

After setup, run `backfield doctor` when diagnosing the local environment. Before submitting a contribution, run `make lint` and `make test`.

## Security reports

Do **not** report vulnerabilities in a public issue. Use [GitHub private vulnerability reporting](https://github.com/localangle/backfield/security/advisories/new). Include the affected component, version or commit, reproduction steps, impact, and any known mitigation.

If private reporting is unavailable, email [opensource@localangle.co](mailto:opensource@localangle.co) with the subject `Security report: Backfield`.

## Deployment and other help

The public repository does not currently include a supported production self-hosting path. For help evaluating Backfield, production deployment, or structured-journalism use cases, [contact Local Angle](https://localangle.co).
