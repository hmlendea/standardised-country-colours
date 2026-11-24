# Troubleshooting

## Symptom to cause

| Symptom | Probable cause | Resolution |
|---------|---------------|------------|
| The mod is absent from the launcher | The extracted folder does not contain `.metadata/metadata.json`, or it sits at the wrong depth | Extract so that `<mod dir>/standardised-country-colours/.metadata/metadata.json` exists |
| The mod is listed without artwork | `picture` names a missing file, or the file is not beside `metadata.json` | Confirm `.metadata/thumbnail.png` exists and matches `picture` |
| The launcher marks the mod as outdated | `supported_game_version` does not cover the installed build | Widen the range if the tag set is unchanged |
| No country colour changed at all | The mod is disabled in the playset, or the file has no BOM, or the tag set was overwritten by a mod using `REPLACE:` | Enable the mod; check the BOM; reorder the playset |
| One country's colour did not change | A conditional map-colour block is active, or another mod replaces the tag | Check the country's government and laws; inspect the playset order |
| A subject shows its overlord's colour | The `subject_map_color` game rule allows inheritance | Expected; change the game rule if unacceptable |
| Colours appear wrong only once a war starts | Map-mode tinting, not a content change | Expected |
| A change made locally has no effect | A stale installation was not removed, or the game was not restarted | Delete the folder, reinstall, restart |
| Soldier uniforms differ from the map colour | Unit colours are separate keys the mod does not touch | Expected |
| A flag does not match the map colour | Coats of arms use their own `color1`–`color4` keys | Expected |
| The game reports an injection error for a tag | The tag no longer exists after a game patch | Remove or retarget the entry |
| The game reports an encoding warning naming the file | The file lost its byte-order mark | Rewrite as UTF-8 with BOM |

## Diagnosing "my colour did not apply"

Work in this order.

### 1. Confirm the mod loaded

Launcher: is **Standardised Country Colours** enabled and not flagged outdated?

If not, see the first three symptoms above.

### 2. Confirm the entry is shipped

```bash
grep -c "^INJECT:<TAG> = {" out/vic3/standardised-country-colours/common/country_definitions/sc_country_colours.txt
```

A result of `0` means the country is not mapped. Check [colour-mappings.md](./colour-mappings.md).

### 3. Confirm the tag is correct

```bash
grep -E "^ <TAG>:" "<game>/localization/english/countries_l_english.yml"
```

If the localised name does not match the country you expected, the entry targets the wrong tag.

### 4. Check the log

```bash
grep -n "sc_country_colours" "<user data>/Victoria 3/logs/error.log"
```

A line naming the file means the engine rejected something. A silent result means the entry applied.

### 5. Rule out a conditional colour

```bash
python3 - <<'PY'
import re
GAME = "/path/to/Victoria 3/game"
tag = "GER"
body = re.sub(r"#.*", "", open(GAME + "/common/dynamic_country_map_colors/00_default.txt").read())
for m in re.finditer(r"^([a-z0-9_]+) = \{(.*?)^\}", body, re.M | re.S):
    if f"c:{tag}" in m.group(2):
        c = re.search(r'color = "([a-z0-9_]+)"', m.group(2))
        print(m.group(1), "->", c.group(1) if c else "?")
PY
```

Any output means a conditional block can override the injected colour. That is intended behaviour.

### 6. Rule out another mod

Look for a mod that defines the same tag. A `REPLACE:` beats this mod's `INJECT:` regardless of order; another `INJECT:` of the same key resolves by file name, so this mod should load later.

## Diagnosing "the wrong country changed colour"

The tag and the palette entry name disagree. Cross-check:

```bash
grep -B1 "^INJECT:<TAG> = {" out/vic3/standardised-country-colours/common/country_definitions/sc_country_colours.txt
grep -E "^ <TAG>:" "<game>/localization/english/countries_l_english.yml"
```

The comment name and the localised name should agree. If they do not, the entry is mis-targeted.

## Diagnosing "a colour is unreadable on the map"

Two mapped countries may share a near-identical colour, or a mapped colour may coincide with an unmapped neighbour's vanilla colour. The palette is curated per country and is not deduplicated globally; this is a palette-level concern, not a defect in the file.

Quick check for exact duplicates among mapped values:

```bash
grep -oE "^# .+ - (#[0-9A-F]{6})" out/vic3/standardised-country-colours/common/country_definitions/sc_country_colours.txt \
  | sed 's/.* - //' | sort | uniq -d
```

## Escalation

If the colour is correct in the file, the tag is correct, no log line names the file, and no conditional block matches, the remaining possibility is that the country is a subject and inherits its overlord's colour. Confirm the `subject_map_color` game rule setting.

## Related documents

- [error-handling.md](./error-handling.md) — the failure taxonomy.
- [flows/country-colour-injection.md](./flows/country-colour-injection.md) — the mechanism.
- [behaviour/map-colour-conflicts.md](./behaviour/map-colour-conflicts.md) — intended non-applications.