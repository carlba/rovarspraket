import rovarspraket
import unittest
from mock import patch
from mock import MagicMock
import sys


class TestRovarspraket(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_alphabet(self):
        alphabet = rovarspraket.get_alphabet()
        correct_alphabet = set([u'\xf6', u'\xd6', u'\xc5', u'\xe5', u'\xc4', u'A', u'C', u'B', u'E', u'D', u'G', u'F', u'I', u'H', u'K', u'J', u'M', u'L', u'O', u'N', u'Q', u'P', u'S', u'R', u'U', u'T', u'W', u'V', u'Y', u'X', u'Z', u'\xe4', u'a', u'c', u'b', u'e', u'd', u'g', u'f', u'i', u'h', u'k', u'j', u'm', u'l', u'o', u'n', u'q', u'p', u's', u'r', u'u', u't', u'w', u'v', u'y', u'x', u'z'])
        self.assertEqual(alphabet, correct_alphabet)

    def test_get_vowels(self):
        correct_vowels = set([u'a', u'A', u'U', u'e', u'\xe4', u'i', u'\xc5', u'\xd6', u'o', u'I', u'u', u'O', u'\xf6', u'y', u'\xe5', u'E', u'Y', u'\xc4'])
        alphabet = rovarspraket.get_vowels()
        self.assertEqual(alphabet, correct_vowels)

    def test_validate_input_false(self):
        result = rovarspraket.validate_input(1)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "Please enter a string")
        self.assertIs(result, False)
        pass

    def test_validate_input_true(self):
        result = rovarspraket.validate_input("A string")
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "")
        self.assertIs(result, True)
        pass

    def test_convert_to_rovar(self):
        the_string = unicode("Detta är ett test","utf-8")
        print type (the_string)
        result = rovarspraket.convert_to_rovar(the_string)

        self.assertEqual(result, unicode("Dodetottota äror etottot totesostot", "utf-8") )

        pass

    def test_convert_to_rovar_empty(self):
        the_string = unicode("","utf-8")
        result = rovarspraket.convert_to_rovar(the_string)

        self.assertEqual(result, unicode("", "utf-8") )

        pass

if __name__ == '__main__':
    unittest.main()