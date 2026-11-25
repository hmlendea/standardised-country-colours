# Build configuration that is specific to the Imperator: Rome edition.
#
# Identity, output layout, and the palette mapping for every shipped tag live
# here. Shared values are imported from the top-level `config` module.

import re

from pathlib import Path

from config import VANILLA_DIRECTORY_NAME

# --- Identity ---

EDITION_KEY = 'imperator'
OUTPUT_GROUP = 'imperator'
MOD_FOLDER_NAME = 'standardised-country-colours'
MOD_NAME = 'Standardised Country Colours'
SUPPORTED_GAME_VERSION = '2.0.*'
MOD_TAGS = ['Historical', 'Map']
MOD_THUMBNAIL_FILENAME = 'thumbnail.png'

# --- Output artwork ---

# The artwork inputs are shared by every edition (`src/icon.png` and
# `src/preview.png`); only the name used inside the mod folder differs.

# Vanilla paths. Imperator replaces the whole per-country file when a tag reads
# one, so a colour override must carry over the vanilla `ship_names` (and the
# commented `#color2`) of the tag it replaces; otherwise the tag's ship name
# pool is lost. Likewise `setup/countries/countries.txt` must keep every
# vanilla tag entry — truncating it to the shipped tags makes provinces whose
# owner tag is absent crash the game on startup.
#
# The required vanilla files are vendored under `vanilla/imperator/`, so the
# build never reads the game installation and stays reproducible everywhere.
REPOSITORY_ROOT_PATH = Path(__file__).resolve().parents[3]
VANILLA_EDITION_DIR = REPOSITORY_ROOT_PATH / VANILLA_DIRECTORY_NAME / EDITION_KEY
VANILLA_COUNTRIES_DIR = VANILLA_EDITION_DIR / 'setup' / 'countries'
VANILLA_COUNTRIES_INDEX = VANILLA_COUNTRIES_DIR / 'countries.txt'
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
    'ANG': 'England',
    'ARM': 'Armenia',
    'BOA': 'Czechia',
    'BYZ': 'Eastern Roman Empire',
    'CAR': 'Carthage',
    'BUR': 'Burgundy',
    'BRT': 'Bruttia',
    'CYR': 'Cyrenaica',
    'DAN': 'Denmark',
    'EGY': 'Egypt',
    'EPI': 'Epirus',
    'ETR': 'Etruscia',
    'GUN': 'Genoa',
    'MAU': 'Mauretania',
    'MAC': 'Macedonia',
    'MRY': 'India',
    'PRS': 'Paris',
    'PAR': 'Parthia',
    'PON': 'Pontus',
    'ROM': 'Rome',
    'SCY': 'Scythia',
    'SEL': 'Seleucia',
    'SXS': 'Frisia',
    'SRM': 'Sarmatia',
    'TIT': 'Teutonia',
    'TRE': 'Thrace',
    'VNT': 'Venice',
    'VSC': 'Basque Country',
}

# Tags whose vanilla localised name differs from the palette entry name. The
# difference is recorded in each block's comment as `(palette: <entry>)`.
VANILLA_COUNTRY_NAMES = {
    'ANG': 'Anglia',
    'BOA': 'Boihaemia',
    'GUN': 'Genuatia',
    'BUR': 'Burgundia',
    'BYZ': 'Byzantion',
    'DAN': 'Dania',
    'PRS': 'Parisia',
    'ETR': 'Etruria',
    'MAC': 'Macedon',
    'MRY': 'Maurya',
    'SEL': 'Seleukid Empire',
    'VNT': 'Veneto',
}
