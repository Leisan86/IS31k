import unittest
from Calc import Calc


class CalcTestCase(unittest.TestCase):
    def test_sum_positive(self):
        a = 2
        b = 3
        res = Calc.sum(a, b)
        self.assertEqual(res, 5)

    def test_sum_negative(self):
        a = -2
        b = 5
        res = Calc.sum(a, b)
        self.assertEqual(res, 3)

    def test_sum_zero(self):
        a = 1
        b = 0
        res = Calc.sum(a, b)
        self.assertEqual(res, 1)

    def test_div_zero(self):
        a = 1
        b = 0
        res = Calc.divizion(a, b)
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
