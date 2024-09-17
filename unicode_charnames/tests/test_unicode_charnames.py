"""Unit tests for unicode_charnames."""

import unittest

from unicode_charnames import (
    charname,
    codepoint,
    search_charnames,
    UNICODE_VERSION,
    UCD_VERSION,
)


class TestVersion(unittest.TestCase):

    def test_UNICODE_VERSION(self):
        self.assertEqual(UNICODE_VERSION, "16.0.0")

    def test_UCD_VERSION(self):
        self.assertEqual(UCD_VERSION, "16.0.0")


class TestCharname(unittest.TestCase):

    def test_name_1(self):
        expected = "LATIN CAPITAL LETTER E WITH ACUTE"

        self.assertEqual(charname("É"),       expected)
        self.assertEqual(charname("\u00C9"),  expected)
        self.assertEqual(charname(chr(0xC9)), expected)

    def test_name_2(self):
        self.assertEqual(
            charname("\u3400"),
            "CJK UNIFIED IDEOGRAPH-3400"
        )

        self.assertEqual(
            charname("\U0002EE4A"),
            "CJK UNIFIED IDEOGRAPH-2EE4A"
        )

        self.assertEqual(
            charname("\uF900"),
            "CJK COMPATIBILITY IDEOGRAPH-F900"
        )

        self.assertEqual(
            charname("\U00017000"),
            "TANGUT IDEOGRAPH-17000"
        )

        self.assertEqual(
            charname("\U0001B170"),
            "NUSHU CHARACTER-1B170"
        )

        self.assertEqual(
            charname("\U00018CD5"),
            "KHITAN SMALL SCRIPT CHARACTER-18CD5"
        )

        self.assertEqual(
            charname("\U00018CFF"),
            "KHITAN SMALL SCRIPT CHARACTER-18CFF"
        )

        self.assertEqual(
            charname("\U00013460"),
            "EGYPTIAN HIEROGLYPH-13460"
        )

    def test_cp_label(self):
        self.assertEqual(
            charname("\u0000"), "<control-0000>"
        )

        self.assertEqual(
            charname("\uF8FF"), "<private-use-F8FF>"
        )

        self.assertEqual(
            charname("\uD800"), "<surrogate-D800>"
        )

        self.assertEqual(
            charname("\U0010FFFF"), "<noncharacter-10FFFF>"
        )

        self.assertEqual(
            charname("\U0002EE5E"), "<reserved-2EE5E>"
        )

    def test_exception_charname_1(self):
        with self.assertRaises(TypeError) as context:
            charname(5)

        expected_msg = "expected a string of length 1, but got 5 of type int"
        self.assertEqual(str(context.exception), expected_msg)

    def test_exception_charname_2(self):
        with self.assertRaises(ValueError) as context:
            charname("ABC")

        expected_msg = \
            "expected a string of length 1, but got 'ABC' of length 3"
        self.assertEqual(str(context.exception), expected_msg)

    def test_exception_charname_3(self):
        with self.assertRaises(ValueError) as context:
            charname("")

        expected_msg = "expected a string of length 1, but got '' of length 0"
        self.assertEqual(str(context.exception), expected_msg)

    def test_exception_charname_4(self):
        with self.assertRaises(TypeError) as context:
            charname()

        expected_msg = \
            "charname() missing 1 required positional argument: 'char'"
        self.assertEqual(str(context.exception), expected_msg)


class TestCodepoint(unittest.TestCase):

    def test_exact_match(self):
        self.assertEqual(codepoint("SQUARE ERA NAME REIWA"), "32FF")
        self.assertEqual(codepoint("BUBBLE TEA"), "1F9CB")

    def test_no_match(self):
        self.assertIsNone(codepoint("Bubble tea"))
        self.assertIsNone(codepoint("SUPERCALIFRAGILISTICEXPIALIDOCIOUS"))
        self.assertIsNone(codepoint(""))

    def test_exception_search_charnames_1(self):
        with self.assertRaises(TypeError) as context:
            codepoint(12345)

        expected_msg = "expected a string, but got int"
        self.assertEqual(str(context.exception), expected_msg)

    def test_exception_search_charnames_2(self):
        with self.assertRaises(TypeError) as context:
            codepoint()

        expected_msg = \
            "codepoint() missing 1 required positional argument: 'name'"
        self.assertEqual(str(context.exception), expected_msg)


class TestSearchCharnames(unittest.TestCase):

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

    def test_no_math(self):
        self.assertEqual(list(search_charnames("CALIFRAGILIS")), [])

    def test_exception_search_charnames_1(self):
        with self.assertRaises(TypeError) as context:
            list(search_charnames(12345))

        expected_msg = "expected a string, but got int"
        self.assertEqual(str(context.exception), expected_msg)

    def test_exception_search_charnames_2(self):
        with self.assertRaises(ValueError) as context:
            list(search_charnames(""))

        expected_msg = "expected a non-empty string for search"
        self.assertEqual(str(context.exception), expected_msg)

    def test_exception_search_charnames_3(self):
        with self.assertRaises(TypeError) as context:
            list(search_charnames())

        expected_msg = \
            "search_charnames() missing 1 required positional " \
            "argument: 'substr'"
        self.assertEqual(str(context.exception), expected_msg)


if __name__ == "__main__":
    unittest.main()
