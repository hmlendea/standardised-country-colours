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
├── scripts/                                  # the build
│   ├── build.py                              # the command-line entry point
│   ├── builder.py                            # shared, game-agnostic build engine
│   ├── palette.py                            # shared palette reader
│   ├── config.py                             # shared, project-wide configuration
│   └── games/                                # one package per game edition
│       ├── __init__.py                       # the edition registry
│       ├── base.py                           # the edition contract
│       └── victoria3/                        # the Victoria 3 edition
│           ├── __init__.py                   # the registered edition
│           ├── config.py                     # identity and tag mappings
│           └── render.py                     # artefact rendering
├── src/                                      # build inputs
│   ├── colours.md                            # the shared palette snapshot
│   └── victoria3/                            # the Victoria 3 edition assets
│       ├── launcher-thumbnail.png            # 600x333 launcher artwork
│       └── thumbnail.png                     # 512x512 Workshop artwork
└── standardised-country-colours/             # the built mod folder
    ├── .metadata/
    │   ├── metadata.json
    │   └── thumbnail.png                     # 600x333 launcher artwork
    ├── common/
    │   └── country_definitions/
    │       └── sc_country_colours.txt        # 131 injections, 665 lines
    └── thumbnail.png                         # 512x512 Workshop artwork
```

## File inventory

| Path | Lines | Role |
|------|-------|------|
| `standardised-country-colours/common/country_definitions/sc_country_colours.txt` | 665 | The entire product: 131 commented `INJECT:` blocks |
| `standardised-country-colours/.metadata/metadata.json` | 22 | Launcher descriptor |
| `standardised-country-colours/.metadata/thumbnail.png` | — | Launcher artwork, 600x333 RGB |
| `standardised-country-colours/thumbnail.png` | — | Workshop artwork, 512x512 RGB |
| `.github/workflows/github-release.yml` | 51 | Release archive publication |
| `.github/workflows/nexus-mods-release.yml` | 31 | Nexus Mods publication |
| `.github/workflows/steam-workshop-release.yml` | 39 | Steam Workshop publication |
| `.github/FUNDING.yml` | 18 | Funding platforms |
| `.github/cover.png` | — | Repository cover image, 1774x887 RGB |
| `description/steam-workshop.bbcode` | — | Steam Workshop page description, in BBCode |
| `scripts/build.py` | 78 | The command-line entry point: selects the editions and delegates |
| `scripts/builder.py` | 54 | The shared, game-agnostic build engine |
| `scripts/palette.py` | 75 | The shared palette reader and colour conversion |
| `scripts/config.py` | 20 | Shared project-wide configuration |
| `scripts/games/__init__.py` | 11 | The registry of supported game editions |
| `scripts/games/base.py` | 37 | The `GameEdition` contract every edition implements |
| `scripts/games/victoria3/__init__.py` | 15 | The registered Victoria 3 edition |
| `scripts/games/victoria3/config.py` | 210 | Edition identity, output layout, and the tag mappings |
| `scripts/games/victoria3/render.py` | 112 | Renders the Victoria 3 content and metadata files |
| `src/colours.md` | 333 | The shared palette snapshot the build reads |
| `src/victoria3/thumbnail.png` | — | Workshop artwork input, 1254x1254 RGB |
| `src/victoria3/launcher-thumbnail.png` | — | Launcher artwork input, 1683x934 RGB |
| `.gitignore` | 8 | Excludes archives, the build output, and transient files |

## Structural conventions

- **The mod folder mirrors `Victoria 3/game`.** `common/country_definitions/` is the counterpart of the game's own path; a wrong depth or a misspelled folder is never read.
- **The mod folder name is the release label.** `standardised-country-colours` appears in the archive name, the extracted directory name, and the GitHub release asset.
- **Every release workflow archives the same folder.** `github-release.yml` attaches the archive to a GitHub release; `steam-workshop-release.yml` uploads the extracted folder to the Workshop item; `nexus-mods-release.yml` uploads the archive to Nexus Mods. None transforms the content.- **Definitions live in one file.** Adding a second file in the same folder would split the shipped set and make review harder; nothing in the engine requires it.
- **Provenance sits above each block.** A comment records the vanilla name, the palette hexadecimal value, and the palette source.
- **No vanilla file name is copied.** `sc_country_colours.txt` cannot collide with `00_countries.txt`, `01_africa.txt`, `01_pacific_and_australasia.txt`, or `99_dynamic.txt`.
- **The Workshop description is version-controlled.** `description/steam-workshop.bbcode` holds the item page body, so a page revision is reviewed and tracked like any other change. It is not part of the mod folder and is never archived into a release.

## Building

`scripts/build.py` renders every registered mod folder from the shared palette snapshot in `src/colours.md` and the per-game configuration under `scripts/games/`:

```bash
python3 scripts/build.py --version 1.0.0
```

The output is written to `out/<folder>/` by default; `-o`/`--out`/`--output` selects another directory and `-g`/`--game` restricts the run to one or more editions. The script produces folders byte-identical to the committed `standardised-country-colours/`, so the tracked output can be regenerated and diffed at any time.

The release workflows still archive the committed folder, so a release is reproducible from the tagged tree alone.

## Adding a game edition

The build is game-agnostic; a new edition supplies its identity, mappings, and rendering and registers itself once.

1. Create `scripts/games/<game>/config.py` with the edition identity, output layout, `COUNTRY_PALETTE_ENTRIES`, and any `VANILLA_COUNTRY_NAMES`.
2. Create `scripts/games/<game>/render.py` with `render_text_files(palette, version)` and `render_asset_files(source_directory_path)`, following the Victoria 3 edition.
3. Create `scripts/games/<game>/__init__.py` exporting an `EDITION` value built from those functions.
4. Register the edition in `scripts/games/__init__.py` and add its assets under `src/<game>/`.

No change to `scripts/build.py`, `scripts/builder.py`, `scripts/palette.py`, or `scripts/config.py` is required.

## Excluded from version control

`.gitignore` excludes:

| Pattern | Reason |
|---------|--------|
| `out/` | The default build output directory |
| `*.zip` | Release archives are attached to GitHub releases, not committed |
| `*.dnspython*`, `.DS_Store`, `Thumbs.db`, `*.tmp` | Editor and OS transients |

## Related documents

- [repository-overview.md](./repository-overview.md) — why the tree looks like this.
- [components/mod-content.md](./components/mod-content.md) — the one content file in detail.
- [build-and-deployment.md](./build-and-deployment.md) — how the folder is built and becomes an archive.