
class CountTimes:
    def a(ss, s):
        n = 0
        i = 1
        while i != -1:
            i = ss.find(s)
            if i >= 0:
                n += 1
            ss = ss[i + 1:]
        return n