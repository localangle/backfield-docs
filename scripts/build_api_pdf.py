#!/usr/bin/env python3
"""Build a single PDF from the API Reference section of the docs site."""

from __future__ import annotations

import argparse
import contextlib
import socket
import subprocess
import sys
import tempfile
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from mkdocs.config import load_config
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "mkdocs.yml"
DEFAULT_SITE_DIR = ROOT / "site"
DEFAULT_OUTPUT = ROOT / "dist" / "backfield-api.pdf"
API_SECTION = "API Reference"

PRINT_CSS = """
@media print {
  .md-header,
  .md-tabs,
  .md-sidebar,
  .md-sidebar--primary,
  .md-sidebar--secondary,
  .md-footer,
  .md-top,
  .md-content__button,
  .md-search,
  [data-md-component="announce"] {
    display: none !important;
  }

  .md-main__inner {
    margin: 0 !important;
  }

  .md-content {
    max-width: none !important;
    margin: 0 !important;
  }

  .md-grid {
    max-width: none !important;
  }

  .md-typeset pre > code {
    white-space: pre-wrap !important;
    word-break: break-word !important;
  }

  a[href^="http"]::after {
    content: " (" attr(href) ")";
    font-size: 0.85em;
  }
}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help="Path to mkdocs.yml (default: %(default)s)",
    )
    parser.add_argument(
        "--site-dir",
        type=Path,
        default=DEFAULT_SITE_DIR,
        help="Built site directory (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output PDF path (default: %(default)s)",
    )
    parser.add_argument(
        "--skip-build",
        action="store_true",
        help="Skip mkdocs build and use the existing site directory",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=0,
        help="HTTP port for serving the site (default: pick a free port)",
    )
    return parser.parse_args()


def load_nav(config_path: Path) -> list:
    config = load_config(config_file=str(config_path))
    nav = config.get("nav")
    if not nav:
        raise SystemExit(f"No nav section found in {config_path}")
    return nav


def walk_api_nav(items: object, *, in_section: bool = False) -> list[str]:
    """Collect docs/api markdown paths in nav order."""
    paths: list[str] = []

    if isinstance(items, list):
        for item in items:
            paths.extend(walk_api_nav(item, in_section=in_section))
        return paths

    if isinstance(items, str):
        if in_section and items.endswith(".md"):
            paths.append(items)
        return paths

    if not isinstance(items, dict):
        return paths

    for key, value in items.items():
        if not in_section and key == API_SECTION:
            paths.extend(walk_api_nav(value, in_section=True))
        elif in_section:
            if isinstance(value, str) and value.endswith(".md"):
                paths.append(value)
            else:
                paths.extend(walk_api_nav(value, in_section=True))

    return paths


def md_path_to_site_html(md_path: str) -> Path:
    path = Path(md_path)
    if path.name == "index.md":
        return path.parent / "index.html"
    return path.with_suffix("") / "index.html"


def pick_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return


@contextlib.contextmanager
def serve_site(site_dir: Path, port: int):
    handler = lambda *args, **kwargs: QuietHandler(  # noqa: E731
        *args, directory=str(site_dir), **kwargs
    )
    server = ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{port}"
    finally:
        server.shutdown()
        thread.join(timeout=5)


def run_mkdocs_build(config_path: Path) -> None:
    mkdocs = ROOT / ".venv" / "bin" / "mkdocs"
    cmd = [str(mkdocs if mkdocs.exists() else "mkdocs"), "build", "--strict"]
    if config_path != DEFAULT_CONFIG:
        cmd.extend(["-f", str(config_path)])
    print("Building docs with mkdocs…", flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True)


def render_page_pdf(page, url: str, output_path: Path) -> None:
    page.goto(url, wait_until="networkidle")
    page.add_style_tag(content=PRINT_CSS)
    page.emulate_media(media="print")
    page.pdf(
        path=str(output_path),
        format="Letter",
        print_background=True,
        margin={"top": "0.6in", "right": "0.6in", "bottom": "0.6in", "left": "0.6in"},
    )


def merge_pdfs(parts: list[Path], output_path: Path) -> None:
    writer = PdfWriter()
    for part in parts:
        writer.append(str(part))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as handle:
        writer.write(handle)


def main() -> int:
    args = parse_args()
    site_dir = args.site_dir.resolve()

    if not args.skip_build:
        run_mkdocs_build(args.config.resolve())

    if not site_dir.is_dir():
        raise SystemExit(f"Site directory not found: {site_dir}")

    md_paths = walk_api_nav(load_nav(args.config.resolve()))
    if not md_paths:
        raise SystemExit(f"No pages found under '{API_SECTION}' in {args.config}")

    html_paths: list[Path] = []
    missing: list[Path] = []
    for md_path in md_paths:
        html_path = md_path_to_site_html(md_path)
        full_path = site_dir / html_path
        if full_path.is_file():
            html_paths.append(html_path)
        else:
            missing.append(full_path)

    if missing:
        missing_list = "\n".join(f"  - {path}" for path in missing)
        raise SystemExit(f"Missing built HTML files:\n{missing_list}")

    port = args.port or pick_free_port()
    output_path = args.output.resolve()

    print(f"Exporting {len(html_paths)} API pages to PDF…", flush=True)

    with serve_site(site_dir, port) as base_url, tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        part_paths: list[Path] = []

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": 1024, "height": 1400})

            for index, html_path in enumerate(html_paths, start=1):
                url = f"{base_url}/{html_path.as_posix()}"
                part_path = tmp / f"{index:03d}.pdf"
                print(f"  [{index}/{len(html_paths)}] {html_path.as_posix()}", flush=True)
                render_page_pdf(page, url, part_path)
                part_paths.append(part_path)

            browser.close()

        merge_pdfs(part_paths, output_path)

    print(f"Wrote {output_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
