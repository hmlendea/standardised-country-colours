# Build configuration that is specific to the Victoria 3 edition.
#
# Identity, output layout, and the palette mapping for every shipped tag live
# here. Shared values are imported from the top-level `config` module.

# --- Identity ---

EDITION_KEY = 'victoria3'
OUTPUT_GROUP = 'vic3'
MOD_FOLDER_NAME = 'standardised-country-colours'
MOD_NAME = 'Standardised Country Colours'
MOD_ID = 'com.github.hmlendea.vic3-standardised-country-colours'
GAME_ID = 'victoria3'
PICTURE_FILENAME = 'thumbnail.png'
SUPPORTED_GAME_VERSION = '1.15.*'
SHORT_DESCRIPTION = 'Standardised map colours for selectable countries'
MOD_TAGS = ['Map', 'Historical']
IS_MULTIPLAYER_SYNCHRONIZED = True

# --- Source paths ---

# The artwork inputs live under `src/<edition key>/`, so each game edition owns
# its own assets without colliding with another edition's.
MOD_THUMBNAIL_FILENAME = 'thumbnail.png'
LAUNCHER_THUMBNAIL_FILENAME = 'launcher-thumbnail.png'

# --- Output paths ---

METADATA_DIRECTORY_NAME = '.metadata'
METADATA_FILENAME = 'metadata.json'
CONTENT_DIRECTORY_PATH = 'common/country_definitions'
CONTENT_FILENAME = 'sc_country_colours.txt'

# --- Content header ---

CONTENT_HEADER_LINES = [
    '# Standardised Country Colours',
    '#',
    '# Overrides the map colour of selected countries with the standardised values',
    '# documented in COUNTRY_COLOURS.md. Only the color key is injected, so every',
    '# other field of the vanilla country definition is left untouched.',
    '#',
    '# Each comment records the vanilla country name, the hexadecimal palette colour,',
    '# and the palette source. Where the palette entry name differs from the vanilla',
    '# name, the palette name is appended in parentheses. Victoria 3 exposes a single',
    '# map colour per country, so only the primary palette colour is applied.',
]

# --- Country mappings ---

