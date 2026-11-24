# Build and deployment

## Build

`scripts/build.py` renders the mod folder from its inputs. The build is game-agnostic: each game edition under `scripts/games/` declares its own identity, mappings, and output layout, and the entry point only selects them and delegates.

| Input | Path | Role |
|-------|------|------|
| Palette snapshot | `src/colours.md` | Supplies each entry's primary colour and source attribution, shared by every edition |
| Game-specific configuration | `scripts/games/<game>/config.py` | Identity, output group, output layout, the palette entry for each shipped tag, and the vanilla name where it differs |
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
| `-o`, `--out`, `--output` | Directory that receives the per-game output groups | `out/` |

The build clears `<output>/<group>/<folder>/` and writes it from scratch, so no file from an earlier build survives. The content file carries a UTF-8 byte-order mark, LF line endings, and tabs, and the metadata is two-space-indented JSON with a trailing newline.

The mod folder is never committed; the build is the only producer of it. Its value is that it is deterministic, so the same inputs and version always produce the same bytes.

## Local packaging

To produce the same archive the workflows produce:

```bash
VERSION=1.0.0

python3 scripts/build.py --version "${VERSION}"
cp -r out/vic3/standardised-country-colours ./
zip -r "standardised-country-colours_${VERSION}.zip" "standardised-country-colours/"
```

The archive root is the folder itself, so extraction yields `standardised-country-colours/...`.

## Release procedure

1. Confirm every shipped tag still exists in the installed game's definitions.
2. Run `python3 scripts/build.py --version <version>`.
3. Run the structural checks in [testing.md](./testing.md) against the built folder.
4. Verify in game that a representative country shows the expected colour.
5. Commit and tag.
6. Publish a GitHub release for the tag.
7. `github-release.yml` builds the mod at the tag's version and attaches `standardised-country-colours_<version>.zip` to the release.
8. The `v*.*.*` tag push triggers `steam-workshop-release.yml`, which builds the same folder and uploads it to the Workshop item with a changenote linking to the GitHub release.
9. The same tag push triggers `nexus-mods-release.yml`, which builds the archive and uploads it to the Nexus Mods file.

Alternatively, trigger any workflow manually with the tag input; each `VERSION` expression resolves to the supplied tag.

## Environments

| Environment | Purpose | Mechanism |
|-------------|---------|-----------|
| Local build | Authoring and verification | `scripts/build.py` into `out/<group>/<folder>/` |
| Local game | Behavioural verification | Copy the built folder into the user mod directory |
| GitHub release | Distribution | Workflow build then archive attachment |
| Steam Workshop | Distribution | `steam-workshop-release.yml` build and item upload |
| Nexus Mods | Distribution | `nexus-mods-release.yml` build and file upload |

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
| `scripts/build.py` argument | `version` | Supplied by the workflow from the tag or manual input; already matches the tag |
| `scripts/games/victoria3/config.py` | `supported_game_version` | Widen or narrow per game patch review, then the next build applies it |
| Git tag | Tag name | `v<version>`; the workflows strip the leading `v` |

## What the workflow deliberately omits

- No checksum file, so a user cannot verify integrity against a published digest.
- No signing, so provenance rests on the GitHub release page.

## Related documents

- [components/packaging-and-distribution.md](./components/packaging-and-distribution.md) — the workflow itself.
- [troubleshooting.md](./troubleshooting.md) — install failures.