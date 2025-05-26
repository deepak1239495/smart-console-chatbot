import unittest
from modules.response_generator import generate_response

class TestResponseGenerator(unittest.TestCase):

    def test_generate_response(self):
        intent = "general"
        question = "What are your working hours?"
        # Remove the answer argument
        response = generate_response(intent, question)
        self.assertIn("working hours", response.lower())

if __name__ == "__main__":
    unittest.main()
