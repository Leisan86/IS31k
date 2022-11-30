from os import system
from typing import NoReturn


def main() -> NoReturn:
    choice: str = input("Какой вариант хотите запустить?\n1) Лаб.7\n2) Лаб.8\nВаш выбор\033[34m:\033[0m ")
    match choice:
        case "1":
            choice_low: str = input(
                "Что хотите выполнить?\n1) запустить main.py\n2) запустить unit test\nВаш выбор\033[34m:\033[0m ")
            match choice_low:
                case "1":
                    print("Идёт выполнение \033[33mmain.py\033[0m:")
                    system("python ./Lab7/main.py")
                    print("Выполнение \033[33mmain.py\033[0m окончено")
                case "2":
                    print("Идёт выполнение \033[33munit test\033[0m:")
                    system("python ./Lab7/quadratic_equation_test.py")
                    print("Выполнение \033[33munit test\033[0m окончено")
                case _:
                    print("\033[31mОшибка!\033[0m")
        case "2":
            choice_low: str = input(
                "Что хотите выполнить?\n1) запустить main.py\n2) запустить unit test\nВаш выбор\033[34m:\033[0m ")
            match choice_low:
                case "1":
                    print("Идёт выполнение \033[33mmain.py\033[0m:")
                    system("python ./Lab8/main.py")
                    print("Выполнение \033[33mmain.py\033[0m окончено")
                case "2":
                    print("Идёт выполнение \033[33munit test\033[0m:")
                    system("python ./Lab8/cypher_test.py")
                    print("Выполнение \033[33munit test\033[0m окончено")
                case _:
                    print("\033[31mОшибка!\033[0m")
        case _:
            print("\033[31mОшибка!\033[0m")


if __name__ == "__main__":
    main()