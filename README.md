# unicode-charnames
[![PyPI Version](https://img.shields.io/pypi/v/unicode-charnames.svg)](https://pypi.python.org/pypi/unicode-charnames) [![PyPI License](https://img.shields.io/pypi/l/unicode-charnames.svg)](https://pypi.python.org/pypi/unicode-charnames)

Unicode characters have names that serve as unique identifiers for each character. The character names in the Unicode Standard are identical to those of ISO/IEC 10646.

The unicode-charnames package performs searches for Unicode character names or code point labels by Unicode character, and searches for Unicode code points by character names. It also performs substring searches in Unicode character names. This package supports version 13.0 of the Unicode Standard (143,859 characters).

The generic term “character name” refers to the Unicode character “Name” property value for an encoded Unicode character. For code points that do not have character names (unassigned, reserved code points and other special code point types), the Unicode Standard uses constructed Unicode code point labels, displayed between angle brackets, to stand in for character names.

### Installation
```shell
pip install unicode-charnames
```

### Features
The library provides:

* A function to get the character name (the normative character property “Name”) or the code point label (for characters that do not have character names) of a single Unicode character.
* A function to get the code point value (in the usual 4- to 6-digit hexadecimal format) corresponding to a Unicode character name; the search is case-sensitive and requires exact string match.
* A function to search characters by character name; the search is case-insensitive but requires exact substring match.

### Example usage
```python
    # -*- coding: utf-8 -*-
    from unicode_charnames import charname, codepoint, search_charnames

    # charname()

    for item in ['龠', '💓', '\u00E5', '\u0002']:
        print(charname(item))
        # Output:
        # CJK UNIFIED IDEOGRAPH-9FA0
        # BEATING HEART
        # LATIN SMALL LETTER A WITH RING ABOVE
        # <control-0002>

    # codepoint()

    names = [
        'LATIN CAPITAL LETTER E WITH ACUTE',
        'SQUARE ERA NAME REIWA',
        'SUPERCALIFRAGILISTICEXPIALIDOCIOUS'
    ]
    for item in names:
        print(codepoint(item))
        # Output:
        # 00C9
        # 32FF
        # None

    # search_charnames()

    for x in search_charnames('sextile'):
        print('\t'.join(x))
        # Output:
        # 26B9	SEXTILE
        # 26BA	SEMISEXTILE
```

### References
* https://www.unicode.org/versions/Unicode13.0.0/ch04.pdf#M9.40526.Heading.48.NameNormative
* https://www.unicode.org/Public/13.0.0/ucd/UnicodeData.txt
* https://www.unicode.org/Public/13.0.0/ucd/extracted/DerivedName.txt

### License
unicode-charnames is released under an MIT license. The full text of the license is available [here](https://github.com/mlodewijck/unicode_charnames/blob/master/LICENSE).

The Unicode Standard “DerivedName.txt” file is licensed under the Unicode License Agreement for Data Files and Software. Please consult the [UNICODE, INC. LICENSE AGREEMENT](https://www.unicode.org/license.html) prior to use.

### Changes
* [CHANGELOG](https://github.com/mlodewijck/unicode_charnames/blob/master/CHANGELOG.md)
