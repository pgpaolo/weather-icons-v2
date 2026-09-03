# Changelog

All notable changes to Weather Icons v2 are documented here.

The project follows semantic versioning for published icon-set releases.

## [Unreleased]

### Changed
- Refreshed `clear-night.png` and `clearn.png` with larger moon artwork while preserving the 110×110 px canvas, RGBA transparency and compact web-oriented file size.
- Added automatic metadata refresh on `develop` when icon assets change, keeping `manifest.json` and the generated icon catalog synchronized.

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
