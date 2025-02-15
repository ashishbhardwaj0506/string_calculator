import unittest

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add_string(""), 0)

    def test_addition(self):
        self.assertEqual(add_string("1,2,3"), 6)
        self.assertEqual(add_string("//;\n1;2"), 3)
        self.assertEqual(add_string("//|\n1|2|3"), 6)

    def test_negative_number(self):
        with self.assertRaises(Exception) as cm:
            add_string("1, -2, 3")
        self.assertIn("Invalid input: No negative numbers pass.", str(cm.exception))

        with self.assertRaises(Exception) as cm:
            add_string("1, -2, 3, -4")
        self.assertIn("Invalid input: No negative numbers pass -2,-4", str(cm.exception))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            add_string("1,a,3")

        with self.assertRaises(TypeError):
            add_string(123)


if __name__ == '__main__':
    unittest.main()