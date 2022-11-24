from os import system

if __name__ == "__main__":
    choise: str = input("Какой вариант хотите запустить?\n1) 7\n2) 8\nВаш выбор: ")
    match choise:
        case "1":
            choise_low: str = input("Что хотите сделать?\n1) запустить main.py\n2) запустить unit test\nВаш выбор: ")
            match choise_low:
                case "1":
                    print("Идёт выполнение \033[33mmain.py\033[0m:")
                    system("python ./L7/main.py")
                    print("Выполнение \033[33mmain.py\033[0m окончено")
                case "2":
                    print("Идёт выполнение \033[33munit test\033[0m:")
                    system("python ./L7/quadratic_equation_test.py")
                    print("Выполнение \033[33munit test\033[0m окончено")
                case _:
                    print("\033[31mОшибка!\033[0m")
        case "2":
            choise_low: str = input("Что хотите сделать?\n1) запустить main.py\n2) запустить unit test\nВаш выбор: ")
            match choise_low:
                case "1":
                    print("Идёт выполнение \033[33mmain.py\033[0m:")
                    system("python ./L8/main.py")
                    print("Выполнение \033[33mmain.py\033[0m окончено")
                case "2":
                    print("Идёт выполнение \033[33munit test\033[0m:")
                    # system("python ./L8/quadratic_equation_test.py")
                    print("Выполнение \033[33munit test\033[0m окончено")
                case _:
                    print("\033[31mОшибка!\033[0m")
        case _:
            print("\033[31mОшибка!\033[0m")
