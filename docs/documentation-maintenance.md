# Documentation maintenance

## Ownership

The repository maintainer owns this tree. There is no delegated documentation owner and no review gate beyond the maintainer's.

## When to update

| Trigger | Documents to revise |
|---------|---------------------|
| A colour value changes | [colour-mappings.md](./colour-mappings.md), `src/colours.md` if the snapshot is refreshed |
| A mapping is added or removed | [colour-mappings.md](./colour-mappings.md), the counts in [INDEX.md](./INDEX.md), [repository-structure.md](./repository-structure.md) if the file length changes, and possibly [design-decisions.md](./design-decisions.md) D7 |
| The content file is renamed | [components/mod-content.md](./components/mod-content.md), [repository-structure.md](./repository-structure.md), `scripts/games/victoria3/config.py`, and every document that names the path |
| The metadata changes | [components/launcher-metadata.md](./components/launcher-metadata.md), [configuration.md](./configuration.md), `scripts/games/victoria3/config.py` |
| A game edition is added | [build-and-deployment.md](./build-and-deployment.md), [repository-structure.md](./repository-structure.md), and the edition registry in `scripts/games/__init__.py` |
| The build changes | [build-and-deployment.md](./build-and-deployment.md), [repository-structure.md](./repository-structure.md), [dependencies.md](./dependencies.md), [CONTRIBUTING.md](../CONTRIBUTING.md) |
| A workflow is added, renamed, or removed | [components/packaging-and-distribution.md](./components/packaging-and-distribution.md), [integrations.md](./integrations.md), and the README GitHub Actions table |
| A distribution channel is added | [integrations.md](./integrations.md), [README.md](../README.md) |
| A game patch changes the tag set | [dependencies.md](./dependencies.md), [colour-mappings.md](./colour-mappings.md), [behaviour/country-colour-conflicts.md](./behaviour/map-colour-conflicts.md) if conditional blocks changed |
| The palette changes | [colour-mappings.md](./colour-mappings.md), the palette snapshot in `src/colours.md`, and the snapshot date in [INDEX.md](./INDEX.md) |

## Facts that must be re-derived rather than trusted

These figures are counts against the installed game and change when the game or the content changes. Re-derive rather than copy:

| Fact | Where it is asserted | How to re-derive |
|------|----------------------|------------------|
| Number of mapped tags | [INDEX.md](./INDEX.md), [components/mod-content.md](./components/mod-content.md) | Count `INJECT:` lines |
| Number of vanilla definitions | [INDEX.md](./INDEX.md) | Count definition blocks across the game's `common/country_definitions` |
| Start/formable split | [INDEX.md](./INDEX.md), [colour-mappings.md](./colour-mappings.md), [data-model.md](./data-model.md) | Cross-reference `common/history/countries/` and `common/country_formation/` |
| Conditional-colour overlap | [behaviour/map-colour-conflicts.md](./behaviour/map-colour-conflicts.md) | Cross-reference `common/dynamic_country_map_colors/00_default.txt` against the mapped tags |
| Redundant mappings | [components/mod-content.md](./components/mod-content.md), [testing.md](./testing.md) | Run the redundancy audit |
| Vanilla syntax census | [architecture.md](./architecture.md) | Count `color =` forms in the game's definition files |

## Verifying this tree

Two mechanical checks exist.

```bash
# 1. The documented structural audit must pass unchanged.
#    Copy the script from testing.md and run it against an installed game.

# 2. The build must reproduce the committed folder exactly.
python3 scripts/build.py --version 1.0.0 -o /tmp/build-check
diff -r /tmp/build-check/standardised-country-colours standardised-country-colours

# 3. Internal links must resolve.
python3 - <<'PY'
import pathlib, re
root = pathlib.Path("docs")
bad = []
for path in root.rglob("*.md"):
    for target in re.findall(r"\]\(([^)#]+?)(?:#[^)]*)?\)", path.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (path.parent / target).resolve().exists():
            bad.append(f"{path}: {target}")
print("\n".join(bad) or "all links resolve")
PY
```

## Style rules for this tree

- Sentence case for headings (`## Repository purpose`).
- Kebab-case file names; plural directory names for collections.
- Relative links from the referencing file, never absolute repository paths.
- Code symbols in backticks with the tag or key spelled exactly.
- State observed facts and mark inference as inference. Do not present an engine behaviour as verified unless it was observed or is documented by the engine's own strings.
- Never document an intended-but-unshipped capability.

## Keeping the root documents in step

The root documents are template-governed. After changing this tree, check that:

1. the README `## 📚 Documentation` table lists every top-level document here;
2. the README `## ⚙️ GitHub Actions` table lists every workflow under `.github/workflows/`;
3. `ARCHITECTURE.md` does not contradict anything asserted here.

## Related documents

- [INDEX.md](./INDEX.md) — the catalogue to keep current.
- [ambiguities-and-open-questions.md](./ambiguities-and-open-questions.md) — where unresolved items are recorded.