# Rendering of every Hearts of Iron IV build artefact.

from pathlib import Path

from config import ENCODING
from games.hoi4.config import (COUNTRIES_DIRECTORY_PATH,
                                COUNTRY_COLOURS_FILENAME,
                                COUNTRY_FILE_HEADER_LINES,
                                COUNTRY_PALETTE_ENTRIES,
                                DESCRIPTOR_FILENAME,
                                LAUNCHER_THUMBNAIL_FILENAME,
                                MOD_NAME,
                                MOD_TAGS,
                                MOD_THUMBNAIL_FILENAME,
                                PARENT_DESCRIPTOR_FILENAME,
                                SUPPORTED_GAME_VERSION)
from palette import to_decimal_components


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
    """Render the country colour overrides."""
    lines = list(COUNTRY_FILE_HEADER_LINES)
    for tag, entry_name in sorted(COUNTRY_PALETTE_ENTRIES.items()):
        if entry_name not in palette:
            raise ValueError(
                f'The tag "{tag}" names the palette entry "{entry_name}", which the palette does not define.')
        source, hexadecimal_colour = palette[entry_name]
        red, green, blue = to_decimal_components(hexadecimal_colour)
        lines.extend([
            '',
            f'# {entry_name} - {hexadecimal_colour} - {source}',
            f'{tag} = {{',
            f'\tcolor = rgb {{ {red} {green} {blue} }}',
            '}',
        ])
    return ('\n'.join(lines) + '\n').encode(ENCODING)


def render_text_files(palette: dict, version: str) -> dict:
    """Return every rendered text artefact."""
    return {
        f'{COUNTRIES_DIRECTORY_PATH}/{COUNTRY_COLOURS_FILENAME}': render_country_colours(palette),
        DESCRIPTOR_FILENAME: build_descriptor(version).encode(ENCODING),
    }


def render_parent_text_files(palette: dict, version: str) -> dict:
    """Return the descriptor placed beside the mod folder."""
    return {PARENT_DESCRIPTOR_FILENAME: build_descriptor(version).encode(ENCODING)}


def render_asset_files(source_directory_path: Path) -> dict:
    """Return copied artwork paths."""
    edition_source_directory_path = source_directory_path / 'hoi4'
    return {
        MOD_THUMBNAIL_FILENAME: edition_source_directory_path / MOD_THUMBNAIL_FILENAME,
        LAUNCHER_THUMBNAIL_FILENAME: edition_source_directory_path / LAUNCHER_THUMBNAIL_FILENAME,
    }
