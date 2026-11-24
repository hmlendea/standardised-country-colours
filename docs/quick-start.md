# Quick start

## Install the mod

The mod is distributed through the Steam Workshop, Nexus Mods, and GitHub Releases. There is no Paradox Mods or package-manager route at version `1.0.0`.

1. Download the archive for your game from the [releases page](https://github.com/hmlendea/standardised-country-colours/releases/latest), for example `standardised-country-colours_vic3_<version>.zip` or `standardised-country-colours_imperator_<version>.zip`.
2. Extract the archive so that `standardised-country-colours/.metadata/metadata.json` exists inside your Victoria 3 or Imperator: Rome mod directory.
3. Add the mod to a playset in the launcher and enable it.

The mod directory is per game edition:

- Victoria 3: GNU/Linux `~/.local/share/Paradox Interactive/Victoria 3/mod/` · macOS `~/Library/Application Support/Paradox Interactive/Victoria 3/mod/` · Windows `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\mod\`
- Imperator: Rome: GNU/Linux `~/.local/share/Paradox Interactive/ImperatorRome/mod/` · macOS `~/Library/Application Support/Paradox Interactive/ImperatorRome/mod/` · Windows `%USERPROFILE%\Documents\Paradox Interactive\ImperatorRome\mod\`

Do not extract into the game installation directory. The games never load mods from `<steam>/steamapps/common/<game>/`.

When replacing an existing installation, delete the previous `standardised-country-colours` directory first, because the game loads every file present in the mod directory and a stale file from an older version continues to apply.

## Verify the installation

1. Open the launcher and confirm **Standardised Country Colours** appears at the edition's version with artwork.
2. Start a campaign and open the map. France should render as a deep navy (`#000099` against vanilla `#1432D2`), and Denmark as a vivid red (`#C8102E` against vanilla `#802019`).
3. Release a country that does not exist at the start, such as Kurdistan, and confirm it appears with the standardised green (`#278E43`) rather than the vanilla value.
4. Read the edition's logs directory and confirm no line names the shipped colour file.

## Use the mod

Enable the mod and play. No configuration exists and no in-game action is required. Each mapped country receives its colour when the engine reads the country definitions, and again whenever the country is released or formed.

## Compare a mapping against vanilla

Open the shipped entry and the vanilla block side by side:

| Shipped | Vanilla |
|---------|---------|
| `out/vic3/standardised-country-colours/common/country_definitions/sc_country_colours.txt` | `<game>/common/country_definitions/00_countries.txt` |

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
2. Add the tag and its palette entry to `COUNTRY_PALETTE_ENTRIES` in `scripts/games/victoria3/config.py`, plus `VANILLA_COUNTRY_NAMES` when the vanilla name differs.
3. Run `python3 scripts/build.py --game victoria3 --version <version>`; the build derives the decimal components, sorts the file, and writes the provenance comment.
4. Run the structural verification in [testing.md](./testing.md).

See [flows/colour-authoring.md](./flows/colour-authoring.md) for the full procedure and [change-guide.md](./change-guide.md) for safety rules.

## Next steps

- Newcomer: [repository-overview.md](./repository-overview.md).
- Contributor: [components/mod-content.md](./components/mod-content.md) and [invariants.md](./invariants.md).
- Looking up a country: [colour-mappings.md](./colour-mappings.md).
- Colour did not change: [troubleshooting.md](./troubleshooting.md).