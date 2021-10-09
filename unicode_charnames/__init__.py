"""Look up Unicode character name or code point label
and search in Unicode character names. This package supports
version 14.0 of the Unicode Standard (144,697 characters).
"""

from sys import version_info as _version_info

if _version_info < (3, 6):
    raise SystemExit(f"\n{__package__} requires Python >= 3.6 to run.")

__all__ = [
    "charname",
    "codepoint",
    "search_charnames",
    "UNICODE_VERSION",
    "UCD_VERSION",
    "__version__",
]

__author__  = "Marc Lodewijck"
__version__ = "14.0.0"

# The Unicode Standard used to process the data
UNICODE_VERSION = "14.0.0"

# The Unicode Character Database
UCD_VERSION = UNICODE_VERSION

from unicode_charnames.charnames import *
