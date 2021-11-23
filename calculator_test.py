
from unittest import TestCase, main

from pyTests.applications.calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)  # add assertion here

    def test_minus(self):
        self.assertEqual(calculator('4-2'), 2)

    def test_multi(self):
        self.assertEqual(calculator('6*2'), 12)

    def test_divide(self):
        self.assertEqual(calculator('12/2'), 6.0)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('adidas')
        self.assertEqual('Вираз повинен містити хоча б один знак (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+4*5')
        self.assertEqual('Вираз повинен містити 2 цілі числа і 1 знак', e.exception.args[0])

    def test_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.0+4*5')
        self.assertEqual('Вираз повинен містити 2 цілі числа і 1 знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Вираз повинен містити 2 цілі числа і 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()