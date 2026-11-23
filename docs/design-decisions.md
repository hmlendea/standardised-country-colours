# Design decisions

## D1. Inject one key instead of restating the block

**Decision.** Every entry is `INJECT:<tag> = { color = { R G B } }`.

**Rationale.** A plain redefinition would replace the whole country block; a `REPLACE:` would do the same but explicitly. Either form pins tier, country type, cultures, capital, religion, regnal numbers, and subject cantons to the values the author typed. When the game changes one of those fields, the restated block keeps the stale value and the mod silently diverges from vanilla.

Injection appends the `color` key to the vanilla block, so every unmentioned key stays whatever the game says it is. The mod's footprint is one key per tag.

**Consequence.** The mod cannot delete or rename a vanilla key. It also cannot change a key that appears more than once in a vanilla block, though no vanilla country block does so for `color`. An injection into a non-existent tag errors and is skipped rather than silently creating a country.

**Evidence.** Victoria 3 exposes `INJECT` as one of six definition-entry modes over an enumerated set of folders that includes `common/country_definitions`. The vanilla content uses no injection keyword itself, so the mode is a modification surface only; first-party content never needs it.

## D2. One file, not one file per country or per region

**Decision.** All 89 injections live in `sc_country_colours.txt`.

**Rationale.** A single file makes the complete change set readable at once, keeps alphabetical ordering meaningful across the whole set, and removes any opportunity for two files in the folder to inject the same tag.

**Consequence.** A merge conflict touches one file. Reviewing a diff shows the whole palette change together.

## D3. Name the file so it cannot collide

**Decision.** `sc_country_colours.txt` rather than a copy of a vanilla file name.

**Rationale.** A file at the same relative path and name as a vanilla file replaces it entirely. Five vanilla files exist in that folder; naming the mod's file after any of them would delete the other four definitions.

**Consequence.** Load order relative to vanilla files is irrelevant, because the injection pass runs after all plain definitions regardless of name.

## D4. Ship one colour per country

**Decision.** Only the palette's primary colour reaches the map.

**Rationale.** Victoria 3 stores a single `color` per country definition. There is no second map colour to assign, and the country list swatch, the map fill, and the colour shown in diplomacy all read the same key.

**Consequence.** The palette's secondary column is recorded in the documentation but cannot be applied. Unit colours are separate keys and are deliberately untouched.

## D5. Record provenance as a comment, not as metadata

**Decision.** Each block is preceded by `# <name> - <#HEX> - <source>`.

**Rationale.** There is no side-car data file and no generated index; the comment is the record. A reviewer can see why a value differs from vanilla without consulting an external artefact, and the game ignores comment lines.

**Consequence.** The comment must be maintained by hand alongside the value. It also makes the file longer, which is accepted as a readability gain. A discrepancy between the comment and the value is a review defect, not a runtime failure.

## D6. Plain RGB decimal components

**Decision.** Always `color = { R G B }` with integers 0–255.

**Rationale.** It is the form vanilla uses most often, it is the easiest to compare against a hexadecimal palette value by inspection, and it avoids floating-point rounding differences between an `hsv` authoring value and the rendered result.

**Consequence.** The four mapped tags whose vanilla value is `hsv` or `hsv360` change syntax. The injected key replaces the vanilla key, so no duplicate exists.

## D7. Partial coverage is intentional

**Decision.** 89 tags are mapped out of 835 vanilla definitions.

**Rationale.** The palette covers titles the game does not model — Crusader Kings II duchies, Total War factions, Civilization city-states — and some titles the game models under a tag whose vanilla name does not match the palette name closely enough to map mechanically. Mapping the wrong tag would be worse than leaving it unmapped, because a mis-coloured major power is immediately visible and hard to explain.

**Consequence.** Most countries keep their vanilla colour. A player sees the effect concentrated on the 40 mapped tags that exist at the 1836 start.

## D8. Declare multiplayer synchronisation

**Decision.** `game_custom_data.multiplayer_synchronized` is `true`.

**Rationale.** A colour difference is visible to every player and is derived from mod content. Two clients with different mod sets would draw different maps.

**Consequence.** The launcher will not join a session whose participants do not share the mod.

## D9. No build step

**Decision.** The release workflow archives the checked-out folder directly.

**Rationale.** There is nothing to generate. A staging directory, a compile step, or a generator script would add a failure mode without adding value.

**Consequence.** Release contents are exactly the tagged tree, which makes a release trivially reproducible from the repository.

## D10. Keep `supported_game_version` narrow

**Decision.** `1.15.*`.

**Rationale.** The tag set is defined by the game. A patch that retires or renames a tag would break an injection, and an injection into a missing tag errors. Narrow declaration makes the incompatibility visible in the launcher rather than in the log.

**Consequence.** Each game release requires a review of the 89 tags and a metadata bump.

## D11. Do not touch conditional map colours

**Decision.** `common/dynamic_country_map_colors/` is not shipped or modified.

**Rationale.** Those blocks express political identity — a communist Germany, a republican France, a Roman restoration — that overrides the definition colour by design. Neutralising them would remove base-game behaviour well beyond recolouring.

**Consequence.** 26 of the 89 mapped tags are also referenced by a conditional block, so in those circumstances the player sees the conditional colour, not the standardised one. See [behaviour/map-colour-conflicts.md](./behaviour/map-colour-conflicts.md).

## Related documents

- [invariants.md](./invariants.md) — the constraints these decisions produce.
- [ambiguities-and-open-questions.md](./ambiguities-and-open-questions.md) — open items.