# Changelog

All notable changes to Weather Icons v2 are documented here.

The project follows semantic versioning for published icon-set releases.

## [Unreleased]

### v3.5 artwork candidate

- Selected `icons-v3.5.zip` as the candidate artwork set after comparing the supplied v2, v2.5, v3 and v3.5 archives.
- Preserves the complete set of **147 PNG filenames** used by the project.
- Preserves the expected canvas dimensions and **RGBA transparency**.
- Automated edge inspection found **0 assets with visible pixels touching a canvas edge** in the v3.5 candidate.
- `icons-v2.5.zip` and `icons-v3.zip` are file-for-file identical; v3.5 is the subsequent artwork revision.
- Relative to v3, **109 assets have different rendered pixels** and 38 remain pixel-identical.
- Aeris mapping names are unchanged, so the existing 113 mapping entries remain compatible.
- Candidate archive size is **3,008,127 bytes**.

### Changed

- Refreshed `clear-night.png` and `clearn.png` with larger moon artwork while preserving the 110×110 px canvas, RGBA transparency and compact web-oriented file size.
- Added automatic metadata refresh on development icon changes, keeping `manifest.json` and the generated icon catalog synchronized.

## [2.0.0] - 2026-09-03

### Added

- Initial public release of Weather Icons v2.
- 147 transparent PNG assets.
- Aeris-style mapping with 113 condition mappings.
- Machine-readable manifest with dimensions, file size, PNG color type and SHA-256.
- Visual gallery and icon catalog.
- CC BY-SA 4.0 licensing and designated attribution to `pgpaolo`.
- Automated bundle synchronization and repository validation.

### Notes

- Most condition icons use a 110×110 px canvas.
- Special-purpose status, station and scale assets retain their native dimensions.
