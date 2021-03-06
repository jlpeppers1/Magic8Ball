
"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY
This program tests a function that prints 'Hello World'
as output.  The function is then called.
"""
import unittest
import unittest.mock as mock
from main import Magic8Ball as m8b
from main import constants

class MyTestCase(unittest.TestCase):

    def test_first_response(self):
        #assertEqual( parameter1, parameter2)
            ## parameter1 == parameter2
        #assertEqual( "Expected Value or outcome", function_call(param3))
        self.assertEqual("It is certain.", m8b.convert_number_to_text(0))

    def test_second_response(self):
        expected_value = "It is decidedly so."
        self.assertEqual(expected_value, m8b.convert_number_to_text(1))
        self.assertTrue(
            m8b.convert_number_to_text(m8b.get_random_number())
            in constants.Eight_Ball_Responses)

    def test_throws_error(self):
        with self.assertRaises(ValueError):
            m8b.convert_number_to_text(21)

    def test_throws_error_text(self):
        with self.assertRaises(ValueError):
            m8b.convert_number_to_text("21")

if __name__ == '__main__':
    unittest.main()