# Every injected tag, mapped to the palette entry that supplies its colour. The
# palette is the external Standardised Country Colours table; a tag is chosen so
# the palette entry name matches the country's vanilla localised name, or so the
# palette entry clearly denotes the same country under another name.
COUNTRY_PALETTE_ENTRIES = {
    'ABK': 'Abkhazia',
    'AFG': 'Afghanistan',
    'ALB': 'Albania',
    'ALD': 'Algeria',
    'ALI': 'Altai',
    'ALK': 'Alaska',
    'ANL': 'Andalusia',
    'AOT': 'Maori',
    'APC': 'Apache',
    'ARA': 'Arabia',
    'ARG': 'Argentina',
    'ARM': 'Armenia',
    'ARN': 'Aragon',
    'AST': 'Australia',
    'ASU': 'Asturias',
    'AUS': 'Austria',
    'AZB': 'Azerbaijan',
    'BAD': 'Baden',
    'BAH': 'Bahamas',
    'BAV': 'Bavaria',
    'BEL': 'Belgium',
    'BEN': 'Benin',
    'BHT': 'India',
    'BHU': 'Bhutan',
    'BOH': 'Czechia',
    'BOL': 'Bolivia',
    'BOS': 'Bosnia',
    'BRD': 'Burundi',
    'BRI': 'Brittany',
    'BRU': 'Brunei',
    'BRY': 'Buryatia',
    'BRZ': 'Brazil',
    'BUG': 'Buganda',
    'BUL': 'Bulgaria',
    'BUR': 'Myanmar',
    'BYE': 'Belarus',
    'BYZ': 'Eastern Roman Empire',
    'CAL': 'California',
    'CAM': 'Cambodia',
    'CAN': 'Canada',
    'CAS': 'Castille',
    'CEY': 'Sri Lanka',
    'CHC': 'Chechnya',
    'CHI': 'China',
    'CHL': 'Chile',
    'CIR': 'Adygea',
    'CLM': 'Colombia',
    'COR': 'Corsica',
    'CRI': 'Crimea',
    'CRO': 'Croatia',
    'CSC': 'Cascadia',
    'CYP': 'Cyprus',
    'CYR': 'Cyrenaica',
    'DEN': 'Denmark',
    'ECU': 'Ecuador',
    'EGY': 'Egypt',
    'ELS': 'El Salvador',
    'ENG': 'England',
    'EST': 'Estonia',
    'ETH': 'Ethiopia',
    'FIN': 'Finland',
    'FLA': 'Flanders',
    'FRA': 'France',
    'GAL': 'Galicia-Volhynia',
    'GEO': 'Georgia',
    'GER': 'Germany',
    'GRE': 'Greece',
    'GRN': 'Greenland',
    'HND': 'India',
    'HRE': 'Holy Roman Empire',
    'HUN': 'Hungary',
    'IDN': 'Indonesia',
    'IRE': 'Ireland',
    'IRO': 'Iroquois',
    'IRQ': 'Iraq',
    'ISR': 'Israel',
    'ITA': 'Italy',
    'JAP': 'Japan',
    'KAZ': 'Kazakhstan',
    'KON': 'Kongo',
    'KOR': 'South Korea',
    'KUK': 'Carpathia',
    'KUR': 'Kurdistan',
    'LAT': 'Latvia',
    'LEO': 'Leon',
    'LIT': 'Lithuania',
    'LOM': 'Lombardy',
    'LUX': 'Luxembourg',
    'MAD': 'Madagascar',
    'MAL': 'Mali',
    'MAY': 'Maya',
    'MEX': 'Mexico',
    'MGB': 'Maghreb',
    'MGL': 'Mongolia',
    'MOL': 'Moldova',
    'MON': 'Montenegro',
    'MOR': 'Morocco',
    'NAV': 'Navarra',
    'NEP': 'Nepal',
    'NET': 'Netherlands',
    'NOR': 'Norway',
    'NZL': 'New Zealand',
    'PAP': 'Rome',
    'PAT': 'Mapuche',
    'PER': 'Persia',
    'PEU': 'Peru',
    'PRM': 'Perm',
    'PNS': 'Polynesia',
    'POL': 'Poland',
    'POR': 'Portugal',
    'PRG': 'Paraguay',
    'RAJ': 'Rajastan',
    'ROM': 'Romania',
    'RUS': 'Russia',
    'SAF': 'South Africa',
    'SAH': 'Sahara',
    'SAR': 'Sardinia',
    'SAX': 'Saxony',
    'SCA': 'Scandinavia',
    'SCO': 'Scotland',
    'SER': 'Serbia',
    'SIA': 'Siam',
    'SIC': 'Sicily',
    'SLO': 'Slovenia',
    'SPA': 'Spain',
    'SWE': 'Sweden',
    'SWI': 'Switzerland',
    'SWZ': 'Eswatini',
    'SYR': 'Syria',
    'TAR': 'Tartaria',
    'TRH': 'Turkestan',
    'TRS': 'Transylvania',
    'TUR': 'Turkey',
    'UKR': 'Ukraine',
    'USA': 'United States',
    'VEN': 'Venice',
    'VNZ': 'Venezuela',
    'WAL': 'Romania',
    'WLS': 'Wales',
    'ZUL': 'Zulu',
}

# Tags whose vanilla localised name differs from the palette entry name. The
# difference is recorded in each block's comment as `(palette: <entry>)`.
VANILLA_COUNTRY_NAMES = {
    'AOT': 'Aotearoa',
    'BOH': 'Bohemia',
    'BOS': 'Bosnia-Herzegovina',
    'BUR': 'Burma',
    'BYZ': 'Byzantium',
    'CAS': 'Castile',
    'CIR': 'Circassia',
    'GAL': 'Galicia-Lodomeria',
    'HRE': 'Central Europe',
    'IRO': 'Haudenosaunee',
    'KOR': 'Korea',
    'KUK': 'Danubian State',
    'LEO': 'León',
    'LOM': 'Lombardia',
    'MOL': 'Moldavia',
    'RAJ': 'Rajputana',
    'SAR': 'Sardinia-Piedmont',
    'SAH': 'Sahrawi',
    'SIC': 'Two Sicilies',
    'SWZ': 'Swaziland',
    'TAR': 'Tatarstan',
    'USA': 'America',
    'WAL': 'Wallachia',
}
