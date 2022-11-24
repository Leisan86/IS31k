import unittest
from second import CountTimes
from first import Disc
from third import shiphr
class MyTestCase(unittest.TestCase):
    def test_Disc1(self):
        a = 2
        b = -5
        c = 2
        res = Disc.d(a, b, c)
        self.assertEqual(res, "x1 = 2.0, x2 = 0.5")
    def test_Disc2(self):
        a = 3
        b = 2
        c = 5
        res = Disc.d(a, b, c)
        self.assertEqual(res, "корней нет")
    def test_Disc3(self):
        a = 3
        b = -12
        c = 0
        res = Disc.d(a, b, c)
        self.assertEqual(res, "x1 = 4.0, x2 = 0.0")
    def test_Disc4(self):
        a = 0
        b = 0
        c = 10
        res = Disc.d(a, b, c)
        self.assertEqual(res, "неразрешимое уравнение")
    def test_Disc5(self):
        a = 0
        b = 0
        c = 0
        res = Disc.d(a, b, c)
        self.assertEqual(res, "неразрешимое уравнение")
    def test_Disc6(self):
        a = 0
        b = 5
        c = 17
        res = Disc.d(a, b, c)
        self.assertEqual(res, "неразрешимое уравнение")
    def test_Disc7(self):
        a = 9
        b = 0
        c = 0
        res = Disc.d(a, b, c)
        self.assertEqual(res, 0.0)
    def test_CountTimes1(self):
        ss = "абвгабвг"
        s = "аб"
        res = CountTimes.a(ss,s)
        self.assertEqual(res, 2)
    def test_CountTimes2(self):
        ss = "стстсап"
        s = "стс"
        res = CountTimes.a(ss,s)
        self.assertEqual(res, 2)
    def test_getStr1(self):
        n = '1213'
        res = shiphr.getStr(n)
        self.assertEqual(res, 'BC')
    def test_getStr2(self):
        n = '123'
        res = shiphr.getStr(n)
        self.assertEqual(res, 'Введите корректные данные')
    def test_getNum1(self):
        n = 'asd'.upper()
        res = shiphr.getNum(n)
        self.assertEqual(res, '114314')
    def test_getNum2(self):
        n = 'ыфва'.upper()
        res = shiphr.getNum(n)
        self.assertEqual(res, 'Введите корректные данные')

if __name__ == '__main__':
    unittest.main()
