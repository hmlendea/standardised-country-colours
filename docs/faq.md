# Frequently asked questions

## What does this mod actually change?

One key, `color`, on 89 Victoria 3 country definitions. Nothing else.

## Will it break my save?

No. The mod introduces no scripted effects, events, or persistent variables. The game stores government, laws, and territory in a save, not map colours, so enabling or disabling the mod mid-campaign simply changes colours. See [state-and-persistence.md](./state-and-persistence.md).

## Will it disable achievements?

Victoria 3 does not disable achievements because of mods. A debug-mode session and console use are separate matters and do disable them.

## Does it work in multiplayer?

Yes, if every participant runs the same mod. The metadata declares `multiplayer_synchronized: true`, so the launcher will not join a session with a mismatched mod set.

## Why is the second colour in the palette not used?

Victoria 3 stores a single map colour per country. There is one `color` key, and the country list swatch, map fill, and diplomacy identifiers all read it. The palette's secondary colour has no destination. See [design-decisions.md](./design-decisions.md) D4.

## Why do the unit uniforms not change?

Unit colours come from `primary_unit_color`, `secondary_unit_color`, and `tertiary_unit_color`, which are separate keys. Only seven vanilla tags define them; the rest derive tinting from the coat of arms. The mod never touches either.

## Why does the flag not match the new colour?

Flags are composed from `common/coat_of_arms` using their own `color1`–`color4` keys resolved against `common/named_colors`. They are a separate colour system.

## Why did my country keep its vanilla colour?

Three possibilities, in order of likelihood:

1. The country is not among the 89. Check [colour-mappings.md](./colour-mappings.md).
2. A conditional map-colour block is active, for example a communist Germany or a republican France. See [behaviour/map-colour-conflicts.md](./behaviour/map-colour-conflicts.md).
3. The country is a subject and the `subject_map_color` rule lets it inherit its overlord's colour.

## Why is Bohemia teal?

The palette's Bohemia entry records `#00AB93` from Age of Empires II HD. The mod applies the palette as recorded rather than substituting its own judgement.

## Why does Scandinavia's colour not change?

`SCA` maps to `#3E7ABD`, which is exactly its vanilla value. The entry is shipped so the palette provenance is recorded; it is a deliberate no-op.

## Can I use only some of the colours?

Yes, by editing your local copy. Remove entries you do not want and the corresponding countries revert to vanilla. There is no in-game toggle. Note that a local edit makes your copy diverge from any release, so a later update will overwrite it.

## Can I add a country the mod does not cover?

Yes. Follow [flows/colour-authoring.md](./flows/colour-authoring.md). The only hard requirement is that the tag exists in the vanilla definitions.

## Why is there no Steam Workshop page?

At version `1.0.0` the only distribution channel is GitHub Releases. Adding Workshop publication would require a separate workflow and Steam credentials, neither of which is present.

## How do I know a release is safe?

Inspect the archive listing. It should contain exactly `.metadata/`, `common/country_definitions/sc_country_colours.txt`, and `thumbnail.png` inside the mod folder. A release that contains events, effects, scripted rules, or any other content folder is not from this repository. See [security.md](./security.md).

## Does the mod need a specific game version?

`supported_game_version` is `1.15.*`. An older build may not define every shipped tag, and an injection into a missing tag errors. See [dependencies.md](./dependencies.md).

## Do the file comments affect performance or behaviour?

No. The engine ignores comment lines. They exist purely as documentation.

## Related documents

- [troubleshooting.md](./troubleshooting.md) — diagnosing a specific symptom.
- [repository-overview.md](./repository-overview.md) — scope and boundaries.
- [design-decisions.md](./design-decisions.md) — why the design is what it is.