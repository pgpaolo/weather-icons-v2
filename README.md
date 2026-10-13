# Weather Icons

A proprietary weather icon collection by **Gianpaolo P. (pgpaolo)**.

This repository provides transparent PNG weather assets with stable filenames
for web dashboards, personal weather stations, embedded projects,
WeeWX/Weather34-style interfaces, and other filename-based weather themes.

> **Copyright:** Weather Icons © 2026 Gianpaolo P. (pgpaolo). Personal use only. Commercial use requires prior written permission.

## Version branches

| Branch | Purpose | Current status |
|---|---|---|
| `v2` | Version 2 artwork | 147 PNG |
| `v2.5` | Version 2.5 artwork | 147 PNG |
| `v3` | Version 3 artwork | 147 PNG |
| `v3.5` | Version 3.5 artwork | 147 PNG |
| `main` | Stable published set | 147 PNG |

Each version branch is independent. GitHub Actions regenerates the
machine-readable manifest, icon catalog, visual gallery, and canonical source
bundle after icon updates.

See [docs/VERSION_BRANCHES.md](docs/VERSION_BRANCHES.md).

## Status

- **Stable branch:** `main`
- **Version branches:** `v2`, `v2.5`, `v3`, `v3.5`
- **Assets:** 147 transparent PNG files per version
- **Weather mapping:** `aeris-icon-list.json` with 113 mappings
- **Primary canvas:** 110×110 px for most weather conditions
- **Transparency:** PNG/RGBA
- **License:** Weather Icons Personal Use License 1.0

## Use

Personal, private, domestic, and hobby use is permitted under the
[Weather Icons Personal Use License](LICENSE).

Commercial, professional, business, institutional, promotional, sponsored,
advertising, or monetized use requires **prior written permission from
Gianpaolo P. (pgpaolo)**.

Preferred credit for permitted publicly accessible personal projects:

```text
Weather Icons © Gianpaolo P. (pgpaolo)
https://github.com/pgpaolo/weather-icons-v2
Personal use only — commercial use requires prior written permission.
```

## Repository layout

```text
weather-icons-v2/
├── icons/
├── mappings/
├── docs/
├── dist/
├── tools/
├── .github/workflows/
├── ATTRIBUTION.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CITATION.cff
├── LICENSE
├── NOTICE.md
└── manifest.json
```

## Quick use

```bash
git clone https://github.com/pgpaolo/weather-icons-v2.git
```

To clone a specific generation:

```bash
git clone --branch v3.5 https://github.com/pgpaolo/weather-icons-v2.git
```

Example HTML:

```html
<img src="icons/clear-day.png" width="110" height="110" alt="Clear sky">
```

## Aeris-style mapping

The repository includes `mappings/aeris-icon-list.json`. Mapping targets are
validated automatically against the PNG files in `icons/`.

## Generated metadata

`manifest.json`, `docs/ICON_CATALOG.md`, and `docs/GALLERY.md` are
generated from the published assets and checked by CI.

See [ATTRIBUTION.md](ATTRIBUTION.md), [NOTICE.md](NOTICE.md), and
[LICENSE](LICENSE).

---

## Italiano

**Weather Icons** è una raccolta proprietaria di icone meteo di
**Gianpaolo P. (pgpaolo)**.

L'uso personale, privato, domestico e hobbistico non commerciale è consentito
secondo la licenza contenuta nel repository. Ogni uso commerciale,
professionale, aziendale, istituzionale, promozionale, sponsorizzato o
monetizzato richiede autorizzazione scritta preventiva dell'autore.

```text
Weather Icons © 2026 Gianpaolo P. (pgpaolo)
https://github.com/pgpaolo/weather-icons-v2
Uso personale consentito — uso commerciale previa autorizzazione scritta.
```
