from typing import NoReturn

from cipher import Cipher


def main() -> NoReturn:
    choice: str = input("Что вы хотите сделать?\n1) Зашифровать\n2) Расшифровать\nВаш выбор: ")
    match choice:
        case "1":
            print(Cipher.encryption(input("Введите строчку: ")))
        case "2":
            print(Cipher.decryption())
        case _:
            print("\033[31mОшибка!\033[0m")


if __name__ == "__main__":
    main()
