# Security

This document elaborates on the root [SECURITY.md](../SECURITY.md). That document is authoritative for reporting and scope; this one describes the trust model and the practical risks of the shipped content.

## Trust model

```mermaid
flowchart LR
  Repo["Repository content"] -->|"same trust domain as vanilla"| Engine["Victoria 3 engine"]
  Vanilla["Vanilla content"] --> Engine
  Repo -->|"archive"| GitHub["GitHub Releases"]
  GitHub -->|"download"| User["User machine"]
  Engine --> Save["Save game"]
```

The mod ships plain text that the engine parses within the same trust domain as vanilla content. There is no sandbox boundary between a mod definition file and a base-game definition file: a mod file can change what the game loads, but it cannot execute code, open sockets, or read arbitrary files.

## Attack surfaces

| Surface | Exposure | Mitigation |
|---------|----------|------------|
| Definitions text | Parsed by the engine | Content is a fixed set of integer colours; a tampered file could at worst change colours or inject other country keys |
| Launcher metadata | Parsed by the launcher | JSON only; a tampered file could misdescribe the mod |
| Thumbnails | Decoded by the launcher and Steam | PNG decode; a malicious image exploits the decoder, not the mod |
| Release workflows | Run `actions/checkout@v7`, `softprops/action-gh-release@v2`, `hmlendea/steam-workshop-update@latest`, `Nexus-Mods/upload-action@v1.0.0-beta.11`, and `zip` | Pinned to major versions; `contents: write` is the only requested scope |
| Distribution channels | GitHub Releases, the Steam Workshop, and Nexus Mods | HTTPS; no signature is published |
| Steam credentials | `STEAM_USERNAME`, `STEAM_PASSWORD`, and `STEAM_2FA_SEED` repository secrets | Referenced only as `${{secrets...}}` expressions; values are never printed, committed, or sent anywhere but Steam |
| Nexus Mods credential | `NEXUSMODS_API_KEY` repository secret | Referenced only as `${{ secrets... }}`; the value is never printed, committed, or sent anywhere but Nexus Mods |

## What a malicious fork could do

A fork can change any byte. The realistic consequences are limited to the content surface:

| Change | Consequence |
|--------|-------------|
| Alter colours | Cosmetic |
| Add `INJECT:` keys beyond `color` | Can change tier, cultures, or capital of a country — a gameplay change, not a system compromise |
| Use `REPLACE:` | Discards a vanilla block entirely, which can break a country |
| Add a definition file named after a vanilla file | Deletes vanilla content |
| Add a non-colour folder | Could inject events, effects, or scripted rules, which is where gameplay risk concentrates |

The last row matters: the repository ships only `common/country_definitions/`, and that is what a user should verify in an archive. A release from this repository never contains events, effects, or scripted rules.

## Verification a user can perform

1. Inspect the archive listing: it should contain exactly `.metadata/`, `common/country_definitions/sc_country_colours.txt`, and `thumbnail.png` inside the mod folder.
2. Confirm the definition file contains only `INJECT:` blocks with a single `color` key each.
3. Confirm no other content folders are present.

## Secrets

The mod content requires none. The Workshop workflow reads `STEAM_USERNAME`, `STEAM_PASSWORD`, and `STEAM_2FA_SEED` from repository secrets, and the Nexus Mods workflow reads `NEXUSMODS_API_KEY`; each is referenced only as a `${{ secrets... }}` expression and no value is stored in the repository. The Steam 2FA seed is required only because the Workshop uploader authenticates non-interactively. The GitHub release workflow uses the automatic `GITHUB_TOKEN`.

## Supply chain

No packages, no lockfiles, no third-party build dependencies to compromise. The build script uses only the Python 3 standard library and runs on the maintainer's machine; the only third-party code that executes during a release runs on GitHub's runners.

## Content-integrity risks specific to this mod

| Risk | Consequence | Control |
|------|-------------|---------|
| A retired tag is left in the file | An injection errors on every load | Review the tag set per game patch |
| A tag is mapped to the wrong country | Silent, persistent mis-colour | Comment records the name; review against the localisation |
| `REPLACE:` is introduced by accident | A vanilla block is destroyed | Invariant C1 |
| A vanilla file name is reused | Vanilla definitions are destroyed | Invariant D3 |

## Privacy

The mod handles no personal data. See [PRIVACY.md](../PRIVACY.md).

## Related documents

- [dependencies.md](./dependencies.md) — supply chain detail.
- [integrations.md](./integrations.md) — trust boundaries per integration.
- [invariants.md](./invariants.md) — the guard conditions.