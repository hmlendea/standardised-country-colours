[![Donate](https://img.shields.io/badge/-%E2%99%A5%20Donate-%23ff69b4)](https://hmlendea.go.ro/funding)
[![License](https://img.shields.io/github/license/hmlendea/standardised-country-colours)](https://github.com/hmlendea/standardised-country-colours/blob/master/LICENSE)

# Standardised Country Colours

A cross-game project that assigns consistent, historically inspired map colours to selectable countries in various grand strategy games. Currently supports Hearts of Iron IV, Imperator: Rome, and Victoria 3.

## 📑 Table of Contents

- [Capabilities](#capabilities)
- [Use Cases](#use-cases)
- [Usage](#usage)
- [Known Limitations](#known-limitations)
- [Installation](#installation)
  - [Manual Installation](#manual-installation)
  - [Verification](#verification)
  - [Upgrading](#upgrading)
- [Compatibility](#compatibility)
- [Privacy and Data](#privacy-and-data)
- [GitHub Actions](#github-actions)
- [Project Structure](#project-structure)
  - [Directories](#directories)
- [Architecture](#architecture)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Related Projects](#related-projects)
- [Acknowledgements](#acknowledgements)
- [Security](#security)
- [Support](#support)
- [Project Engagement](#project-engagement)
- [License](#license)

## ✨ Capabilities

- Standardised map colours for 135 countries, applied through each game's definition-injection mechanism
- A single shared palette, so neighbouring countries no longer share near-identical map colours
- Historical and flag-derived colours, sourced from established strategy-game palettes and national flags
- Colour-only overrides: every other field of the affected country definition, such as tier, culture, and capital, is left to the base game
- Renewed whenever the game re-reads the definition, so a country released or formed during play receives the standardised colour
- Empty save-game footprint: no scripted effects, events, or state are introduced

## 🎯 Use Cases

- **Players:** Prefer a cleaner, more legible world map with distinct colours for the countries they encounter.
- **Multiplayer groups:** Give each participant a stable, recognisable colour across sessions without manual map-colour agreements.
- **Modders:** Use the palette as a reference when deciding a colour for a new or reworked country.

## 🚀 Usage

Enable the mod for a playset in your game's launcher, then start or load a campaign:

```text
Standardised Country Colours  [x]
```

Each affected country receives the standardised colour when the country definitions are read, and again whenever the country is released or formed. No in-game action is required.

## ⚠️ Known Limitations

- Only the countries listed in this mod are recoloured; countries outside that list keep their vanilla colours.
- The palette records the primary colour only, because the supported games expose a single map colour per country. Secondary and alternative colours are not represented on the map.
- The mod changes map colours, not unit colours. Countries that define `primary_unit_color`, `secondary_unit_color`, or `tertiary_unit_color` keep their vanilla unit colours.
- Coat-of-arms based flags still draw from their own colour definitions, so a country's flag may not match its new map colour.
- Countries at war, subjects, and other map-colour overlays continue to use the game's own colouring rules on top of the standardised colour.

## 📦 Installation

[![Obtain it from Nexus Mods](https://raw.githubusercontent.com/hmlendea/readme-assets/master/badges/stores/nexus.png)](https://nexusmods.com/victoria3/mods/54)
[![Obtain it from Steam Workshop](https://raw.githubusercontent.com/hmlendea/readme-assets/master/badges/stores/steam-workshop.png)](https://steamcommunity.com/sharedfiles/filedetails/?id=3844790373)
[![Obtain it from GitHub](https://raw.githubusercontent.com/hmlendea/readme-assets/master/badges/stores/github.png)](https://github.com/hmlendea/standardised-country-colours/releases)

The mod is published for Hearts of Iron IV, Imperator: Rome and Victoria 3:

| Game | Steam Workshop | Nexus Mods |
|------|----------------|------------|
| Hearts of Iron IV | To be published | To be published |
| Victoria 3 | [3844790373](https://steamcommunity.com/sharedfiles/filedetails/?id=3844790373) | [54](https://nexusmods.com/victoria3/mods/54) |
| Imperator: Rome | [3845414842](https://steamcommunity.com/sharedfiles/filedetails/?id=3845414842) | [36](https://nexusmods.com/imperatorrome/mods/36) |

### Manual Installation

1. Download the [latest release](https://github.com/hmlendea/standardised-country-colours/releases/latest) for your game edition
2. Extract the contents into the game's mod directory:
   - Hearts of Iron IV Linux: `~/.local/share/Paradox Interactive/Hearts of Iron IV/mod/`
   - Hearts of Iron IV macOS: `~/Library/Application Support/Paradox Interactive/Hearts of Iron IV/mod/`
   - Hearts of Iron IV Windows: `%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV/mod/`
   - Imperator: Rome Linux: `~/.local/share/Paradox Interactive/ImperatorRome/mod/`
   - Imperator: Rome macOS: `~/Library/Application Support/Paradox Interactive/ImperatorRome/mod/`
   - Imperator: Rome Windows: `%USERPROFILE%\Documents\Paradox Interactive\ImperatorRome\mod\`
   - Victoria 3 Linux: `~/.local/share/Paradox Interactive/Victoria 3/mod/`
   - Victoria 3 macOS: `~/Library/Application Support/Paradox Interactive/Victoria 3/mod/`
   - Victoria 3 Windows: `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\mod\`
3. Add the mod to a playset in the launcher and enable it

Do not extract the archive into the game installation directory; the games do not load mods from there.

### Verification

After enabling the mod and starting a campaign, open the map and confirm that France is a deeper blue and that Denmark is a brighter red than vanilla.

### Upgrading

Remove the previously extracted `standardised-country-colours` directory, then extract the new release in its place. Victoria 3 loads every file present in the mod directory, so a stale copy of a renamed or removed file continues to apply until the directory is replaced.

## 🧩 Compatibility

| Component | Supported Versions | Notes |
|-----------|--------------------|-------|
| Hearts of Iron IV | `1.19.*` | Declared as `supported_version` in the mod descriptor |
| Imperator: Rome | `2.0.*` | Declared as `supported_version` in the mod descriptor |
| Victoria 3 (older releases) | Not supported | The mod uses definition-injection keywords that require a compatible content revision |
| Victoria 3 | `1.15.*` | Declared as `supported_game_version` in `.metadata/metadata.json` |
| Other mods that redefine the same countries | Not verified | A later whole-country redefinition replaces the injected colour; the mod with the later file name wins |

## 🛡️ Privacy and Data

Standardised Country Colours does not collect personal data; it consists of local game definitions.

For the detailed description of how the application handles privacy and personal data, see the [Privacy Statement](./PRIVACY.md).

## ⚙️ GitHub Actions

| Workflow | Purpose | What it does |
|----------|---------|--------------|
| [ github-release.yml ](https://github.com/hmlendea/standardised-country-colours/blob/master/.github/workflows/github-release.yml) | Publish the mod package | Runs on a published release or manual dispatch: two parallel jobs (`victoria3` and `imperator`), each checks out the requested tag, builds its edition with `scripts/build.py`, archives the `standardised-country-colours/` folder as `standardised-country-colours_<group>_<version>.zip`, and attaches the archive to the release |
| [ steam-workshop-release.yml ](https://github.com/hmlendea/standardised-country-colours/blob/master/.github/workflows/steam-workshop-release.yml) | Publish the Steam Workshop items | Runs on a `v*.*.*` tag push or manual dispatch: two parallel jobs (`victoria3` and `imperator`), each checks out the requested tag, builds its edition with `scripts/build.py`, and uploads the `out/<group>/standardised-country-colours/` folder to its Workshop item with the `thumbnail.png` preview image and a changenote linking to the GitHub release |
| [ nexus-mods-release.yml ](https://github.com/hmlendea/standardised-country-colours/blob/master/.github/workflows/nexus-mods-release.yml) | Publish the Nexus Mods files | Runs on a `v*.*.*` tag push or manual dispatch: two parallel jobs (`imperator` and `victoria3`), each checks out the requested tag, builds its edition with `scripts/build.py`, archives the `standardised-country-colours/` folder, and uploads it to its Nexus Mods file (`8454045` for Imperator: Rome, `8446233` for Victoria 3) with the tag as its version |

## 🗂️ Project Structure

The build renders the mod folder into `out/<game>/standardised-country-colours/`, so the generated tree mirrors each game's directory layout. The folder is produced by `scripts/build.py` from the shared palette snapshot and the per-game configuration and artwork:

```bash
python3 scripts/build.py --game victoria3 --game imperator --version 1.0.0
```

The mod folder is build output and is not committed. The build is game-agnostic: each game edition under `scripts/games/` declares its own identity, mappings, and output layout, so further editions can be added without touching the shared engine.

### Directories

| Directory | Purpose |
|-----------|---------|
| `standardised-country-colours/` | The mod folder, generated under `out/<game>/`; named identically for every distribution channel |
| `standardised-country-colours/.metadata/` | Launcher metadata and the launcher thumbnail |
| `standardised-country-colours/common/country_definitions/` | The colour overrides for the affected countries |
| `scripts/` | The build: a shared engine plus one module per game edition under `scripts/games/` |
| `src/` | Build inputs: the shared palette snapshot, icon, and preview artwork |
| `vanilla/` | Vendored vanilla game data the build preserves, so it needs no game installation |
| `description/` | The Steam Workshop page description, in BBCode |

## 🏗️ Architecture

Standardised Country Colours is a single-concern definition repository that injects one colour key into each affected vanilla country definition and relies on the game's own load order for precedence.

See the [Architecture Documentation](./ARCHITECTURE.md) for the system context, principal components, runtime processes, ownership boundaries, dependencies, constraints, and extension points.

## 📚 Documentation

Comprehensive documentation is available in the [docs/](./docs/) directory:

| Resource | Description |
|----------|-------------|
| [Documentation Index](./docs/INDEX.md) | Master navigation for the knowledge base |
| [Quick Start](./docs/quick-start.md) | Getting started guide for newcomers |
| [Repository Overview](./docs/repository-overview.md) | Purpose, scope, boundaries, and entry points |
| [Architecture](./docs/architecture.md) | Colour pipeline and precedence layers complementing the root ARCHITECTURE.md |
| [Colour Mappings](./docs/colour-mappings.md) | Every shipped mapping with its vanilla value and source |
| [Components](./docs/components/) | Per-component deep dives |
| [Flows](./docs/flows/) | End-to-end flows, from mod discovery to colour authoring |
| [Behaviour](./docs/behaviour/) | Observed behaviour and map-colour conflicts |
| [Testing](./docs/testing.md) | Verification strategy and coverage gaps |
| [Troubleshooting](./docs/troubleshooting.md) | Common issues and solutions |
| [FAQ](./docs/faq.md) | Frequently asked questions |
| [Change Guide](./docs/change-guide.md) | How to modify common areas safely |
| [Design Decisions](./docs/design-decisions.md) | Key design choices and their rationale |
| [Invariants](./docs/invariants.md) | System-wide invariants and how to verify them |
| [Ambiguities and Open Questions](./docs/ambiguities-and-open-questions.md) | Unresolved items and known gaps |

## 🤝 Contributing

You are welcome to submit any suggestion, feedback, or modification to this project.

When doing so, please:
- Maintain cross-platform compatibility
- Submit focused pull requests that conform to the existing code style
- Maintain your branch synchronised with `master`
- Revise the documentation when functionality changes
- Raise a new [issue](https://github.com/hmlendea/standardised-country-colours/issues) for problems or suggestions

See the [Contributing Guidelines](./CONTRIBUTING.md) for details on how to report issues, suggest enhancements, and submit changes.

## 📜 Code of Conduct

See the [Code of Conduct](./CODE_OF_CONDUCT.md) for the standards of conduct expected in all project spaces.

## 🔗 Related Projects

- [More Cultural Names](https://github.com/hmlendea/more-cultural-names): Mod for various strategy games that dynamically changes province names based on the ruler's culture.
- [Imperator: Rome Latinised English](https://github.com/hmlendea/imperator-latinised-english): Localisation mod for Imperator: Rome that replaces selected vanilla Germanic-origin words with Latin-origin alternatives.

## 🙏 Acknowledgements

- [Crusader Kings II](https://store.steampowered.com/app/203770/) by Paradox Development Studio, for the Crusader Kings II title colours.
- [Civilization IV](https://store.steampowered.com/app/3900/) by Firaxis Games, for the Civilization IV palette entries.
- [Civilization V](https://store.steampowered.com/app/8930/) by Firaxis Games, for the Civilization V palette entries.
- [Civilization VI](https://store.steampowered.com/app/289070/) by Firaxis Games, for the Civilization VI palette entries.
- [Civilization: Beyond Earth](https://store.steampowered.com/app/65980/) by Firaxis Games, for the sponsor colour entries.
- [Total War: Rome](https://store.steampowered.com/app/4760/) by Creative Assembly, for the faction colour entries.
- [Total War: Medieval II](https://store.steampowered.com/app/4780/) by Creative Assembly, for the faction colour entries, including the Kingdoms expansion.
- [Victoria 3](https://store.steampowered.com/app/529340/) by Paradox Development Studio, whose definition format this mod targets.

## 🔒 Security

Standardised Country Colours follows a coordinated disclosure policy for security vulnerabilities.

For information on reporting security vulnerabilities, see the [Security Policy](./SECURITY.md).

## 💬 Support

For support, please [open an issue](https://github.com/hmlendea/standardised-country-colours/issues).

## 💝 Project Engagement

Discovered a problem with Standardised Country Colours or have a suggestion for it? [Open an issue](https://github.com/hmlendea/standardised-country-colours/issues)!

If you find this project useful, consider [funding it](https://hmlendea.go.ro/funding) or starring ⭐️ it on GitHub!

[![Donate](https://raw.githubusercontent.com/hmlendea/readme-assets/master/donate_generic.png)](https://hmlendea.go.ro/funding)

## 📄 License

This project is being distributed under the `GNU General Public License v3.0`.
See [LICENSE](./LICENSE) for additional information.
