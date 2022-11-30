from typing import NoReturn

import matrix


def main() -> NoReturn:
    w, h = map(int, input("Введите длину и ширину матрицы через пробел\033[34m:\033[0m ").split())

    variable = matrix.create_matrix(h, w)

    print(variable, '\nМаксимальный элемент: ', matrix.maximum_element(variable))


if __name__ == "__main__":
    main()
