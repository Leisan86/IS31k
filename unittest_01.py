import unittest
from Equal import Equation
from table_str_test_1 import Str_test
from Cube_01 import Cube

class This_Unit_Test(unittest.TestCase):
    def test_1_disc(self):
        a = 2
        b = -5
        c = 2
        s = Equation.equation(a, b, c)
        self.assertEqual(s, None)
    def test_2_disc(self):
        a = 3
        b = 2
        c = 5
        s = Equation.equation(a, b, c)
        self.assertEqual(s, 'Корней нет')
    def test_3_disc(self):
        a = 2
        b = -12
        c = 0
        s = Equation.equation(a, b, c)
        self.assertEqual(s, None)
    def test_4_disc(self):
        a = 0
        b = 0
        c = 10
        s = Equation.equation(a, b, c)
        self.assertEqual(s, 'Нерешимое уравнение')
    def test_5_disc(self):
        a = 0
        b = 0
        c = 0
        s = Equation.equation(a, b, c)
        self.assertEqual(s, 'Нерешимое уравнение')
    def test_6_disc(self):
        a = 0
        b = 5
        c = 17
        s = Equation.equation(a, b, c)
        self.assertEqual(s, "Неквадратное уравнение")
    def test_7_disc(self):
        a = 9
        b = 0
        c = 0
        s = Equation.equation(a, b, c)
        self.assertIn(s, "Нулевые корни")

    def test_1(self):
        a = 'абвгабвг'
        b = 'аб'
        c = Str_test.test(a, b)
        self.assertEqual(c, 2)
    def test_2(self):
        a = 'стстсап'
        b = 'стс'
        c = Str_test.test(a, b)
        self.assertEqual(c, 2)

    def test_Strr1(self):
        n = '2344443543'
        s = Cube.Strr(n)
        self.assertEqual(s, 'HTTPS')
    def test_Strr2(self):
        n = '348'
        s = Cube.Strr(n)
        self.assertEqual(s, 'Введите корректные данные')
    def test_Numm1(self):
        n = 'milf'.upper()
        s = Cube.Numm(n)
        self.assertEqual(s, '32243121')
    def test_Numm2(self):
        n = 'аиаи'.upper()
        s = Cube.Numm(n)
        self.assertEqual(s, 'Введите корректные данные')

if __name__ == '__main__':
    unittest.main()




