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

    def test_delimiter(self):
        self.assertEqual(calculator("//;\n1;2;3"), 6)

    def test_special_char(self):
        self.assertEqual(calculator("//*\n2*3*4"), 9)

    def test_single_number(self):
        self.assertEqual(calculator("//;\n7"), 7)

    def test_not_present_in_numbers(self):
        self.assertEqual(calculator("//;\n123"), 123)