# Testing

## There is no test suite

The repository has no test project, no test runner, and no CI test job. Verification is structural auditing plus in-game inspection.

## Structural audit

Run against an installed game. Every assertion below maps to an invariant in [invariants.md](./invariants.md).

```bash
python3 - <<'PY'
import glob, re

GAME = "/path/to/Victoria 3/game"
MOD = "standardised-country-colours/common/country_definitions/sc_country_colours.txt"

raw = open(MOD, "rb").read()
assert raw[:3] == b"\xef\xbb\xbf", "C8: missing BOM"

text = raw.decode("utf-8-sig")
assert text.count("{") == text.count("}"), "C7: unbalanced braces"

blocks = re.findall(
    r"^# (.+?) - (#[0-9A-F]{6}) - (.+?)\nINJECT:([A-Z0-9]{3}) = \{\n\tcolor = \{ (\d+) (\d+) (\d+) \}\n\}",
    text, re.M,
)
assert blocks, "C1/C6: no commented injections parsed"

tags = [b[3] for b in blocks]
assert len(tags) == len(set(tags)), "C5: duplicate tag"
assert tags == sorted(tags), "C5: tags out of order"
assert all(0 <= int(v) <= 255 for b in blocks for v in b[4:]), "C3: component out of range"

vanilla = set()
for path in glob.glob(GAME + "/common/country_definitions/*.txt"):
    body = open(path, encoding="utf-8", errors="replace").read().lstrip("\ufeff")
    vanilla |= {m.group(1) for m in re.finditer(r"^([A-Z0-9]{3})\s*=\s*\{", body, re.M)}

missing = [t for t in tags if t not in vanilla]
assert not missing, f"C2: unknown tags {missing}"

# C4: each block body holds exactly one color line
bodies = re.findall(r"INJECT:[A-Z0-9]{3} = \{\n(.*?)\n\}", text, re.S)
assert all(len([l for l in b.splitlines() if l.strip()]) == 1 for b in bodies), "C4: extra keys"

print(f"ok: {len(blocks)} entries, {len(missing)} unknown tags")
PY
```

Expected output for the shipped content: `ok: 89 entries, 0 unknown tags`.

## Comment-versus-value consistency

The comment hexadecimal value and the decimal triple must agree. This is a review invariant (C6) with no runtime effect, but a mismatch destroys the file's value as documentation.

```bash
python3 - <<'PY'
import re
text = open("standardised-country-colours/common/country_definitions/sc_country_colours.txt",
            encoding="utf-8-sig").read()
entries = re.findall(
    r"^# .+? - #([0-9A-F]{6}) - .+?\nINJECT:([A-Z0-9]{3}) = \{\n\tcolor = \{ (\d+) (\d+) (\d+) \}\n\}",
    text, re.M)
mismatched = [tag for hexv, tag, r, g, b in entries
              if (int(hexv[0:2], 16), int(hexv[2:4], 16), int(hexv[4:6], 16))
                 != (int(r), int(g), int(b))]
print("mismatched:", mismatched)
PY
```

Expected: `mismatched: []`.

## Redundancy audit

A mapping that equals its vanilla value is harmless but changes nothing. The shipped set contains exactly one:

