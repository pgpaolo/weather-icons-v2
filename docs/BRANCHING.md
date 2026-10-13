# Branching model

The repository keeps the stable published set on `main` and preserves each
artwork generation in a dedicated permanent branch.

- `main` — stable published set.
- `develop` — integration branch, kept aligned with `main` unless active development is in progress.
- `v2` — version 2 artwork.
- `v2.5` — version 2.5 artwork.
- `v3` — version 3 artwork.
- `v3.5` — version 3.5 artwork.

## Recommended flow

1. Work on the appropriate version branch for artwork changes.
2. Keep filenames and canvas dimensions compatible unless a breaking change is intentional.
3. Let GitHub Actions regenerate metadata and the canonical source bundle.
4. Validate the branch.
5. Promote the selected version to `main` only after review.
6. Realign `develop` with `main` after publication.

The version branches are long-lived historical/artwork branches and should not
be deleted after release.
