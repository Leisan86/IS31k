class crypt:
    def num(n):
        square = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
                  'F': 21, 'G': 22, 'H': 23, 'I': 24, 'K': 25,
                  'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
                  'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
                  'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
        }
        list1 = ''
        list2 = list(n)
        for i in n:
            if i in square:
                list1 += str(square.get(i, 0))
            elif i not in square:
                list1 = 'Нужны корректные данные'
                break
            else:
                list1 += (i + i)
        return list1


    def str(n):
        square = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
                  'F': 21, 'G': 22, 'H': 23, 'I': 24, 'K': 25,
                  'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
                  'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
                  'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
        }

        if n.isnumeric() != True:
            ab = f'Нужны корректные данные'
        else:
            ab = ''
            list_ab = []
            step = 2
            for i in range(0, len(n), 2):
                list_ab.append(n[i:step])
                step += 2
            list_ab = list(map(int, list_ab))
            key_square = list(square.keys())
            val_square = list(square.values())

            for i in list_ab:
                if i in val_square:
                    i = val_square.index(i)
                    ab += key_square[i]
                elif i not in val_square:
                    ab = f'Нужны корректные данные'

                    break
                else:
                    ab += i[0:1]
            return ab


