#!/usr/bin/env python3
"""Synchronize the canonical ZIP bundle into icons/ and mappings/."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / "icons"
MAPPINGS = ROOT / "mappings"

ALLOWED_NON_PNG = {"aeris-icon-list.json"}


def safe_members(zf: zipfile.ZipFile):
    for info in zf.infolist():
        if info.is_dir():
            continue
        path = Path(info.filename)
        if path.is_absolute() or ".." in path.parts:
            raise SystemExit(f"Unsafe ZIP path: {info.filename}")
        yield info


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: sync_bundle.py <source-icons.zip>", file=sys.stderr)
        return 2

    bundle = Path(sys.argv[1]).resolve()
    if not bundle.is_file():
        raise SystemExit(f"Bundle not found: {bundle}")

    with tempfile.TemporaryDirectory(prefix="weather-icons-v2-") as tmp:
        tmpdir = Path(tmp)
        with zipfile.ZipFile(bundle) as zf:
            members = list(safe_members(zf))
            zf.extractall(tmpdir, members=members)

        files = [p for p in tmpdir.rglob("*") if p.is_file()]
        pngs = [p for p in files if p.suffix.lower() == ".png"]
        non_png = [p for p in files if p.suffix.lower() != ".png"]

        unexpected = [p.name for p in non_png if p.name not in ALLOWED_NON_PNG]
        if unexpected:
            raise SystemExit(f"Unexpected non-PNG files in bundle: {unexpected}")
        if not pngs:
            raise SystemExit("No PNG assets found in bundle")

        shutil.rmtree(ICONS, ignore_errors=True)
        shutil.rmtree(MAPPINGS, ignore_errors=True)
        ICONS.mkdir(parents=True)
        MAPPINGS.mkdir(parents=True)

        seen = set()
        for src in sorted(pngs, key=lambda p: p.name.lower()):
            if src.name in seen:
                raise SystemExit(f"Duplicate PNG basename: {src.name}")
            seen.add(src.name)
            shutil.copy2(src, ICONS / src.name)

        mapping_sources = [p for p in non_png if p.name == "aeris-icon-list.json"]
        if mapping_sources:
            with mapping_sources[0].open("r", encoding="utf-8") as fh:
                mapping = json.load(fh)
            if not isinstance(mapping, dict):
                raise SystemExit("aeris-icon-list.json must contain a JSON object")
            with (MAPPINGS / "aeris-icon-list.json").open("w", encoding="utf-8", newline="\n") as fh:
                json.dump(mapping, fh, indent=2, sort_keys=False)
                fh.write("\n")

        print(f"Synchronized {len(pngs)} PNG assets")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
