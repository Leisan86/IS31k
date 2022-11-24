from typing import NoReturn


class Cipher:
    def work8__1(self) -> NoReturn:
        square = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
                  'F': 21, 'G': 22, 'H': 23, 'I': 24, 'K': 25,
                  'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
                  'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
                  'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
                  }
        vr: str = input("Что вы хотите сделать?\n1) Зашифровать\n2) Расшифровать\nВаш выбор: ")

        match vr:
            case "1":
                strng: str = input("Введите строчку: ").upper()

                mess: str = ''
                list_mess: list = list(strng)
                for i in strng:
                    if i in square:
                        mess += str(square.get(i, 0))
                    elif i not in square:
                        print('Введите корректные данные')
                        break
                    else:
                        mess += (i + i)

                with open(".last string", "w") as file:
                    file.write(mess)
                    file.close()
                print("Шифр записан в файл \033[32m\".last string\"\033[0m")
            case "2":
                with open(".last string", "r") as file:
                    intgr: str = file.read()
                    file.close()

                if not intgr.isnumeric():
                    print("Введите числа!")
                    quit()
                else:
                    ss: str = ''
                    list_ss: list = []
                    step: int = 2
                    for i in range(0, len(intgr), 2):
                        list_ss.append(intgr[i:step])
                        step += 2
                    list_ss: list = list(map(int, list_ss))
                    key_square: list = list(square.keys())
                    val_square: list = list(square.values())

                    for i in list_ss:
                        if i in val_square:
                            i = val_square.index(i)
                            ss += key_square[i]
                        elif i not in val_square:
                            print("Введите числа!")
                        else:
                            ss += i[0:1]
                    print(f"\033[32m{ss}\033[0m")
            case _:
                print("Ошибка!")