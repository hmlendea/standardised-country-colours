# Component: launcher metadata

## Location

```text
standardised-country-colours/.metadata/metadata.json
standardised-country-colours/.metadata/thumbnail.png
```

## Current values

```json
{
  "name": "Standardised Country Colours",
  "id": "com.github.hmlendea.vic3-standardised-country-colours",
  "version": "1.0.0",
  "game_id": "victoria3",
  "picture": "thumbnail.png",
  "supported_game_version": "1.15.*",
  "short_description": "Standardised map colours for selectable countries",
  "tags": ["Map", "Historical"],
  "relationships": [],
  "game_custom_data": {
    "multiplayer_synchronized": true
  }
}
```

## Field effects

| Field | Effect | Change policy |
|-------|--------|---------------|
| `name` | Launcher display name and, by default, the Workshop title | May change; it is user-visible branding |
| `id` | Stable identity used by updates and relationships | **Never** change; a new id orphans every published reference |
| `version` | Launcher version label | Bump with every release |
| `game_id` | Tells the launcher which game the folder belongs to | Fixed at `victoria3` |
| `picture` | Names the launcher thumbnail file beside the JSON | Must match an existing file in the same directory |
| `supported_game_version` | Range the launcher considers compatible | Review on every game patch |
| `short_description` | Launcher subtitle | May change |
| `tags` | Local categories | Re-specified at upload; must not exceed five. Currently `Map` and `Historical` |
| `relationships` | Load-order and conflict declarations | Empty; no ordering requirement exists |
| `game_custom_data.multiplayer_synchronized` | Whether every client must run the mod | `true`, because colours are visible content |

## Absence consequences

| Missing or malformed | Result |
|----------------------|--------|
| The whole `.metadata` folder | The launcher does not list the mod |
| `metadata.json`, invalid JSON | The launcher does not list the mod |
| `game_id` | The folder may not be associated with Victoria 3 |
| `picture` file | The mod is listed without artwork |
| `supported_game_version` matching the installed build | The launcher marks the mod as outdated |

Note the contrast with Imperator: Rome, Stellaris, CK3, and EU5, which require an outer `.mod` descriptor as well. Victoria 3 identifies a mod solely by `.metadata/metadata.json`.

## Thumbnails

Victoria 3 reads two unrelated images.

| Purpose | Path | Size | Read by |
|---------|------|------|---------|
| Launcher artwork | `.metadata/thumbnail.png` | 600x333 | Launcher, via the `picture` key |
| Workshop artwork | `thumbnail.png` at the mod folder root | 512x512 | Steam, on upload only |

Both are RGB PNGs. Neither is referenced by the other, and the engine never reads the 512x512 file.

The current artwork was generated from an SVG composition: a dark gradient background, the mod name in a serif face, the subtitle "for Victoria 3" in gold, and a strip of eleven palette swatches. Regenerating requires `rsvg-convert`; the SVG source is not committed.

## Boundaries

- `.metadata/` must sit at the mod folder root, beside `common/`. A deeper or shallower placement makes the mod invisible.
- `metadata.json` must be valid JSON. The wiki's illustrative sample contains comments; real files cannot.
- The `picture` file name is a filename, not a path, and is resolved relative to `.metadata/`.

## Related documents

- [components/mod-content.md](./mod-content.md) — the content this metadata makes loadable.
- [configuration.md](../configuration.md) — the field reference in context.
- [integrations.md](../integrations.md) — the launcher as an integration point.