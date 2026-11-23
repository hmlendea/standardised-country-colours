# Error handling

The repository cannot catch, retry, or recover from anything. Every failure originates in the engine or the launcher, is reported there, and either suppresses the affected change or the whole mod.

## Failure taxonomy

| ID | Failure | Origin | Detection | Effect | Recovery |
|----|---------|--------|-----------|--------|----------|
| E1 | `.metadata/metadata.json` absent | Packaging | Launcher does not list the mod | No change of any kind | Extract the folder correctly |
| E2 | `metadata.json` invalid JSON | Authoring | Launcher does not list the mod | No change of any kind | Fix the JSON; comments are not permitted |
| E3 | `game_id` wrong | Authoring | Mod may not be associated with Victoria 3 | Mod not loadable | Set `victoria3` |
| E4 | `supported_game_version` excludes the build | Version drift | Launcher flags the mod as outdated | No change until the user forces it | Widen or bump the range |
| E5 | `picture` names a missing file | Authoring | Mod listed without artwork | Cosmetic only | Add the file or fix the name |
| E6 | File saved without a byte-order mark | Authoring | `error.log` encoding warning | File may not be read at all | Rewrite as UTF-8 with BOM |
| E7 | Injection target absent | Game patch retired a tag | `error.log` line naming the tag | That one injection skipped | Remove or retarget the entry |
| E8 | Malformed `color` value | Authoring | `error.log` parse warning | That injection discarded; vanilla colour stands | Fix the value |
| E9 | Another mod `REPLACE:`s the same tag | Compatibility | The other colour appears | This mod's colour is not shown for that tag | Accept, or provide a compatibility patch mod |
| E10 | Conditional map-colour block matches | Game design | The conditional colour appears | This mod's colour is not shown while the trigger holds | Intentional; no action |
| E11 | Subject inherits the overlord colour | Game design | Overlord colour on subject territory | This mod's colour is not shown on the map | Intentional; change the game rule if unacceptable |
| E12 | File name collides with a vanilla file | Authoring | Vanilla definitions missing | Catastrophic: many countries lose their definitions | Rename the file |

## Severity

| Severity | IDs | Character |
|----------|-----|-----------|
| Catastrophic | E12 | Destroys unrelated vanilla content |
| Blocking | E1, E2, E3, E6 | The mod does nothing |
| Degrading | E4, E7, E8 | One mapping or a version gate is lost |
| Cosmetic | E5 | Presentation only |
| Intended | E10, E11 | Base-game behaviour the mod deliberately does not override |
| Compatibility | E9 | Outside repository control |

## Why nothing is retried

There is no execution model to retry. The engine reads the file once at start-up and composes the definitions. A failed injection is not queued; it is logged and abandoned.

## Why most failures are silent

A wrong colour is not an error condition: the engine cannot know that `#000099` was meant for France and not for Italy. Only structural problems — a missing target, a malformed value, a bad encoding — are detectable, and only those reach the log. Consequently:

- the primary authoring risk is a **wrong but valid** value, which no tool will flag;
- the verification strategy must therefore be structural checks plus in-game inspection, as described in [testing.md](./testing.md).

## Authoring safeguards that substitute for error handling

| Safeguard | Prevents |
|-----------|----------|
| Resolve every tag against the installed definitions | E7 |
| Convert hex to decimal arithmetically, never by eye | E8 |
| Write the file with a UTF-8 BOM | E6 |
| Keep the file name unique in its folder | E12 |
| Validate the metadata as JSON | E2 |
| Keep the tag's localised name in the comment | Silent mis-mapping |

## Related documents

- [troubleshooting.md](./troubleshooting.md) — symptom-driven diagnosis.
- [logging.md](./logging.md) — where failures appear.
- [invariants.md](./invariants.md) — the properties the safeguards defend.