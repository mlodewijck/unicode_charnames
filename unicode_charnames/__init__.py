"""Unicode character name lookup and search.

This library provides functions to explore and search Unicode character names
and code points, supporting Unicode standard version 16.0 (released in
September 2024).

Copyright (c) 2019-2024, Marc Lodewijck
All rights reserved.

This software is distributed under the MIT license.
"""

import sys

if sys.version_info < (3, 8):
    raise SystemExit(f"\n{__package__} requires Python 3.8 or later.")
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
UNICODE_VERSION = UCD_VERSION = "16.0.0"


from unicode_charnames import _version
__version__ = _version.__version__
del _version

from unicode_charnames.charnames import *
