# Contract that every Standardised Country Colours game edition implements.
#
# A game edition owns its own identity, palette mappings, output layout, and
# file rendering. The shared builder and command line depend only on this
# contract, so adding a game means dropping in one module under `games/` and
# registering it in `games/__init__.py`.

from dataclasses import dataclass

from pathlib import Path

from typing import Callable

# Renders every text artefact for one build into relative path -> content.
# The palette maps a palette entry name to `(source, #RRGGBB)`.
RenderTextFiles = Callable[[dict, str], dict]
# Maps a destination relative path to the source asset it is copied from.
AssetFiles = Callable[[Path], dict]


@dataclass(frozen=True)
class GameEdition:
    """Everything the shared builder needs to render one game edition.

    Attributes:
        key: Short identifier used to select the edition on the command line.
        name: Human-readable edition name, used only in messages.
        output_group: Directory under the output root that the edition writes to,
            so each game's mod folders stay grouped.
        folder_name: Name of the mod folder the build produces.
        render_text_files: Returns relative path -> bytes for the version.
        asset_files: Returns destination relative path -> source path.
    """

    key: str
    name: str
    output_group: str
    folder_name: str
    render_text_files: RenderTextFiles
    asset_files: AssetFiles
