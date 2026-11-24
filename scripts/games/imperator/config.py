# Build configuration that is specific to the Imperator: Rome edition.
#
# Identity, output layout, and the palette mapping for every shipped tag live
# here. Shared values are imported from the top-level `config` module.

# --- Identity ---

EDITION_KEY = 'imperator'
OUTPUT_GROUP = 'imperator'
MOD_FOLDER_NAME = 'standardised-country-colours'
MOD_NAME = 'Standardised Country Colours'
SUPPORTED_GAME_VERSION = '2.0.*'
MOD_TAGS = ['Historical', 'Map']
MOD_THUMBNAIL_FILENAME = 'thumbnail.png'

# --- Source paths ---

# The artwork inputs live under `src/<edition key>/`, so each game edition owns
# its own assets without colliding with another edition's.
LAUNCHER_THUMBNAIL_FILENAME = 'launcher-thumbnail.png'

# --- Output paths ---

DESCRIPTOR_FILENAME = 'descriptor.mod'
COUNTRIES_DIRECTORY_PATH = 'setup/countries'
COUNTRIES_INDEX_FILENAME = 'countries.txt'
COUNTRY_FILE_EXTENSION = '.txt'

# --- Content header ---

COUNTRY_FILE_HEADER_LINES = [
    '# Standardised Country Colours',
    '#',
    '# Replaces the map colour of this country with the standardised value',
    '# documented in src/colours.md. Only the colour keys are emitted, so the',
    '# game keeps every other value of the vanilla country file.',
    '#',
    '# Each file records the vanilla country name, the hexadecimal palette colour,',
    '# and the palette source. Where the palette entry name differs from the',
    '# vanilla name, the palette name is appended in parentheses. Imperator: Rome',
    '# exposes a primary and a secondary map colour, so both palette colours are',
    '# applied.',
]

# --- Country mappings ---

# Every shipped tag, mapped to the palette entry that supplies its colour. The
# palette is the external Standardised Country Colours table; a tag is chosen so
# the palette entry name matches the country's vanilla localised name.
COUNTRY_PALETTE_ENTRIES = {
    'ALB': 'Albania',
    'ARM': 'Armenia',
    'CAR': 'Carthage',
    'EGY': 'Egypt',
    'EPI': 'Epirus',
    'MAU': 'Mauretania',
    'PAR': 'Parthia',
    'PON': 'Pontus',
    'ROM': 'Rome',
    'SCY': 'Scythia',
    'SRM': 'Sarmatia',
    'TRE': 'Thrace',
}

# Tags whose vanilla localised name differs from the palette entry name. The
# difference is recorded in each block's comment as `(palette: <entry>)`.
VANILLA_COUNTRY_NAMES = {
    # Every mapping currently matches its palette entry name exactly.
}
