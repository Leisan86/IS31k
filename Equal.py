class Equation:
    @staticmethod
    def equation(a, b, c):
        disc = b ** 2 - 4 * a * c
        if a == 0 and b == 0:
            return f'Нерешимое уравнение'
        elif a == 0:
            return f'Неквадратное уравнение'
        elif b == 0 and c == 0:
            return f'Нулевые корни'
        elif disc < 0:
            return f'Корней нет'
        else:
            if disc > 0:
                x1 = (-b + disc ** 0.5) / (2 * a)
                x2 = (-b - disc ** 0.5) / (2 * a)
                print('x1 = ' + str(x1))
                print('x2 = ' + str(x2))
            elif disc == 0:
                return f'x = {-b / (2 * a)}'