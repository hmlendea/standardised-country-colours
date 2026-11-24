# Registry of the Standardised Country Colours game editions the build supports.
#
# To add a game, drop a module beside `victoria3.py` that exposes a single
# `EDITION` value and register it in `EDITIONS` below.

from games.base import GameEdition
from games.imperator import EDITION as IMPERATOR_EDITION
from games.victoria3 import EDITION as VICTORIA3_EDITION

EDITIONS = {
    VICTORIA3_EDITION.key: VICTORIA3_EDITION,
    IMPERATOR_EDITION.key: IMPERATOR_EDITION,
}
