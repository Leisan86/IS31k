a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
D = b ** 2 - 4 * a * c

if a == 0 and b == 0:
    print("Неразрешимое уравнение")
elif a == 0:
    print("Неквадратное уравнение")
elif D > 0:
    x1 = (-b + D ** (1 / 2)) / (2 * a)
    x2 = (-b - D ** (1 / 2)) / (2 * a)
    print('x1 =', x1)
    print('x2 =', x2)
    print("Случай вещественных корней")
elif D == 0:
    x = (-b) / (2 * a)
    print("x1 = x2 =", x)
    print("Нулевые корни")
else:
    print("Случай комплексных чисел")
