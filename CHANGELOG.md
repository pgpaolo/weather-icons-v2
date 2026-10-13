# Changelog

All notable changes to Weather Icons v2 are documented here.

The project follows semantic versioning for published icon-set releases.

## [Unreleased]

### Repository structure
- Introduced dedicated artwork branches: `v2`, `v2.5`, `v3`, and `v3.5`.
- `main` remains the stable published branch.
- Version branches are isolated workspaces for their corresponding 147-PNG icon packages.
- Populated `v2`, `v2.5`, `v3`, and `v3.5` with 147 PNG assets each.
- Generated branch metadata and canonical source bundles successfully after each upload.
- Metadata refresh automation now supports all version branches.
- Stable validation is enforced on `main` and pull requests before promotion.

### Artwork history
- Four supplied artwork archives are tracked as distinct generations: v2, v2.5, v3, and v3.5.
- All generations preserve the filename-based integration model used by the project.
- Aeris mapping compatibility remains part of the release validation process.

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
