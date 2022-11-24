import unittest
from lab8 import cyphr
from lab72 import CountTimes
from lab71 import Disc

class MyTestCase(unittest.TestCase):
    def test_Disc1(self):
        a = 2
        b = -5
        c = 2
        res = Disc.urav(a, b, c)
        self.assertEqual(res, "x2 = 0.5 x1 = 2.0")

    def test_Disc2(self):
        a = 3
        b = 2
        c = 5
        res = Disc.urav(a, b, c)
        self.assertEqual(res, "Случай комплексных корней")

    def test_Disc3(self):
        a = 3
        b = -12
        c = 0
        res = Disc.urav(a, b, c)
        self.assertEqual(res, "x2 = 0.0 x1 = 4.0")

    def test_Disc4(self):
        a = 0
        b = 0
        c = 10
        res = Disc.urav(a, b, c)
        self.assertEqual(res, "Неразрешимое уравнение")

    def test_Disc5(self):
        a = 0
        b = 0
        c = 0
        res = Disc.urav(a, b, c)
        self.assertEqual(res, "Неразрешимое уравнение")

    def test_Disc6(self):
        a = 0
        b = 5
        c = 17
        res = Disc.urav(a, b, c)
        self.assertEqual(res, "Неквадратное уравнение")

    def test_Disc7(self):
        a = 9
        b = 0
        c = 0
        res = Disc.urav(a, b, c)
        self.assertEqual(res, "Уравнение имеет один корень x = 0.0")

    def test_CountTimes1(self):
        a = "абвгабвг"
        b = "аб"
        res = CountTimes.stroka(b, a)
        self.assertEqual(res, 2)

    def test_CountTimes2(self):
        a = "стстсап"
        b = "стс"
        res = CountTimes.stroka(b, a)
        self.assertEqual(res, 2)

    def decode1(self):
        n = '1213'
        res = cyphr.decode(n)
        self.assertEqual(res, 'bc')

    def decode2(self):
        n = '123'
        res = cyphr.decode(n)
        self.assertEqual(res, 'Введите четную длину кол-ва чисел')

    def shiphr1(self):
        n = 'asd'.upper()
        res = cyphr.shiphr(n)
        self.assertEqual(res, '114314')

    def shiphr2(self):
        n = 'ыфва'.upper()
        res = cyphr.shiphr(n)
        self.assertEqual(res, 'Введены не верные данные!')


if __name__ == '__main__':
    unittest.main()
