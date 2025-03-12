# test_calculator.py

import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(5, 0), "Error: Division by zero")

if __name__ == "__main__":
    unittest.main()
