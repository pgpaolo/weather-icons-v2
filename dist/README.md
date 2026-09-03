# Distribution bundle

`dist/source-icons.zip` is the canonical import bundle for Weather Icons v2.

When this ZIP is added or replaced on `main`, the `Sync source bundle` GitHub Actions workflow automatically:

1. validates the ZIP archive;
2. publishes all PNG files into `icons/`;
3. publishes `aeris-icon-list.json` into `mappings/`;
4. regenerates `manifest.json`;
5. regenerates `docs/ICON_CATALOG.md` and `docs/GALLERY.md`;
6. commits the synchronized assets back to `main`.

The source archive may contain a single top-level folder. The synchronization tool normalizes the published repository layout.

See `docs/PUBLISHING.md` for the one-file publishing procedure.
