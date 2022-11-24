class Disc:
    def urav(a,b,c):
        if type(a) != int or type(b) != int or type(c) != int:
            return f"Нужны числа!"
        if a == 0 and b != 0 and c != 0:
            return f"Неквадратное уравнение"
        elif a == 0 and b == 0 or a == 0 and c == 0:
            return f"Неразрешимое уравнение"
        D = b**2 - 4 * a * c
        if D < 0:
            return f"Случай комплексных корней"
        elif D > 0:
            return f"x2 = {(-b - D ** 0.5) / (2 * a)} x1 = {(-b + D**0.5)/(2 * a)}"

        elif D == 0:
            return f"Уравнение имеет один корень x = {-b/(2 * a)}"

