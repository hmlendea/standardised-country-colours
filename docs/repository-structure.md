# Repository structure

## Tree

```text
vic3-standardised-country-colours/
├── .github/
│   ├── FUNDING.yml
│   ├── cover.png
│   └── workflows/
│       ├── github-release.yml
│       ├── nexus-mods-release.yml
│       └── steam-workshop-release.yml
├── .gitignore
├── ARCHITECTURE.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── description/
│   └── steam-workshop.bbcode                 # the Steam Workshop page body
├── docs/                                     # this knowledge base
├── LICENSE
├── PRIVACY.md
├── README.md
├── SECURITY.md
└── standardised-country-colours/             # the mod folder
    ├── .metadata/
    │   ├── metadata.json
    │   └── thumbnail.png                     # 600x333 launcher artwork
    ├── common/
    │   └── country_definitions/
    │       └── sc_country_colours.txt        # 101 injections, 515 lines
    └── thumbnail.png                         # 512x512 Workshop artwork
```

## File inventory

| Path | Lines | Role |
|------|-------|------|
| `standardised-country-colours/common/country_definitions/sc_country_colours.txt` | 515 | The entire product: 101 commented `INJECT:` blocks |
| `standardised-country-colours/.metadata/metadata.json` | 22 | Launcher descriptor |
| `standardised-country-colours/.metadata/thumbnail.png` | — | Launcher artwork, 600x333 RGB |
| `standardised-country-colours/thumbnail.png` | — | Workshop artwork, 512x512 RGB |
| `.github/workflows/github-release.yml` | 51 | Release archive publication |
| `.github/workflows/nexus-mods-release.yml` | 31 | Nexus Mods publication |
| `.github/workflows/steam-workshop-release.yml` | 39 | Steam Workshop publication |
| `.github/FUNDING.yml` | 18 | Funding platforms |
| `.github/cover.png` | — | Repository cover image, 1774x887 RGB |
| `description/steam-workshop.bbcode` | — | Steam Workshop page description, in BBCode |
| `.gitignore` | 7 | Excludes archives and transient output |

## Structural conventions

- **The mod folder mirrors `Victoria 3/game`.** `common/country_definitions/` is the counterpart of the game's own path; a wrong depth or a misspelled folder is never read.
- **The mod folder name is the release label.** `standardised-country-colours` appears in the archive name, the extracted directory name, and the GitHub release asset.
- **Every release workflow archives the same folder.** `github-release.yml` attaches the archive to a GitHub release; `steam-workshop-release.yml` uploads the extracted folder to the Workshop item; `nexus-mods-release.yml` uploads the archive to Nexus Mods. None transforms the content.- **Definitions live in one file.** Adding a second file in the same folder would split the shipped set and make review harder; nothing in the engine requires it.
- **Provenance sits above each block.** A comment records the vanilla name, the palette hexadecimal value, and the palette source.
- **No vanilla file name is copied.** `sc_country_colours.txt` cannot collide with `00_countries.txt`, `01_africa.txt`, `01_pacific_and_australasia.txt`, or `99_dynamic.txt`.
- **The Workshop description is version-controlled.** `description/steam-workshop.bbcode` holds the item page body, so a page revision is reviewed and tracked like any other change. It is not part of the mod folder and is never archived into a release.

## Why there is no build step

The distributable artefact is the mod folder itself. The release workflow archives the folder as it stands in the tagged commit. Nothing is generated, compiled, copied into a staging directory, or post-processed, so a checkout is byte-identical to a release archive's contents.

## Excluded from version control

`.gitignore` excludes:

| Pattern | Reason |
|---------|--------|
| `out/` | Conventional local staging directory, unused by this mod |
| `*.zip` | Release archives are attached to GitHub releases, not committed |
| `*.dnspython*`, `.DS_Store`, `Thumbs.db`, `*.tmp` | Editor and OS transients |

## Related documents

- [repository-overview.md](./repository-overview.md) — why the tree looks like this.
- [components/mod-content.md](./components/mod-content.md) — the one content file in detail.
- [build-and-deployment.md](./build-and-deployment.md) — how the folder becomes an archive.