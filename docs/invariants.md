# Invariants

Each invariant is a property that must hold for the mod to behave correctly, with the check that demonstrates it.

## Content invariants

| ID | Invariant | Verification |
|----|-----------|--------------|
| C1 | Every block uses `INJECT:<TAG>` at the top level, never a plain redefinition | `grep -cE '^INJECT:[A-Z0-9]{3} = \{$'` equals the number of tags in the file |
| C2 | Every injected tag exists in the vanilla definitions | Resolve each tag against `<game>/common/country_definitions/*.txt` |
| C3 | Every value is `color = { R G B }` with three integers in 0–255 | Regex match plus range check |
| C4 | No block declares any key other than `color` | Each block body is exactly one `color` line |
| C5 | Tags are unique and in ascending order | Compare the parsed tag list to its sorted form |
| C6 | Every entry carries a provenance comment of the form `# <name> - <#HEX> - <source>` | Count matching comment lines |
| C7 | Braces balance | Count `{` and `}` |
| C8 | The file is UTF-8 with a byte-order mark | Inspect the first three bytes |
| C9 | The shipped content is reproduced only by the build, never committed | `git ls-files standardised-country-colours` is empty and the path is git-ignored |
| C10 | The build is deterministic for the same inputs and version | Build twice into different directories and `diff -r` them |

## Packaging invariants

| ID | Invariant | Verification |
|----|-----------|--------------|
| P1 | `.metadata/metadata.json` exists at the mod folder root | Path check |
| P2 | `game_id` is `victoria3` | JSON field check |
| P3 | `picture` names a PNG that exists beside `metadata.json` | Compare `picture` to the directory listing |
| P4 | The launcher thumbnail is 600x333 | Image dimension check |
| P5 | The Workshop thumbnail at the mod folder root is 512x512 | Image dimension check |
| P6 | `id` never changes between releases | Diff against the previous tag |
| P7 | `supported_game_version` names a version whose tag set is unchanged | Manual review per game patch |

## Release invariants

| ID | Invariant | Verification |
|----|-----------|--------------|
| R1 | The archive contains the mod folder itself, not its contents | `unzip -l` shows `standardised-country-colours/…` |
| R2 | The archive name carries the tag version without the leading `v` | Workflow computes `VERSION="${VERSION#v}"` |
| R3 | The workflow publishes on a published release and accepts a manual tag | Trigger block inspection |
| R4 | The workflow declares `contents: write` | Permissions block inspection |
| R5 | The Workshop uploads point at the extracted mod folders | Upload steps use `release-vic3/standardised-country-colours/` and `release-imperator/standardised-country-colours/` |
| R6 | The Workshop uploads set the preview image explicitly | Upload steps declare `icon: "release-<game>/standardised-country-colours/thumbnail.png"` |
| R7 | The Nexus Mods uploads use file ids `8446233` (Victoria 3) and `8454045` (Imperator: Rome) and version `${{ env.VERSION }}` | Upload step inspection |
| R8 | Every release workflow builds each edition before archiving it | Each workflow runs `python3 scripts/build.py --game <game> --version` for both editions with the tag version and archives the freshly built `out/<game>/standardised-country-colours` |
| R9 | The archived folder is the build output, not a committed tree | The repository tracks no `standardised-country-colours/` path |
## Behavioural invariants

| ID | Invariant | Verification |
|----|-----------|--------------|
| B1 | The mod changes no key other than `color` | Compare a composed definition with vanilla for one tag |
| B2 | Unit colours are unchanged | Inspect `primary_unit_color` and friends in game |
| B3 | Flags are unchanged | Inspect a coat of arms in game |
| B4 | A mapped country released during play uses the injected colour | Release a non-start mapped tag in game |
| B5 | No `error.log` line names the shipped file | Read the log after start-up |

## Non-invariants

These are often mistaken for invariants and are not:

- **Colour uniqueness.** Nothing prevents two mapped tags sharing a colour, or a mapped colour coinciding with an unmapped country's vanilla colour. The palette is curated per country, not deduplicated globally.
- **Relevance of every mapping.** `SCA` maps to the exact vanilla value `#3E7ABD`. The entry is a deliberate no-op that records the palette source; removing it would change nothing on the map.
- **Total coverage.** Countries outside the 131 keep vanilla colours by design.

## Related documents

- [testing.md](./testing.md) — the executable checks.
- [change-guide.md](./change-guide.md) — which invariants a given edit threatens.