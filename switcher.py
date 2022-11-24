import os
from typing import NoReturn


def main() -> NoReturn:
    choice = int(input("Введите вариант работы(1-18): "))

    if choice in range(1, 19):
        if os.system(f"git switch {choice}") == 0:
            print(f"\033[33mИдет выполнение работы\033[0m \033[31m{choice}\033[33m варианта\033[0m")
            if os.path.exists("main.py"):
                os.system("python main.py")
            else:
                print("\033[31mОшибка!\033[0m\nНе найден \033[33mmain.py\033[0m")
        else:
            print("\033[31mОшибка!\033[0m\nВетка не была найдена. Попробуйте обновить командой \033[33mgit pull\033[0m")
    else:
        print("\033[31mОшибка!\033[0m\nДоступные значение с 1 до 18")


if __name__ == "__main__":
    main()