```bash
python3 - <<'PY'
import colorsys, glob, re

GAME = "/path/to/Victoria 3/game"
MOD = "standardised-country-colours/common/country_definitions/sc_country_colours.txt"

named = {}
for path in glob.glob(GAME + "/common/named_colors/*.txt"):
    body = open(path, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"^\s*([A-Za-z0-9_]+)\s*=\s*(hsv360?\s*\{[^}]*\}|rgb\s*\{[^}]*\}|\{[^}]*\})", body, re.M):
        named.setdefault(m.group(1), m.group(2))

def to_rgb(expr):
    e = expr.strip()
    m = re.fullmatch(r'"([A-Za-z0-9_]+)"', e)
    if m:
        e = named.get(m.group(1), "")
    m = re.fullmatch(r"hsv360\s*\{\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\}", e)
    if m:
        h, s, v = (float(x) for x in m.groups())
        return tuple(round(x * 255) for x in colorsys.hsv_to_rgb(h / 360, s / 100, v / 100))
    m = re.fullmatch(r"hsv\s*\{\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\}", e)
    if m:
        return tuple(round(x * 255) for x in colorsys.hsv_to_rgb(*(float(x) for x in m.groups())))
    m = re.fullmatch(r"(?:rgb\s*)?\{\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\}", e)
    if m:
        v = [float(x) for x in m.groups()]
        return tuple(round(x * 255) for x in v) if all(x <= 1 for x in v) else tuple(round(x) for x in v)
    return None

vanilla = {}
for path in glob.glob(GAME + "/common/country_definitions/*.txt"):
    body = re.sub(r"#[^\n]*", "", open(path, encoding="utf-8", errors="replace").read().lstrip("\ufeff"))
    for m in re.finditer(r"^([A-Z0-9]{3})\s*=\s*\{(.*?)^\}", body, re.M | re.S):
        c = re.search(r"color\s*=\s*([^\n]+)", m.group(2))
        if c and m.group(1) not in vanilla:
            vanilla[m.group(1)] = to_rgb(c.group(1))

text = open(MOD, encoding="utf-8-sig").read()
entries = re.findall(r"INJECT:([A-Z0-9]{3}) = \{\n\tcolor = \{ (\d+) (\d+) (\d+) \}\n\}", text)
equal = [t for t, r, g, b in entries if vanilla.get(t) == (int(r), int(g), int(b))]
near = [(t, max(abs(a - b) for a, b in zip((int(r), int(g), int(b)), vanilla[t])))
        for t, r, g, b in entries if t in vanilla and vanilla[t] and vanilla[t] != (int(r), int(g), int(b)) and max(abs(a - b) for a, b in zip((int(r), int(g), int(b)), vanilla[t])) <= 8]
print("equal to vanilla:", equal)
print("within 8 units:", near)
PY
```

Expected result for the shipped content: `equal to vanilla: ['SCA']`, `within 8 units: [('APC', 3)]`.

This audit exists to catch an accidental duplicate introduced during authoring, not to enforce a rule.

## Metadata audit

```bash
python3 -c "import json;d=json.load(open('standardised-country-colours/.metadata/metadata.json'));print(d['game_id'],d['version'],d['supported_game_version'],d['picture'])"
test -f standardised-country-colours/.metadata/thumbnail.png
test -f standardised-country-colours/thumbnail.png
```

Expected: `victoria3 1.0.0 1.15.* thumbnail.png` followed by two successful file tests.

## Workflow audit

```bash
python3 ~/.copilot/skills/github-actions-workflow/validate_github_actions.py \
  --variant mod . github-release.yml .github/workflows/github-release.yml

python3 ~/.copilot/skills/github-actions-workflow/validate_github_actions.py \
  . steam-workshop-release.yml .github/workflows/steam-workshop-release.yml

python3 ~/.copilot/skills/github-actions-workflow/validate_github_actions.py \
  . nexus-mods-release.yml .github/workflows/nexus-mods-release.yml
```

Expected: `VALIDATION PASSED: 100% template fidelity confirmed` for each workflow.

## In-game verification

| Check | Procedure | Pass condition |
|-------|-----------|----------------|
| Start-date colour | Start a campaign, open the map | France is `#000099`; Denmark is `#C8102E` |
| Release-only colour | Release Babylon | Babylon appears in `#2B5162` |
| Formable colour | Form Italy, or spawn it in debug mode | Italy appears in `#F4E3A0` |
| No regressions | Inspect an unmapped country | It keeps its vanilla colour |
| Log cleanliness | Read `error.log` | No line names `sc_country_colours.txt` |
| Unit colours untouched | Start a war | Soldier uniforms match vanilla |

## Coverage gaps

| Gap | Consequence |
|-----|-------------|
| No automated test suite | A regression is caught only by manual audit |
| No reference-image comparison | A wrong-but-valid colour passes every structural check |
| Conditional colours never suppressed in tests | A player may attribute an intended conditional colour to a mod failure |
| Engine behaviour verifiable only on a licensed install | The repository cannot be validated in isolation |
| No assertion that a mapping is *desirable* | Only that it is structurally valid and tag-resolvable |

## Related documents

- [invariants.md](./invariants.md) — the properties under test.
- [troubleshooting.md](./troubleshooting.md) — diagnosing a failure.
- [change-guide.md](./change-guide.md) — the workflow this supports.