# Publishing icon updates

Weather Icons uses direct PNG publication on the version branches and a stable
published branch on `main`.

## Version branches

The permanent artwork branches are:

- `v2`
- `v2.5`
- `v3`
- `v3.5`

To update a version:

1. switch to the required version branch;
2. upload or replace PNG files in `icons/`;
3. commit the changes;
4. wait for the **Refresh icon metadata** workflow.

The workflow regenerates:

- `manifest.json`;
- `docs/ICON_CATALOG.md`;
- `docs/GALLERY.md`;
- `dist/source-icons.zip`.

## Stable main branch

`main` is the stable published branch.

A version should be promoted to `main` only after checking:

- expected filenames;
- expected dimensions;
- PNG/RGBA transparency;
- mapping targets;
- generated metadata;
- visual margins/cropping;
- licensing/documentation consistency.

## Canonical ZIP

`dist/source-icons.zip` is the canonical ZIP generated from the PNG files in
that branch. It is a distribution artifact, not the preferred manual editing
surface.

The preferred source-of-truth workflow is to update `icons/` on the selected
version branch and let automation rebuild the ZIP.
