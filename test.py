import unittest
import re

def add_string(input_string):
    if not input_string:
        return 0  # Return 0 for empty input

    # Check for a custom delimiter
    match = re.match(r"//(.+)\n(.*)", input_string)
    if match:
        delimiter, numbers = match.groups()
    else:
        delimiter, numbers = ",", input_string  # Default delimiter is ","

    try:
        negative_num = []
        num_list = list(map(int, numbers.split(delimiter)))
        for num in num_list:
            if num < 0:
                negative_num.append(num)
        if negative_num and len(negative_num) == 1:
            raise Exception("Invalid input: No negative numbers pass.")
        if negative_num and len(negative_num) > 1:
            raise Exception("Invalid input: No negative numbers pass {}".format(",".join(map(str, negative_num))))
        return sum(num_list)
    except ValueError:
        raise ValueError("Invalid input: Ensure all values are numbers.")


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