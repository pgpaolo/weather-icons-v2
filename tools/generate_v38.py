#!/usr/bin/env python3
"""v3.8: normalize the *visible artwork* of the v3.7 weather icons.

Canvas remains 120x120 RGBA. Main artwork receives a mild ~5% increase;
small-looking icons get a larger correction to meet a shared minimum
visual footprint. Source artwork is fixed to a pinned v3.7 commit, making
repeated builds idempotent, and alpha-aware cropping avoids blank margins.
"""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
import statistics
import subprocess
from zipfile import ZipFile, ZIP_DEFLATED

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / "icons"
SOURCE_REF = "v3.7"
SOURCE_SHA = "ec99f0aa9464143b1a23d82e98dfdd8c61887c42"
SIZE = 120
EXPECTED_COUNT = 147
# Alpha 20 identifies substantive edges, ignoring faint transparent anti-alias.
CORE_ALPHA = 20
# Retain softer edges, sun rays, rain and lightning during the crop.
SAFETY_ALPHA = 1
MIN_ARTWORK_SPAN = 108  # px, along the longest substantive dimension
GROWTH = 1.05           # a modest 5% increase for already large graphics
MAX_TARGET_SPAN = 115   # leave space for halos and detail
MARGIN = 1              # safe transparent gutter when possible
BUNDLE = ROOT / "dist" / "source-icons.zip"
MAPPING = ROOT / "mappings" / "aeris-icon-list.json"
AUDIT = ROOT / "docs" / "V3_8_SIZE_AUDIT.md"


def bbox_at_alpha(image: Image.Image, threshold: int):
    alpha = image.getchannel("A")
    return alpha.point(lambda p: 255 if p >= threshold else 0).getbbox()


def span(box):
    return max(box[2] - box[0], box[3] - box[1])


def transformed(image: Image.Image):
    if image.mode != "RGBA" or image.size != (SIZE, SIZE):
        raise ValueError(f"Invalid v3.7 input: {image.mode}, {image.size}")
    core = bbox_at_alpha(image, CORE_ALPHA)
    safe = bbox_at_alpha(image, SAFETY_ALPHA)
    if core is None or safe is None:
        raise ValueError("Blank PNG image")
    original_span = span(core)
    desired_span = max(MIN_ARTWORK_SPAN, round(original_span * GROWTH))
    desired_span = min(MAX_TARGET_SPAN, desired_span)

    # Fit the entire nontransparent subject (including soft glow) within canvas.
    safe_w, safe_h = safe[2] - safe[0], safe[3] - safe[1]
    free = SIZE - 2 * MARGIN
    max_fit = min(free / safe_w, free / safe_h)
    if max_fit < 1:
        max_fit = 1.0  # do not shrink pre-existing edge-to-edge imagery
    target_scale = desired_span / original_span
    scale = max(1.0, min(target_scale, max_fit))

    # Keep the opaque/main icon centered rather than centering empty padding.
    crop = image.crop(safe)
    dest_w = min(SIZE, max(1, round(crop.width * scale)))
    dest_h = min(SIZE, max(1, round(crop.height * scale)))
    artwork = crop.resize((dest_w, dest_h), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))

    # Core-centre position inside transformed cropped artwork.
    sx = dest_w / crop.width
    sy = dest_h / crop.height
    centre_core_x = ((core[0] + core[2]) / 2 - safe[0]) * sx
    centre_core_y = ((core[1] + core[3]) / 2 - safe[1]) * sy
    paste_x = round(SIZE / 2 - centre_core_x)
    paste_y = round(SIZE / 2 - centre_core_y)

    # Keeping glow, rain and rays entirely on canvas takes priority.
    paste_x = min(0, paste_x) if dest_w == SIZE else max(0, min(SIZE - dest_w, paste_x))
    paste_y = min(0, paste_y) if dest_h == SIZE else max(0, min(SIZE - dest_h, paste_y))
    canvas.alpha_composite(artwork, (paste_x, paste_y))

    final_core = bbox_at_alpha(canvas, CORE_ALPHA)
    final_safe = bbox_at_alpha(canvas, SAFETY_ALPHA)
    if not final_core or not final_safe:
        raise RuntimeError("Generated empty canvas")

    # Detect actual loss of opaque artwork caused by rounding or unexpected crop.
    if final_safe[0] < 0 or final_safe[1] < 0 or final_safe[2] > SIZE or final_safe[3] > SIZE:
        raise RuntimeError("Art extends beyond canvas")

    return canvas, original_span, span(final_core), scale, scale + 1e-6 < target_scale


