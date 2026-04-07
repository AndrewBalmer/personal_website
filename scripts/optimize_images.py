#!/usr/bin/env python3

from __future__ import annotations

import argparse
import io
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "assets" / "images"
SIGNIFICANT_SAVINGS_BYTES = 25_000
SIGNIFICANT_SAVINGS_RATIO = 0.08


def optimized_bytes(path: Path) -> bytes | None:
    suffix = path.suffix.lower()
    if suffix not in {".jpg", ".jpeg", ".png"}:
        return None

    image = Image.open(path)
    buffer = io.BytesIO()
    if suffix in {".jpg", ".jpeg"}:
        image.convert("RGB").save(buffer, format="JPEG", optimize=True, progressive=True, quality=82)
    else:
        image.save(buffer, format="PNG", optimize=True)
    return buffer.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if any image can be reduced materially.")
    parser.add_argument("target", nargs="?", default=str(DEFAULT_DIR))
    args = parser.parse_args()

    target = Path(args.target)
    candidates = sorted([path for path in target.rglob("*") if path.is_file()])
    findings = []

    for path in candidates:
        new_bytes = optimized_bytes(path)
        if new_bytes is None:
            continue
        current_size = path.stat().st_size
        saved = current_size - len(new_bytes)
        ratio = saved / current_size if current_size else 0
        if saved > 0 and (saved >= SIGNIFICANT_SAVINGS_BYTES or ratio >= SIGNIFICANT_SAVINGS_RATIO):
            findings.append((path, saved, ratio, new_bytes))

    if args.check:
        if findings:
            for path, saved, ratio, _ in findings:
                print(f"Needs optimization: {path.relative_to(ROOT)} saves {saved} bytes ({ratio:.1%})")
            return 1
        print("Images are within optimization thresholds.")
        return 0

    for path, saved, ratio, new_bytes in findings:
        path.write_bytes(new_bytes)
        print(f"Optimized {path.relative_to(ROOT)} by {saved} bytes ({ratio:.1%})")

    if not findings:
        print("No image changes were necessary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
