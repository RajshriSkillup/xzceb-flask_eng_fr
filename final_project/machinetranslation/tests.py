import unittest
from deep_translator import MyMemoryTranslator
from translator import frenchToEnglish, englishToFrench

class TranslationTests(unittest.TestCase):
    def test_translation(self):
        # Test translation of a simple phrase
        french_text = "Bonjour"
        expected_translation = "Hello"
        translation = frenchToEnglish(french_text)
        self.assertEqual(translation, expected_translation)

        # Test translation of an empty string
        eng_text = "Hello"
        expected_translation = "Bonjour"
        translation = englishToFrench(eng_text)
        self.assertEqual(translation, expected_translation)

if __name__ == '__main__':
    unittest.main()