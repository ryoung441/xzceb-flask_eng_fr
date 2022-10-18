import unittest

from machinetranslation import translator

class TestTranslator(unittest.TestCase): 
    def test_english(self): 
        self.assertNotEqual(frenchToEnglish(None)
        self.assertEqual(frenchToEnglish(Bonjour), Hello)

    def test_french(self): 
        self.assertNotEqual(EnglishToFrench(None)
        self.assertEqual(EnglishToFrench(Hello), Bonjour)

unittest.main()
