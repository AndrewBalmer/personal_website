#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import textwrap

import yaml
from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "images" / "social-card.png"
PHOTO = ROOT / "ab69.jpg"


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def pick_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def fit_text(draw: ImageDraw.ImageDraw, text: str, width: int, start_size: int, bold: bool = False):
    size = start_size
    while size > 20:
        font = pick_font(size, bold=bold)
        bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=8)
        if bbox[2] - bbox[0] <= width:
            return font
        size -= 2
    return pick_font(20, bold=bold)


def build_card():
    config = load_yaml(ROOT / "_config.yml")
    profile = load_yaml(ROOT / "_data" / "profile.yml")

    width, height = 1200, 630
    image = Image.new("RGB", (width, height), "#0f172a")
    draw = ImageDraw.Draw(image)

    for offset, color in [(0, "#0f172a"), (160, "#12263f"), (420, "#0f766e")]:
        draw.ellipse((width - 520 + offset, -120 + offset // 8, width + 120 + offset, 440 + offset), fill=color)
    image = image.filter(ImageFilter.GaussianBlur(radius=14))
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle((48, 48, width - 48, height - 48), radius=32, outline="#334155", width=2)
    draw.rounded_rectangle((48, 48, width - 48, height - 48), radius=32, fill=(15, 23, 42, 160))

    photo = Image.open(PHOTO).convert("RGB").resize((280, 280))
    mask = Image.new("L", photo.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, photo.size[0], photo.size[1]), fill=255)
    photo = Image.composite(photo, Image.new("RGB", photo.size, "#0f172a"), mask)
    image.paste(photo, (860, 172), mask)
    draw.ellipse((858, 170, 1142, 454), outline="#e2e8f0", width=5)

    accent_font = pick_font(26, bold=False)
    title_font = fit_text(draw, "Andrew Balmer", 620, 62, bold=True)
    wrapped_headline = textwrap.fill(profile["headline"], width=52)
    subtitle_font = fit_text(draw, wrapped_headline, 560, 24, bold=False)
    body_font = pick_font(22)
    stat_value_font = pick_font(18, bold=True)
    stat_label_font = pick_font(14, bold=False)

    draw.text((80, 88), "Computational Biology · Pathogen Genomics · Scientific Software", font=accent_font, fill="#5eead4")
    draw.multiline_text((80, 140), "Andrew\nBalmer", font=title_font, fill="#f8fafc", spacing=2)
    draw.multiline_text((80, 290), wrapped_headline, font=subtitle_font, fill="#cbd5e1", spacing=8)

    role_text = f"{profile['current_role']['title']} · {profile['current_role']['institution']}"
    draw.text((80, 414), role_text, font=body_font, fill="#e2e8f0")
    draw.text((80, 450), profile["contact"]["location"], font=body_font, fill="#94a3b8")

    x = 80
    y = 504
    box_width = 212
    box_height = 62
    for item in profile["proof_points"][:3]:
        draw.rounded_rectangle((x, y, x + box_width, y + box_height), radius=18, fill="#eff6ff")
        draw.text((x + 14, y + 12), item["value"], font=stat_value_font, fill="#0f172a")
        draw.text((x + 14, y + 35), item["label"], font=stat_label_font, fill="#475569")
        x += box_width + 14

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    build_card()
