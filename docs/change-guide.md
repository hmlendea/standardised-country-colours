# Change guide

## Change categories and their blast radius

| Change | Files touched | Risk | Required verification |
|--------|---------------|------|-----------------------|
| Change one country's colour | `sc_country_colours.txt` only | Low | Structural audit plus in-game check |
| Add a mapping | `sc_country_colours.txt`, `docs/colour-mappings.md` | Low | Structural audit, comment/hex consistency, in-game check |
| Remove a mapping | `sc_country_colours.txt`, `docs/colour-mappings.md` | Low | Confirm intent; the country reverts to vanilla |
| Retarget a mapping to a different tag | `sc_country_colours.txt` | Medium | Two in-game checks: old tag reverts, new tag changes |
| Rename the content file | `sc_country_colours.txt` plus every doc that names it | Low | Confirm the new name is unique in the folder |
| Change the metadata version | `metadata.json` | Low | Match the Git tag |
| Widen `supported_game_version` | `metadata.json` | Medium | Confirm every tag exists in the newly covered build |
| Change the release workflow | `.github/workflows/github-release.yml` | Medium | Re-validate against the workflow template |
| Change the thumbnails | `.metadata/thumbnail.png`, `thumbnail.png` | Cosmetic | Confirm the dimensions and that `picture` still resolves |
| Introduce `REPLACE:` | `sc_country_colours.txt` | **Severe** | Never; it destroys the vanilla block |
| Reuse a vanilla file name | `sc_country_colours.txt` | **Severe** | Never; it destroys the vanilla file |

## Procedure: change a colour

1. Locate the entry by tag.
2. Write the new decimal triple.
3. Update the comment's hexadecimal value to match.
4. If the palette source changed, update it too.
5. Run the structural audit and the comment/hex consistency check from [testing.md](./testing.md).
6. Confirm in game.

## Procedure: add a country

Follow [flows/colour-authoring.md](./flows/colour-authoring.md). In addition:

7. Add a row to [colour-mappings.md](./colour-mappings.md).
8. Update the counts in [INDEX.md](./INDEX.md) if the totals changed.

## Procedure: respond to a game patch

1. Read the patch notes for country tag changes.
2. Re-resolve every shipped tag against the new definitions:
   - a tag that no longer exists must be removed or retargeted;
   - a tag whose localised name changed should have its comment updated.
3. Decide whether `supported_game_version` can be widened.
4. Bump `metadata.json` `version`.
5. Run the audits and verify in game.

Nothing in the repository can detect a retired tag automatically, because the tag set lives in the game installation rather than in the repository.

## Procedure: respond to a palette change

The palette is external. When it changes:

1. Diff the palette's primary colours against the shipped values.
2. Apply any intended change as an ordinary colour change, updating the comment's hexadecimal and source.
3. Apply any tag-relevant rename — an alias split or merge — as an add/retarget/remove sequence.
4. Refresh [colour-mappings.md](./colour-mappings.md) and the counts in [INDEX.md](./INDEX.md).
5. Note the palette snapshot date in [INDEX.md](./INDEX.md).

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

## What not to edit

| Target | Reason |
|--------|--------|
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
- [ ] Documentation that names the file, the counts, or a mapping is updated.
- [ ] The structural audit passes.
- [ ] The change is visible in game.

## Related documents

- [flows/colour-authoring.md](./flows/colour-authoring.md) — the authoring procedure.
- [invariants.md](./invariants.md) — what each rule protects.
- [documentation-maintenance.md](./documentation-maintenance.md) — keeping the docs in step.