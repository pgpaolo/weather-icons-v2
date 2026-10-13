# Weather Icons v2

A curated weather icon set maintained by **pgpaolo**.

This repository provides transparent PNG weather assets with stable filenames for use in web dashboards, personal weather stations, embedded projects, WeeWX/Weather34-style interfaces, and other filename-based weather themes.

> **Designated attribution:** `Weather Icons v2 by pgpaolo — https://github.com/pgpaolo/weather-icons-v2 — CC BY-SA 4.0`

## Version branches

The project keeps the stable published set on `main` and uses one dedicated branch for each artwork generation:

| Branch | Purpose |
|---|---|
| `v2` | Version 2 artwork |
| `v2.5` | Version 2.5 artwork |
| `v3` | Version 3 artwork |
| `v3.5` | Version 3.5 artwork |
| `main` | Stable published set |

Each version branch is intentionally independent. Its `icons/` directory is the upload target for that specific icon package. After PNG files are uploaded, GitHub Actions regenerates the machine-readable manifest, icon catalog, visual gallery, and canonical ZIP bundle for that branch.

See [docs/VERSION_BRANCHES.md](docs/VERSION_BRANCHES.md).

## Status

- **Stable branch:** `main`
- **Version branches:** `v2`, `v2.5`, `v3`, `v3.5`
- **Expected icon set:** 147 transparent PNG assets per version
- **Weather mapping:** `aeris-icon-list.json` with 113 mappings
- **Primary canvas:** 110×110 px for most weather conditions
- **Transparency:** PNG/RGBA
- **License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

## Repository layout

```text
weather-icons-v2/
├── icons/                  # PNG assets for the selected branch/version
├── mappings/               # Weather-code / filename mappings
├── docs/                   # Catalog, gallery and project documentation
├── dist/                   # Canonical source bundle generated for the branch
├── tools/                  # Validation / metadata utilities
├── .github/workflows/      # Automated validation and metadata refresh
├── ATTRIBUTION.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CITATION.cff
├── LICENSE
├── NOTICE.md
└── manifest.json
```

## Quick use

Clone the stable set:

```bash
git clone https://github.com/pgpaolo/weather-icons-v2.git
```

Clone a specific artwork generation:

```bash
git clone --branch v3.5 https://github.com/pgpaolo/weather-icons-v2.git
```

Then copy the files you need from `icons/` into your application's weather-icon directory. The published filenames are intentionally stable so applications can map a weather condition directly to a PNG file.

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

The repository includes `mappings/aeris-icon-list.json`. It maps weather-condition identifiers to icon basenames. Mapping targets are validated against the files in `icons/` before a version is promoted to `main`.

## Automated metadata

On version branches, an icon upload automatically refreshes:

- `manifest.json`
- `docs/ICON_CATALOG.md`
- `docs/GALLERY.md`
- `dist/source-icons.zip`

Validation is enforced on `main` and on pull requests toward the stable branch.

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

---

## Italiano

**Weather Icons v2** è una raccolta di icone meteo mantenuta da **pgpaolo**.

Il repository usa un branch separato per ogni generazione grafica:

- `v2`
- `v2.5`
- `v3`
- `v3.5`

Il branch `main` rimane la versione stabile pubblicata. In ogni branch versione la cartella `icons/` è dedicata esclusivamente alle PNG di quella release. Dopo il caricamento delle immagini, GitHub Actions rigenera automaticamente manifest, catalogo, gallery e archivio ZIP canonico.

Le icone sono distribuite con licenza **CC BY-SA 4.0**.

```text
Weather Icons v2 by pgpaolo
https://github.com/pgpaolo/weather-icons-v2
CC BY-SA 4.0
```
