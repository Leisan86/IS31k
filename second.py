
class vhojdenie:
    def vhod(ab, a):
        n = 0
        i = 1
        while i != -1:
            i = ab.find(a)
            if i >= 0:
                n += 1
            ab = ab[i + 1:]
        return n