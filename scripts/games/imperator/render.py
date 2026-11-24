# Rendering of every Imperator: Rome build artefact.
#
# Each function returns the artefacts for one build without touching the
# filesystem, so the shared builder decides where they are written.
#
# Imperator: Rome does not support VICTORIA-style `INJECT:*` keyword injection,
# so colour overrides ship as per-country `setup/countries/<TAG>.txt` files
# holding `color = rgb { R G B }`. Each per-country file replaces only its own
# colour values while the rest of the country block (government, capital,
# cultures...) stays owned by `setup/main/<TAG>` in the vanilla game, so nothing
# besides the map colour is touched. The tag-to-file index lives in
# `setup/countries/countries.txt`, which is regenerated wholesale with every
# build so that every shipped tag remains listed.

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
                                    MOD_THUMBNAIL_FILENAME,
                                    SUPPORTED_GAME_VERSION)

from palette import to_decimal_components


def build_country_file(tag: str, entry_name: str, hexadecimal_colour: str,
                       source: str) -> str:
    """Render one `setup/countries/<TAG>.txt` colour file."""
    lines = list(COUNTRY_FILE_HEADER_LINES)

    lines.append('')
    lines.append(f'# Vanilla tag: {tag}')
    lines.append(f'# Palette entry: {entry_name}')
    lines.append(f'# Primary colour: {hexadecimal_colour} - {source}')
    lines.append('')

    if hexadecimal_colour:
        red, green, blue = to_decimal_components(hexadecimal_colour)
        lines.append(f'color = rgb {{ {red} {green} {blue} }}')

    text = '\n'.join(lines) + '\n'
    return text


def render_text_files(palette: dict, version: str) -> dict:
    """Return every rendered text artefact as relative path -> content."""
    artefacts = {}

    entries = sorted(COUNTRY_PALETTE_ENTRIES.items())

    for tag, entry_name in entries:
        if entry_name not in palette:
            raise ValueError(
                f'The tag "{tag}" names the palette entry "{entry_name}", which the palette does not define.')

        source, hexadecimal_colour = palette[entry_name]

        artefacts[f'{COUNTRIES_DIRECTORY_PATH}/{tag}{COUNTRY_FILE_EXTENSION}'] = (
            build_country_file(tag, entry_name, hexadecimal_colour, source)
            .encode(ENCODING))

    # The tag index is regenerated wholesale so every shipped tag remains listed.
    index_lines = [
        '# Standardised Country Colours',
        '#',
        '# Tag -> colour file index. Each entry names a file under',
        '# setup/countries/ whose colour keys this mod injects.',
        '#',
    ]

    for tag in sorted(COUNTRY_PALETTE_ENTRIES):
        index_lines.append(f'{tag} = "{COUNTRIES_DIRECTORY_PATH}/{tag}{COUNTRY_FILE_EXTENSION}"')

    artefacts[f'{COUNTRIES_DIRECTORY_PATH}/{COUNTRIES_INDEX_FILENAME}'] = (
        ('\n'.join(index_lines) + '\n').encode(ENCODING))

    # Launcher descriptor.
    descriptor = [
        'name="{}"'.format(MOD_NAME),
        'legacy_spec = no',
        'supported_version = "{}"'.format(SUPPORTED_GAME_VERSION),
        f'path = "mod/{MOD_FOLDER_NAME}"',
    ]
    artefacts[DESCRIPTOR_FILENAME] = ('\n'.join(descriptor) + '\n').encode(ENCODING)

    return artefacts


def render_asset_files(source_directory_path: Path) -> dict:
    """Return every copied asset as destination relative path -> source path."""
    edition_source_directory_path = source_directory_path / 'imperator'

    return {
        MOD_THUMBNAIL_FILENAME: edition_source_directory_path / MOD_THUMBNAIL_FILENAME,
    }
