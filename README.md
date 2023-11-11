# unicode-charnames
This package supports Unicode version&nbsp;15.1, released in September&nbsp;2023.

The library provides:

* A function to get the character name (the normative character property “Name”) or the code point label (for characters that do not have character names) of a single Unicode character.
* A function to get the code point value (in the usual 4- to 6-digit hexadecimal format) corresponding to a Unicode character name; the search is case-sensitive and requires exact string match.
* A function to search characters by character name; the search is case-insensitive but requires exact substring match.

The generic term “character name” refers to the Unicode character “Name” property value for an encoded Unicode character. For code points that do not have character names (unassigned, reserved code points and other special code point types), the Unicode standard uses constructed Unicode code point labels, displayed between angle brackets, to stand in for character names.

### Installation or upgrade
The easiest method to install is using pip:
```shell
pip install unicode-charnames
```

To update the package to the latest version:
```shell
pip install --upgrade unicode-charnames
```

### UCD version
To get the version of the Unicode character database currently used:
```python
>>> from unicode_charnames import UCD_VERSION
>>> UCD_VERSION
'15.1.0'
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
This implementation is based on the following resource: [Section 4.8, Name, in the Unicode core specification, version&nbsp;15.1.0](https://www.unicode.org/versions/Unicode15.1.0/ch04.pdf#G2082).

### Licenses
The code is available under the [MIT license](https://github.com/mlodewijck/unicode_charnames/blob/master/LICENSE).

Usage of Unicode data files is governed by the [UNICODE TERMS OF USE](https://www.unicode.org/copyright.html). Further specifications of rights and restrictions pertaining to the use of the Unicode data files and software can be found in the [Unicode Data Files and Software License](https://www.unicode.org/license.txt), a copy of which is included as [UNICODE-LICENSE](https://github.com/mlodewijck/unicode_charnames/blob/master/UNICODE-LICENSE).
