# Build configuration that is specific to the Imperator: Rome edition.
#
# Identity, output layout, and the palette mapping for every shipped tag live
# here. Shared values are imported from the top-level `config` module.

import re

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

# Vanilla paths. Imperator replaces the whole per-country file when a tag reads
# one, so a colour override must carry over the vanilla `ship_names` (and the
# commented `#color2`) of the tag it replaces; otherwise the tag's ship name
# pool is lost. Likewise `setup/countries/countries.txt` must keep every
# vanilla tag entry — truncating it to the shipped tags makes provinces whose
# owner tag is absent crash the game on startup.
VANILLA_COUNTRIES_INDEX = '/home/horatiu/.steam/steam/steamapps/common/ImperatorRome/game/setup/countries/countries.txt'
VANILLA_COUNTRIES_DIR = '/home/horatiu/.steam/steam/steamapps/common/ImperatorRome/game/setup/countries'
VANILLA_TAG_INDEX_PATTERN = re.compile(r'^\s*([A-Z0-9]{3})\s*=\s*"([^"]+)"')

# The ship_names block is preserved verbatim so the country keeps its exact
# fleet roster. A per-country file drops the block when omitted; carrying it
# over keeps the tag's identity intact.
SHIP_NAMES_HEADER = 'ship_names = {'
SHIP_NAMES_FOOTER = '}'

# --- Output paths ---

# Imperator: Rome identifies a mod by a descriptor that sits *beside* the mod
# folder, named after it, plus a copy inside the folder. The sibling file is
# what the launcher reads; the inner one is what the launcher rewrites on
# upload, so both are emitted with the same content.
DESCRIPTOR_FILENAME = 'descriptor.mod'
PARENT_DESCRIPTOR_FILENAME = f'{MOD_FOLDER_NAME}.mod'
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
    'BOA': 'Czechia',
    'BYZ': 'Eastern Roman Empire',
    'CAR': 'Carthage',
    'EGY': 'Egypt',
    'EPI': 'Epirus',
    'MAU': 'Mauretania',
    'MAC': 'Macedonia',
    'MRY': 'India',
    'PAR': 'Parthia',
    'PON': 'Pontus',
    'ROM': 'Rome',
    'SCY': 'Scythia',
    'SEL': 'Seleucia',
    'SXS': 'Frisia',
    'SRM': 'Sarmatia',
    'TRE': 'Thrace',
}

# Tags whose vanilla localised name differs from the palette entry name. The
# difference is recorded in each block's comment as `(palette: <entry>)`.
VANILLA_COUNTRY_NAMES = {
    'BOA': 'Boihaemia',
    'BYZ': 'Byzantion',
    'MAC': 'Macedon',
    'MRY': 'Maurya',
    'SEL': 'Seleukid Empire',
}
