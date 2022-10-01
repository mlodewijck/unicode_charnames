"""Unicode character names and code point labels."""

from pathlib import Path as _Path

from unicode_charnames import UCD_VERSION

# File from the Unicode character database (UCD)
_UNICODE_FILE = "DerivedName.txt"


def _make_dict():
    character_names = {}

    def resolve(cp_range, prefix):
        start, end = cp_range.split("..")
        character_names.update({
            cp: f"{prefix}{cp:04X}"
            for cp in range(int(start, 16), int(end, 16) + 1)
        })

    path = _Path(__file__).parent.joinpath(_UNICODE_FILE)
    with path.open() as f:
        if UCD_VERSION not in f.readline():
            raise SystemExit(
                f"\n{__package__}: "
                f"wrong UCD version number in {_UNICODE_FILE}."
            )
        lines = f.read().splitlines()

    for line in lines:
        if line and not line.startswith("#"):
            cp, name = [x.strip() for x in line.split(";")]
            if ".." in cp:
                resolve(cp, name[:-1])
            else:
                character_names[int(cp, 16)] = name

    return character_names


# Normative Unicode character names
_CHARACTER_NAMES = _make_dict()

# Inverted character names dictionary
_CHARACTER_NAMES_INV = {v: k for k, v in _CHARACTER_NAMES.items()}

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
    *range(0x00D800, 0x00DFFF + 1)
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
# print(f"{len(_CHARACTER_NAMES):,}")  # 149,186
# assert len(_CHARACTER_NAMES_INV) == len(_CHARACTER_NAMES)

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
    """Return the Unicode name or the code point label of a single
    Unicode character.

    >>> charname("A")
    'LATIN CAPITAL LETTER A'

    >>> charname("龠")
    'CJK UNIFIED IDEOGRAPH-9FA0'

    >>> charname("\U00012F90")
    'CYPRO-MINOAN SIGN CM001'

    >>> charname("\uA7F4")
    'MODIFIER LETTER CAPITAL Q'
    """
    char = ord(char)

    if char in _CHARACTER_NAMES:
        return _CHARACTER_NAMES[char]

    for set_, label in _LABELS.items():
        if char in set_:
            _CHARACTER_NAMES[char] = f"<{label}-{char:04X}>"
            break
    else:
        _CHARACTER_NAMES[char] = f"<reserved-{char:04X}>"

    return _CHARACTER_NAMES[char]


def codepoint(name):
    """Return the Unicode code point (in the usual 4- to 6-digit
    hexadecimal format) corresponding to a Unicode character name.
    The search is case-sensitive and requires exact string match.

    >>> codepoint("LATIN CAPITAL LETTER E WITH ACUTE")
    '00C9'

    >>> codepoint("MODIFIER LETTER CAPITAL Q")
    'A7F4'

    >>> codepoint('BUBBLE TEA')
    '1F9CB'

    >>> codepoint("SUPERCALIFRAGILISTICEXPIALIDOCIOUS")
    >>>
    """
    if name in _CHARACTER_NAMES_INV:
        return f"{_CHARACTER_NAMES_INV[name]:04X}"
    return None


def search_charnames(substr):
    """Search characters by character name. Input value: word or phrase
    from the normative Unicode character name. The search is case-
    insensitive but requires exact substring match.

    >>> for each in search_charnames("sextile"): print(each)
    ...
    ('26B9', 'SEXTILE')
    ('26BA', 'SEMISEXTILE')

    >>> for each in search_charnames("French"): print(each)
    ...
    ('20A3', 'FRENCH FRANC SIGN')
    ('1F35F', 'FRENCH FRIES')
    """
    for name, codepoint in _CHARACTER_NAMES_INV.items():
        if substr.upper() in name:
            yield f"{codepoint:04X}", name


if __name__ == "__main__":
    import doctest
    doctest.testmod()
