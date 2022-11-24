class cyphr:
    def shiphr(word):
        matrix = [['a', 'b', 'c', 'd', 'e'],
                  ['f', 'g', 'h', 'i', 'k'],
                  ['l', 'm', 'n', 'o', 'p'],
                  ['q', 'r', 's', 't', 'u'],
                  ['v', 'w', 'x', 'y', 'z']]

        try:
            if int(word) > 0:
                return f"Введите строку!"
        except ValueError:

            a = 0
            for i in range(len(word)+2):
                if a == 12:
                    break
                for j in range(len(matrix[i])):
                    if i+2 > len(matrix[i]):
                        a = 12
                    if matrix[i][j] in word:
                        word = word.replace(matrix[i][j], str(i+1) + (str(j+1)))
            return word

    def decode(word):
        matrix = [['a', 'b', 'c', 'd', 'e'],
                  ['f', 'g', 'h', 'i', 'k'],
                  ['l', 'm', 'n', 'o', 'p'],
                  ['q', 'r', 's', 't', 'u'],
                  ['v', 'w', 'x', 'y', 'z']]

        try:
            word1 = word
            for i in range(len(word)):
                if i+2 > len(word):
                    break
                try:
                    if len(word1) % 2 != 0:
                        return f"Введите четную длину кол-ва чисел"
                    else:
                        try:
                            word = word.replace(word[i] + word[i+1], matrix[int(word[i]) - 1][int(word[i+1]) - 1],1)
                        except IndexError:
                            return f"Зашифрованные числа должны быть двухзначными и от 1-5"
                except ValueError:
                    return f"Введены не верные данные!"

            return word
        except TypeError:
            return f"Для расшифрофки нужны числа!"


