import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self. calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(4, 2), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_multiplication_method_calculator(self):
        self.assertEqual(self.calculator.multiplication(4, 2), 8)
        self.assertEqual(self.calculator.result, 8)

    def test_division_method_calculator(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(4), 16)
        self.assertEqual(self.calculator.result, 16)

    def test_sqrt_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.result, 2)


if __name__ == '__main__':
    unittest.main()
