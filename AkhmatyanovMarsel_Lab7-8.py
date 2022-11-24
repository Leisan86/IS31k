# работа 1

import math

a, b, c = int(input()), int(input()), int(input())

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('корней нет')

# работа 2

ss = input()
s = input()

n = 0
i = 1

while i != -1:
    i = ss.find(s)
    if i >= 0:
        n += 1
    ss = ss[i + 1:]
print(n)

# работа 3

square = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
          'F': 21, 'G': 22, 'H': 23, 'I': 24, 'K': 25,
          'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
          'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
          'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
          }

# n = input().upper()
m = input().upper()


def getNum(n):
    mess = ''
    list_mess = list(n)
    for i in n:
        if i in square:
            mess += str(square.get(i, 0))
        elif i not in square:
            print('Введите корректные данные')
            break
        else:
            mess += (i + i)
    return mess


def getStr(n):
    if n.isnumeric() != True:
        return f'Введите корректные данные'
    else:
        ss = ''
        list_ss = []
        step = 2
        for i in range(0, len(n), 2):
            list_ss.append(n[i:step])
            step += 2
        list_ss = list(map(int, list_ss))
        key_square = list(square.keys())
        val_square = list(square.values())

        for i in list_ss:
            if i in val_square:
                i = val_square.index(i)
                ss += key_square[i]
            elif i not in val_square:
                return f'Введите корректные данные'
            else:
                ss += i[0:1]
        return ss


# print(getNum(n))
print(getStr(m))