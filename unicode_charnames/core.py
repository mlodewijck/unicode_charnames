# -*- coding: utf-8 -*-

import os.path
import sys


UNIDATA_VERSION = '12.1.0'
FILE = 'DerivedName.txt'
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE)

names = {}

with open(PATH, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        cp, name = [x.strip() for x in line.split(';')]
        if '..' in cp:
            start, stop = cp.split('..')
            for each in range(int(start, 16), int(stop, 16)+1):
                names[each] = name[:-1] + format(each, '04X')
        else:
            names[int(cp, 16)] = name

names_inv = {v: k for k, v in names.items()}

control = set()
private_use = set()
surrogate = set()
noncharacter = set()

control.update(
    range(0x000000, 0x00001F+1),
    range(0x00007F, 0x00009F+1)
)
private_use.update(
    range(0x00E000, 0x00F8FF+1),
    range(0x0F0000, 0x0FFFFD+1),
    range(0x100000, 0x10FFFD+1)
)
surrogate.update(
    range(0x00D800, 0x00DFFF+1)
)
noncharacter.update(
    range(0x00FDD0, 0x00FDEF+1),
    range(0x00FFFE, 0x00FFFF+1),
    range(0x01FFFE, 0x01FFFF+1),
    range(0x02FFFE, 0x02FFFF+1),
    range(0x03FFFE, 0x03FFFF+1),
    range(0x04FFFE, 0x04FFFF+1),
    range(0x05FFFE, 0x05FFFF+1),
    range(0x06FFFE, 0x06FFFF+1),
    range(0x07FFFE, 0x07FFFF+1),
    range(0x08FFFE, 0x08FFFF+1),
    range(0x09FFFE, 0x09FFFF+1),
    range(0x0AFFFE, 0x0AFFFF+1),
    range(0x0BFFFE, 0x0BFFFF+1),
    range(0x0CFFFE, 0x0CFFFF+1),
    range(0x0DFFFE, 0x0DFFFF+1),
    range(0x0EFFFE, 0x0EFFFF+1),
    range(0x0FFFFE, 0x0FFFFF+1),
    range(0x10FFFE, 0x10FFFF+1)
)

def charname(char):
    """Return the Unicode name or the code point label of a single
    Unicode character.

    >>> charname('龠')
    'CJK UNIFIED IDEOGRAPH-9FA0'
    >>> charname('\U0001B170')
    'NUSHU CHARACTER-1B170'
    >>> charname('\u32FF')
    'SQUARE ERA NAME REIWA'
    """
    char = ord(char)

    name = names.get(char, None)
    if name is not None:
        return name

    # Constructed Unicode code point labels:
    if char in control:
        label = '<control-'
    elif char in private_use:
        label = '<private-use-'
    elif char in surrogate:
        label = '<surrogate-'
    elif char in noncharacter:
        label = '<noncharacter-'
    else:
        label = '<reserved-'

    name = names[char] = label + format(char, '04X') + '>'
    return name

def codepoint(name):
    """Return the Unicode code point (in the usual 4- to 6-digit
    hexadecimal format) corresponding to a Unicode character name. The
    search is case-sensitive and requires exact string match.

    >>> codepoint('LATIN CAPITAL LETTER E WITH ACUTE')
    '00C9'
    >>> codepoint('SQUARE ERA NAME REIWA')
    '32FF'
    >>> codepoint('SUPERCALIFRAGILISTICEXPIALIDOCIOUS')
    >>> 
    """
    if name in names_inv:
        return format(names_inv[name], '04X')
    return None

def search_charnames(substr):
    """Search characters by character name. Input value: word or phrase
    from the normative Unicode character name. The search is case-
    insensitive but requires exact substring match.

    >>> type(search_charnames('ERA NAME'))
    <class 'list'>
    >>> type(search_charnames('ERA NAME')[0])
    <class 'tuple'>
    >>> for each in search_charnames('era name'):
    ...     print(each)
    ...
    ('32FF', 'SQUARE ERA NAME REIWA')
    ('337B', 'SQUARE ERA NAME HEISEI')
    ('337C', 'SQUARE ERA NAME SYOUWA')
    ('337D', 'SQUARE ERA NAME TAISYOU')
    ('337E', 'SQUARE ERA NAME MEIZI')
    """
    res = []
    for name in names.values():
        if substr.upper() in name:
            res.append((codepoint(name), name))
    return res

def unidata_version():
    return UNIDATA_VERSION


if __name__ == '__main__':

    # Package version:
    from release import __version__
    print(__version__)

    # Unicode version:
    print(unidata_version())

    # Code points assigned to an abstract character:
    print(len(names))         # 137929

    # Code points with a normative function:
    print(len(control))       #     65
    print(len(private_use))   # 137468
    print(len(surrogate))     #   2048
    print(len(noncharacter))  #     66

    # Docstrings testing:
#    import doctest
#    doctest.testmod()
