# Distribution bundle

`dist/source-icons.zip` is the canonical generated bundle for the currently
selected branch.

For version branches (`v2`, `v2.5`, `v3`, `v3.5`), update PNG files in
`icons/`. The **Refresh icon metadata** workflow then regenerates:

1. `manifest.json`;
2. `docs/ICON_CATALOG.md`;
3. `docs/GALLERY.md`;
4. `dist/source-icons.zip`.

`main` remains the stable published branch.

See `docs/PUBLISHING.md` and `docs/VERSION_BRANCHES.md` for the publishing
and branch model.
