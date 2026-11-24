# Build and deployment

## Build

`scripts/build.py` renders the mod folder from its inputs. The build is game-agnostic: each game edition under `scripts/games/` declares its own identity, mappings, and output layout, and the entry point only selects them and delegates.

| Input | Path | Role |
|-------|------|------|
| Palette snapshot | `src/colours.md` | Supplies each entry's primary colour and source attribution, shared by every edition |
| Game-specific configuration | `scripts/games/<game>/config.py` | Identity, output layout, the palette entry for each shipped tag, and the vanilla name where it differs |
| Game-specific rendering | `scripts/games/<game>/render.py` | Turns the palette and configuration into the shipped files |
| Artwork | `src/<game>/thumbnail.png`, `src/<game>/launcher-thumbnail.png` | Copied into the mod folder and the metadata directory |
| Version | `--version` argument | Written as the metadata `version` |

The Victoria 3 edition keeps its name, id, game id, supported game version, description, tags, and multiplayer flag in `scripts/games/victoria3/config.py`.

```bash
python3 scripts/build.py --version 1.0.0
```

| Option | Meaning | Default |
|--------|---------|---------|
| `-v`, `--ver`, `--version` | Mod version recorded in the metadata; required | — |
| `-g`, `--game` | Game edition to build; repeatable | Every registered edition |
| `-o`, `--out`, `--output` | Directory that receives the mod folders | `out/` |

The build clears `<output>/<folder>/` and writes it from scratch, so no file from an earlier build survives. The result is byte-identical to the committed mod folder: the content file carries a UTF-8 byte-order mark, LF line endings, and tabs, and the metadata is two-space-indented JSON with a trailing newline.

## Local packaging

To produce the same archive the workflow produces:

```bash
python3 scripts/build.py --version 1.0.0
VERSION=1.0.0
(cd out && zip -r "../standardised-country-colours_${VERSION}.zip" "standardised-country-colours/")
```

`zip` can equivalently archive the committed `standardised-country-colours/` folder, because the build reproduces it exactly. The archive root is the folder itself, so extraction yields `standardised-country-colours/...`.

## Release procedure

1. Confirm the metadata `version` matches the intended tag.
2. Confirm every shipped tag still exists in the installed game's definitions.
3. Run the build and confirm `<output>/standardised-country-colours/` matches the committed folder.
4. Run the structural checks in [testing.md](./testing.md).
5. Verify in game that a representative country shows the expected colour.
6. Commit and tag.
7. Publish a GitHub release for the tag.
8. The workflow attaches `standardised-country-colours_<version>.zip` to the release.
9. The `v*.*.*` tag push triggers `steam-workshop-release.yml`, which uploads the same folder to the Workshop item with a changenote linking to the GitHub release.
10. The same tag push triggers `nexus-mods-release.yml`, which uploads the archive to the Nexus Mods file.

Alternatively, trigger any workflow manually with the tag input; each `VERSION` expression resolves to the supplied tag.

## Environments

| Environment | Purpose | Mechanism |
|-------------|---------|-----------|
| Local checkout | Authoring and verification | Direct edit of the mod folder |
| Local build | Regenerating the mod folder | `scripts/build.py` into `out/` |
| Local game | Behavioural verification | Copy the folder into the user mod directory |
| GitHub release | Distribution | Workflow archive attachment |
| Steam Workshop | Distribution | `steam-workshop-release.yml` item upload |
| Nexus Mods | Distribution | `nexus-mods-release.yml` file upload |

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
| `scripts/games/victoria3/config.py` or build argument | `version` | Supplied to `scripts/build.py`; match the tag, so the launcher label agrees with the archive name |
| `scripts/games/victoria3/config.py` | `supported_game_version` | Widen or narrow per game patch review, then rebuild |
| Git tag | Tag name | `v<version>`; the workflow strips the leading `v` |

## What the workflow deliberately omits

- No checksum file, so a user cannot verify integrity against a published digest.
- No signing, so provenance rests on the GitHub release page.

## Related documents

- [components/packaging-and-distribution.md](./components/packaging-and-distribution.md) — the workflow itself.
- [troubleshooting.md](./troubleshooting.md) — install failures.