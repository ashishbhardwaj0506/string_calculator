import unittest
import re

def calculator(input_string):
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

    def test_single_negative_number(self):
        with self.assertRaises(Exception) as context:
            calculator("1,-2,3")
        self.assertEqual(str(context.exception), "Invalid input: No negative numbers pass.")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            calculator("//;\n1;-2;-3")
        self.assertEqual(str(context.exception), "Invalid input: No negative numbers pass -2,-3")

    def test_negative_number_with_delimiter(self):
        with self.assertRaises(Exception) as context:
            calculator("//|\n-5|6")
        self.assertEqual(str(context.exception), "Invalid input: No negative numbers pass.")

    def test_invalid_non_numeric_input(self):
        with self.assertRaises(ValueError) as context:
            calculator("1,a,3")
        self.assertEqual(str(context.exception), "Invalid input: Ensure all values are numbers.")

    def test_custom_delimiter_non_numeric_input(self):
        with self.assertRaises(ValueError) as context:
            calculator("//;\n1;2;a")
        self.assertEqual(str(context.exception), "Invalid input: Ensure all values are numbers.")

    def test_custom_delimiter_multi_character(self):
        self.assertEqual(calculator("//abc\n1abc2abc3"), 6)

if __name__ == "__main__":
    unittest.main()