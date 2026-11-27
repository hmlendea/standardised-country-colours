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
│       ├── hoi4/                             # the Hearts of Iron IV edition
│       ├── imperator/                        # the Imperator: Rome edition
│       └── victoria3/                        # the Victoria 3 edition
│           ├── __init__.py                   # the registered edition
│           ├── config.py                     # identity and tag mappings
│           └── render.py                     # artefact rendering
├── src/                                      # build inputs
│   ├── colours.md                            # the shared palette snapshot
│   ├── icon.png                              # shared Workshop artwork
│   └── preview.png                           # shared launcher artwork
├── vanilla/                                  # vendored vanilla game data
│   └── imperator/                            # the Imperator: Rome snapshot
│       └── setup/countries/                  # countries.txt and the shipped tag files
└── (out/)                                    # generated, git-ignored
    └── vic3/
        └── standardised-country-colours/      # the built mod folder
            ├── .metadata/
            │   ├── metadata.json
            │   └── thumbnail.png              # 600x333 launcher artwork
            ├── common/
            │   └── country_definitions/
            │       └── sc_country_colours.txt # 135 injections, 685 lines
            └── thumbnail.png                  # 512x512 Workshop artwork
```

The mod folder is not tracked. It exists only as build output, so the repository holds inputs and the code that renders them, not a duplicated artefact.

## File inventory

| Path | Lines | Role |
|------|-------|------|
| `.github/workflows/github-release.yml` | 104 | Release archive publication, one job per game edition |
| `.github/workflows/nexus-mods-release.yml` | 114 | Nexus Mods publication, one job per game edition |
| `.github/workflows/steam-workshop-release.yml` | 99 | Steam Workshop publication, one job per game edition |
| `.github/FUNDING.yml` | 18 | Funding platforms |
| `.github/cover.png` | — | Repository cover image, 1774x887 RGB |
| `description/steam-workshop.bbcode` | — | Steam Workshop page description, in BBCode |
| `scripts/build.py` | 78 | The command-line entry point: selects the editions and delegates |
| `scripts/builder.py` | 56 | The shared, game-agnostic build engine |
| `scripts/palette.py` | 75 | The shared palette reader and colour conversion |
| `scripts/config.py` | 20 | Shared project-wide configuration |
| `scripts/games/__init__.py` | 11 | The registry of supported game editions |
| `scripts/games/base.py` | 39 | The `GameEdition` contract every edition implements |
| `scripts/games/victoria3/__init__.py` | 18 | The registered Victoria 3 edition |
| `scripts/games/victoria3/config.py` | 216 | Edition identity, output layout, and the tag mappings |
| `scripts/games/victoria3/render.py` | 112 | Renders the Victoria 3 content and metadata files |
| `src/colours.md` | 432 | The shared palette snapshot the build reads |
| `src/icon.png` | — | Shared Workshop artwork input, 1254x1254 RGB |
| `src/preview.png` | — | Shared launcher artwork input, 1683x934 RGB |
| `vanilla/imperator/setup/countries/countries.txt` | 682 | The vendored vanilla tag index, preserved verbatim in the build |
| `vanilla/imperator/setup/countries/<group>/<tag>.txt` | — | The 29 vendored vanilla country files the Imperator build overrides |
| `.gitignore` | 8 | Excludes archives, the build output, and transient files |

The generated files appear only under `out/`: `common/country_definitions/sc_country_colours.txt` (685 lines, 135 commented `INJECT:` blocks), `.metadata/metadata.json` (22 lines), and the two copied PNGs.

## Structural conventions

- **The mod folder mirrors each game's own `game/` tree.** `common/country_definitions/` is the counterpart of the game's own path; a wrong depth or a misspelled folder is never read, for either Victoria 3 or Imperator: Rome.
- **The mod folder is build output and per game.** It is rendered into `out/<game>/standardised-country-colours/` and never tracked, so the repository holds one copy of every value: in `src/colours.md`, the game edition's `config.py`, and the vendored `vanilla/<game>/` snapshot.
- **The mod folder name is the release label.** `standardised-country-colours` appears in the archive name, the extracted directory name, and the GitHub release asset; the game key (`vic3`, `imperator`) distinguishes the per-edition archives.
- **Every release workflow builds then archives the same folder.** Each runs `scripts/build.py` for the tag's version, then archives the freshly built folder; none of them transforms content, and `github-release.yml` produces one archive per game edition.
- **Provenance sits above each block.** A comment records the vanilla name, the palette hexadecimal value, and the palette source.
- **The Imperator build reads vendored vanilla data.** `vanilla/imperator/setup/countries/` holds the vanilla index and every shipped tag's country file, so the build needs no game installation and stays reproducible everywhere; the files are a read-only snapshot of the vanilla `setup/countries/` tree.
- **No vanilla file name is copied.** `sc_country_colours.txt` cannot collide with `00_countries.txt`, `01_africa.txt`, `01_pacific_and_australasia.txt`, or `99_dynamic.txt`.
- **The Workshop description is version-controlled.** `description/steam-workshop.bbcode` holds the item page body, so a page revision is reviewed and tracked like any other change. It is not part of the mod folder and is never archived into a release.

## Building

`scripts/build.py` renders every registered mod folder from the shared palette snapshot in `src/colours.md` and the per-game configuration under `scripts/games/`:

```bash
python3 scripts/build.py --game victoria3 --version 1.0.0
```

The output is written to `out/<group>/<folder>/` by default, where `<group>` is the edition's output group (`vic3` for Victoria 3); `-o`/`--out`/`--output` selects another root and `-g`/`--game` selects one or more editions. Because the mod folder is not tracked, the build is the only way to produce it.

## Release artefact

The release workflows build the mod at the tag's version and archive it, so a release is the build output for that tag. A local greyscale of the same steps:

```bash
python3 scripts/build.py --game victoria3 --game imperator --version 1.0.0
(cd out/vic3 && zip -r "${OLDPWD}/standardised-country-colours_vic3_1.0.0.zip" "standardised-country-colours/")
(cd out/imperator && zip -r "${OLDPWD}/standardised-country-colours_imperator_1.0.0.zip" "standardised-country-colours/")
```

The archive root is the mod folder itself, so extracting it into the mod directory yields `<mod dir>/standardised-country-colours/`.

## Adding a game edition

The build is game-agnostic; a new edition supplies its identity, mappings, and rendering and registers itself once.

1. Create `scripts/games/<game>/config.py` with the edition identity, output group, output layout, `COUNTRY_PALETTE_ENTRIES`, and any `VANILLA_COUNTRY_NAMES`.
2. Create `scripts/games/<game>/render.py` with `render_text_files(palette, version)` and `render_asset_files(source_directory_path)`; add `render_parent_text_files(palette, version)` only when the game needs a descriptor beside the mod folder instead of inside it (as Imperator: Rome does).
3. Create `scripts/games/<game>/__init__.py` exporting an `EDITION` value built from those functions.
4. Register the edition in `scripts/games/__init__.py` and use the shared assets `src/icon.png` and `src/preview.png`.

No change to `scripts/build.py`, `scripts/builder.py`, `scripts/palette.py`, or `scripts/config.py` is required.

## Excluded from version control

`.gitignore` excludes:

| Pattern | Reason |
|---------|--------|
| `out/` | The default build output directory, grouped per game |
| `*.zip` | Release archives are attached to GitHub releases, not committed |
| `*.dnspython*`, `.DS_Store`, `Thumbs.db`, `*.tmp` | Editor and OS transients |

## Related documents

- [repository-overview.md](./repository-overview.md) — why the tree looks like this.
- [components/mod-content.md](./components/mod-content.md) — the one content file in detail.
- [build-and-deployment.md](./build-and-deployment.md) — how the folder is built and becomes an archive.