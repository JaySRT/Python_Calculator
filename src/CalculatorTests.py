import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(4, 2), 2)
        self.assertEqual(calculator.result, 2)

    def test_multiplication_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiplication(4, 2), 8)
        self.assertEqual(calculator.result, 8)


if __name__ == '__main__':
    unittest.main()
