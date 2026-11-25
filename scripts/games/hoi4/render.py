# Rendering of every Hearts of Iron IV build artefact.

import re

from pathlib import Path

from config import ENCODING, ICON_FILENAME, PREVIEW_FILENAME
from games.hoi4.config import (COUNTRIES_DIRECTORY_PATH,
                                COUNTRY_COLOURS_FILENAME,
                                COUNTRY_PALETTE_ENTRIES,
                                DESCRIPTOR_FILENAME,
                                LAUNCHER_THUMBNAIL_FILENAME,
                                MOD_NAME,
                                MOD_TAGS,
                                MOD_THUMBNAIL_FILENAME,
                                PARENT_DESCRIPTOR_FILENAME,
                                SUPPORTED_GAME_VERSION,
                                VANILLA_COLORS_FILE_PATH,
                                VANILLA_COUNTRIES_DIRECTORY_PATH,
                                COUNTRY_FILE_PATHS)
from palette import to_decimal_components


TAG_HEADER_PATTERN = re.compile(r'^(?P<tag>[A-Z0-9]{3})\s*=\s*\{', re.MULTILINE)
# Matches the `color` key only: `color_ui` is left untouched because the key
# name continues with `_`, which the `\s*=` requirement cannot follow.
COLOR_VALUE_PATTERN = re.compile(
    r'\bcolor\s*=\s*(?:rgb\s*\{[^}]*\}|hsv\s*\{[^}]*\}|\{[^}]*\}|[^\s#]+)',
    re.IGNORECASE)


def build_descriptor(version: str) -> str:
    """Render the descriptor used by the Hearts of Iron IV launcher."""
    lines = [f'name="{MOD_NAME}"', 'tags={']
    lines.extend(f'\t"{tag}"' for tag in MOD_TAGS)
    lines.extend([
        '}',
        f'version="{version}"',
        f'supported_version="{SUPPORTED_GAME_VERSION}"',
        'path="mod/standardised-country-colours"',
    ])
    return '\n'.join(lines) + '\n'


def render_country_colours(palette: dict) -> bytes:
    """Render the hardcoded HOI4 colour table with mapped values substituted.

    Hearts of Iron IV reads country colours from `common/countries/colors.txt`
    at a fixed path, so a differently named file is ignored. The build therefore
    rewrites that file, replacing each mapped tag's `color` while leaving every
    other tag, and every `color_ui`, byte-identical to vanilla.
    """
    replacements = {}
    for tag, entry_name in COUNTRY_PALETTE_ENTRIES.items():
        if entry_name not in palette:
            raise ValueError(
                f'The tag "{tag}" names the palette entry "{entry_name}", which the palette does not define.')
        _, hexadecimal_colour = palette[entry_name]
        red, green, blue = to_decimal_components(hexadecimal_colour)
        replacements[tag] = f'color = rgb {{ {red} {green} {blue} }}'

    text = VANILLA_COLORS_FILE_PATH.read_text(encoding=ENCODING)
    colour_tags = {match.group('tag') for match in TAG_HEADER_PATTERN.finditer(text)}
    replacements = {tag: value for tag, value in replacements.items()
                    if tag in colour_tags}

    rendered_lines = []
    current_tag = None
    replaced_tags = set()

    for line in text.splitlines(keepends=True):
        header = TAG_HEADER_PATTERN.match(line)
        if header:
            current_tag = header.group('tag')
            replaced_tags.add(current_tag)

        if current_tag in replacements:
            line, substitutions = COLOR_VALUE_PATTERN.subn(
                replacements[current_tag], line, count=1)
            if substitutions:
                # The key is handled once per tag, so stop rewriting this block.
                replacements.pop(current_tag)

        if line.rstrip('\r\n') == '}':
            current_tag = None

        rendered_lines.append(line)

    missing = sorted(set(replacements) - replaced_tags)
    if missing:
        raise ValueError(
            f'The vanilla HOI4 colour table has no entries for: {", ".join(missing)}.')

    if replacements:
        raise ValueError(
            f'The vanilla HOI4 colour table has no color key for: {", ".join(sorted(replacements))}.')

    return ''.join(rendered_lines).encode(ENCODING)


def render_country_file(tag: str, palette: dict) -> bytes:
    """Render a per-country file, replacing only its top-level color key."""
    entry_name = COUNTRY_PALETTE_ENTRIES[tag]
    _, hexadecimal_colour = palette[entry_name]
    red, green, blue = to_decimal_components(hexadecimal_colour)
    source_path = VANILLA_COUNTRIES_DIRECTORY_PATH / COUNTRY_FILE_PATHS[tag]
    text = source_path.read_text(encoding=ENCODING)
    replacement = f'color = rgb {{ {red} {green} {blue} }}'
    rendered, substitutions = COLOR_VALUE_PATTERN.subn(replacement, text, count=1)
    if substitutions != 1:
        raise ValueError(f'The vanilla HOI4 country file has no color key for "{tag}".')
    return rendered.encode(ENCODING)


def render_text_files(palette: dict, version: str) -> dict:
    """Return every rendered text artefact."""
    artefacts = {
        f'{COUNTRIES_DIRECTORY_PATH}/{COUNTRY_COLOURS_FILENAME}': render_country_colours(palette),
        DESCRIPTOR_FILENAME: build_descriptor(version).encode(ENCODING),
    }
    for tag in sorted(COUNTRY_FILE_PATHS):
        artefacts[f'{COUNTRIES_DIRECTORY_PATH}/{COUNTRY_FILE_PATHS[tag]}'] = (
            render_country_file(tag, palette))
    return artefacts


def render_parent_text_files(palette: dict, version: str) -> dict:
    """Return the descriptor placed beside the mod folder."""
    return {PARENT_DESCRIPTOR_FILENAME: build_descriptor(version).encode(ENCODING)}


def render_asset_files(source_directory_path: Path) -> dict:
    """Return copied artwork paths."""
    return {
        MOD_THUMBNAIL_FILENAME: source_directory_path / ICON_FILENAME,
        LAUNCHER_THUMBNAIL_FILENAME: source_directory_path / PREVIEW_FILENAME,
    }
