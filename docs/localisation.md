# Localisation

## The mod ships no localisation

A country colour is a number, not a string. The mod therefore adds no `localization/` directory, no `_l_<language>.yml` file, and no translation keys.

## What this means for users

| Question | Answer |
|----------|--------|
| Does the mod need a language pack? | No |
| Does the mod work with a non-English game language? | Yes; the colour applies regardless of the display language |
| Could the mod be localised? | Not meaningfully; it introduces no user-visible text |
| Do the file comments need translation? | No; the engine ignores comment lines and no player reads them |

## Language coverage

| Language | Locale | Status |
|----------|--------|--------|
| All game languages | n/a | Unaffected; the mod introduces no text |

## Country names in the file comments

The comments record the vanilla English localised name of each country, taken from `localization/english/countries_l_english.yml`. They are documentation, not localisation:

- the engine does not read them;
- a player never sees them;
- they exist so a reviewer can tell which country a tag denotes without opening the game.

Where the palette entry name differs from the vanilla name, the comment carries both, for example `# Cambodia (palette: Khmer)`.

## Consequences for contributors

A contributor who localises a mod generally adds `localization/<language>/<file>_l_<language>.yml`. That pattern does not apply here. The equivalent contribution is a change to a country's colour, documented in [flows/colour-authoring.md](./flows/colour-authoring.md).

## Related documents

- [components/mod-content.md](./components/mod-content.md) — the shipped content.
- [colour-mappings.md](./colour-mappings.md) — the names and their sources.