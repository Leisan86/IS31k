import unittest
from second import vhojdenie
from first import urav
from third import crypt
class MyTestCase(unittest.TestCase):
    def test_Disc1(self):
        a = 2
        b = -5
        c = 2
        res = urav.d(a, b, c)
        self.assertEqual(res, "x1 = 2.0, x2 = 0.5")
    def test_Disc2(self):
        a = 3
        b = 2
        c = 5
        res = urav.d(a, b, c)
        self.assertEqual(res, "корней нет")
    def test_Disc3(self):
        a = 3
        b = -12
        c = 0
        res = urav.d(a, b, c)
        self.assertEqual(res, "x1 = 4.0, x2 = 0.0")
    def test_Disc4(self):
        a = 0
        b = 0
        c = 10
        res = urav.d(a, b, c)
        self.assertEqual(res, "неразрешимое уравнение")
    def test_Disc5(self):
        a = 0
        b = 0
        c = 0
        res = urav.d(a, b, c)
        self.assertEqual(res, "неразрешимое уравнение")
    def test_Disc6(self):
        a = 0
        b = 5
        c = 17
        res = urav.d(a, b, c)
        self.assertEqual(res, "неразрешимое уравнение")
    def test_Disc7(self):
        a = 9
        b = 0
        c = 0
        res = urav.d(a, b, c)
        self.assertEqual(res, 0.0)
    def test_CountTimes1(self):
        ab = "абвгабвг"
        a = "аб"
        res = vhojdenie.vhod(ab,a)
        self.assertEqual(res, 2)
    def test_CountTimes2(self):
        ab = "стстсап"
        a = "стс"
        res = vhojdenie.vhod(ab,a)
        self.assertEqual(res, 2)
    def test_getStr1(self):
        n = '1213'
        res = crypt.str(n)
        self.assertEqual(res, 'BC')
    def test_getStr2(self):
        n = '12907'
        res = crypt.str(n)
        self.assertEqual(res, 'Нужны корректные данные')
    def test_getNum1(self):
        n = 'asd'.upper()
        res = crypt.num(n)
        self.assertEqual(res, '114314')
    def test_getNum2(self):
        n = 'kmo7е'.upper()
        res = crypt.num(n)
        self.assertEqual(res, 'Нужны корректные данные')

if __name__ == '__main__':
    unittest.main()
