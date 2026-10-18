# Changelog

All notable changes to Weather Icons are documented here.

## [3.8.0] - 2026-10-18

### Artwork
- Derived the new v3.8 branch from v3.7, preserving earlier versions.
- Retained identical 120×120 PNG canvases but enlarged *visible* weather pictograms by approximately 5% where margin permits.
- Applied a stronger alpha-aware correction for visibly smaller symbols (e.g., rain and thunderstorm), seeking a 108px minimum substantive artwork span when possible.
- Respected full alpha content to avoid losing rain, lightning, sunlight or cloud glow; see `docs/V3_8_SIZE_AUDIT.md` for individual measurements and size-limited exceptions.
- Retained all 147 names, 113 Aeris mappings, PNG transparency and Personal Use License.
- Regenerated the manifest, gallery, catalog and source-icons ZIP.

## [3.7.0] - 2026-10-17

### Artwork
- Created separate `v3.7` branch from `v3.6`, preserving older branches and `main`.
- Upscaled all 147 v3.6 RGBA PNGs from 110×110 to 120×120 using high-quality Lanczos interpolation, including visible subject and transparent margins.
- Preserved filenames, Aeris mapping (113 entries), alpha transparency, and Personal Use License.
- Rebuilt metadata, gallery, and canonical icon ZIP with 120×120 assets.

## [3.6.0] - 2026-10-17

### Artwork
- Created dedicated `v3.6` branch from `v3.5` without changing the existing versions.
- Normalized all 147 PNG canvases to 110×110 pixels, including previously smaller icons.
- Increased the visible artwork size by 2 pixels where margins allow; small icons are brought to the collection's reference visual scale.
- Preserved RGBA transparency, filenames, mapping keys, and the proprietary Personal Use License.
- Rebuilt manifest, catalog, gallery and source ZIP from the normalized icons.

## [Unreleased]

### Licensing
- Replaced CC BY-SA 4.0 with the proprietary Weather Icons Personal Use License 1.0.
- Personal, private, domestic and hobby non-commercial use is permitted.
- Commercial, professional, business and institutional use requires prior written permission from Gianpaolo P. (pgpaolo).
- Updated copyright, attribution, contribution and repository documentation accordingly.

### Repository structure
- Dedicated artwork branches: `v2`, `v2.5`, `v3`, and `v3.5`.
- `main` remains the stable published branch.
- Each version branch contains 147 PNG assets.
- Metadata and canonical source bundles are generated automatically.

## [2.0.0] - 2026-09-03

### Added
- Initial public release.
- 147 transparent PNG assets.
- Aeris-style mapping with 113 condition mappings.
- Machine-readable manifest, visual gallery and icon catalog.
- Automated bundle synchronization and repository validation.
