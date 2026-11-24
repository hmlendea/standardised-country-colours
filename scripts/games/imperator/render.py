# Rendering of every Imperator: Rome build artefact.
#
# Each function returns the artefacts for one build without touching the
# filesystem, so the shared builder decides where they are written.
#
# Imperator: Rome does not support VICTORIA-style `INJECT:*` keyword injection,
# so colour overrides ship as per-country `setup/countries/<TAG>.txt` files
# holding `color = rgb { R G B }`. A per-country file fully replaces the
# vanilla one of the same tag, so the build preserves what would otherwise be
# lost: every vanilla entry in `setup/countries/countries.txt` (dropping one
# breaks startup because provinces whose owner tag is absent cannot be
# resolved) and each shipped country's `ship_names` block. Only the colour of
# the shipped tags changes; everything else stays byte-identical to vanilla.

from pathlib import Path

from config import BYTE_ORDER_MARK, ENCODING

from games.imperator.config import (COUNTRY_FILE_EXTENSION,
                                    COUNTRY_FILE_HEADER_LINES,
                                    COUNTRY_PALETTE_ENTRIES,
                                    COUNTRIES_DIRECTORY_PATH,
                                    COUNTRIES_INDEX_FILENAME,
                                    DESCRIPTOR_FILENAME,
                                    MOD_FOLDER_NAME,
                                    MOD_NAME,
                                    MOD_TAGS,
                                    MOD_THUMBNAIL_FILENAME,
                                    PARENT_DESCRIPTOR_FILENAME,
                                    SHIP_NAMES_FOOTER,
                                    SHIP_NAMES_HEADER,
                                    SUPPORTED_GAME_VERSION,
                                    VANILLA_COUNTRIES_DIR,
                                    VANILLA_COUNTRIES_INDEX,
                                    VANILLA_COUNTRY_NAMES,
                                    VANILLA_TAG_INDEX_PATTERN)

from palette import to_decimal_components


def build_descriptor(version: str) -> str:
    """Render the mod descriptor the launcher reads, in its canonical form."""
    lines = [
        f'version="{version}"',
        f'name="{MOD_NAME}"',
        'tags={',
    ]
    for tag in MOD_TAGS:
        lines.append(f'\t"{tag}"')
    lines.append('}')
    lines.append(f'supported_version="{SUPPORTED_GAME_VERSION}"')
    lines.append(f'path="mod/{MOD_FOLDER_NAME}"')

    return '\n'.join(lines) + '\n'


def read_vanilla_tag_path(tag: str) -> str:
    """Return the vanilla countries-index path for a tag, e.g. `italia/rome.txt`."""
    for line in Path(VANILLA_COUNTRIES_INDEX).read_text(encoding=ENCODING).splitlines():
        match = VANILLA_TAG_INDEX_PATTERN.match(line)
        if not match or match.group(1) != tag:
            continue
        relative = line.split('"')[1]
        return relative.split('setup/countries/', 1)[1]
    raise FileNotFoundError(f'Vanilla country index has no entry for tag "{tag}".')


def read_vanilla_country_file(tag: str) -> str:
    """Return the vanilla `setup/countries/<FILE>` content for a tag.

    Imperator replaces the whole file when a tag reads one, so the mod must
    carry over anything the colour override would otherwise drop.
    """
    vanilla_path = f'{VANILLA_COUNTRIES_DIR}/{read_vanilla_tag_path(tag)}'
    return Path(vanilla_path).read_text(encoding=ENCODING)


def extract_block(text: str, header: str, footer: str) -> str:
    """Return the verbatim lines of a brace-delimited block, if present."""
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip().startswith(header):
            for end in range(index + 1, len(lines)):
                if lines[end].strip() == footer:
                    return '\n'.join(lines[index:end + 1])
    return ''


def extract_color2(text: str) -> str:
    """Return the vanilla `color2` line (or the commented original), else white."""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('#color2 = '):
            return stripped[len('#'):].strip()
        if stripped.startswith('color2 = '):
            return stripped
    return 'color2 = rgb { 255 255 255 }'


def build_country_file(tag: str, entry_name: str, hexadecimal_colour: str,
                       source: str, original_file_text: str) -> str:
    """Render one `setup/countries/<TAG>.txt` colour file."""
    lines = list(COUNTRY_FILE_HEADER_LINES)

    lines.append('')
    vanilla_name = VANILLA_COUNTRY_NAMES.get(tag, entry_name)
    comment = vanilla_name
    if vanilla_name != entry_name:
        comment += f' (palette: {entry_name})'
    lines.append(f'# {comment}')
    lines.append(f'# {hexadecimal_colour} - {source}')
    lines.append('')

    red, green, blue = to_decimal_components(hexadecimal_colour)
    lines.append(f'color = rgb {{ {red} {green} {blue} }}')

    # A per-country file replaces the whole vanilla one, so the ship_names block
    # and the vanilla color2 are carried over; otherwise the tag loses them.
    ship_names_block = extract_block(original_file_text, SHIP_NAMES_HEADER, SHIP_NAMES_FOOTER)
    if ship_names_block:
        lines.append('')
        lines.extend(ship_names_block.splitlines())

    lines.append('')
    lines.append(extract_color2(original_file_text))

    return '\n'.join(lines) + '\n'


def render_text_files(palette: dict, version: str) -> dict:
    """Return every rendered text artefact as relative path -> content."""
    artefacts = {}

    for tag, entry_name in sorted(COUNTRY_PALETTE_ENTRIES.items()):
        if entry_name not in palette:
            raise ValueError(
                f'The tag "{tag}" names the palette entry "{entry_name}", which the palette does not define.')

        source, hexadecimal_colour = palette[entry_name]
        original_file_text = read_vanilla_country_file(tag)

        # Each override goes to the exact vanilla path the tag already uses, so
        # the preserved countries.txt resolves it without any index rewrite.
        artefacts[f'{COUNTRIES_DIRECTORY_PATH}/{read_vanilla_tag_path(tag)}'] = (
            build_country_file(tag, entry_name, hexadecimal_colour, source, original_file_text)
            .encode(ENCODING))

    # Every vanilla tag entry is preserved so that provinces whose owner tag is
    # absent cannot crash the game on startup; the shipped tags already point at
    # the files this mod rewrites.
    artefacts[f'{COUNTRIES_DIRECTORY_PATH}/{COUNTRIES_INDEX_FILENAME}'] = (
        Path(VANILLA_COUNTRIES_INDEX).read_text(encoding=ENCODING).encode(ENCODING))

    # The inner descriptor is a copy of the sibling one, so the launcher finds a
    # descriptor inside the folder it resolves as well.
    artefacts[DESCRIPTOR_FILENAME] = build_descriptor(version).encode(ENCODING)

    return artefacts


def render_parent_text_files(palette: dict, version: str) -> dict:
    """Return the artefacts that sit beside the mod folder, not inside it."""
    return {
        PARENT_DESCRIPTOR_FILENAME: build_descriptor(version).encode(ENCODING),
    }


def render_asset_files(source_directory_path: Path) -> dict:
    """Return every copied asset as destination relative path -> source path."""
    edition_source_directory_path = source_directory_path / 'imperator'

    return {
        MOD_THUMBNAIL_FILENAME: edition_source_directory_path / MOD_THUMBNAIL_FILENAME,
    }
