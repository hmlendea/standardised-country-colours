# Change guide

## Change categories and their blast radius

| Change | Files touched | Risk | Required verification |
|--------|---------------|------|-----------------------|
| Change one country's colour | `src/colours.md` (palette value) | Low | Rebuild, structural audit plus in-game check |
| Add a mapping | `scripts/games/victoria3/config.py`, `docs/colour-mappings.md` | Low | Rebuild, structural audit, in-game check |
| Remove a mapping | `scripts/games/victoria3/config.py`, `docs/colour-mappings.md` | Low | Confirm intent; the country reverts to vanilla |
| Retarget a mapping to a different tag | `scripts/games/victoria3/config.py` | Medium | Two in-game checks: old tag reverts, new tag changes |
| Rename the content file | `scripts/games/victoria3/config.py` plus every doc that names it | Low | Confirm the new name is unique in the folder |
| Change the metadata version | `--version` build argument | Low | Match the Git tag |
| Widen `supported_game_version` | `scripts/games/victoria3/config.py` | Medium | Confirm every tag exists in the newly covered build |
| Change the release workflow | `.github/workflows/github-release.yml`, `.github/workflows/steam-workshop-release.yml`, `.github/workflows/nexus-mods-release.yml` | Medium | Re-validate against the workflow template |
| Change the thumbnails | `src/victoria3/thumbnail.png`, `src/victoria3/launcher-thumbnail.png` | Cosmetic | Rebuild; confirm the dimensions and that `picture` still resolves |
| Add a game edition | `scripts/games/<game>/`, `scripts/games/__init__.py` | Medium | Rebuild and confirm every edition's output |
| Introduce `REPLACE:` | `scripts/games/<game>/render.py` | **Severe** | Never; it destroys the vanilla block |
| Reuse a vanilla file name | `scripts/games/<game>/config.py` | **Severe** | Never; it destroys the vanilla file |

## Procedure: change a colour

1. Locate the palette entry in `src/colours.md` by name.
2. Change its Principal Colours value and, if needed, its source.
3. Run `python3 scripts/build.py --game victoria3 --version <version>`.
4. Run the structural audit and the comment/hex consistency check from [testing.md](./testing.md) against the build output.
5. Confirm in game.

## Procedure: add a country

Follow [flows/colour-authoring.md](./flows/colour-authoring.md). In addition:

7. Add a row to [colour-mappings.md](./colour-mappings.md).
8. Update the counts in [INDEX.md](./INDEX.md) if the totals changed.

## Procedure: respond to a game patch

1. Read the patch notes for country tag changes.
2. Re-resolve every shipped tag against the new definitions:
   - a tag that no longer exists must be removed or retargeted in `scripts/games/victoria3/config.py`;
   - a tag whose localised name changed should have `VANILLA_COUNTRY_NAMES` updated.
3. Decide whether `supported_game_version` can be widened in `scripts/games/victoria3/config.py`.
4. Run `python3 scripts/build.py --game victoria3 --version <version>` and inspect its output.
5. Run the audits and verify in game.

Nothing in the repository can detect a retired tag automatically, because the tag set lives in the game installation rather than in the repository.

## Procedure: respond to a palette change

The palette is external, and its snapshot lives in `src/colours.md`. When it changes:

1. Diff the palette's primary colours against the snapshot in `src/colours.md`.
2. Apply the intended change to the Principal Colours row, updating the value and the source.
3. Apply any tag-relevant rename — an alias split or merge — as an add/retarget/remove sequence in `scripts/games/victoria3/config.py`.
4. Run `python3 scripts/build.py --game victoria3 --version <version>` and inspect its output.
5. Refresh [colour-mappings.md](./colour-mappings.md) and the counts in [INDEX.md](./INDEX.md).
6. Note the palette snapshot date in [INDEX.md](./INDEX.md).

## Safe-edit rules

| Rule | Reason |
|------|--------|
| Keep the `INJECT:` keyword | A plain redefinition discards the vanilla block |
| Keep `color` as the only key in a block | The mod's footprint is one key; anything else pins unrelated behaviour |
| Keep the file UTF-8 with a BOM | Without it the engine may not read the file |
| Keep the file name unique in its folder | A collision with a vanilla name deletes the vanilla file |
| Keep the tags unique and sorted | Duplicates are ambiguous; sorting makes review tractable |
| Keep the provenance comment in step with the value | The comment is the only record of why a value differs |
| Keep the tag's localised name accurate | A stale name hides a mis-mapping |
| Change the inputs, not the output | Editing the shipped file by hand is overwritten by the next build |
| Add a game's configuration under its own `scripts/games/<game>/` module | Keeps edition-specific identity and mappings out of the shared build |

## What not to edit

| Target | Reason |
|--------|--------|
| The built `standardised-country-colours/` folder by hand | `scripts/build.py` regenerates it; edit the matching `scripts/games/victoria3/config.py` or `src/colours.md` instead |
| Anything under the game installation | Game updates and file verification overwrite it |
| `common/dynamic_country_map_colors/` | Conditional colours are intentional; see [design-decisions.md](./design-decisions.md) D11 |
| Unit colour keys | Out of scope by design |
| Coat-of-arms and flag definitions | A separate colour system |

## Review checklist

- [ ] Every new or changed block uses `INJECT:`.
- [ ] Every block body contains exactly one `color` line.
- [ ] Every tag exists in the installed definitions.
- [ ] Tags are unique and sorted.
- [ ] Decimal components are 0–255.
- [ ] Comments match their values and carry a source.
- [ ] The file has a BOM and balanced braces.
- [ ] The build runs cleanly and its output passes the structural audit.
- [ ] Documentation that names the file, the counts, or a mapping is updated.
- [ ] The structural audit passes.
- [ ] The change is visible in game.

## Related documents

- [flows/colour-authoring.md](./flows/colour-authoring.md) — the authoring procedure.
- [invariants.md](./invariants.md) — what each rule protects.
- [documentation-maintenance.md](./documentation-maintenance.md) — keeping the docs in step.