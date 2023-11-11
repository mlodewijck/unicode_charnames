"""Unicode character names and code point labels."""

try:
    from importlib.resources import files as _files
    # Python 3.9 or later
except ImportError:
    from importlib.resources import open_text as _open_text
    # Python 3.7 or later
    # Deprecated starting from Python 3.11

from unicode_charnames import UCD_VERSION

# File from the Unicode character database (UCD)
# Source: https://www.unicode.org/Public/15.1.0/ucd/extracted/DerivedName.txt
_UNICODE_FILE = "DerivedName.txt"


def _make_dict():
    try:
        fh = _files(__package__).joinpath(_UNICODE_FILE).open(encoding="utf-8")
    except NameError:
        fh = _open_text(__package__, _UNICODE_FILE)

    if UCD_VERSION not in fh.readline():
        raise SystemExit(f"\n{__package__}: wrong UCD version number.")

    lines = fh.read().splitlines()
    fh.close()

    character_names = {}

    for line in lines:
        if not line.startswith("#"):
            item, _, name = line.partition(";")
            if ".." in item:
                start, _, end = item.rstrip().partition("..")
                character_names.update({
                    x: f"{name.lstrip()[:-1]}{x:04X}"
                    for x in range(int(start, 16), int(end, 16) + 1)
                })
            elif line:
                character_names[int(item.rstrip(), 16)] = name.lstrip()

    return character_names


# Normative Unicode character names
_CHARACTER_NAMES = _make_dict()

# Inverted character names dictionary
_CHARACTER_NAMES_INV = {v: k for k, v in _CHARACTER_NAMES.items()}

# assert len(_CHARACTER_NAMES_INV) == len(_CHARACTER_NAMES)

_control = [
    *range(0x000000, 0x00001F + 1),
    *range(0x00007F, 0x00009F + 1),
]

_private_use = [
    *range(0x00E000, 0x00F8FF + 1),
    *range(0x0F0000, 0x0FFFFD + 1),
    *range(0x100000, 0x10FFFD + 1),
]

_surrogate = [
    *range(0x00D800, 0x00DFFF + 1),
]

_noncharacter = [
    *range(0x00FDD0, 0x00FDEF + 1),
    *range(0x00FFFE, 0x00FFFF + 1),
    *range(0x01FFFE, 0x01FFFF + 1),
    *range(0x02FFFE, 0x02FFFF + 1),
    *range(0x03FFFE, 0x03FFFF + 1),
    *range(0x04FFFE, 0x04FFFF + 1),
    *range(0x05FFFE, 0x05FFFF + 1),
    *range(0x06FFFE, 0x06FFFF + 1),
    *range(0x07FFFE, 0x07FFFF + 1),
    *range(0x08FFFE, 0x08FFFF + 1),
    *range(0x09FFFE, 0x09FFFF + 1),
    *range(0x0AFFFE, 0x0AFFFF + 1),
    *range(0x0BFFFE, 0x0BFFFF + 1),
    *range(0x0CFFFE, 0x0CFFFF + 1),
    *range(0x0DFFFE, 0x0DFFFF + 1),
    *range(0x0EFFFE, 0x0EFFFF + 1),
    *range(0x0FFFFE, 0x0FFFFF + 1),
    *range(0x10FFFE, 0x10FFFF + 1),
]

# Code points assigned to an abstract character
# print(f"{len(_CHARACTER_NAMES):,}")  # 149,813

# Code points with a normative function
# print(f"{len(_control):,}")          #      65
# print(f"{len(_private_use):,}")      # 137,468
# print(f"{len(_surrogate):,}")        #   2,048
# print(f"{len(_noncharacter):,}")     #      66

_LABELS = {
    frozenset(_control)      : "control",
    frozenset(_private_use)  : "private-use",
    frozenset(_surrogate)    : "surrogate",
    frozenset(_noncharacter) : "noncharacter",
}

del _control, _private_use, _surrogate, _noncharacter


def charname(char):
    """Return the Unicode name or the code point label of a single Unicode
    character.

    Args:
        char (str): A single Unicode character.

    Returns:
        str: The Unicode name or the code point label of the character.

    Raises:
        TypeError: If `char` is not a single Unicode character (a string
            of length 1).

    Examples:

        >>> charname("A")
        'LATIN CAPITAL LETTER A'

        >>> charname("龠")
        'CJK UNIFIED IDEOGRAPH-9FA0'

        >>> charname("\U00012F90")
        'CYPRO-MINOAN SIGN CM001'

        >>> charname("\uF8FF")
        '<private-use-F8FF>'

    """
    cp = ord(char)

    if cp not in _CHARACTER_NAMES:
        for fset, label in _LABELS.items():
            if cp in fset:
                _CHARACTER_NAMES[cp] = f"<{label}-{cp:04X}>"
                break
        else:
            _CHARACTER_NAMES[cp] = f"<reserved-{cp:04X}>"

    return _CHARACTER_NAMES[cp]


def codepoint(name):
    """Return the Unicode code point corresponding to a Unicode character name.

    This function takes a Unicode character name as input and returns
    its Unicode code point in the usual 4- to 6-digit hexadecimal format.
    The search is case-sensitive and requires an exact string match.

    Args:
        name (str): The Unicode character name.

    Returns:
        str: The Unicode code point of the character in the hexadecimal format,
            or `None` if the name is not found.

    Examples:

        >>> codepoint("LATIN CAPITAL LETTER E WITH ACUTE")
        '00C9'

        >>> codepoint("MODIFIER LETTER CAPITAL Q")
        'A7F4'

        >>> codepoint("BUBBLE TEA")
        '1F9CB'

        >>> print(codepoint("SUPERCALIFRAGILISTICEXPIALIDOCIOUS"))
        None

    """
    if value := _CHARACTER_NAMES_INV.get(name):
        return f"{value:04X}"
    return value


def search_charnames(substr):
    """Search characters by character name.

    This function allows you to search for Unicode characters based on their
    names. The input value should be a word or phrase from the normative
    Unicode character name. The search is case-insensitive, but it requires
    an exact substring match.

    Args:
        substr (str): The word or phrase to search for in Unicode character
            names.

    Returns:
        generator: A generator that yields tuples containing the hexadecimal
            code point and the character name holding the input substring.
            No tuple is yielded if there is no match.

    Examples:

        >>> list(search_charnames("SEXTILE"))
        [('26B9', 'SEXTILE'), ('26BA', 'SEMISEXTILE')]

        >>> list(search_charnames("CALIFRAGILIS"))
        []

        >>> for match in search_charnames("era name"):
        ...     print(match)
        ...
        ('32FF', 'SQUARE ERA NAME REIWA')
        ('337B', 'SQUARE ERA NAME HEISEI')
        ('337C', 'SQUARE ERA NAME SYOUWA')
        ('337D', 'SQUARE ERA NAME TAISYOU')
        ('337E', 'SQUARE ERA NAME MEIZI')

    """
    for name, cp in _CHARACTER_NAMES_INV.items():
        if substr.upper() in name:
            yield f"{cp:04X}", name
