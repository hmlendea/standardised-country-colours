# Build configuration specific to the Hearts of Iron IV edition.

from config import VANILLA_DIRECTORY_NAME

EDITION_KEY = 'hoi4'
OUTPUT_GROUP = 'hoi4'
MOD_FOLDER_NAME = 'standardised-country-colours'
MOD_NAME = 'Standardised Country Colours'
SUPPORTED_GAME_VERSION = '1.19.*'
MOD_TAGS = ['Map', 'Historical']
MOD_THUMBNAIL_FILENAME = 'thumbnail.png'
LAUNCHER_THUMBNAIL_FILENAME = 'launcher-thumbnail.png'
DESCRIPTOR_FILENAME = 'descriptor.mod'
PARENT_DESCRIPTOR_FILENAME = f'{MOD_FOLDER_NAME}.mod'
COUNTRIES_DIRECTORY_PATH = 'common/countries'
COUNTRY_COLOURS_FILENAME = 'zz_standardised_country_colours.txt'

COUNTRY_FILE_HEADER_LINES = [
    '# Standardised Country Colours',
    '#',
    '# Overrides the map colour of selected countries with the standardised values',
    '# documented in src/colours.md.',
    '#',
    '# Each entry records the palette colour and source.',
]

COUNTRY_PALETTE_ENTRIES = {
    'AFA': 'Afar',
    'CHR': 'Charrúa',
    'KUR': 'Kurdistan',
    'VGE': 'Volga Germany',
    'YUG': 'Yugoslavia',
    'YUN': 'Yunnan',
}
