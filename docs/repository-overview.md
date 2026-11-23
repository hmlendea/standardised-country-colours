# Repository overview

## Purpose

Assign one standardised map colour to each of 89 Victoria 3 countries, so that the world map is legible and historically suggestive rather than a patchwork of near-identical hues.

## Scope

The repository owns exactly three things:

1. one country-definition file that injects a `color` key into 89 vanilla country blocks;
2. the launcher metadata that makes the folder a discoverable mod;
3. documentation, licence, and the release workflow that packages the folder.

## What the mod changes

| Changed | Detail |
|---------|--------|
| Country map colour | The `color` key of 89 country definitions |
| Nothing else | Tier, country type, cultures, capital, religion, regnal numbers, unit colours, flag definitions, coat of arms |

## What the mod deliberately does not change

| Surface | Why |
|---------|-----|
| Unit colours | `primary_unit_color`, `secondary_unit_color`, and `tertiary_unit_color` are separate keys, present on only 7 vanilla tags |
| Flags and coats of arms | `common/coat_of_arms` draws from its own `color1`–`color4` keys resolved against `common/named_colors` |
| Secondary palette colour | Victoria 3 stores a single map colour per country; the palette's second column cannot be represented |
| Conditional map colours | `common/dynamic_country_map_colors/00_default.txt` overrides the definition colour at runtime when its triggers match |
| Subject colouring | Governed by the `subject_map_color` game rule |
| Countries outside the 89 | Out of palette scope or not modelled by the game |

## Boundaries

- **Host boundary.** The mod is inert without Victoria 3. Nothing runs, schedules, or listens.
- **Trust boundary.** The shipped text is parsed by the game within the same trust domain as vanilla content. No network, credentials, or executables exist in the repository.
- **Version boundary.** `supported_game_version` is `1.15.*`. A tag retired by a future patch must be removed in the same release.
- **Palette boundary.** Colours come from an external curated palette. The repository records the value and its source but does not derive it from game data.

## Entry points

| Entry point | Consumer | Documented in |
|-------------|----------|---------------|
| `.metadata/metadata.json` | Paradox launcher | [components/launcher-metadata.md](./components/launcher-metadata.md) |
| `common/country_definitions/sc_country_colours.txt` | Victoria 3 engine | [components/mod-content.md](./components/mod-content.md) |
| `.github/workflows/github-release.yml` | GitHub Actions | [components/packaging-and-distribution.md](./components/packaging-and-distribution.md) |

## Lifecycle position

The mod has no lifecycle of its own. Its content is read at engine start-up and re-evaluated when a country is released or formed. See [state-and-persistence.md](./state-and-persistence.md).

## Success criteria

The mod is functioning correctly when, in a running game:

- the mapped countries show the documented colours;
- no `error.log` line names the shipped file or one of its tags;
- countries released or formed during play show their standardised colour.

## Related documents

- [repository-structure.md](./repository-structure.md) — the tree itself.
- [architecture.md](./architecture.md) — how the pieces relate.
- [colour-mappings.md](./colour-mappings.md) — the shipped set.