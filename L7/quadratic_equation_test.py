import unittest

from quadratic_equation import QuadraticEquation


class MyTestCase(unittest.TestCase):

    def test1(self):
        a, b, c = 2, -5, 2
        result = QuadraticEquation.rooting(a, b, c)
        self.assertEqual(result, "x1 = 2.0\nx2 = 0.5")

    def test2(self):
        a, b, c = 3, 2, 5
        result = QuadraticEquation.rooting(a, b, c)
        self.assertEqual(result, "Случай комплексных корней")

    def test3(self):
        a, b, c = 3, -12, 0
        result = QuadraticEquation.rooting(a, b, c)
        self.assertEqual(result, "x1 = 4.0\nx2 = 0.0")

    def test4(self):
        a, b, c = 0, 0, 10
        result = QuadraticEquation.rooting(a, b, c)
        self.assertEqual(result, "Неразрешимое уравнение")

    def test5(self):
        a, b, c = 0, 0, 0
        result = QuadraticEquation.rooting(a, b, c)
        self.assertEqual(result, "Неразрешимое уравнение")

    def test6(self):
        a, b, c = 0, 5, 17
        result = QuadraticEquation.rooting(a, b, c)
        self.assertEqual(result, "Неквадратное уравнение")

    def test7(self):
        a, b, c = 9, 0, 0
        result = QuadraticEquation.rooting(a, b, c)
        self.assertEqual(result, "x1 = 0\n x2 = 0")


if __name__ == '__main__':
    unittest.main()