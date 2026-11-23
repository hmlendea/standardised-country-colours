# Dependencies

## Runtime dependencies

| Dependency | Version | Responsibility | Consequence of change |
|------------|---------|----------------|-----------------------|
| Victoria 3 | `1.15.*` | Parses the metadata, loads country definitions, runs the injection pass, resolves map colours | A patch can retire or rename a tag, which makes the matching injection error |
| Vanilla `common/country_definitions` | shipped with the game | Supplies the 835 baseline blocks the mod targets | A changed tag set invalidates the affected entries |
| Vanilla `common/named_colors` | shipped with the game | Resolves the named colours used by conditional map-colour blocks | A renamed colour changes a conditional appearance, not the mod's own values |

## Authoring dependencies

| Dependency | Responsibility | Consequence |
|------------|----------------|-------------|
| `COUNTRY_COLOURS.md` palette | Source of every standardised value and its attribution | The repository records the value; it does not derive it |
| Hex-to-decimal conversion | Converts `#RRGGBB` to three 0–255 components | A wrong conversion is a silent mis-colour, invisible to the engine |
| Tag resolution | Maps a palette entry name to a three-letter tag | A wrong tag colours the wrong country and is immediately visible |

## Development dependencies

None. Editing the mod requires only a text editor that preserves the UTF-8 byte-order mark. No SDK, package manager, runtime, compiler, or test framework is required.

## Tooling dependencies

| Tool | Used by | Optional |
|------|---------|----------|
| `zip` | Release workflow | No, for releases |
| `rsvg-convert` | Regenerating the thumbnails from the SVG source | Yes, only when the artwork changes |
| `python3` | The verification snippets in [testing.md](./testing.md) | Yes, for verification only |
| Victoria 3 with `-debug_mode` | In-game verification | Yes, but required for behavioural checks |

## Internal dependencies between documents and content

```mermaid
flowchart LR
  Palette["COUNTRY_COLOURS.md<br/>external"] --> Content["sc_country_colours.txt"]
  Content --> Docs["docs/colour-mappings.md"]
  Content --> RootArch["ARCHITECTURE.md"]
  Meta["metadata.json"] --> Release["github-release.yml"]
  Content --> Release
```

Documentation depends on content; content depends on nothing in the repository. No document is read by the engine.

## Supply chain assessment

The repository has no packages, lockfiles, SBOM, or third-party code. The only executable elements are:

1. a GitHub Action (`actions/checkout@v7`, `softprops/action-gh-release@v2`), pinned to major versions;
2. the `zip` command from the runner image.

Both run only in the release workflow, never on a player's machine.

## Related documents

- [integrations.md](./integrations.md) — the external systems these dependencies represent.
- [security.md](./security.md) — the trust boundary.