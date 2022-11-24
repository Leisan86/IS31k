from first import Disc
from second import CountTimes
from third import shiphr
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    ss = input()
    s = input()

    n = input().upper()
    m = input()

    print(Disc.d(a, b, c))
    print(CountTimes.a(ss, s))
    print(shiphr.getNum(n))
    print(shiphr.getStr(m))