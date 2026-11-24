# Component: mod content

The mod content is the build's entire product: a single country-definition file per game carrying 131 injections.

## Location

```text
standardised-country-colours/common/country_definitions/sc_country_colours.txt
```

This path is inside the built folder (`out/<game>/standardised-country-colours/`). The file is rendered by the edition of `scripts/build.py` and is never committed; its inputs are `src/colours.md` and `scripts/games/<game>/config.py`.

## File shape (Victoria 3)

```text
# Standardised Country Colours
#
# Overrides the map colour of selected countries with the standardised values
# documented in COUNTRY_COLOURS.md. Only the color key is injected, so every
# other field of the vanilla country definition is left untouched.
#
# Each comment records the vanilla country name, the hexadecimal palette colour,
# and the palette source. Where the palette entry name differs from the vanilla
# name, the palette name is appended in parentheses. Victoria 3 exposes a single
# map colour per country, so only the primary palette colour is applied.

# France - #000099 - Official flag (Capet)
INJECT:FRA = {
	color = { 0 0 153 }
}
```

## File shape (Imperator: Rome)

```text
# Standardised Country Colours
#
# Overrides the map colour of selected countries with the standardised values
# documented in COUNTRY_COLOURS.md. Only the color key is injected, so every
# other field of the vanilla country definition is left untouched.
#
# Each comment records the vanilla country name, the hexadecimal palette colour,
# and the palette source. Where the palette entry name differs from the vanilla
# name, the palette name is appended in parentheses. Imperator: Rome exposes a
# single map colour per country, so only the primary palette colour is applied.

# Rome - #8B0000 - Official flag (Roman)
INJECT:ROM = {
	color = { 139 0 0 }
}
```

| Part | Meaning | Mutability |
|------|---------|-----------|
| Header block | States what the file does and how to read a comment | Free to reword |
| `# <name>` | The vanilla localised name of the country | Must track vanilla localisation |
| `(palette: <entry>)` | The palette row name, present only when it differs from the vanilla name | Informational |
| `#<HEX>` | The palette's primary colour | Must equal the decimal triple |
| `<source>` | The palette's attribution | Informational |
| `INJECT:<TAG>` | Three-letter tag, the block key | Must exist in vanilla |
| `color = { R G B }` | Decimal red, green, blue, 0–255 | Range-checked |

## Entry census

| Property | Value |
|----------|-------|
| Entries | 131 |
| Distinct tags | 131 |
| Comment lines matching the provenance pattern | 131 |
| Entries with a palette-name suffix | 19 |
| Entries whose colour equals vanilla exactly | 1 (`SCA`) |
| Entries within 8 of a component of vanilla | 3 (`APC`, `BAH`, `SCA`) |
| Entries that change the colour's syntax | 7 (`BAH`, `BRZ`, `CAS`, `CEY`, `DEN`, `NET`, `SPA`) |

## Tags sharing one palette entry

Two palette entries map to more than one tag:

| Palette entry | Tags | Reason |
|---------------|------|--------|
| India | `BHT`, `HND` | `BHT` is the formable Indian unification target; `HND` is a release-only unrecognised Indian tag. Both carry the same vanilla localised name, "India". |
| Romania | `ROM`, `WAL` | `ROM` is the formable Romanian state; `WAL` is Wallachia, which exists at the start under the same flag colours. |

The palette itself lists Wallachia as an alias of Romania. The mod colours both so that a pre-unification campaign and a unified campaign look consistent.

## Colour derivation

Every value is an exact decimal expansion of the palette hexadecimal triple, with no gamma adjustment, no lightening for map legibility, and no collision avoidance. `#000099` becomes `{ 0 0 153 }`. The Victoria 3 renderer derives the expansion from the `src/colours.md` snapshot, so the triple, the hexadecimal in the comment, and the source attribution always agree.

## Boundaries

- The folder must stay `common/country_definitions/`. An extra `game/` level, a missing `common/`, or a misspelled folder is never read.
- The file name must not match a vanilla file name in the same folder.
- The file must remain UTF-8 with a byte-order mark.
- No second definition file should be added to this folder.

## Dependants

| Dependant | Relationship |
|-----------|--------------|
| Victoria 3 engine | Reads the file and runs the injection pass |
| Release workflow | Archives the enclosing mod folder |
| [colour-mappings.md](../colour-mappings.md) | Documents every entry |
| [ARCHITECTURE.md](../../ARCHITECTURE.md) | Describes the file's role |

## Modification impact

| Edit | Effect | Guards |
|------|--------|--------|
| Change a palette value | That country's map colour changes | Change `src/colours.md` and rebuild |
| Change a tag | The old tag reverts to vanilla; the new tag takes the colour | Change `scripts/games/victoria3/config.py`; confirm the new tag exists |
| Add an entry | One more country recoloured | Add to `scripts/games/victoria3/config.py`; confirm the palette entry exists |
| Remove an entry | That country reverts to vanilla | Confirm it was the intent, not a merge accident |
| Change the keyword to `REPLACE:` | The whole vanilla block is discarded | Never do this |
| Rename the file | Harmless if unique; breaks no contract | Keep it unique in the folder |
| Edit the built file directly | The change is lost on the next build | Edit the inputs instead |

The build always writes the file alphabetically by tag with the provenance comment and range-checked components, so those properties hold without manual care.

## Related documents

- [flows/country-colour-injection.md](../flows/country-colour-injection.md) — what the engine does with the file.
- [colour-mappings.md](../colour-mappings.md) — the values themselves.
- [launcher-metadata.md](./launcher-metadata.md) — the sibling component.