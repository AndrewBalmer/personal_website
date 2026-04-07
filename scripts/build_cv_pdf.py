#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "cv" / "andrew_balmer_cv.pdf"


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def inline_links(profile: dict) -> str:
    contact = profile["contact"]
    parts = [
        f"<link href='mailto:{escape(contact['professional_email'])}'>{escape(contact['professional_email'])}</link>",
        escape(contact["location"]),
        f"<link href='{escape(contact['github_url'])}'>GitHub</link>",
        f"<link href='{escape(contact['scholar_url'])}'>Scholar</link>",
        f"<link href='{escape(contact['orcid_url'])}'>ORCID</link>",
        f"<link href='{escape(contact['linkedin_url'])}'>LinkedIn</link>",
    ]
    return "  ·  ".join(parts)


def plain_text(value: str) -> str:
    return value.replace("**", "").replace("*", "")


def cv_line(body: str, year: str, styles: dict) -> Table:
    year_para = Paragraph(escape(year), styles["cv_year"])
    body_para = Paragraph(body, styles["cv_body"])
    table = Table([[year_para, body_para]], colWidths=[28 * mm, 148 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def add_section(story: list, heading: str, styles: dict) -> None:
    story.append(Spacer(1, 8))
    story.append(Paragraph(heading.upper(), styles["section"]))
    story.append(Spacer(1, 2))


def build_pdf() -> None:
    profile = load_yaml(ROOT / "_data" / "profile.yml")
    cv = load_yaml(ROOT / "_data" / "cv.yml")
    pubs = load_yaml(ROOT / "_data" / "publications.yml")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title="Andrew Balmer CV",
        author="Andrew Balmer",
    )

    base = getSampleStyleSheet()
    styles = {
        "title": ParagraphStyle(
            "title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=3,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#475569"),
            spaceAfter=10,
        ),
        "summary": ParagraphStyle(
            "summary",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#334155"),
            spaceAfter=8,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=11,
            textColor=colors.HexColor("#0f766e"),
            spaceAfter=0,
            borderPadding=0,
        ),
        "cv_year": ParagraphStyle(
            "cv_year",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=12,
            alignment=TA_RIGHT,
            textColor=colors.HexColor("#64748b"),
        ),
        "cv_body": ParagraphStyle(
            "cv_body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=13.5,
            textColor=colors.HexColor("#0f172a"),
        ),
    }

    story = [
        Paragraph("Andrew Balmer", styles["title"]),
        Paragraph(
            f"{escape(profile['current_role']['title'])} · {escape(profile['current_role']['institution'])}",
            styles["subtitle"],
        ),
        Paragraph(inline_links(profile), styles["subtitle"]),
        Paragraph(escape(profile["bios"]["jobs"]), styles["summary"]),
    ]

    add_section(story, "Positions", styles)
    for entry in cv["positions"]:
        body = (
            f"<b>{escape(entry['title'])}</b><br/>"
            f"{escape(entry['institution'])}, {escape(entry['location'])}<br/>"
            f"{escape(entry.get('note', ''))}"
        )
        story.append(cv_line(body, entry["year"], styles))

    add_section(story, "Education", styles)
    for entry in cv["education"]:
        body = (
            f"<b>{escape(entry['degree'])}</b><br/>"
            f"{escape(entry['institution'])}, {escape(entry['location'])}<br/>"
            f"{escape(entry.get('note', ''))}"
        )
        story.append(cv_line(body, entry["year"], styles))

    add_section(story, "Selected Publications", styles)
    for pub in pubs:
        journal_bits = [pub["journal"]]
        if pub.get("volume"):
            journal_bits.append(str(pub["volume"]))
        if pub.get("pages"):
            journal_bits.append(str(pub["pages"]))
        paper_link = pub.get("paper_url") or ""
        link_start = f"<link href='{escape(paper_link)}'>" if paper_link else ""
        link_end = "</link>" if paper_link else ""
        body = (
            f"{escape(plain_text(pub['authors']))}. "
            f"{link_start}<b>{escape(pub['title'])}</b>{link_end}. "
            f"<i>{escape(', '.join(journal_bits))}</i>."
        )
        story.append(cv_line(body, str(pub["year"]), styles))

    for heading, key, title_key, detail_key in [
        ("Grants & Funding", "grants", "title", "funder"),
        ("Awards & Honours", "awards", "title", "institution"),
        ("Teaching", "teaching", "title", "role"),
        ("Service", "service", "title", "venue"),
    ]:
        entries = cv.get(key, [])
        if not entries:
            continue
        add_section(story, heading, styles)
        for entry in entries:
            detail = escape(entry.get(detail_key, ""))
            if entry.get("amount"):
                amount = escape(entry["amount"])
                detail = f"{detail} · {amount}" if detail else amount
            if entry.get("role") and detail_key != "role":
                detail = f"{detail}<br/>{escape(entry['role'])}" if detail else escape(entry["role"])
            body = f"<b>{escape(entry[title_key])}</b><br/>{detail}"
            story.append(cv_line(body, entry["year"], styles))

    add_section(story, "Skills", styles)
    for group in cv["skills"]:
        body = f"<b>{escape(group['category'])}</b><br/>{escape(group['items'])}"
        story.append(cv_line(body, "", styles))

    doc.build(story)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
