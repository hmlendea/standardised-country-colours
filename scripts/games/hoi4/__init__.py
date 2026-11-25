# Hearts of Iron IV edition of the Standardised Country Colours build.

from games.base import GameEdition
from games.hoi4.config import EDITION_KEY, MOD_FOLDER_NAME, MOD_NAME, OUTPUT_GROUP
from games.hoi4.render import (render_asset_files,
                               render_parent_text_files,
                               render_text_files)

EDITION = GameEdition(
    key=EDITION_KEY,
    name=MOD_NAME,
    output_group=OUTPUT_GROUP,
    folder_name=MOD_FOLDER_NAME,
    render_text_files=render_text_files,
    asset_files=render_asset_files,
    parent_text_files=render_parent_text_files,
)
