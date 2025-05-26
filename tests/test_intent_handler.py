import unittest
from modules.intent_handler import detect_intent

class TestIntentHandler(unittest.TestCase):

    def test_detect_intent_general(self):
        text = "What are your working hours?"
        intent = detect_intent(text)
        self.assertIn(intent, ['general', 'customer_support', 'loan', 'education'])

    def test_detect_intent_loan(self):
        text = "Can I prepay my loan without penalty?"
        intent = detect_intent(text)
        self.assertEqual(intent, 'loan')

    def test_detect_intent_unknown(self):
        text = "Blah blah unknown text"
        intent = detect_intent(text)
        self.assertEqual(intent, 'general')

if __name__ == "__main__":
    unittest.main()
