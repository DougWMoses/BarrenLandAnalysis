from unittest import TestCase
from utils.utils import input_set_to_actual_set


class TestUtils(TestCase):

    def test_input_set_to_actual_set_should_convert_string_to_set(self):
        input_string = '{"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}'
        expected = ["48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"]
        actual = input_set_to_actual_set(input_string)
        self.assertEqual(expected, actual)

    def test_input_set_to_actual_set_should_convert_string_with_leading_and_trailing_spaces(self):
        input_string = '{ "48 192 351 207" , "48 392 351 407" , "120 52 135 547" , "260 52 275 547" }'
        expected = ["48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"]
        actual = input_set_to_actual_set(input_string)
        self.assertEqual(expected, actual)

    def test_input_set_to_actual_set_should_empty_set_if_empty_string_is_passed(self):
        input_string = ''
        expected = []
        actual = input_set_to_actual_set(input_string)
        self.assertEqual(expected, actual)
