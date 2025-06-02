# test_main.py
import unittest
from main import to_uppercase # Assuming your function is in main.py

class TestUppercase(unittest.TestCase):

    def test_to_uppercase(self):
        """Test that the to_uppercase function correctly converts to uppercase."""
        input_str = "Welcome to devops"
        expected_output = "WELCOME TO DEVOPS"
        self.assertEqual(to_uppercase(input_str), expected_output)

    def test_empty_string(self):
        """Test that an empty string remains an empty string."""
        input_str = ""
        expected_output = ""
        self.assertEqual(to_uppercase(input_str), expected_output)

    def test_already_uppercase(self):
        """Test that an already uppercase string remains unchanged."""
        input_str = "HELLO"
        expected_output = "HELLO"
        self.assertEqual(to_uppercase(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()
#python -m unittest test_main.py    