# Version branches

Weather Icons v2 keeps artwork generations separated by branch.

| Branch | Source archive | Status |
|---|---|---|
| `v2` | `icons-v2.zip` | Populated — 147 PNG |
| `v2.5` | `icons-v2.5.zip` | Populated — 147 PNG |
| `v3` | `icons-v3.zip` | Populated — 147 PNG |
| `v3.5` | `icons-v3.5.zip` | Populated — 147 PNG |

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
