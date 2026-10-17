#!/usr/bin/env python3
"""Build v3.7 icons by proportionally scaling all 147 v3.6 PNGs to 120x120.

The complete transparent 110x110 canvas is enlarged to 120x120, including
the visible subject. Relative margins and proportions remain consistent.
Always start from the pinned v3.6 input, so repeated runs do not enlarge
already-generated v3.7 images.
"""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
import subprocess
from zipfile import ZipFile, ZIP_DEFLATED

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / "icons"
BASE_BRANCH = "v3.6"
BASE_SHA = "8d4162345a7144a7f85aac4db2334d3a5ed4acdc"
SOURCE_SIZE = (110, 110)
TARGET_SIZE = (120, 120)
EXPECTED_ICONS = 147
BUNDLE = ROOT / "dist" / "source-icons.zip"
MAPPING = ROOT / "mappings" / "aeris-icon-list.json"


def main() -> None:
    files = sorted(ICONS.glob("*.png"), key=lambda p: p.name.lower())
    if len(files) != EXPECTED_ICONS:
        raise SystemExit(f"Expected {EXPECTED_ICONS} icons, got {len(files)}")

    subprocess.run(
        ["git", "fetch", "--no-tags", "--depth=1", "origin", BASE_BRANCH],
        cwd=ROOT, check=True,
    )
    fetched = subprocess.check_output(
        ["git", "rev-parse", "FETCH_HEAD"], cwd=ROOT, text=True
    ).strip()
    if fetched != BASE_SHA:
        raise SystemExit(
            "Source v3.6 commit has changed: verify the reference before "
            "regenerating v3.7."
        )

    for path in files:
        raw = subprocess.check_output(
            ["git", "show", f"FETCH_HEAD:icons/{path.name}"], cwd=ROOT
        )
        with Image.open(BytesIO(raw)) as source:
            if source.size != SOURCE_SIZE or source.mode != "RGBA":
                raise ValueError(
                    f"{path.name}: expected RGBA 110x110, "
                    f"got {source.mode} {source.size}"
                )
            source.load()
            # Pillow resamples RGBA with alpha handling; transparency is kept.
            resized = source.resize(TARGET_SIZE, Image.Resampling.LANCZOS)

        resized.save(path, format="PNG", optimize=True)

        with Image.open(path) as verified:
            if verified.size != TARGET_SIZE or verified.mode != "RGBA":
                raise RuntimeError(f"Incorrect output for {path.name}")
            alpha = verified.getchannel("A")
            if alpha.getbbox() is None:
                raise RuntimeError(f"Blank icon generated: {path.name}")
            lo, hi = alpha.getextrema()
            if lo != 0:
                raise RuntimeError(f"Transparency lost: {path.name}")
        print(f"OK {path.name}: 110x110 -> 120x120 RGBA")

    BUNDLE.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(BUNDLE, "w", compression=ZIP_DEFLATED, compresslevel=9) as zip_file:
        zip_file.write(MAPPING, "weather-icons/aeris-icon-list.json")
        for path in files:
            zip_file.write(path, f"weather-icons/{path.name}")

    print(
        f"Successfully converted {len(files)} icons to 120x120 RGBA; "
        "mapping and distribution bundle updated."
    )


if __name__ == "__main__":
    main()
