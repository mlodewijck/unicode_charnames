"""Look up Unicode character name or code point label
and search in Unicode character names. This package supports version 15.0
of the Unicode standard (released on September 13, 2022).
"""

import sys
if sys.version_info < (3, 6):
    raise SystemExit(f"\n{__package__} requires Python 3.6 or later.")
del sys

__all__ = [
    "charname",
    "codepoint",
    "search_charnames",
    "UCD_VERSION",
    "UNICODE_VERSION",
    "__version__",
]

# Unicode standard used to process the data
# Version released on September 13, 2022
UNICODE_VERSION = UCD_VERSION = "15.0.0"


from unicode_charnames import _version
__version__ = _version.__version__
del _version

from unicode_charnames.charnames import (
    charname,
    codepoint,
    search_charnames,
)
