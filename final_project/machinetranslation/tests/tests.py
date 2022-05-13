import unittest
import translator
class TestTranslator(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(translator.french_to_english(None), '')
        self.assertEqual(translator.english_to_french(None), '')
    
    def test_hello_translation(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
    
    def test_incorrect_hello_translation(self):
        self.assertNotEqual(translator.french_to_english('Bonjour'), 'Bonjour')
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hello')
    


if __name__=='__main__':
    unittest.main()
