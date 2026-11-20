#!/usr/bin/env python3
"""Render the 480x800 BootLogo guide with the bundled Noto Sans JP font."""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT_PATH = ROOT / 'fonts/NotoSansJP-Bold.ttf'
CONTROLS = [
    ('CROP', 'G + L2', 68, 516),
    ('BRIGHTNESS', 'G + L1/R1', 228, 516),
    ('GAP', 'G + R2', 68, 588),
    ('FAST-FORWARD', 'L3', 228, 588),
    ('x2/HI-RES', 'G+STA', 68, 660),
    ('LID    MIC', 'L2  R2', 228, 660),
    ('SWAP', 'G+SEL', 68, 732),
    ('SCREENSHOT', 'G+A', 228, 732),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='Output PNG or BMP path; BMP is saved as 24-bit RGB')
    args = parser.parse_args()
    image = Image.new('RGB', (480, 800), (38, 38, 38))
    draw = ImageDraw.Draw(image)
    fonts = {size: ImageFont.truetype(str(FONT_PATH), size) for size in (16, 24, 36)}

    def label(text, x, y, size, color):
        draw.text((x + 2, y + 2), text, font=fonts[size], fill=(0, 0, 0))
        draw.text((x, y), text, font=fonts[size], fill=color)

    label('DS ZERO40 JP+', 6, 6, 24, (187, 187, 187))
    label('NINTENDO DS', 6, 42, 36, (255, 255, 255))
    for title, shortcut, x, y in CONTROLS:
        label(title, x, y, 16, (187, 187, 187))
        label(shortcut, x, y + 20, 24, (255, 255, 255))
    label('G+↑Y G+↓B', 68, 566, 16, (255, 255, 255))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output)
    print(args.output)


if __name__ == '__main__':
    main()
