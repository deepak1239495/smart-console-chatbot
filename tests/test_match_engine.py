import unittest
from modules.match_engine import find_best_answer

class TestMatchEngine(unittest.TestCase):

    def test_find_best_answer(self):
        question = "How can I reset my password?"
        intent = "general"
        answer = find_best_answer(intent, question)
        self.assertIsInstance(answer, str)
        self.assertTrue(len(answer) > 0)

    def test_no_answer(self):
        question = "This question does not exist"
        intent = "loan"
        answer = find_best_answer(intent, question)
        self.assertIsInstance(answer, str)

if __name__ == "__main__":
    unittest.main()
