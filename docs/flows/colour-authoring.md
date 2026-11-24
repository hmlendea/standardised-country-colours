# Flow: colour authoring

How a maintainer adds or changes a mapping, and what must be true before the change ships.

## Procedure

### 1. Choose the palette entry

Open the external palette and locate the title. Note four facts:

| Fact | Example |
|------|---------|
| Palette entry name | `Czechia` |
| Alias, if the palette supplies one | `Bohemia` |
| Primary colour | `#00AB93` |
| Source attribution | `Age of Empires II HD (Teal)` |

Use the primary colour of the palette's **Principal Colours** table. That table holds one authoritative value per country; the **Alternative Colours** table records values from other games and is not the shipped source. When a country appears in both, the Principal row wins. The secondary colour, and every alternative, has no destination in the game's country model.

### 2. Resolve the tag

Search the installed definitions for the country:

```bash
grep -rA2 '^[A-Z0-9]\{3\} = {' "<game>/common/country_definitions/" \
  | grep -i 'bohemia\|czech'
```

Then confirm the localised name, which is the authoritative label:

```bash
grep -E '^ (BOH|CZE):' "<game>/localization/english/countries_l_english.yml"
```

Prefer the tag whose localised name matches the palette entry most closely. A tag sharing the name of a formable unification target is usually the right choice for a canonical state; a nearby minor tag carrying the same localised name is a release-only entity and should only be added when the palette clearly intends it.

### 3. Register the mapping

Add the tag and its palette entry to `COUNTRY_PALETTE_ENTRIES` in `scripts/games/victoria3/config.py`:

```python
'BOH': 'Czechia',
```

When the vanilla localised name differs from the palette entry name, also add the tag to `VANILLA_COUNTRY_NAMES`:

```python
'BOH': 'Bohemia',
```

No colour value is typed anywhere: the build reads the palette snapshot and derives the decimal triple.

### 4. Confirm the palette snapshot

The palette entry must exist in `src/colours.md` under Principal Colours, with its source attribution and primary colour. A missing entry fails the build rather than shipping a wrong value.

### 5. Build the entry

```bash
python3 scripts/build.py --version 1.0.0
```

The build writes the commented block, keeping the file alphabetical by tag and the encoding UTF-8 with a byte-order mark:

```text
# Bohemia (palette: Czechia) - #00AB93 - Age of Empires II HD (Teal)
INJECT:BOH = {
	color = { 0 171 147 }
}
```

Rules the build enforces:

- The comment name is the vanilla localised name.
- ` (palette: <entry>)` is appended exactly when the palette entry name differs from the vanilla name.
- The hexadecimal value is the palette's principal colour and always matches the decimal triple.
- The source is the palette attribution, with runs of spaces collapsed.

### 6. Verify

Run the build and confirm `<output>/vic3/standardised-country-colours/` matches the committed folder, then run the structural checks in [testing.md](../testing.md). At minimum:

```bash
python3 - <<'PY'
import re
p = "standardised-country-colours/common/country_definitions/sc_country_colours.txt"
raw = open(p, "rb").read()
assert raw[:3] == b"\xef\xbb\xbf", "missing BOM"
t = raw.decode("utf-8-sig")
assert t.count("{") == t.count("}"), "unbalanced braces"
inj = re.findall(r"INJECT:([A-Z0-9]{3}) = \{\n\tcolor = \{ (\d+) (\d+) (\d+) \}\n\}", t)
assert inj, "no injections parsed"
tags = [i[0] for i in inj]
assert len(tags) == len(set(tags)), "duplicate tag"
assert tags == sorted(tags), "out of order"
assert all(0 <= int(v) <= 255 for i in inj for v in i[1:]), "component out of range"
print("ok", len(inj))
PY
```

### 7. Verify in game

Enable the mod, start or load a campaign, and inspect the country. For a country that exists at the start, the map shows it immediately. For a formable or releasable country, either form or release it, or use debug mode to spawn it.

### 8. Check the log

```text
<user data>/Victoria 3/logs/error.log
```

No line should name `sc_country_colours.txt`.

## Decision points

| Situation | Action |
|-----------|--------|
| The palette entry has no corresponding tag | Skip it. Record it under [ambiguities-and-open-questions.md](../ambiguities-and-open-questions.md) if it looks mappable. |
| The country appears in both palette tables | Use the Principal Colours row. Alternative rows are reference material, not shipped values. |
| Two tags carry the same localised name | Colour both if the palette clearly intends the concept; otherwise colour the canonical one and note the omission. |
| The palette value matches vanilla exactly | Still ship it, with the comment, so the mapping's provenance is recorded. |
| The palette value is within a few units of vanilla | Ship it. The value is authoritative even when visually identical. |
| The country has a conditional map-colour block | Ship the mapping anyway. The conditional colour is intentional behaviour. |
| The country's vanilla value uses `hsv` or `hsv360` | Ship a plain RGB block. The injected key replaces the value. |

## Anti-patterns

| Anti-pattern | Why it fails |
|--------------|--------------|
| `REPLACE:<tag> = { color = ... }` | Discards tier, cultures, capital, and regnal numbers |
| `INJECT:<tag> = { color = ... }` with the wrong tag | Colours an unrelated country |
| Omitting the byte-order mark | The engine may not read the file |
| Adding a second definition file | Splits the shipped set and risks two injections of one tag |
| Editing a value without the comment | Loses the provenance the comment exists to preserve |
| Naming the file after a vanilla file | Replaces that vanilla file entirely |

## Related documents

- [change-guide.md](../change-guide.md) — the broader modification workflow.
- [invariants.md](../invariants.md) — the properties these steps defend.
- [colour-mappings.md](../colour-mappings.md) — the current set.