# Configuration

The mod has no user configuration. Nothing can be toggled in game, and no settings file is read.

## Effective configuration

The only configurable surface is the launcher metadata, which is repository-authoritative rather than user-editable.

| Area | Source | Controls | Secret policy |
|------|--------|----------|---------------|
| Identity | `.metadata/metadata.json` `name`, `id`, `version` | How the launcher lists the mod | None |
| Compatibility | `.metadata/metadata.json` `supported_game_version` | Whether the launcher treats the mod as current | None |
| Artwork | `.metadata/metadata.json` `picture` plus `.metadata/thumbnail.png` | Launcher presentation | None |
| Synchronisation | `.metadata/metadata.json` `game_custom_data.multiplayer_synchronized` | Whether every client must run the mod | None |
| Enablement | Launcher playset | Whether the mod loads and in what order | Owned by the user |
| Content | `sc_country_colours.txt` | The shipped colours | None |

## What a user can change

| Action | Effect |
|--------|--------|
| Enable or disable the mod | Adds or removes every colour change at once |
| Move the mod within the playset | Changes precedence against another mod using the same mode |
| Edit the shipped file | Changes colours, at the cost of no longer matching a release |

There is no per-country toggle. A user who wants a subset should copy the file and delete entries.

## Load order as implicit configuration

Order does not affect the mod's own injections, because the injection pass runs after all plain definitions. Order matters only when another mod also touches the same tag:

| Other mod's mode | Effect of the order |
|------------------|---------------------|
| `INJECT:` | Later file name wins on the same key |
| `REPLACE:` | The other mod wins regardless of order |
| Plain definition | The mod's injection wins regardless of order |

## Environment variables

None.

## Network ports

None. The mod binds and listens on nothing.

## Validation

No command validates configuration. The equivalent checks are the structural audit in [testing.md](./testing.md) and the launcher's own listing.

## Related documents

- [components/launcher-metadata.md](./components/launcher-metadata.md) — the field reference.
- [flows/mod-discovery-and-load.md](./flows/mod-discovery-and-load.md) — how the metadata is consumed.