def vrstica(s):
    niz=[]
    a = int(s.split(":")[0])
    b = s.split(":")[1].lstrip().split(" ")
    for c1, d2 in enumerate(b):
        if c1 == len(b)-1:
            e, f = int(d2.split("-")[0]), int(d2.split("-")[1])
        else:
            e, f = int(d2.split("-")[0]), int(d2.split("-")[1][:-1])
        niz.append((e, f ,a))
    return niz

def preberi(s):
    s = s.splitlines()
    seznam = []
    for x in s:
        seznam.extend(vrstica(x))
    return(seznam)

def intervali(xs):
    seznam=[]
    for x0, x1 in xs:
        x = str(x0)+'-'+(str(x1))
        seznam.append(x)
    return seznam

def zapisi_vrstico(y, xs):
    x = intervali(xs)
    rezultat = str(y) + ':'
    a = 0
    for e in x:
        if a != 0:
            rezultat = rezultat + ', ' + e
        else:
            rezultat = rezultat + ' ' + e
            a = 1
    return(rezultat)





#intervali, join, :




import unittest


class Obvezna(unittest.TestCase):
    def test_vrstica(self):
        self.assertEqual([(1, 3, 4), (5, 11, 4), (15, 33, 4)], vrstica("4: 1-3, 5-11, 15-33"))
        self.assertEqual([(989, 1300, 1234)], vrstica("1234: 989-1300"))

    def test_preberi(self):
        self.assertEqual([(5, 6, 4),
                          (90, 100, 13), (5, 8, 13), (9, 11, 13),
                          (9, 11, 5), (19, 20, 5), (30, 34, 5),
                          (9, 11, 4),
                          (22, 25, 13), (17, 19, 13)], preberi(
"""4: 5-6
13: 90-100, 5-8, 9-11
5: 9-11, 19-20, 30-34
4: 9-11
13:  22-25, 17-19
"""))

    def test_intervali(self):
        self.assertEqual(["6-10", "12-16", "20-22", "98-102"], intervali([(6, 10), (12, 16), (20, 22), (98, 102)]))

    def test_zapisi_vrstico(self):
        self.assertEqual("5: 6-10, 12-16", zapisi_vrstico(5, [(6, 10), (12, 16)]).rstrip("\n"))
        self.assertEqual("8: 6-10, 12-16, 20-22, 98-102", zapisi_vrstico(8, [(6, 10), (12, 16), (20, 22), (98, 102)]).rstrip("\n"))
        self.assertEqual("8: 6-10, 12-16, 20-22, 98-102", zapisi_vrstico(8, [(6, 10), (12, 16), (20, 22), (98, 102)]).rstrip("\n"))


class Dodatna(unittest.TestCase):
    def test_zapisi(self):
        ovire = [(5, 6, 4),
          (90, 100, 13), (5, 8, 13), (9, 11, 13),
          (9, 11, 5), (19, 20, 5), (30, 34, 5),
          (9, 11, 4),
          (22, 25, 13), (17, 19, 13)]
        kopija_ovir = ovire.copy()
        self.assertEqual("""4: 5-6, 9-11
5: 9-11, 19-20, 30-34
13: 5-8, 9-11, 17-19, 22-25, 90-100""", zapisi(ovire).rstrip("\n"))
        self.assertEqual(ovire, kopija_ovir)


if __name__ == "__main__":
    unittest.main()