from typing import NoReturn

from cypher import Cypher


def main() -> NoReturn:
    choice: str = input("Что вы хотите сделать?\n1) Зашифровать\n2) Расшифровать\nВаш выбор\033[34m:\033[0m ")
    match choice:
        case "1":
            print(Cypher.encryption(input("Введите строчку: ")))
        case "2":
            print(Cypher.decryption())
        case _:
            print("\033[31mОшибка!\033[0m")


if __name__ == "__main__":
    main()