import unittest
from main import division_remainder

class TestRemainder(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(division_remainder(10, 3), 1)

    def test_negative_numbers(self):
        self.assertEqual(division_remainder(-10, 3), 2)
        self.assertEqual(division_remainder(10, -3), -2)
        self.assertEqual(division_remainder(-10, -3), -1)

    def test_float_numbers(self):
        self.assertAlmostEqual(division_remainder(10.5, 3.2), 10.5 % 3.2)
        self.assertAlmostEqual(division_remainder(-10.5, 3.2), -10.5 % 3.2)

    def test_zero_dividend(self):
        self.assertEqual(division_remainder(0, 5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            division_remainder(10, 0)

    def test_division_by_one(self):
        self.assertEqual(division_remainder(10, 1), 0)

    def test_same_numbers(self):
        self.assertEqual(division_remainder(5, 5), 0)
        self.assertEqual(division_remainder(-5, -5), 0)

    def test_larger_divisor(self):
        self.assertEqual(division_remainder(3, 10), 3)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            division_remainder("10", 3)
        with self.assertRaises(TypeError):
            division_remainder(10, "3")
        with self.assertRaises(TypeError):
            division_remainder("10", "3")


if __name__ == '__main__':
    unittest.division_remainder