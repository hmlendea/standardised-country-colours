# Quick start

## Install the mod

The mod is distributed through GitHub Releases only. There is no Steam Workshop, Paradox Mods, Nexus Mods, or package-manager route at version `1.0.0`.

1. Download `standardised-country-colours_<version>.zip` from the [releases page](https://github.com/hmlendea/vic3-standardised-country-colours/releases/latest).
2. Extract the archive so that `standardised-country-colours/.metadata/metadata.json` exists inside your Victoria 3 mod directory.
3. Add the mod to a playset in the Victoria 3 launcher and enable it.

The mod directory is:

- GNU/Linux: `~/.local/share/Paradox Interactive/Victoria 3/mod/`
- macOS: `~/Library/Application Support/Paradox Interactive/Victoria 3/mod/`
- Windows: `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\mod\`

Do not extract into the game installation directory. Victoria 3 never loads mods from `<steam>/steamapps/common/Victoria 3/`.

When replacing an existing installation, delete the previous `standardised-country-colours` directory first, because the game loads every file present in the mod directory and a stale file from an older version continues to apply.

## Verify the installation

1. Open the launcher and confirm **Standardised Country Colours** appears at version `1.0.0` with artwork.
2. Start a campaign and open the map. France should render as a deep navy (`#000099` against vanilla `#1432D2`), and Denmark as a vivid red (`#C8102E` against vanilla `#801219`).
3. Release a country that does not exist at the start, such as Babylon, and confirm it appears with the standardised brown (`#2B5162`) rather than the vanilla value.
4. Read `<user data>/Victoria 3/logs/error.log` and confirm no line names `sc_country_colours.txt`.

## Use the mod

Enable the mod and play. No configuration exists and no in-game action is required. Each mapped country receives its colour when the engine reads the country definitions, and again whenever the country is released or formed.

## Compare a mapping against vanilla

Open the shipped entry and the vanilla block side by side:

| Shipped | Vanilla |
|---------|---------|
| `standardised-country-colours/common/country_definitions/sc_country_colours.txt` | `<game>/common/country_definitions/00_countries.txt` |

The shipped entry is three lines plus a provenance comment:

```text
# France - #000099 - Official flag (Capet)
INJECT:FRA = {
	color = { 0 0 153 }
}
```

The vanilla block carries the tier, cultures, capital, and regnal numbers that the injection leaves intact.

## Author a mapping

1. Identify the vanilla three-letter tag in `<game>/common/country_definitions/`.
2. Convert the palette hexadecimal value to three decimal components.
3. Insert a commented `INJECT:<tag>` block, keeping the file alphabetical.
4. Run the structural verification in [testing.md](./testing.md).

See [flows/colour-authoring.md](./flows/colour-authoring.md) for the full procedure and [change-guide.md](./change-guide.md) for safety rules.

## Next steps

- Newcomer: [repository-overview.md](./repository-overview.md).
- Contributor: [components/mod-content.md](./components/mod-content.md) and [invariants.md](./invariants.md).
- Looking up a country: [colour-mappings.md](./colour-mappings.md).
- Colour did not change: [troubleshooting.md](./troubleshooting.md).