# Contributing

Contributions may be proposed for review, but acceptance does not grant a
right to redistribute or commercially exploit the Weather Icons collection.

## Workflow

1. Fork the repository.
2. Create a branch from the appropriate version branch or from `main`.
3. Add or modify the relevant PNG files.
4. Preserve transparent backgrounds and intended weather semantics.
5. Run:

```bash
python tools/build_metadata.py
python tools/build_metadata.py --check
```

6. Commit generated metadata together with icon changes.
7. Open a pull request with before/after context.

## Asset requirements

- PNG format.
- RGBA color type with transparency.
- Keep existing filenames and dimensions stable for replacements.
- Weather semantics must remain consistent with filename/mapping.

## Rights in contributions

Do not submit material unless you have authority to provide it for inclusion
in this project.

By submitting a contribution, you grant Gianpaolo P. (pgpaolo) a perpetual,
worldwide, non-exclusive, royalty-free right to use, reproduce, modify,
integrate, and distribute the contribution as part of the Weather Icons
project under the project's current or future licensing terms.

This does not grant contributors or third parties commercial rights to the
existing Weather Icons collection.

See [LICENSE](LICENSE).
