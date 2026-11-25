# Shared build configuration for the Standardised Country Colours project.
#
# The values here are common to every game edition. Game-specific identity,
# mappings, and output layout live in the matching module under `games/`.

# --- Source paths ---

SOURCE_DIRECTORY_NAME = 'src'
PALETTE_FILENAME = 'colours.md'

# Vanilla game data that the build reads is vendored under this directory, so a
# build needs no game installation and works on any machine, including CI.
VANILLA_DIRECTORY_NAME = 'vanilla'

# --- Output ---

DEFAULT_OUTPUT_DIRECTORY = 'out'

# --- Encoding ---

ENCODING = 'utf-8'
# Every shipped text artefact carries a byte-order mark, and it is written
# explicitly to keep the output identical on every platform.
BYTE_ORDER_MARK = b'\xef\xbb\xbf'
