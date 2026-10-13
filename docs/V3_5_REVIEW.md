# Weather Icons v3.5 — Candidate Review

This document records the pre-publication validation of the artwork supplied for the v3.5 candidate.

## Selected source

**Selected:** `icons-v3.5.zip`

The archive was selected after inspecting all four supplied candidate bundles.

| Archive | PNGs | RGBA | Edge-touch check | Notes |
|---|---:|---:|---:|---|
| `icons-v2.zip` | 147 | 147/147 | 8 flagged | Includes a 1254×1254 `clearn.png` outlier and several assets touching canvas edges |
| `icons-v2.5.zip` | 147 | 147/147 | 0 flagged | Valid candidate |
| `icons-v3.zip` | 147 | 147/147 | 0 flagged | File-for-file identical to v2.5 |
| **`icons-v3.5.zip`** | **147** | **147/147** | **0 flagged** | **Selected: latest coherent revision and smallest supplied archive** |

## Compatibility checks

The v3.5 candidate passed the following checks:

- exactly **147 PNG files**
- filename set matches the existing published icon contract
- every PNG uses **RGBA / alpha transparency**
- native dimensions remain compatible with the current icon set
- most weather-condition icons remain **110×110 px**
- special station, scale and status assets retain their dedicated dimensions
- no non-transparent bounding box reaches a canvas edge in the automated crop-safety check
- no filename changes are required in `mappings/aeris-icon-list.json`
- current Aeris-style mapping remains at **113 entries**

## Artwork delta

Compared with the supplied v3 archive:

- **109 icons** contain different rendered pixels
- **38 icons** are pixel-identical
- v2.5 and v3 are themselves file-for-file identical

This confirms that v3.5 is a meaningful artwork refresh rather than a rename of the previous package.

## Publication workflow

The candidate is reviewed on:

```text
feature/weather-icons-v3-redesign
```

The intended publication flow is:

```text
validated v3.5 source bundle
        ↓
candidate branch
        ↓
metadata / mapping validation
        ↓
visual review
        ↓
pull request
        ↓
main
```

`main` remains the stable branch until the candidate has passed review and is explicitly merged.

## Licensing and attribution

The v3.5 candidate remains covered by the repository licensing and attribution policy:

```text
Weather Icons v2 by pgpaolo
https://github.com/pgpaolo/weather-icons-v2
CC BY-SA 4.0
```

See `LICENSE`, `ATTRIBUTION.md` and `NOTICE.md`.
