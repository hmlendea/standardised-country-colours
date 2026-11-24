# Shared build engine for the Standardised Country Colours project.
#
# The engine is game-agnostic: it asks an edition for the artefacts to write
# and copies the assets the edition names, so a new game needs no change here.

import shutil

from pathlib import Path

from games.base import GameEdition


def write_file(file_path: Path, content: bytes) -> None:
    """Write a build artefact, creating its parent directory when required."""
    file_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        file_path.write_bytes(content)
    except OSError as exception:
        raise OSError(f'Cannot write "{file_path}": {exception}') from exception


def copy_file(source_path: Path, destination_path: Path) -> None:
    """Copy a binary artefact into the built mod folder."""
    if not source_path.is_file():
        raise FileNotFoundError(f'The source file is missing: {source_path}')

    destination_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        shutil.copyfile(source_path, destination_path)
    except OSError as exception:
        raise OSError(f'Cannot copy "{source_path}": {exception}') from exception


def build_edition(edition: GameEdition, palette: dict, source_directory_path: Path,
                  output_directory_path: Path, version: str) -> Path:
    """Build one game edition and return the path of the mod folder it wrote."""
    mod_directory_path = output_directory_path / edition.folder_name

    # Starting from scratch guarantees that no file from an earlier build survives.
    if mod_directory_path.exists():
        try:
            shutil.rmtree(mod_directory_path)
        except OSError as exception:
            raise OSError(f'Cannot clear "{mod_directory_path}": {exception}') from exception

    for relative_path, content in edition.render_text_files(palette, version).items():
        write_file(mod_directory_path / relative_path, content)

    for relative_path, asset_source_path in edition.asset_files(source_directory_path).items():
        copy_file(asset_source_path, mod_directory_path / relative_path)

    return mod_directory_path
