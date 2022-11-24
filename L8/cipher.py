class Cipher:
    square = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
              'F': 21, 'G': 22, 'H': 23, 'I': 24, 'K': 25,
              'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
              'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
              'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
              }

    @staticmethod
    def encryption(string: str) -> str:
        string = string.upper()
        result: str = ''
        list_mess: list = list(string)
        for i in string:
            if i in Cipher.square:
                result += str(Cipher.square.get(i, 0))
            elif i not in Cipher.square:
                return "Введите корректные данные"
            else:
                result += (i + i)

        with open(".cipher", "w") as file:
            file.write(result)
            file.close()

        return f"Шифр записан в файл \"\033[32m.cipher\033[0m\" как {result}"

    @staticmethod
    def decryption():
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
            key_square: list = list(Cipher.square.keys())
            val_square: list = list(Cipher.square.values())

            for i in list_ss:
                if i in val_square:
                    i = val_square.index(i)
                    result += key_square[i]
                elif i not in val_square:
                    return "Введите числа!"
                else:
                    result += i[0:1]

            return f"\033[32m{result}\033[0m"
