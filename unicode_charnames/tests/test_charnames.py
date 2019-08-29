# -*- coding: utf-8 -*-

import unittest

from unicode_charnames import (
    charname,
    codepoint,
    search_charnames,
    unidata_version
)


class TestSuite(unittest.TestCase):

    def test_unidata_version(self):
        self.assertEqual(unidata_version(), '12.1.0')

    def test_charname(self):
        self.assertEqual(
            charname('É'),
            'LATIN CAPITAL LETTER E WITH ACUTE')
        self.assertEqual(
            charname('\u00C9'),
            'LATIN CAPITAL LETTER E WITH ACUTE')
        self.assertEqual(
            charname(chr(0x00C9)),
            'LATIN CAPITAL LETTER E WITH ACUTE')
        self.assertEqual(
            charname('\u32FF'),
            'SQUARE ERA NAME REIWA')

        self.assertEqual(
            charname('\u3400'),
            'CJK UNIFIED IDEOGRAPH-3400')
        self.assertEqual(
            charname('\uF900'),
            'CJK COMPATIBILITY IDEOGRAPH-F900')
        self.assertEqual(
            charname('\U00017000'),
            'TANGUT IDEOGRAPH-17000')
        self.assertEqual(
            charname('\U0001B170'),
            'NUSHU CHARACTER-1B170')

        self.assertEqual(
            charname('\u0000'),
            '<control-0000>')
        self.assertEqual(
            charname('\uF8FF'),
            '<private-use-F8FF>')
        self.assertEqual(
            charname('\uD800'),
            '<surrogate-D800>')
        self.assertEqual(
            charname('\U0010FFFF'),
            '<noncharacter-10FFFF>')

    def test_codepoint(self):
        self.assertEqual(
            codepoint('LATIN CAPITAL LETTER E WITH ACUTE'),
            '00C9')
        self.assertEqual(
            codepoint('SQUARE ERA NAME REIWA'),
            '32FF')
        self.assertEqual(
            codepoint('SUPERCALIFRAGILISTICEXPIALIDOCIOUS'),
            None)

    def test_search_charnames(self):
        lst = [
            ('32FF', 'SQUARE ERA NAME REIWA'),
            ('337B', 'SQUARE ERA NAME HEISEI'),
            ('337C', 'SQUARE ERA NAME SYOUWA'),
            ('337D', 'SQUARE ERA NAME TAISYOU'),
            ('337E', 'SQUARE ERA NAME MEIZI')
        ]

        self.assertEqual(
            search_charnames('ERA NAME'),
            lst)
        self.assertEqual(
            search_charnames('ERA NAME'),
            search_charnames('era name'))

if __name__ == '__main__':
    unittest.main()
