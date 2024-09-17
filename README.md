# unicode-charnames
This package is built for Unicode version&nbsp;16.0, released in September&nbsp;2024.

The library provides:

* A function to retrieve the character name (the normative “Name” property) or the code point label (for characters without names) for any Unicode character.
* A function to get the code point (in the usual 4- to 6-digit hexadecimal format) for a given Unicode character name. The search is case-sensitive and requires an exact match.
* A function to search for characters by name. The search is case-insensitive but requires an exact substring match.

The generic term “character name” refers to the Unicode character “Name” property value for an encoded character. For code points that do not have character names (unassigned, reserved code points, and other special code point types), the Unicode standard uses constructed code point labels in angle brackets to represent these characters.

### Installation and updates
To install the package, run:
```shell
pip install unicode-charnames
```

To upgrade to the latest version, run:
```shell
pip install unicode-charnames --upgrade
```

### Unicode character database (UCD) version
To retrieve the version of the Unicode character database in use:
```python
>>> from unicode_charnames import UCD_VERSION
>>> UCD_VERSION
'16.0.0'
```

### Example usage
```python
    from unicode_charnames import charname, codepoint, search_charnames

    # charname
    for char in '龠💓\u00E5\u0002':
        print(charname(char))
        # CJK UNIFIED IDEOGRAPH-9FA0
        # BEATING HEART
        # LATIN SMALL LETTER A WITH RING ABOVE
        # <control-0002>

    # codepoint
    for name in [
            'LATIN CAPITAL LETTER E WITH ACUTE',
            'SQUARE ERA NAME REIWA',
            'SUPERCALIFRAGILISTICEXPIALIDOCIOUS'
    ]:
        print(codepoint(name))
        # 00C9
        # 32FF
        # None

    # search_charnames
    for x in search_charnames('break'):
        print('\t'.join(x))
        # 00A0    NO-BREAK SPACE
        # 2011    NON-BREAKING HYPHEN
        # 202F    NARROW NO-BREAK SPACE
        # 4DEA    HEXAGRAM FOR BREAKTHROUGH
        # FEFF    ZERO WIDTH NO-BREAK SPACE
```

### Related resource
This library is based on [Section 4.8, “Name,” in the Unicode Core Specification, version&nbsp;16.0.0](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-4/#G2082).

### Licenses
The code is licensed under the [MIT license](https://github.com/mlodewijck/unicode_charnames/blob/master/LICENSE).

Usage of Unicode data files is subject to the [UNICODE TERMS OF USE](https://www.unicode.org/copyright.html). Additional rights and restrictions regarding Unicode data files and software are outlined in the [Unicode Data Files and Software License](https://www.unicode.org/license.txt), a copy of which is included as [UNICODE-LICENSE](https://github.com/mlodewijck/unicode_charnames/blob/master/UNICODE-LICENSE).
