import unittest

def calculator():
    pass

class TestCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(calculator(""), 0)

    def test_single_number(self):
        self.assertEqual(calculator("5"), 5)

    def test_multiple_numbers_default_delimiter(self):
        self.assertEqual(calculator("1,2,3"), 6)
