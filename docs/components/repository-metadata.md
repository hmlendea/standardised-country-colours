# Component: repository metadata

## Scope

Files that describe or support the repository without being read by the game.

| Path | Role |
|------|------|
| `README.md` | Project overview, capabilities, installation, usage |
| `ARCHITECTURE.md` | Verified current architecture |
| `CONTRIBUTING.md` | Contribution process and code style |
| `CODE_OF_CONDUCT.md` | Conduct standards |
| `SECURITY.md` | Vulnerability reporting and scope |
| `PRIVACY.md` | Data-handling statement |
| `LICENSE` | GNU General Public License v3.0 |
| `.github/FUNDING.yml` | Funding platform declarations |
| `.github/cover.png` | Repository cover image (1774x887 RGB) |
| `.github/workflows/github-release.yml` | Release automation |
| `.github/workflows/nexus-mods-release.yml` | Nexus Mods automation |
| `.github/workflows/steam-workshop-release.yml` | Steam Workshop automation |
| `.gitignore` | Version-control exclusions |
| `docs/` | This knowledge base |

## Licence

GNU General Public License v3.0. The `LICENSE` file carries the unmodified licence text. The README states the licence name without the "or later" suffix, because the repository does not declare a later-version grant.

## Funding

`.github/FUNDING.yml` declares `github`, `patreon`, `ko_fi`, `liberapay`, `buy_me_a_coffee`, and a `custom` URL. `custom` takes precedence when a document needs a single donation link.

## Documentation consistency rules

The root documents are template-governed and validated for prose fidelity. Practical consequences for a contributor:

- Heading text, emoji, and order are fixed by the template.
- Fixed prose outside placeholders must be preserved verbatim.
- Configuration tables, capability lists, and per-workflow rows are the only places content is invented.
- The README's `## ⚙️ GitHub Actions` table must list every workflow present under `.github/workflows/`.

## Boundaries

- Repository metadata must not depend on mod content semantics; it describes the package.
- Documentation claims must be grounded in the shipped content and the observed engine contract. Do not document intended but unshipped behaviour.

## Related documents

- [documentation-maintenance.md](../documentation-maintenance.md) — how to keep these in step.
- [security.md](../security.md) — the policy content. (Root [SECURITY.md](../../SECURITY.md) is authoritative.)