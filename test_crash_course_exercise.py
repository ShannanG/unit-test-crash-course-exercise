import unittest
from crash_course_exercise import divide, IncorrectInputError


class MainTestCase(unittest.TestCase):
    def test_divide_valid_3_2(self):
        self.assertEqual(1.5, divide(3, 2))

    def test_divide_invalid_string3_string2(self):
        with self.assertRaises(IncorrectInputError):
            divide("3", "2")

    def test_divide_boundary_string3_integer2(self):
        with self.assertRaises(IncorrectInputError):
            divide("3", 2)
