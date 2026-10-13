# Weather Icons v2

A curated, weather icon set maintained by **pgpaolo**.

This repository provides transparent PNG weather assets with stable filenames for use in web dashboards, personal weather stations, embedded projects, WeeWX/Weather34-style interfaces, and other filename-based weather themes.

> **Designated attribution:** `Weather Icons v2 by pgpaolo — https://github.com/pgpaolo/weather-icons-v2 — CC BY-SA 4.0`

## v3.5 artwork candidate

The branch `feature/weather-icons-v3-redesign` is the review branch for the **v3.5 artwork refresh**.

The candidate source archive has been checked before publication:

- **147 PNG assets**
- the **same 147 filenames** as the current published set
- **PNG/RGBA transparency** for every asset
- dimensions compatible with the existing filename contract
- **no detected non-transparent pixels touching the canvas edges**
- Aeris mapping filenames remain compatible
- source archive size: **3,008,127 bytes**

The detailed verification record is available in [docs/V3_5_REVIEW.md](docs/V3_5_REVIEW.md).

Until the candidate is reviewed and merged, **`main` remains the stable published branch**.

## Status

- **Stable version:** 2.0.0 (`main`)
- **Artwork candidate:** v3.5 (`feature/weather-icons-v3-redesign`)
- **Assets:** 147 transparent PNG files
- **Weather mapping:** `aeris-icon-list.json` with 113 mappings
- **Primary canvas:** 110×110 px for most weather conditions
- **Transparency:** PNG/RGBA
- **License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

## Repository layout

```text
weather-icons-v2/
├── icons/                  # Published PNG assets
├── mappings/               # Weather-code / filename mappings
├── docs/                   # Catalog, gallery and review notes
├── dist/                   # Canonical source bundle
├── tools/                  # Validation / metadata utilities
├── .github/workflows/      # Automated validation and bundle sync
├── ATTRIBUTION.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CITATION.cff
├── LICENSE
├── NOTICE.md
└── manifest.json
```

## Quick use

Clone the stable repository:

```bash
git clone https://github.com/pgpaolo/weather-icons-v2.git
```

To review the v3.5 candidate:

```bash
git clone --branch feature/weather-icons-v3-redesign https://github.com/pgpaolo/weather-icons-v2.git
```

Copy the files you need from `icons/` into your application's weather-icon directory. The published filenames are intentionally stable so applications can map a weather condition directly to a PNG file.

Example HTML:

```html
<img src="icons/clear-day.png" width="110" height="110" alt="Clear sky">
```

Example CSS:

```css
.weather-icon {
  width: 110px;
  height: 110px;
  object-fit: contain;
}
```

## Aeris-style mapping

The repository includes `mappings/aeris-icon-list.json`. It maps weather-condition identifiers to icon basenames. All mapping targets are validated automatically against the files in `icons/`.

## Attribution and reuse

The icon assets are published under **CC BY-SA 4.0**. You may share and adapt them, including commercially, subject to the license conditions, including attribution and ShareAlike for adaptations.

Preferred attribution:

```text
Weather Icons v2 by pgpaolo
https://github.com/pgpaolo/weather-icons-v2
CC BY-SA 4.0
```

Where hyperlinks are supported, linking `pgpaolo` or `Weather Icons v2` to this repository is recommended. If you modify the icons, indicate that modifications were made.

See [ATTRIBUTION.md](ATTRIBUTION.md), [NOTICE.md](NOTICE.md), and [LICENSE](LICENSE).

## Extending the set

Contributions are welcome. New icons should preserve the visual language of the set, use a transparent PNG canvas, follow the existing filename conventions, and avoid silently changing the semantics of existing filenames.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Generated metadata

`manifest.json`, `docs/ICON_CATALOG.md`, and `docs/GALLERY.md` are generated from the published assets and checked by CI. This makes filename, dimensions, file size, PNG color type, and SHA-256 information auditable.

---

## Italiano

**Weather Icons v2** è una raccolta di icone meteo curate e rifinite da **pgpaolo**, pensata per applicazioni web, stazioni meteo personali e progetti che associano le condizioni atmosferiche al nome del file.

Il branch `feature/weather-icons-v3-redesign` contiene il candidato grafico **v3.5**. Prima della pubblicazione il pacchetto è stato verificato per nomi file, dimensioni, trasparenza RGBA e margini; il dettaglio è in [docs/V3_5_REVIEW.md](docs/V3_5_REVIEW.md).

Le icone sono distribuite con licenza **CC BY-SA 4.0**. È consentito usarle, redistribuirle e modificarle nel rispetto delle condizioni della licenza. L'attribuzione designata è:

```text
Weather Icons v2 by pgpaolo
https://github.com/pgpaolo/weather-icons-v2
CC BY-SA 4.0
```

Per modifiche o nuove condizioni meteo, aprire una issue o una pull request seguendo [CONTRIBUTING.md](CONTRIBUTING.md).
