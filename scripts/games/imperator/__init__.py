# Imperator: Rome edition of the Standardised Country Colours build.
#
# The module exposes the `EDITION` value that `games/__init__.py` registers.

from games.base import GameEdition
from games.imperator.config import (COUNTRIES_DIRECTORY_PATH,
                                    EDITION_KEY,
                                    MOD_FOLDER_NAME,
                                    MOD_NAME,
                                    OUTPUT_GROUP)
from games.imperator.render import render_asset_files, render_text_files

EDITION = GameEdition(
    key=EDITION_KEY,
    name=MOD_NAME,
    output_group=OUTPUT_GROUP,
    folder_name=MOD_FOLDER_NAME,
    render_text_files=render_text_files,
    asset_files=render_asset_files,
)