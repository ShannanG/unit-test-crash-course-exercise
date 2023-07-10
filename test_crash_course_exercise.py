import unittest
from crash_course_exercise import divide, IncorrectInputError


class MainTestCase(unittest.TestCase):
    def test_divide_valid_3_2(self):
        self.assertEqual(1.5, divide(3, 2))

    def test_divide_invalid_string3_string2(self):
        with self.assertRaises(IncorrectInputError):
            divide("3", "2")

    # invalid case - testing to check a ZeroDivisionError is raised with a custom message
    def test_divide_invalid_3_0(self):
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)

    def test_divide_boundary_string3_integer2(self):
        with self.assertRaises(IncorrectInputError):
            divide("3", 2)

    # boundary case - testing whether the program handles floats correctly
    def test_divide_boundary_float375_2(self):
        self.assertEqual(1.875, divide(3.75, 2))

    # boundary case - testing whether program can handle dividing a large num by a tiny float num
    def test_divide_boundary_3mil_float01(self):
        self.assertEqual(3000000000, divide(300000000, 0.1))        
