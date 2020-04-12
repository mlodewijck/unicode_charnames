# -*- coding: utf-8 -*-

__all__ = (
    'charname',
    'codepoint',
    'search_charnames',
    '__version__',
    'UNICODE_VERSION',
    'UCD_VERSION'
)

import os.path

from unicode_charnames.release import __version__

UNICODE_VERSION = '13.0.0'     # the Unicode Standard used to process the data
UCD_VERSION = UNICODE_VERSION  # the Unicode Character Database

FILE = 'DerivedName.txt'
DIR_PATH = os.path.dirname(__file__)

NAMES = {}


def _convert(range_, prefix):
    start, end = range_.split('..')
    frmt = '{}{:04X}'.format
    names = {
        cp: frmt(prefix, cp)
        for cp in range(int(start, 16),
                        int(end, 16) + 1)
    }
    NAMES.update(names)


with open(os.path.join(DIR_PATH, FILE), 'r') as file:
    #assert re.match(
    #    '^#.*{}-(.+).txt.*$'.format(FILE[:-4]), file.readline()
    #).group(1) == UCD_VERSION
    frmt = '{}{:04X}'.format
    for line in file:
        line = line.strip()
        if line and not line.startswith('#'):
            cp, name = [x.strip() for x in line.split(';')]
            if '..' in cp:
                _convert(cp, name[:-1])
            else:
                NAMES[int(cp, 16)] = name

NAMES_INV = {v: k for k, v in NAMES.items()}

control = [
    *range(0x000000, 0x00001F + 1), *range(0x00007F, 0x00009F + 1)
]

private_use = [
    *range(0x00E000, 0x00F8FF + 1), *range(0x0F0000, 0x0FFFFD + 1),
    *range(0x100000, 0x10FFFD + 1)
]

surrogate = [
    *range(0x00D800, 0x00DFFF + 1)
]

noncharacter = [
    *range(0x00FDD0, 0x00FDEF + 1), *range(0x00FFFE, 0x00FFFF + 1),
    *range(0x01FFFE, 0x01FFFF + 1), *range(0x02FFFE, 0x02FFFF + 1),
    *range(0x03FFFE, 0x03FFFF + 1), *range(0x04FFFE, 0x04FFFF + 1),
    *range(0x05FFFE, 0x05FFFF + 1), *range(0x06FFFE, 0x06FFFF + 1),
    *range(0x07FFFE, 0x07FFFF + 1), *range(0x08FFFE, 0x08FFFF + 1),
    *range(0x09FFFE, 0x09FFFF + 1), *range(0x0AFFFE, 0x0AFFFF + 1),
    *range(0x0BFFFE, 0x0BFFFF + 1), *range(0x0CFFFE, 0x0CFFFF + 1),
    *range(0x0DFFFE, 0x0DFFFF + 1), *range(0x0EFFFE, 0x0EFFFF + 1),
    *range(0x0FFFFE, 0x0FFFFF + 1), *range(0x10FFFE, 0x10FFFF + 1)
]

LABELS = {
    frozenset(control)      : 'control',
    frozenset(private_use)  : 'private-use',
    frozenset(surrogate)    : 'surrogate',
    frozenset(noncharacter) : 'noncharacter',
}

# Code points assigned to an abstract character
# print(len(NAMES))         # 143859

# Code points with a normative function
# print(len(control))       #     65
# print(len(private_use))   # 137468
# print(len(surrogate))     #   2048
# print(len(noncharacter))  #     66


def charname(char):
    """Return the Unicode name or the code point label of a single
    Unicode character.

    >>> charname('É')
    'LATIN CAPITAL LETTER E WITH ACUTE'

    >>> charname('龠')
    'CJK UNIFIED IDEOGRAPH-9FA0'

    >>> charname('\u32FF')
    'SQUARE ERA NAME REIWA'

    >>> charname('\U00018CD5')
    'KHITAN SMALL SCRIPT CHARACTER-18CD5'
    """
    char = ord(char)

    if char in NAMES:
        return NAMES[char]

    for set_, label in LABELS.items():
        if char in set_:
            NAMES[char] = '<{}-{:04X}>'.format(label, char)
            break
    else:
        NAMES[char] = '<reserved-{:04X}>'.format(char)

    return NAMES[char]


def codepoint(name):
    """Return the Unicode code point (in the usual 4- to 6-digit
    hexadecimal format) corresponding to a Unicode character name.
    The search is case-sensitive and requires exact string match.

    >>> codepoint('LATIN CAPITAL LETTER E WITH ACUTE')
    '00C9'

    >>> codepoint('SQUARE ERA NAME REIWA')
    '32FF'

    >>> codepoint('BUBBLE TEA')
    '1F9CB'

    >>> codepoint('SUPERCALIFRAGILISTICEXPIALIDOCIOUS')
    >>>
    """
    if name in NAMES_INV:
        return format(NAMES_INV[name], '04X')
    return None


def search_charnames(substr):
    """Search characters by character name. Input value: word or phrase
    from the normative Unicode character name. The search is case-
    insensitive but requires exact substring match.

    >>> for each in search_charnames('sextile'): print(each)
    ...
    ('26B9', 'SEXTILE')
    ('26BA', 'SEMISEXTILE')

    >>> for each in search_charnames('French'): print(each)
    ...
    ('20A3', 'FRENCH FRANC SIGN')
    ('1F35F', 'FRENCH FRIES')
    """
    for name, codepoint in NAMES_INV.items():
        if substr.upper() in name:
            yield format(codepoint, '04X'), name


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import sys
    if '--unittest' in sys.argv:
        import unittest
        suite = unittest.TestLoader().discover('tests', pattern='test*.py')
        unittest.TextTestRunner(verbosity=2).run(suite)
