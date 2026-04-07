#!/usr/bin/env python3

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DOCX = ROOT / "Andrew Jonathan Balmer (2025) - CV - Sbioinformatician.docx"
TARGET_DOCX = ROOT / "assets" / "cv" / "andrew_balmer_cv.docx"
TARGET_PDF = ROOT / "assets" / "cv" / "andrew_balmer_cv.pdf"


def export_with_word(source: Path, target_pdf: Path) -> None:
    applescript = f"""
tell application "Microsoft Word"
  activate
  open POSIX file "{source}"
  delay 2
  save as active document file name "{target_pdf}" file format format PDF
  close active document saving no
end tell
"""
    subprocess.run(["osascript"], input=applescript, text=True, check=True)


def main() -> None:
    if not SOURCE_DOCX.exists():
        raise SystemExit(f"Missing source CV document: {SOURCE_DOCX}")

    TARGET_DOCX.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE_DOCX, TARGET_DOCX)
    export_with_word(SOURCE_DOCX, TARGET_PDF)
    print(f"Wrote {TARGET_DOCX}")
    print(f"Wrote {TARGET_PDF}")


if __name__ == "__main__":
    main()
