"""
This tests the translation program.
"""
import unittest

from machinetranslation import translator

class TestTranslator(unittest.TestCase): 
    def test_french_to_english(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english(None)

    def test_english_to_french(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french(None)

if__name__ == '__main__':

unittest.main()
