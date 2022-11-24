from quadratic_equation import QuadraticEquation

if __name__ == '__main__':
    quadraticEquation = QuadraticEquation()
    a, b, c = list(map(int, input("Введите три числа через пробел: ").split()))
    print(quadraticEquation.work7__1(a, b, c))