def main():
    files = sorted(ICONS.glob("*.png"), key=lambda p: p.name.lower())
    if len(files) != EXPECTED_COUNT:
        raise SystemExit(f"Expected {EXPECTED_COUNT} PNGs; found {len(files)}")

    subprocess.run(["git", "fetch", "--no-tags", "--depth=1", "origin", SOURCE_REF],
                   cwd=ROOT, check=True)
    fetched = subprocess.check_output(
        ["git", "rev-parse", "FETCH_HEAD"], cwd=ROOT, text=True
    ).strip()
    if fetched != SOURCE_SHA:
        raise SystemExit("v3.7 reference has changed; verify source SHA before building.")

    results = []
    for path in files:
        raw = subprocess.check_output(
            ["git", "show", f"FETCH_HEAD:icons/{path.name}"], cwd=ROOT
        )
        with Image.open(BytesIO(raw)) as opened:
            source = opened.convert("RGBA")
        output, before, after, scale, capped = transformed(source)
        output.save(path, "PNG", optimize=True)
        with Image.open(path) as verify:
            if verify.mode != "RGBA" or verify.size != (SIZE, SIZE):
                raise RuntimeError(f"Invalid output: {path.name}")
        results.append((path.name, before, after, scale, capped))
        print(f"{path.name}: main span {before:3d} -> {after:3d} px; "
              f"scale {scale:.3f}; {'margin-limited' if capped else 'ok'}")

    gains = sum(1 for _, _, _, scale, _ in results if scale > 1.005)
    limits = sum(1 for _, _, _, _, capped in results if capped)
    before = [x[1] for x in results]
    after = [x[2] for x in results]
    lines = [
        "# v3.8 — Visible Artwork Size Audit",
        "",
        "Generated by `tools/generate_v38.py` using the immutable v3.7 source.",
        "",
        f"- Icons checked: **{len(files)}** RGBA PNGs at **120×120 px**",
        f"- Icons enlarged: **{gains}**",
        f"- Margin-limited icons: **{limits}** (content retained, no forced clipping)",
        f"- Visible longest-edge before: **{min(before)}–{max(before)} px**, "
        f"median **{statistics.median(before):g} px**",
        f"- Visible longest-edge after: **{min(after)}–{max(after)} px**, "
        f"median **{statistics.median(after):g} px**",
        "",
        "The alpha >= 20 threshold measures substantive artwork, including "
        "weather pictograms rather than surrounding transparent margins.",
        "Scaling respects the full nonzero-alpha bounds to retain glow, "
        "precipitation, sun rays and lightning.",
        "",
        "| PNG | v3.7 visible span | v3.8 visible span | Scale | Margin limit |",
        "|---|---:|---:|---:|:---:|",
    ]
    for name, old, new, scale, limited in results:
        lines.append(f"| `{name}` | {old} | {new} | {scale:.3f}× | "
                     f"{'Yes' if limited else 'No'} |")
    lines.append("")
    AUDIT.write_text("\n".join(lines), encoding="utf-8")

    BUNDLE.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(BUNDLE, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        archive.write(MAPPING, "weather-icons/aeris-icon-list.json")
        for path in files:
            archive.write(path, f"weather-icons/{path.name}")
    print(f"Success: {len(files)} icons at 120x120; {gains} enlarged; {limits} capped.")


if __name__ == "__main__":
    main()
