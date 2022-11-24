from typing import NoReturn

from quadratic_equation import QuadraticEquation


def main() -> NoReturn:
    a, b, c = list(map(int, input("Введите три числа через пробел: ").split()))
    print(QuadraticEquation.rooting(a, b, c))


if __name__ == "__main__":
    main()
