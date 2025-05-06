import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(7, 2), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(5, 3.2), 16)
        self.assertEqual(multiply(0, 2), 0)
        self.assertEqual(multiply(7, 1), 7)

    def test_divide(self):
        self.assertEqual(divide(3, 2), 1.5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(0, 2), 0)
        self.assertEqual(divide(7, 1), 7)
        self.assertEqual(divide(7, 0), None)

if __name__ == '__main__':
    unittest.main()
