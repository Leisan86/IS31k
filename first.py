import math

class urav():

    def d(a, b, c):
        try:
            D = b ** 2 - 4 * a * c

            if D > 0:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                return f'x1 = {x1}, x2 = {x2}'
            elif D == 0:
                x = -b / (2 * a)
                return x
            else:
                return f'корней нет'
        except (ZeroDivisionError):
            return f'неразрешимое уравнение'

