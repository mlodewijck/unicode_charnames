import sys
if not (sys.version_info[0] == 3 and sys.version_info[1] >= 3):
    sys.tracebacklimit = None
    raise ImportError('Python version 3.3 or above is required.')

from .core import (
    charname,
    codepoint,
    search_charnames,
    unidata_version
)
from .release import __version__
