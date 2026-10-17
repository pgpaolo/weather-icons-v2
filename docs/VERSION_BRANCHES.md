# Version branches

Weather Icons v2 keeps artwork generations separated by branch.

| Branch | Icon archive to upload |
|---|---|
| `v2` | `icons-v2.zip` |
| `v2.5` | `icons-v2.5.zip` |
| `v3` | `icons-v3.zip` |
| `v3.5` | `icons-v3.5.zip` |
| `v3.6` | `dist/source-icons.zip` (all 147 PNGs at 110×110) |
| `v3.7` | `dist/source-icons.zip` (all 147 PNGs at 120×120) |

## Upload procedure

1. Switch to the required version branch.
2. Open `icons/`.
3. Upload the PNG files for that version.
4. Remove `.gitkeep` if GitHub leaves it in the folder.
5. Commit the upload.

The branch workflow then regenerates metadata and `dist/source-icons.zip`.

## Promotion to main

A version branch is promoted to `main` only after review of:

- expected filename set;
- expected dimensions;
- RGBA transparency;
- Aeris mapping targets;
- generated manifest/catalog consistency;
- visual margin/cropping checks.

`main` is the stable branch and should not be used as a staging area for direct bulk icon uploads.
