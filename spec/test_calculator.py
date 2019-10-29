import unittest as pyunit
import calculator as calc

class TestCalculator(pyunit.TestCase):
    
    def test_add(self):
        result = calc.add(0,0)
        self.assertEqual(result, 0)

        result = calc.add(-1,-1)
        self.assertEqual(result, -2)

        result = calc.add(5, 4)
        self.assertEqual(result, 9)

    def test_add_of_many(self):
        result = calc.add(1, 2, 3)
        self.assertEqual(result, 6)

        result = calc.add(1, -2, 3)
        self.assertEqual(result, 2)

        result = calc.add(-1, -2, -3)
        self.assertEqual(result, -6)

        result = calc.add(1, 2, 3, 4)
        self.assertEqual(result, 10)

    def test_multiply(self):
        result = calc.multiply(4, 2)
        self.assertEqual(result, 8)

        result = calc.multiply(4, 0)
        self.assertEqual(result, 0)

        result = calc.multiply(4, -2)
        self.assertEqual(result, -8)

    def test_multiply_of_many(self):
        result = calc.multiply(4, 2, 1)
        self.assertEqual(result, 8)

        result = calc.multiply(4, 0)
        self.assertEqual(result, 0)

        result = calc.multiply(4, -2, 9)
        self.assertEqual(result, -72)

        result = calc.multiply(4, -2, -1)
        self.assertEqual(result, 8)

        result = calc.multiply(4, 2, 2, 2)
        self.assertEqual(result, 32)

if __name__ == '__main__':
    pyunit.main()