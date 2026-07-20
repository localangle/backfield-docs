"""API-only MkDocs hook: make `/` land on the API overview."""

from __future__ import annotations

from pathlib import Path

REDIRECT_HTML = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="refresh" content="0; url=api/" />
    <link rel="canonical" href="api/" />
    <title>Redirecting…</title>
  </head>
  <body>
    <p>Redirecting to <a href="api/">API Reference</a>…</p>
  </body>
</html>
"""


def on_post_build(config, **kwargs) -> None:
    site_dir = Path(config["site_dir"])
    (site_dir / "index.html").write_text(REDIRECT_HTML, encoding="utf-8")
