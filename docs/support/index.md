# Support

**Have a question? Email [backfield@localangle.co](mailto:backfield@localangle.co).**

Start with the resource closest to your question:

- [Platform overview](../platform/index.md) explains Backfield, Agate,
  Stylebook, and the API.
- [Tutorials](../tutorials/index.md) provide verified, step-by-step workflows.
- [API reference](../api/index.md) documents endpoints, authentication, and
  response formats.

## Help with hosted Backfield

Contact your organization's Backfield administrator first for:

- account access and user roles;
- workspace or project access;
- Stylebook assignments;
- AI model and integration settings;
- project API keys.

For help evaluating Backfield, planning a deployment, or discussing a
structured-journalism project, [contact Local Angle](https://localangle.co).

When asking for help, include:

1. The organization, workspace, and project.
2. What you were trying to do.
3. The steps that led to the problem.
4. What you expected and what happened instead.
5. The approximate time of the problem.
6. A screenshot or error message with private information removed.

Do not send API keys, passwords, provider credentials, private article content,
or unnecessary personal data.

## API troubleshooting

Use the hosted [API Playground](../api/playground.md) to confirm the request
before adding it to an application. Open the Playground from Backfield so it
uses the correct organization.

Check these resources:

- [Authentication](../api/authentication.md) for key types, scopes, and
  revocation.
- [Errors](../api/conventions/errors.md) for status codes and error bodies.
- [Rate limits](../api/conventions/rate-limits.md) for `429` responses and
  `Retry-After`.
- [Get project](../api/projects/get-project.md) to confirm that a key belongs
  to the expected project.

For a failed request, record the endpoint, HTTP method, status, sanitized
response body, and the `X-Request-ID` response header or matching `request_id`
from the error body. Never include the API key.

## Report a bug or request a feature

Use the public [Backfield issue tracker](https://github.com/localangle/backfield/issues)
for non-security reports:

- [Report a bug](https://github.com/localangle/backfield/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/localangle/backfield/issues/new?template=feature_request.yml)

Search existing issues first. A useful bug report includes:

1. What you were trying to do
2. Steps to reproduce the problem
3. What you expected and what happened instead
4. Relevant versions or commit SHA
5. Sanitized logs or error details
6. How often the problem occurs

Do not post customer data or credentials in a public issue.

## Local development and contributions

The public [Backfield repository](https://github.com/localangle/backfield)
supports local development, source inspection, and external contributions. It
does not currently provide a supported production self-hosting path.

Start with the repository's
[quickstart](https://github.com/localangle/backfield#quickstart) and
[contribution guide](https://github.com/localangle/backfield/blob/main/CONTRIBUTING.md).
Local setup requires Python 3.11, Docker with Compose v2, `uv`, Node.js 20, and
Git:

```bash
git clone https://github.com/localangle/backfield.git
cd backfield
make bootstrap
source .venv/bin/activate
backfield init
```

Run `backfield doctor` to diagnose the local environment. Before opening a pull
request, run `make lint` and `make test`.

## Report a security vulnerability

Do not report vulnerabilities in a public issue. Use
[GitHub private vulnerability reporting](https://github.com/localangle/backfield/security/advisories/new).
Include the affected component, version or commit, reproduction steps, impact,
and any known mitigation.
