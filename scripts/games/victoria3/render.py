# Rendering of every Victoria 3 build artefact.
#
# Each function returns the artefacts for one build without touching the
# filesystem, so the shared builder decides where they are written.

import json
import re

from pathlib import Path

from config import BYTE_ORDER_MARK, ENCODING, ICON_FILENAME, PREVIEW_FILENAME

from games.victoria3.config import (CONTENT_DIRECTORY_PATH,
                                    CONTENT_FILENAME,
                                    CONTENT_HEADER_LINES,
                                    COUNTRY_PALETTE_ENTRIES,
                                    GAME_ID,
                                    IS_MULTIPLAYER_SYNCHRONIZED,
                                    METADATA_DIRECTORY_NAME,
                                    METADATA_FILENAME,
                                    MOD_ID,
                                    MOD_NAME,
                                    MOD_TAGS,
                                    MOD_THUMBNAIL_FILENAME,
                                    PICTURE_FILENAME,
                                    SHORT_DESCRIPTION,
                                    SUPPORTED_GAME_VERSION,
                                    VANILLA_COUNTRY_NAMES)

from palette import to_decimal_components

TAG_PATTERN = re.compile(r'^[A-Z0-9]{3}$')


def build_entry_comment(tag: str, entry_name: str, hexadecimal_colour: str,
                        source: str) -> str:
    """Render the provenance comment that precedes an injection block."""
    vanilla_name = VANILLA_COUNTRY_NAMES.get(tag, entry_name)

    if vanilla_name == entry_name:
        return f'# {vanilla_name} - {hexadecimal_colour} - {source}'

    return f'# {vanilla_name} (palette: {entry_name}) - {hexadecimal_colour} - {source}'


def render_content_file(palette: dict) -> bytes:
    """Render the country-definition file, including its byte-order mark."""
    lines = list(CONTENT_HEADER_LINES)

    for tag in sorted(COUNTRY_PALETTE_ENTRIES):
        if not TAG_PATTERN.match(tag):
            raise ValueError(f'The tag "{tag}" is not a three-character key.')

        entry_name = COUNTRY_PALETTE_ENTRIES[tag]

        if entry_name not in palette:
            raise ValueError(
                f'The tag "{tag}" names the palette entry "{entry_name}", which the palette does not define.')

        source, hexadecimal_colour = palette[entry_name]
        red, green, blue = to_decimal_components(hexadecimal_colour)

        lines.append('')
        lines.append(build_entry_comment(tag, entry_name, hexadecimal_colour, source))
        lines.append(f'INJECT:{tag} = {{')
        lines.append(f'\tcolor = {{ {red} {green} {blue} }}')
        lines.append('}')

    text = '\n'.join(lines) + '\n'

    return BYTE_ORDER_MARK + text.encode(ENCODING)


def render_metadata_file(version: str) -> bytes:
    """Render the launcher metadata document."""
    metadata = {
        'name': MOD_NAME,
        'id': MOD_ID,
        'version': version,
        'game_id': GAME_ID,
        'picture': PICTURE_FILENAME,
        'supported_game_version': SUPPORTED_GAME_VERSION,
        'short_description': SHORT_DESCRIPTION,
        'tags': MOD_TAGS,
        'relationships': [],
        'game_custom_data': {
            'multiplayer_synchronized': IS_MULTIPLAYER_SYNCHRONIZED,
        },
    }

    return (json.dumps(metadata, indent=2) + '\n').encode(ENCODING)


def render_text_files(palette: dict, version: str) -> dict:
    """Return every rendered text artefact as relative path -> content."""
    return {
        f'{CONTENT_DIRECTORY_PATH}/{CONTENT_FILENAME}': render_content_file(palette),
        f'{METADATA_DIRECTORY_NAME}/{METADATA_FILENAME}': render_metadata_file(version),
    }


def render_asset_files(source_directory_path: Path) -> dict:
    """Return every copied asset as destination relative path -> source path."""
    return {
        MOD_THUMBNAIL_FILENAME: source_directory_path / ICON_FILENAME,
        f'{METADATA_DIRECTORY_NAME}/{PICTURE_FILENAME}': source_directory_path / PREVIEW_FILENAME,
    }
