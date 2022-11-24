from math import sqrt


class QuadraticEquation:
    def work7__1(self, a: int, b: int, c: int) -> str:
        # a, b, c = map(int, input("Введите три числа через пробел: ").split())
        D: int = b ** 2 - 4 * a * c

        if not a and not b:
            return "Неразрешимое уравнение"
        elif not a:
            return "Неквадратное уравнение"
        elif D < 0:
            return "Случай комплексных корней"
        elif not b and not c:
            return "x1 = 0\n x2 = 0"
        else:
            if D > 0:
                return f"x1 = {(-b + sqrt(D)) / (2 * a)}\nx2 = {(-b - sqrt(D)) / (2 * a)}"
            elif not D:
                return f"x = {-b / (2 * a)}"
