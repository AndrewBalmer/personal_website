#!/usr/bin/env python3

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]
SOFT_FAIL_DOMAINS = {
    "doi.org",
    "dx.doi.org",
    "linkedin.com",
    "www.linkedin.com",
    "scholar.google.com",
    "onlinelibrary.wiley.com",
    "nsojournals.onlinelibrary.wiley.com",
}
HEADERS = {"User-Agent": "andrew-balmer-site-link-checker/1.0"}
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8")) or {}
BASEURL = (CONFIG.get("baseurl") or "").rstrip("/")


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            value = attrs.get("href")
            if value:
                self.hrefs.append(value)
        elif tag in {"img", "script"}:
            value = attrs.get("src")
            if value:
                self.hrefs.append(value)
        elif tag == "link":
            rel = attrs.get("rel", "")
            if rel in {"stylesheet", "icon"}:
                value = attrs.get("href")
                if value:
                    self.hrefs.append(value)
        element_id = attrs.get("id")
        if element_id:
            self.ids.add(element_id)


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def print(self) -> None:
        for warning in self.warnings:
            print(f"WARNING: {warning}")
        for error in self.errors:
            print(f"ERROR: {error}")


def parse_html(path: Path):
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.hrefs, parser.ids


def html_files(site_dir: Path) -> Iterable[Path]:
    return sorted(site_dir.rglob("*.html"))


def anchor_map(site_dir: Path) -> dict[Path, set[str]]:
    anchors = {}
    for path in html_files(site_dir):
        _, ids = parse_html(path)
        anchors[path.resolve()] = ids
    return anchors


def resolve_internal(site_dir: Path, current: Path, href: str) -> tuple[Path | None, str | None]:
    fragment = None
    path_part = href
    if "#" in path_part:
        path_part, fragment = path_part.split("#", 1)
    if "?" in path_part:
        path_part = path_part.split("?", 1)[0]

    if not path_part:
        return current.resolve(), fragment

    if BASEURL and path_part == BASEURL:
        path_part = "/"
    elif BASEURL and path_part.startswith(f"{BASEURL}/"):
        path_part = path_part[len(BASEURL) :]

    if path_part.startswith("/"):
        target = site_dir / path_part.lstrip("/")
    else:
        target = (current.parent / path_part).resolve()
        try:
            target = target.relative_to(site_dir.resolve())
            target = site_dir / target
        except ValueError:
            pass

    if target.is_dir():
        target = target / "index.html"
    elif target.suffix == "":
        if (target / "index.html").exists():
            target = target / "index.html"
        elif target.with_suffix(".html").exists():
            target = target.with_suffix(".html")

    return target.resolve(), fragment


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def external_urls() -> set[str]:
    urls = set()

    def capture(value):
        if isinstance(value, dict):
            for nested in value.values():
                capture(nested)
        elif isinstance(value, list):
            for nested in value:
                capture(nested)
        elif isinstance(value, str) and value.startswith(("http://", "https://")):
            urls.add(value)

    for rel_path in [
        "_data/profile.yml",
        "_data/projects.yml",
        "_data/publications.yml",
        "_data/research_highlights.yml",
        "_data/talks.yml",
    ]:
        capture(load_yaml(ROOT / rel_path))
    return urls


def should_soft_fail(url: str) -> bool:
    hostname = (urlparse(url).hostname or "").lower()
    return hostname in SOFT_FAIL_DOMAINS


def check_external(url: str, report: Report) -> None:
    try:
        response = requests.get(url, headers=HEADERS, timeout=20, allow_redirects=True)
        if response.status_code >= 400:
            message = f"{url} returned HTTP {response.status_code}"
            if should_soft_fail(url):
                report.warnings.append(message)
            else:
                report.errors.append(message)
    except requests.RequestException as exc:
        message = f"{url} failed: {exc}"
        if should_soft_fail(url):
            report.warnings.append(message)
        else:
            report.errors.append(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", default=str(ROOT / "_site"))
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    report = Report()
    anchors = anchor_map(site_dir)

    external = set()
    for html_path in html_files(site_dir):
        hrefs, _ = parse_html(html_path)
        for href in hrefs:
            if href.startswith(("mailto:", "tel:", "javascript:")):
                continue
            if href.startswith(("http://", "https://")):
                external.add(href)
                continue

            target, fragment = resolve_internal(site_dir, html_path, href)
            if target is None or not target.exists():
                report.errors.append(f"{html_path.relative_to(site_dir)} -> {href} does not resolve to a file")
                continue
            if fragment and target.suffix == ".html" and fragment not in anchors.get(target, set()):
                report.errors.append(f"{html_path.relative_to(site_dir)} -> {href} is missing anchor #{fragment}")

    external.update(external_urls())
    for url in sorted(external):
        check_external(url, report)

    report.print()
    if report.errors:
        return 1
    print("Link checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
