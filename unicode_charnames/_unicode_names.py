"""Handles loading and processing of Unicode character names from the UCD."""

try:
    from importlib.resources import files as _files
    # Python 3.9 or later
    # Changed in version 3.12
except ImportError:
    from importlib.resources import open_text as _open_text
    # Python 3.7 or later
    # Deprecated in versions 3.11 and 3.12
    # Un-deprecated and changed in version 3.13

from unicode_charnames import UCD_VERSION

# File from the Unicode character database (UCD)
# Source: https://www.unicode.org/Public/16.0.0/ucd/extracted/DerivedName.txt
_FILE = "DerivedName.txt"


def _make_dict():
    try:
        with _files(__package__).joinpath(_FILE).open(encoding="utf-8") as fh:
            first_line = fh.readline()
            lines = fh.read().splitlines()
    except NameError:
        with _open_text(__package__, _FILE) as fh:
            first_line = fh.readline()
            lines = fh.read().splitlines()

    if UCD_VERSION not in first_line:
        raise SystemExit(f"\n{__package__}: UCD version mismatch in {_FILE}.")

    character_names = {}

    for line in lines:
        if not line or line.startswith("#"):
            continue

        key, _, val = line.partition("; ")
        key = key.rstrip()

        if line.endswith("*"):
            if ".." in key:
                start, _, end = key.partition("..")
                character_names.update({
                    x: f"{val[:-1]}{x:04X}"
                    for x in range(int(start, 16), int(end, 16) + 1)
                })
            else:
                character_names[int(key, 16)] = f"{val[:-1]}{key}"
        else:
            character_names[int(key, 16)] = val

    return character_names


# Dictionary of normative Unicode character names
_CHARACTER_NAMES = _make_dict()

# Inverted dictionary of character names
_CHARACTER_NAMES_INV = {v: k for k, v in _CHARACTER_NAMES.items()}

assert len(_CHARACTER_NAMES_INV) == len(_CHARACTER_NAMES)
