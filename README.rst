``unicode-charnames``
=====================

Unicode characters have names that serve as unique identifiers for each character. The character names in the Unicode Standard are identical to those of ISO/IEC 10646.

The unicode-charnames package performs searches for Unicode character names or code point labels by Unicode character, and searches for Unicode code points by character names. It also performs substring searches in Unicode character names. This package supports version 12.1 of the Unicode Standard (137,929 characters).

The generic term "character name" refers to the Unicode character "Name" property value for an encoded Unicode character. For code points that do not have character names (unassigned, reserved code points and other special code point types), the Unicode Standard uses constructed Unicode code point labels, displayed between angle brackets, to stand in for character names.

Features
--------

The library provides:

* A function to get the character name (the normative character property "Name") or the code point label (for characters that do not have character names) of a single Unicode character.
* A function to get the code point value (in the usual 4- to 6-digit hexadecimal format) corresponding to a Unicode character name; the search is case-sensitive and requires exact string match.
* A function to search characters by character name; the search is case-insensitive but requires exact substring match.

Example usage::

    # -*- coding: utf-8 -*-

    from unicode_charnames import (
        charname,
        codepoint,
        search_charnames
    )

    # charname()
    print('charname():\n')
    print(charname('龠'))
    print(charname('\U0001F60A'))
    print(charname('\u00E5'))
    print(charname('\u0002'))

    # codepoint()
    print('\ncodepoint():\n')
    print(codepoint('LATIN CAPITAL LETTER E WITH ACUTE'))
    print(codepoint('SUPERCALIFRAGILISTICEXPIALIDOCIOUS'))
    print(codepoint('SQUARE ERA NAME REIWA'))

    # search_charnames()
    print('\nsearch_charnames():\n')
    for x in search_charnames('era name'):
        print('\t'.join(x))

Will produce the following output::

    charname():

    CJK UNIFIED IDEOGRAPH-9FA0
    SMILING FACE WITH SMILING EYES
    LATIN SMALL LETTER A WITH RING ABOVE
    <control-0002>

    codepoint():

    00C9
    None
    32FF

    search_charnames():

    32FF	SQUARE ERA NAME REIWA
    337B	SQUARE ERA NAME HEISEI
    337C	SQUARE ERA NAME SYOUWA
    337D	SQUARE ERA NAME TAISYOU
    337E	SQUARE ERA NAME MEIZI

References
----------

* https://www.unicode.org/versions/Unicode12.1.0/ch04.pdf#M9.40526.Heading.48.NameNormative
* https://www.unicode.org/Public/12.1.0/ucd/UnicodeData.txt
* https://www.unicode.org/Public/12.1.0/ucd/extracted/DerivedName.txt

License
-------

unicode-charnames is released under an MIT license. The full text of the license is available `here <https://github.com/mlodewijck/unicode_charnames/LICENSE>`_.

The Unicode Standard v12.1.0 *DerivedName.txt* file is licensed under the Unicode License Agreement for Data Files and Software. Please consult the `UNICODE, INC. LICENSE AGREEMENT <https://www.unicode.org/license.html>`_ prior to use.
