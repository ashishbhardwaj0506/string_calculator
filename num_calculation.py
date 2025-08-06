import unittest

def calculator():
    pass

class TestCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(calculator(""), 0)
