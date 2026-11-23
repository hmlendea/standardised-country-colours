# Documentation index

Master navigation for the Standardised Country Colours Victoria 3 edition repository knowledge base. It catalogues every document under `docs/`, the root policy documents, and the recommended reading order for each audience.

## Repository summary

Standardised Country Colours is a cross-game project that assigns consistent, historically inspired map colours to selectable countries in various grand strategy games; this repository is the Victoria 3 edition. It is a content-only mod that ships a single country-definition file under `standardised-country-colours/common/country_definitions/` that injects one `color` key into 89 vanilla country definitions, giving each mapped country a standardised map colour drawn from the palette shared across the project's editions. Every other field of an affected country definition — tier, country type, cultures, capital, religion, regnal numbers, subject cantons — is left to the base game because the mod uses the `INJECT:` definition-entry mode rather than restating the block.

The repository owns no runtime, no build step, and no executable code. Every observable effect is produced by the Victoria 3 engine reading the file.

Current state, verified against the installed game (`1.15.2`, launcher label `Ivan-Chai`) and vanilla content revision:

| Metric | Value |
|--------|-------|
| Mapped country tags | 89 |
| Content files | 1 (`sc_country_colours.txt`, 455 lines) |
| Tags defined by vanilla | 835 |
| Mapped tags present at the 1836 start | 40 |
| Mapped tags that are formation targets | 32 |
| Mapped tags that are both | 10 |
| Mapped tags that are neither (release-only in practice) | 27 |
| Mapped tags also referenced by a conditional map-colour block | 26 |
| Exact no-op mappings | 1 (`SCA`) |
| Declared game version | `1.15.*` |
| Declared mod version | `1.0.0` |

## Root document map

| Document | Purpose |
|----------|---------|
| [README.md](../README.md) | Project overview, capabilities, installation, and usage |
| [ARCHITECTURE.md](../ARCHITECTURE.md) | System context, architectural areas, runtime flow, and constraints |
| [SECURITY.md](../SECURITY.md) | Security policy and vulnerability reporting |
| [PRIVACY.md](../PRIVACY.md) | Privacy statement |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Contribution guidelines |
| [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) | Standards of conduct |
| [LICENSE](../LICENSE) | GNU General Public License v3.0 |

The `docs/` tree complements these documents rather than duplicating them. Where a root document already states architecture or policy, the corresponding `docs/` file elaborates and links back.

There is no `api-reference/` directory because the repository exposes no HTTP, RPC, or command interface. The public contract surface is the definition file format and the launcher metadata, both documented under [components/](./components/) and [data-model.md](./data-model.md).

## Documentation catalogue

### Orientation

| Document | Description |
|----------|-------------|
| [quick-start.md](./quick-start.md) | Fastest path to installing, verifying, and modifying the mod |
| [repository-overview.md](./repository-overview.md) | Purpose, scope, boundaries, and entry points |
| [repository-structure.md](./repository-structure.md) | Repository tree and file inventory |

### Architecture and design

| Document | Description |
|----------|-------------|
| [architecture.md](./architecture.md) | Decomposition, colour pipeline, and precedence layers |
| [design-decisions.md](./design-decisions.md) | Why injection, why one file, why a single colour |
| [invariants.md](./invariants.md) | System-wide invariants with their verification |
| [dependencies.md](./dependencies.md) | Game, palette, and tooling dependencies |

### Components

| Document | Description |
|----------|-------------|
| [components/mod-content.md](./components/mod-content.md) | The colour override file and its 89 entries |
| [components/launcher-metadata.md](./components/launcher-metadata.md) | `metadata.json` and the two thumbnails |
| [components/repository-metadata.md](./components/repository-metadata.md) | Documentation, licence, ignore rules, funding |
| [components/packaging-and-distribution.md](./components/packaging-and-distribution.md) | Release workflows, the published archive, and the Workshop and Nexus Mods items |

### Behaviour and flows

| Document | Description |
|----------|-------------|
| [behaviour/country-colour-override.md](./behaviour/country-colour-override.md) | What a player observes when the mod is enabled |
| [behaviour/map-colour-conflicts.md](./behaviour/map-colour-conflicts.md) | How other mods and conditional colours interact |
| [flows/mod-discovery-and-load.md](./flows/mod-discovery-and-load.md) | Launcher discovery through to composed definitions |
| [flows/country-colour-injection.md](./flows/country-colour-injection.md) | The injection pass in detail |
| [flows/colour-authoring.md](./flows/colour-authoring.md) | Authoring and verifying a new mapping |

### Reference

| Document | Description |
|----------|-------------|
| [data-model.md](./data-model.md) | Tags, colour entries, palette rows, and their relationships |
| [configuration.md](./configuration.md) | Metadata fields and their effect |
| [integrations.md](./integrations.md) | Engine, launcher, Steam, and GitHub integration points |
| [logging.md](./logging.md) | Log surfaces and what the engine writes there |
| [error-handling.md](./error-handling.md) | Failure modes and their visibility |
| [security.md](./security.md) | Trust boundary and content-integrity concerns |
| [state-and-persistence.md](./state-and-persistence.md) | Why the repository owns no state |
| [localisation.md](./localisation.md) | Language coverage of the shipped content |
| [colour-mappings.md](./colour-mappings.md) | Full table of all 89 mappings with vanilla values |

### Operations and maintenance

| Document | Description |
|----------|-------------|
| [build-and-deployment.md](./build-and-deployment.md) | Archiving, release, and publication |
| [testing.md](./testing.md) | Verification strategy and coverage gaps |
| [change-guide.md](./change-guide.md) | Safe modification procedures |
| [troubleshooting.md](./troubleshooting.md) | Recurring problems and resolutions |
| [faq.md](./faq.md) | Frequently asked questions |
| [documentation-maintenance.md](./documentation-maintenance.md) | Keeping this tree current |
| [ambiguities-and-open-questions.md](./ambiguities-and-open-questions.md) | Unresolved items and known gaps |

## Navigation aids

### Start here

Newcomer who wants to install and play: [quick-start.md](./quick-start.md), then [repository-overview.md](./repository-overview.md).

### Deep dive

Contributor who wants to change a country colour: [flows/colour-authoring.md](./flows/colour-authoring.md), [components/mod-content.md](./components/mod-content.md), [invariants.md](./invariants.md), and [change-guide.md](./change-guide.md).

### Flows

Maintainer diagnosing why a colour did or did not change: [flows/country-colour-injection.md](./flows/country-colour-injection.md), [behaviour/map-colour-conflicts.md](./behaviour/map-colour-conflicts.md), then [troubleshooting.md](./troubleshooting.md).

### Reference lookup

Looking up a specific country: [colour-mappings.md](./colour-mappings.md).

## Maintenance metadata

| Field | Value |
|-------|-------|
| Last reviewed | 2026-11-23 |
| Owner | Repository maintainer |
| Coverage status | Complete for the shipped content surface |
| Source revision | `5b5655d` |
| Evidence base | Installed Victoria 3 `1.15.2`; palette `COUNTRY_COLOURS.md` as of 2026-11-23 |