import unittest

from unicode_charnames import (
    charname,
    codepoint,
    search_charnames,
    UNICODE_VERSION,
    UCD_VERSION,
)


class TestSuite(unittest.TestCase):

    def test_UNICODE_VERSION(self):
        self.assertEqual(UNICODE_VERSION, "15.0.0")

    def test_UCD_VERSION(self):
        self.assertEqual(UCD_VERSION, "15.0.0")

    def test_charname(self):
        expected = "LATIN CAPITAL LETTER E WITH ACUTE"
        self.assertEqual(charname("É"), expected)
        self.assertEqual(charname("\u00C9"), expected)
        self.assertEqual(charname(chr(0xC9)),expected)

        self.assertEqual(charname("\u3400"), "CJK UNIFIED IDEOGRAPH-3400")
        self.assertEqual(charname("\U0003134A"), "CJK UNIFIED IDEOGRAPH-3134A")
        self.assertEqual(charname("\uF900"), "CJK COMPATIBILITY IDEOGRAPH-F900")
        self.assertEqual(charname("\U00017000"), "TANGUT IDEOGRAPH-17000")
        self.assertEqual(charname("\U0001B170"), "NUSHU CHARACTER-1B170")
        self.assertEqual(charname("\U00018CD5"), "KHITAN SMALL SCRIPT CHARACTER-18CD5")

        self.assertEqual(charname("\u0000"), "<control-0000>")
        self.assertEqual(charname("\uF8FF"), "<private-use-F8FF>")
        self.assertEqual(charname("\uD800"), "<surrogate-D800>")
        self.assertEqual(charname("\U0010FFFF"), "<noncharacter-10FFFF>")

    def test_codepoint(self):
        self.assertEqual(codepoint("SQUARE ERA NAME REIWA"), "32FF")
        self.assertEqual(codepoint("BUBBLE TEA"), "1F9CB")
        self.assertIsNone(codepoint("SUPERCALIFRAGILISTICEXPIALIDOCIOUS"))

    def test_search_charnames(self):
        expected = [
            ("32FF", "SQUARE ERA NAME REIWA"),
            ("337B", "SQUARE ERA NAME HEISEI"),
            ("337C", "SQUARE ERA NAME SYOUWA"),
            ("337D", "SQUARE ERA NAME TAISYOU"),
            ("337E", "SQUARE ERA NAME MEIZI"),
        ]

        self.assertEqual(list(search_charnames("ERA NAME")), expected)
        self.assertEqual(list(search_charnames("era name")), expected)


if __name__ == "__main__":
    unittest.main()
