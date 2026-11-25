# Design decisions

## D1. Inject one key instead of restating the block

**Decision.** Every entry is `INJECT:<tag> = { color = { R G B } }`.

**Rationale.** A plain redefinition would replace the whole country block; a `REPLACE:` would do the same but explicitly. Either form pins tier, country type, cultures, capital, religion, regnal numbers, and subject cantons to the values the author typed. When the game changes one of those fields, the restated block keeps the stale value and the mod silently diverges from vanilla.

Injection appends the `color` key to the vanilla block, so every unmentioned key stays whatever the game says it is. The mod's footprint is one key per tag.

**Consequence.** The mod cannot delete or rename a vanilla key. It also cannot change a key that appears more than once in a vanilla block, though no vanilla country block does so for `color`. An injection into a non-existent tag errors and is skipped rather than silently creating a country.

**Evidence.** Victoria 3 exposes `INJECT` as one of six definition-entry modes over an enumerated set of folders that includes `common/country_definitions`. The vanilla content uses no injection keyword itself, so the mode is a modification surface only; first-party content never needs it.

## D2. One file, not one file per country or per region

**Decision.** All 135 injections live in `sc_country_colours.txt`.

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

**Rationale.** There is no side-car data file and no generated index; the comment is the record. A reviewer can see why a value differs from vanilla without consulting an external artefact, and the game ignores comment lines. The comment is rendered by the build from the palette entry and the vanilla name, so it cannot drift from the value.

**Consequence.** The comment is regenerated on every build, so it is never edited by hand. It makes the file longer, which is accepted as a readability gain. A discrepancy between the comment and the value can only arise if the palette snapshot and the shipped file are out of step, which a rebuild rectifies.

## D6. Plain RGB decimal components

**Decision.** Always `color = { R G B }` with integers 0–255.

**Rationale.** It is the form vanilla uses most often, it is the easiest to compare against a hexadecimal palette value by inspection, and it avoids floating-point rounding differences between an `hsv` authoring value and the rendered result.

**Consequence.** The seven mapped tags whose vanilla value is `hsv` or `hsv360` (`BAH`, `BRZ`, `CAS`, `CEY`, `DEN`, `NET`, `SPA`) change syntax. The injected key replaces the vanilla key, so no duplicate exists.

## D7. Partial coverage is intentional

**Decision.** 135 tags are mapped out of 835 vanilla definitions.

**Rationale.** The palette covers titles the game does not model — Crusader Kings 2 duchies, Total War factions, Civilization city-states — and some titles the game models under a tag whose vanilla name does not match the palette name closely enough to map mechanically. Mapping the wrong tag would be worse than leaving it unmapped, because a mis-coloured major power is immediately visible and hard to explain.

**Consequence.** Most countries keep their vanilla colour. A player sees the effect concentrated on the 64 mapped tags that exist at the 1836 start.

## D8. Declare multiplayer synchronisation

**Decision.** `game_custom_data.multiplayer_synchronized` is `true`.

**Rationale.** A colour difference is visible to every player and is derived from mod content. Two clients with different mod sets would draw different maps.

**Consequence.** The launcher will not join a session whose participants do not share the mod.

## D9. Render the mod, do not commit it

**Decision.** `scripts/build.py` renders the mod folder from the palette snapshot and the hardcoded mappings into an ignored `out/` directory, and every release workflow runs the build for the tag's version before archiving.

**Rationale.** The shipped artefact is static data, but it does not have to be tracked. Rendering it removes the duplicate copy of every colour and provenance comment that a committed folder would carry, so a value lives once, in `src/colours.md` and the game edition's `config.py`. Colours, provenance comments, and the metadata version are derived from those inputs rather than retyped, which removes the silent mis-conversion and stale-comment failure modes of hand editing.

**Consequence.** Release contents are exactly the build output for the tagged inputs, so a release stays reproducible. A local build is the only way to obtain the folder, and a release that was not built from its tag is not possible through the workflows.

## D10. Keep `supported_game_version` narrow

**Decision.** `1.15.*`.

**Rationale.** The tag set is defined by the game. A patch that retires or renames a tag would break an injection, and an injection into a missing tag errors. Narrow declaration makes the incompatibility visible in the launcher rather than in the log.

**Consequence.** Each game release requires a review of the 135 tags and a metadata bump.

## D11. Do not touch conditional map colours

**Decision.** `common/dynamic_country_map_colors/` is not shipped or modified.

**Rationale.** Those blocks express political identity — a communist Germany, a republican France, a Roman restoration — that overrides the definition colour by design. Neutralising them would remove base-game behaviour well beyond recolouring.

**Consequence.** 28 of the 135 mapped tags are also referenced by a conditional block, so in those circumstances the player sees the conditional colour, not the standardised one. See [behaviour/map-colour-conflicts.md](./behaviour/map-colour-conflicts.md).

## Related documents

- [invariants.md](./invariants.md) — the constraints these decisions produce.
- [ambiguities-and-open-questions.md](./ambiguities-and-open-questions.md) — open items.