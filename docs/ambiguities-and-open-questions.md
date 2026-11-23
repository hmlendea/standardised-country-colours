# Ambiguities and open questions

Items that repository evidence does not settle, recorded so a future contributor does not have to re-derive the uncertainty.

## A1. Whether an injected scalar key replaces or precedes the existing one

The engine appends injected keys to the target block. For a scalar key a block cannot hold two values, so the injected value wins; the observable result confirms this — the map shows the injected colour for all 89 tags. The precise internal mechanism, whether the injected value overwrites in place or the last-parsed value takes precedence, is not documented. It has no practical consequence for this mod, because the mod injects one scalar and never injects a block.

## A2. No commit timestamp for the palette snapshot

The palette is an external document. This tree records that the snapshot used is current as of the date in [INDEX.md](./INDEX.md), but the palette itself is not versioned and carries no revision identifier. A `#` and date were considered and not added.

**Recommendation.** If palette drift becomes a problem, commit a copy of the palette alongside the mod and reference it, so a release pins the exact source values.

## A3. Two deliberate near-no-op mappings

`SCA` equals vanilla exactly and `APC` is within three units per component. Both are shipped.

**Open question.** Whether to keep them. Keeping them records the palette's provenance for those two countries; removing them changes nothing on the map. The current position is to keep them, because the palette's intent is authoritative and a later palette change to either row would then be a one-line edit rather than a re-addition.

## A4. Whether Babylon should be mapped anyway

The palette lists Babylon, and `localization/english/countries_l_english.yml` has a `BAB` key, but no country definition block exists in `common/country_definitions`. There is nothing to inject into.

**Open question.** Whether the tag is defined elsewhere, for example in a DLC content pack that is not installed in the verification environment. The installed `game/dlc` tree contains no `country_definitions` folder, so if a DLC defines `BAB`, it is delivered differently.

**Recommendation.** Re-check after installing every DLC. If a definition appears, add the entry.

## A5. Tags whose localised name is shared

Two pairs of tags share a localised name, and the palette supplies one entry for each pair:

| Shared name | Tags | Resolution |
|-------------|------|------------|
| India | `BHT` (formable unification), `HND` (release-only entity) | Both mapped |
| Romania | `ROM` (formable), `WAL` (Wallachia, exists at the start) | Both mapped |

**Open question.** Whether the palette intends other shared-name cases to be doubled. `KHM` (Khmu) versus `CAM` (Cambodia) is a different case: the palette entry is `Khmer`, and `CAM` carries the `khmer` culture and capital `STATE_CAMBODIA`, so `CAM` is the closer match. `KLO` (Khmer Loeu) is a distinct highland people and was not mapped.

## A6. Whether the palette's title names should drive tag selection more strictly

Some mappings required a judgement because the palette name is a historical or alternative name rather than the vanilla name:

| Palette name | Mapped tag | Vanilla name |
|--------------|------------|--------------|
| Byzantine Empire | `BYZ` | Byzantium |
| Holy Roman Empire | `HRE` | Central Europe |
| Iroquois | `IRO` | Haudenosaunee |
| Lombardy | `LOM` | Lombardia |
| Maori | `AOT` | Aotearoa |
| Moldova | `MOL` | Moldavia |
| Rajastan | `RAJ` | Rajputana |
| Sardinia | `SAR` | Sardinia-Piedmont |
| Sicily | `SIC` | Two Sicilies |
| United States | `USA` | America |
| Carpathia | `KUK` | Danubian State |
| Galicia-Volhynia | `GAL` | Galicia-Lodomeria |
| Khmer | `CAM` | Cambodia |
| Bosnia | `BOS` | Bosnia-Herzegovina |

Each is recorded in the file comment as `(palette: <entry>)`.

**Open question.** Whether any of these is the wrong choice. The strongest candidates for review are `KUK`, where the palette entry is a Crusader Kings II formable whose territory overlaps but does not coincide with the game's Danubian State, and `AOT`, where Aotearoa is a modern name whose territory matches the game's `AOT` but not the pre-colonial `maori` identity.

## A7. Whether the conditional-colour overlap should be documented per country

[behaviour/map-colour-conflicts.md](./behaviour/map-colour-conflicts.md) lists the 26 overlapping tags but does not enumerate the trigger conditions of every block, because 25 of them concern Russian Civil War warlord states and would triple the document's length for little value.

**Recommendation.** Add a per-tag appendix only when a user reports a discrepancy.

## A8. No integrity evidence for the published archive

The release workflow publishes no checksum and no signature. A user cannot verify that a downloaded archive is the one built from a given tag.

**Open question.** Whether to add a SHA-256 file. The canonical workflow template for a content-only repository deliberately omits a checksum, so adding one would diverge from the template.

## A9. The palettes's secondary colours are unrecorded in the mod

The palette records a secondary colour for every entry, and the mod cannot apply it. The values are not reproduced anywhere in the repository.

**Open question.** Whether to record them for reference. The current position is not to, because a value the mod cannot apply invites the misapprehension that it does.

## A10. Whether `supported_game_version` should be narrowed per patch

`1.15.*` covers the verified build. A future patch within the same minor version may still change a tag, in which case the declared range would be too permissive.

**Recommendation.** Treat any patch that touches `common/country_definitions` as requiring a review, regardless of the range.

## Related documents

- [design-decisions.md](./design-decisions.md) — decisions that are settled.
- [documentation-maintenance.md](./documentation-maintenance.md) — where re-derivable facts live.