# Component: mod content

The mod content is the repository's entire product: a single country-definition file carrying 101 injections.

## Location

```text
standardised-country-colours/common/country_definitions/sc_country_colours.txt
```

## File shape

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

# Byzantium (palette: Eastern Roman Empire) - #460076 - Civilization 5 (Rome)
INJECT:BYZ = {
	color = { 70 0 118 }
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
| Entries | 101 |
| Distinct tags | 101 |
| Comment lines matching the provenance pattern | 101 |
| Entries with a palette-name suffix | 17 |
| Entries whose colour equals vanilla exactly | 1 (`SCA`) |
| Entries within 8 of a component of vanilla | 2 (`SCA`, `APC`) |
| Entries that change the colour's syntax | 5 (`BRZ`, `CAS`, `DEN`, `NET`, `SPA`) |

## Tags sharing one palette entry

Two palette entries map to more than one tag:

| Palette entry | Tags | Reason |
|---------------|------|--------|
| India | `BHT`, `HND` | `BHT` is the formable Indian unification target; `HND` is a release-only unrecognised Indian tag. Both carry the same vanilla localised name, "India". |
| Romania | `ROM`, `WAL` | `ROM` is the formable Romanian state; `WAL` is Wallachia, which exists at the start under the same flag colours. |

The palette itself lists Wallachia as an alias of Romania. The mod colours both so that a pre-unification campaign and a unified campaign look consistent.

## Colour derivation

Every value is an exact decimal expansion of the palette hexadecimal triple, with no gamma adjustment, no lightening for map legibility, and no collision avoidance. `#000099` becomes `{ 0 0 153 }`.

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
| Change a `color` triple | That country's map colour changes | Keep the comment hexadecimal in step |
| Change a tag | The old tag reverts to vanilla; the new tag takes the colour | Confirm the new tag exists |
| Add an entry | One more country recoloured | Alphabetical position, provenance comment, range check |
| Remove an entry | That country reverts to vanilla | Confirm it was the intent, not a merge accident |
| Change the keyword to `REPLACE:` | The whole vanilla block is discarded | Never do this |
| Rename the file | Harmless if unique; breaks no contract | Keep it unique in the folder |
| Reorder entries | Harmless | Preserve alphabetical order for reviewability |

## Related documents

- [flows/country-colour-injection.md](../flows/country-colour-injection.md) — what the engine does with the file.
- [colour-mappings.md](../colour-mappings.md) — the values themselves.
- [launcher-metadata.md](./launcher-metadata.md) — the sibling component.