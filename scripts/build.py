#!/usr/bin/env python3
# Builds the Standardised Country Colours mod for one or more game editions.
#
# The build is game-agnostic: each edition under `games/` declares its own
# identity, palette mappings, and output layout, and this entry point only
# selects them and delegates. Its output is byte-identical to the mod folder
# tracked in the repository.

import argparse
import sys

from pathlib import Path

from builder import build_edition
from config import (DEFAULT_OUTPUT_DIRECTORY,
                    PALETTE_FILENAME,
                    SOURCE_DIRECTORY_NAME)
from games import EDITIONS
from palette import load_palette

REPOSITORY_ROOT_PATH = Path(__file__).resolve().parent.parent
SOURCE_DIRECTORY_PATH = REPOSITORY_ROOT_PATH / SOURCE_DIRECTORY_NAME
PALETTE_FILE_PATH = SOURCE_DIRECTORY_PATH / PALETTE_FILENAME


def parse_arguments() -> argparse.Namespace:
    """Parse the command line: a mandatory game, an output directory, a version."""
    parser = argparse.ArgumentParser(
        description='Build the Standardised Country Colours mod for one game.')
    parser.add_argument(
        '-g', '--game',
        dest='game_keys',
        action='append',
        required=True,
        choices=sorted(EDITIONS),
        help='Game edition to build; repeatable. Required.')
    parser.add_argument(
        '-o', '--out', '--output',
        dest='output_directory_path',
        default=DEFAULT_OUTPUT_DIRECTORY,
        help=f'Directory that receives the built mod folders (default: {DEFAULT_OUTPUT_DIRECTORY}/).')
    parser.add_argument(
        '-v', '--ver', '--version',
        dest='version',
        required=True,
        help='Version of the mod, recorded in the launcher metadata.')

    return parser.parse_args()


def resolve_editions(game_keys: list) -> list:
    """Return the requested editions from the supplied game keys."""
    return [EDITIONS[game_key] for game_key in game_keys]


def main() -> int:
    """Build the requested editions and report the result."""
    arguments = parse_arguments()
    output_directory_path = Path(arguments.output_directory_path).resolve()

    try:
        palette = load_palette(PALETTE_FILE_PATH)

        for edition in resolve_editions(arguments.game_keys):
            mod_directory_path = build_edition(edition, palette, SOURCE_DIRECTORY_PATH,
                                               output_directory_path, arguments.version)
            print(f'Built {edition.name} {arguments.version} into "{mod_directory_path}".')
    except (OSError, ValueError) as exception:
        print(f'[ERROR] {exception}', file=sys.stderr)

        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())