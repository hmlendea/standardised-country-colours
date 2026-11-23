# Build and deployment

## There is no build

The distributable artefact is the mod folder as committed. Nothing is compiled, generated, minified, or copied into a staging directory. A tagged checkout is byte-identical to the contents of a release archive.

## Local packaging

To produce the same archive the workflow produces:

```bash
VERSION=1.0.0
zip -r "standardised-country-colours_${VERSION}.zip" "standardised-country-colours/"
```

The archive root is the folder itself, so extraction yields `standardised-country-colours/…`.

## Release procedure

1. Confirm the metadata `version` matches the intended tag.
2. Confirm every shipped tag still exists in the installed game's definitions.
3. Run the structural checks in [testing.md](./testing.md).
4. Verify in game that a representative country shows the expected colour.
5. Commit and tag.
6. Publish a GitHub release for the tag.
7. The workflow attaches `standardised-country-colours_<version>.zip` to the release.

Alternatively, trigger the workflow manually with the tag input; the `VERSION` expression resolves to the supplied tag.

## Environments

| Environment | Purpose | Mechanism |
|-------------|---------|-----------|
| Local checkout | Authoring and verification | Direct edit of the mod folder |
| Local game | Behavioural verification | Copy the folder into the user mod directory |
| GitHub release | Distribution | Workflow archive attachment |

No staging, canary, or production distinction exists.

## Installation for a player

1. Download the archive for the release.
2. Extract into the Victoria 3 mod directory so the folder sits at `<mod dir>/standardised-country-colours/`.
3. Enable it in a playset.

Removal is deleting the folder. Nothing is written outside it.

## Rollback

Check out an earlier tag, or download an earlier release archive, and replace the folder. Because the mod owns no state, a rollback needs no data conversion; see [state-and-persistence.md](./state-and-persistence.md).

## Version bumping

| File | Field | Rule |
|------|-------|------|
| `.metadata/metadata.json` | `version` | Match the tag, so the launcher label agrees with the archive name |
| `.metadata/metadata.json` | `supported_game_version` | Widen or narrow per game patch review |
| Git tag | Tag name | `v<version>`; the workflow strips the leading `v` |

## What the workflow deliberately omits

- No checksum file, so a user cannot verify integrity against a published digest.
- No signing, so provenance rests on the GitHub release page.
- No Workshop or third-party upload.

## Related documents

- [components/packaging-and-distribution.md](./components/packaging-and-distribution.md) — the workflow itself.
- [troubleshooting.md](./troubleshooting.md) — install failures.