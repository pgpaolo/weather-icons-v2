#!/usr/bin/env python3
"""Normalize all v3.5 PNG assets for the v3.6 110x110 canvas.

Regular icons: visible content enlarged by two pixels in its longest dimension.
Small-format icons: visible content normalized to the collection's median
visual footprint, then enlarged by two pixels. Preserve filenames, RGBA,
aspect ratios and existing artwork. Never crop the content.
"""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
import subprocess
from statistics import median
from zipfile import ZipFile, ZIP_DEFLATED

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / "icons"
CANVAS = 110
MIN_BORDER = 1
ENLARGE_PX = 2
EXPECTED_ICONS = 147
BUNDLE = ROOT / "dist" / "source-icons.zip"
MAPPING = ROOT / "mappings" / "aeris-icon-list.json"


def visible_bbox(img: Image.Image) -> tuple[int, int, int, int]:
    # Ignore essentially transparent rounding noise, but retain soft edges.
    alpha = img.getchannel("A").point(lambda x: 255 if x > 2 else 0)
    box = alpha.getbbox()
    if box is None:
        raise ValueError("Image is fully transparent")
    return box


def convert(img: Image.Image, median_footprint: int) -> tuple[Image.Image, str]:
    img = img.convert("RGBA")
    width, height = img.size
    left, top, right, bottom = visible_bbox(img)
    bbox_w, bbox_h = right - left, bottom - top
    longest = max(bbox_w, bbox_h)

    if width < CANVAS or height < CANVAS:
        # A 20x20 icon must not remain a tiny spot in a 110x110 canvas.
        desired_long = median_footprint + ENLARGE_PX
        mode = "small normalized"
    else:
        # Preserve the normal v3.5 relative footprint; add two pixels.
        desired_long = round(longest * min(CANVAS / width, CANVAS / height)) + ENLARGE_PX
        mode = "standard enlarged"

    max_long = CANVAS - 2 * MIN_BORDER
    desired_long = max(1, min(desired_long, max_long))
    scale = desired_long / longest
    new_w = max(1, min(max_long, round(bbox_w * scale)))
    new_h = max(1, min(max_long, round(bbox_h * scale)))

    # Preserve nearly invisible edge glow with one-pixel safety padding,
    # without letting it reduce the visible desired footprint.
    p = 1
    crop_box = (max(0, left - p), max(0, top - p),
                min(width, right + p), min(height, bottom + p))
    subject = img.crop(crop_box)
    scaled_w = max(1, round(subject.width * scale))
    scaled_h = max(1, round(subject.height * scale))
    fit = min(1, max_long / max(scaled_w, scaled_h))
    scaled_w, scaled_h = max(1, round(scaled_w * fit)), max(1, round(scaled_h * fit))
    if scaled_w > max_long or scaled_h > max_long:
        scaled_w = min(scaled_w, max_long)
        scaled_h = min(scaled_h, max_long)
    subject = subject.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)

    out = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    out.alpha_composite(subject, ((CANVAS - scaled_w) // 2, (CANVAS - scaled_h) // 2))
    if out.getchannel("A").getbbox() is None:
        raise ValueError("Transparency error during resizing")
    return out, mode


def main() -> None:
    files = sorted(ICONS.glob("*.png"), key=lambda x: x.name.lower())
    if len(files) != EXPECTED_ICONS:
        raise SystemExit(f"Expected {EXPECTED_ICONS} icons, found {len(files)}")

    # Always regenerate from the original v3.5 sources, not previously
    # enlarged v3.6 assets: rerunning this workflow is therefore idempotent.
    base_commit = "d15b43e7c7c0a7aeda22c469ee583df0d8a83517"
    subprocess.run(
        ["git", "fetch", "--no-tags", "--depth=1", "origin", "v3.5"],
        cwd=ROOT, check=True,
    )
    fetched = subprocess.check_output(
        ["git", "rev-parse", "FETCH_HEAD"], cwd=ROOT, text=True
    ).strip()
    if fetched != base_commit:
        raise SystemExit("v3.5 source changed; inspect it before rebuilding v3.6")

    originals = {}
    reference_footprints = []
    for path in files:
        raw = subprocess.check_output(
            ["git", "show", f"FETCH_HEAD:icons/{path.name}"], cwd=ROOT
        )
        with Image.open(BytesIO(raw)) as source:
            img = source.convert("RGBA")
        originals[path] = img
        if img.size == (CANVAS, CANVAS):
            a, b, c, d = visible_bbox(img)
            reference_footprints.append(max(c - a, d - b))

    if not reference_footprints:
        raise SystemExit("Missing reference-size icons")
    target = min(CANVAS - 2 * MIN_BORDER - ENLARGE_PX,
                 max(1, round(median(reference_footprints))))
    normalized = 0
    for path, img in originals.items():
        rendered, mode = convert(img, target)
        rendered.save(path, "PNG", optimize=True)
        with Image.open(path) as verify:
            if verify.size != (CANVAS, CANVAS) or verify.mode != "RGBA":
                raise RuntimeError(f"Invalid generated file: {path.name}")
        if mode == "small normalized":
            normalized += 1
        print(f"{path.name}: {img.width}x{img.height} -> 110x110 [{mode}]")

    BUNDLE.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(BUNDLE, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        archive.write(MAPPING, "weather-icons/aeris-icon-list.json")
        for path in files:
            archive.write(path, f"weather-icons/{path.name}")
    print(f"OK: {len(files)} PNG RGBA 110x110, {normalized} originally small files, bundle rebuilt")


if __name__ == "__main__":
    main()
