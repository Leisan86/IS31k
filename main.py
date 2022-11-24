from first import urav
from second import vhojdenie
from third import crypt
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    ab = input()
    a1 = input()

    n = input().upper()
    m = input()

    print(urav.d(a, b, c))
    print(vhojdenie.vhod(ab, a1))
    print(crypt.num(n))
    print(crypt.str(m))