from lab8 import cyphr
from lab72 import CountTimes
from lab71 import Disc

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    a1 = input()
    b1 = input()

    n = input().lower()
    m = input()

    print(Disc.urav(a, b, c))
    print(CountTimes.stroka(b1, a1))
    print(cyphr.shiphr(n))
    print(cyphr.decode(m))