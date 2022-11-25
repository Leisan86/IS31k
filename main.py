from math import sqrt
from typing import NoReturn


def work7__1() -> str:
    a, b, c = map(int, input("Введите три числа через пробел: ").split())
    D: int = b ** 2 - 4 * a * c

    if not a and not b:
        return "Неразрешимое уравнение"
    elif not a:
        return "Неквадратное уравнение"
    elif D < 0:
        return "Случай комплексных корней"
    elif not b and not c:
        return "x1 = 0\nx2 = 0"
    else:
        if D > 0:
            return f"x1 = {(-b + sqrt(D)) / (2 * a)}\nx2 = {(-b - sqrt(D)) / (2 * a)}"
        elif not D:
            return f"x = {-b / (2 * a)}"


def work7__3() -> NoReturn:
    s1, s2 = map(str, input("Введите две строки через пробел: ").split())

    result: int = 0
    counter: int = 1
    while counter != -1:
        counter = s1.find(s2)
        if counter >= 0:
            result += 1
        s1 = s1[counter + 1:]
    return f"Вывод: {str(result)}"


def work8__1() -> NoReturn:
    square = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
              'F': 21, 'G': 22, 'H': 23, 'I': 24, 'K': 25,
              'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
              'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
              'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
              }
    choice: str = input("Что вы хотите сделать?\n1) Зашифровать\n2) Расшифровать\nВаш выбор\033[34m:\033[0m ")

    match choice:
        case "1":
            string = input("Введите строчку\033[34m:\033[0m ").upper()
            result: str = ''
            list_mess: list = list(string)
            for i in string:
                if i in square:
                    result += str(square.get(i, 0))
                elif i not in square:
                    return "Введите корректные данные"
                else:
                    result += (i + i)

            with open(".cipher", "w") as file:
                file.write(result)
                file.close()

            return f"Шифр записан в файл \"\033[32m.cipher\033[0m\" как {result}"

        case "2":
            with open(".cipher", "r") as file:
                integer: str = file.read()
                file.close()

            if not integer.isnumeric():
                return "Введите числа!"
            else:
                result: str = ''
                list_ss: list = list()
                step: int = 2
                for i in range(0, len(integer), 2):
                    list_ss.append(integer[i:step])
                    step += 2
                list_ss: list = list(map(int, list_ss))
                key_square: list = list(square.keys())
                val_square: list = list(square.values())

                for i in list_ss:
                    if i in val_square:
                        i = val_square.index(i)
                        result += key_square[i]
                    elif i not in val_square:
                        return "Введите числа!"
                    else:
                        result += i[0:1]

                return f"\033[32m{result}\033[0m"
        case _:
            return "\033[31mОшибка!\033[0m"


def work8__3() -> NoReturn:
    return "Будет в отчете"


def main() -> NoReturn:
    variant = input("Введите вариант(7-8)\033[34m:\033[0m ")
    match variant:
        case "7":
            work = input("Введите задание(1-3)\033[34m:\033[0m ")

            match work:
                case "1":
                    print(work7__1())
                case "2":
                    print(work7__1())
                case "3":
                    print(work7__3())
                case _:
                    print("\033[31mОшибка!\033[0m")
        case "8":
            work = input("Введите задание(1-3)\033[34m:\033[0m ")

            match work:
                case "1":
                    print(work8__1())
                case "2":
                    print(work8__1())
                case "3":
                    print(work8__3())
                case _:
                    print("\033[31mОшибка!\033[0m")


if __name__ == "__main__":
    main()
