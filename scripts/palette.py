# Shared reader for the Standardised Country Colours palette document.
#
# The palette is one external table shared by every game edition, so this
# module holds no game-specific behaviour.

import re

from pathlib import Path

from config import ENCODING

PALETTE_SECTION_TITLE = 'Principal Colours'
HEXADECIMAL_PATTERN = re.compile(r'^#[0-9A-Fa-f]{6}$')


def load_palette(palette_file_path: Path) -> dict:
    """Read the palette into `entry name -> (source, #RRGGBB)`.

    Only the Principal Colours table is read; the Alternative Colours table
    records values from other games and is not a shipped source.
    """
    if not palette_file_path.is_file():
        raise FileNotFoundError(f'The palette file is missing: {palette_file_path}')

    try:
        text = palette_file_path.read_text(encoding=ENCODING, errors='replace')
    except OSError as exception:
        raise OSError(f'Cannot read the palette file: {exception}') from exception

    palette = {}
    is_inside_principal_table = False

    for line in text.splitlines():
        if line.startswith('## '):
            is_inside_principal_table = line[3:].strip() == PALETTE_SECTION_TITLE
            continue

        if not is_inside_principal_table or not line.startswith('|'):
            continue

        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(cells) < 4:
            continue

        entry_name = cells[0]
        source = cells[2]
        primary_colour = cells[3]

        if entry_name == 'Country' or set(entry_name) <= {'-'}:
            continue

        if not HEXADECIMAL_PATTERN.match(primary_colour):
            continue

        if entry_name in palette:
            raise ValueError(f'The palette defines "{entry_name}" twice.')

        # The palette pads some attributions with a second space; the mod
        # records them with single spacing.
        palette[entry_name] = (re.sub(r'\s+', ' ', source).strip(), primary_colour.upper())

    if not palette:
        raise ValueError('The palette contains no Principal Colours rows.')

    return palette


def to_decimal_components(hexadecimal_colour: str) -> tuple:
    """Convert `#RRGGBB` into a red, green, blue triple of integers 0-255."""
    hexadecimal_digits = hexadecimal_colour[1:]
    red = int(hexadecimal_digits[0:2], 16)
    green = int(hexadecimal_digits[2:4], 16)
    blue = int(hexadecimal_digits[4:6], 16)

    return red, green, blue
