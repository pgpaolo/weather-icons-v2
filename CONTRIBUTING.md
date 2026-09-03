# Contributing

Contributions are welcome. The goal is to keep Weather Icons v2 visually
coherent and filename-compatible.

## Workflow

1. Fork the repository.
2. Create a branch from `develop` when available, otherwise from `main`.
3. Add or modify the relevant PNG files.
4. Preserve transparent backgrounds and intended weather semantics.
5. Run:

```bash
python tools/build_metadata.py
python tools/build_metadata.py --check
```

6. Commit the generated `manifest.json`, `docs/ICON_CATALOG.md`, and
   `docs/GALLERY.md` together with the icon changes.
7. Open a pull request with before/after context.

## Asset requirements

- PNG format.
- RGBA color type with transparency.
- No embedded text inside normal weather-condition icons.
- Keep existing filenames stable unless a breaking change is explicitly intended.
- Keep existing dimensions stable for replacements.
- New filenames should be lowercase unless compatibility requires otherwise.
- Day/night variants should remain semantically paired.
- A `w` suffix should visibly communicate wind where the mapping uses that meaning.
- Snow, sleet, rain, fog and thunder should remain visually distinguishable at the final canvas size.

## Existing icon replacement

For an existing filename, do not silently change its meaning. A replacement
should depict the same weather condition while improving clarity or artwork.

## Mapping changes

If `mappings/aeris-icon-list.json` is changed, every target basename must
resolve to an existing PNG in `icons/`.

## Licensing of contributions

By submitting a contribution, you agree that the contributed material may be
distributed under CC BY-SA 4.0 as part of this project, to the extent you have
authority to grant those rights. Do not submit material for which you cannot
provide the necessary permissions.
