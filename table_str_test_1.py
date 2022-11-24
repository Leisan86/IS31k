class Str_test:
    @staticmethod
    def test(a, b):
        n = 0
        i = 1
        while i != -1:
            i = a.find(b)
            if i >= 0:
                n += 1
            a = a[i + 1:]
        return n
