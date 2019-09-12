import unittest as pyunit
import calculator as calc

class TestCalculator(pyunit.TestCase):
    
    def test_add(self):
        result = calc.add(5, 5)
        self.assertEqual(result, 10)

    def test_subtract(self):
        result = calc.subtract(3, 2)
        self.assertEqual(result, 1)

        result = calc.subtract(2, 3)
        self.assertEqual(result, -1)

    def test_multiply(self):
        result = calc.multiply(4, 2)
        self.assertEqual(result, 8)

        result = calc.multiply(4, 0)
        self.assertEqual(result, 0)

    def test_divide(self):
        result = calc.divide(6, 3)
        self.assertEqual(result, 2)

        self.assertRaises(ValueError, calc.divide, 6, 0)

if __name__ == '__main__':
    pyunit.main()