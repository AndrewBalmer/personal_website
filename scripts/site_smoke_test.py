#!/usr/bin/env python3

from __future__ import annotations

import sys

import requests


CHECKS = [
    ("/", "Research Snapshots"),
    ("/about/", "Short bio"),
    ("/research/", "Research Gallery"),
    ("/publications/", "listed publications"),
    ("/projects/", "Project Briefs"),
    ("/cv/", "Download CV"),
    ("/speaking/", "Talks &amp; Presentations"),
    ("/now/", "Currently working on"),
]


def main(base_url: str) -> int:
    session = requests.Session()
    session.headers.update({"User-Agent": "andrew-balmer-site-smoke-test/1.0"})

    failures = []
    for path, needle in CHECKS:
        url = f"{base_url.rstrip('/')}{path}"
        try:
            response = session.get(url, timeout=20)
        except requests.RequestException as exc:
            failures.append(f"{url} failed: {exc}")
            continue
        if response.status_code != 200:
            failures.append(f"{url} returned HTTP {response.status_code}")
            continue
        if needle not in response.text:
            failures.append(f"{url} missing expected text: {needle}")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    print("Smoke test passed.")
    return 0


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:4000/personal_website"
    raise SystemExit(main(base))
