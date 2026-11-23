# Logging

The repository emits no logs. Every diagnostic surface belongs to the game, and the only actionable one is the engine's own log directory.

## Repository-side logging

| Facility | Present |
|----------|---------|
| Application logger | No |
| Build log | No build step exists |
| Workflow log | Yes, GitHub Actions console output |
| Test output | No test suite exists |

## Engine log surfaces

| File | Relevance |
|------|-----------|
| `<user data>/Victoria 3/logs/error.log` | Parse, encoding, and injection errors; the primary diagnostic |
| `warning.log` | Non-fatal warnings |
| `debug.log` | Detail available in debug mode |
| `database_conflicts.log` | Duplicate or conflicting database entries |
| `checksum.log` | Content checksum changes |
| `setup.log` | Start-up sequence |

All are under the user data directory:

- GNU/Linux: `~/.local/share/Paradox Interactive/Victoria 3/logs/`
- macOS: `~/Library/Application Support/Paradox Interactive/Victoria 3/logs/`
- Windows: `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\logs\`

Logs rotate; older entries appear with numeric suffixes.

## What the engine writes about this mod

| Condition | Likely message character |
|-----------|--------------------------|
| An injection targets a tag that does not exist | Names the tag, the mode, and the file, in the form used by the binary: `You are trying to inject/replace to a non-existing entry: …` |
| The file has no byte-order mark | Encoding or lexer warning naming the file |
| A value is malformed | Parse warning naming the key and file |
| Everything is valid | No line names the file |

The engine writes nothing when a mapping applies successfully. Silence is the success signal.

## Correlation

No correlation identifiers exist, because nothing emits structured events. Correlating a symptom to a cause relies on the country tag and the file name, both of which appear in any relevant log line.

## Redaction

No log line produced by this mod could contain sensitive data: the content is country tags and colour integers.

## Audit logging

None.

## Practical diagnostic procedure

1. Reproduce with `-debug_mode`.
2. Read `error.log` and search for `sc_country_colours`.
3. If the file is named, read the entry it names.
4. If the file is not named, the entry applied; the colour difference is elsewhere — a conditional block, or subject colour inheritance. See [troubleshooting.md](./troubleshooting.md).

## Related documents

- [error-handling.md](./error-handling.md) — failure taxonomy.
- [troubleshooting.md](./troubleshooting.md) — symptom-to-cause table.