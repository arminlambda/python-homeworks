import unittest


def stevilo_ovir(ovire):

    a = len(ovire)
    return a

def dolzina_ovir(ovire):
    b = 0
    for y in range(0, len(ovire)):
        b = b + (ovire[y][1] - ovire[y][0] + 1)
    return b

def sirina(ovire):
    c = 0
    for x1, x2,y in ovire:
        if x2 > c:
            c = x2
    return c

def pretvori_vrstico(vrstica):
    vrstice = []
    vrstica = "." + vrstica + "."
    for i in  range(len(vrstica)):
        if vrstica[i] == "#":
            if vrstica[i-1] == ".":
                zac = i
            if vrstica[i+1] == ".":
                vrstice.append((zac,i))
    return vrstice

def dodaj_vrstico(bloki,y):
    dv = []
    for x1, x2 in bloki:
        dv.append((x1,x2,y))
    return dv

def pretvori_zemljevid(zemljevid):
    karta = []
    for y in range(0,  len(zemljevid)):
        z = dodaj_vrstico(pretvori_vrstico(zemljevid[y]), y + 1)
        if z:
            karta = karta + z
    return karta


def globina(ovire,x):
    g = x
    ovr = 100
    for i in range(0, len(ovire)):
        vrs = ovire[i]
        if vrs[0] <= g <= vrs[1]:
            x = vrs[2]
            if ovr > x:
                ovr = x
    if ovr == 100:
        return None
    else:
        return ovr


def naj_stolpec(ovire):
    z = []
    d = len(ovire)
    x = 0
    b = 0
    kolo = 1
    for i in range(0, len(ovire)):
        o = ovire[i]
        if b < o[1]:
            b = o[1]
    y = b
    ovira1 = y
    kolesa = 1
    for i in range(0, d):
        vr = ovire[i]
        if vr[0] <= kolesa <= vr[1]:
            x= vr[2]
        if ovira1 > x:
            ovira1 = x

    while kolo <= b:
        naj_ovira = y
        for i in range(0,d):
            vr = ovire[i]
            if vr[0] <= kolo <= vr[1]:
                x = vr[2]
                if naj_ovira > x:
                    naj_ovira = x
        z.append(naj_ovira)
        kolo += 1
    for i in range(0, len(z)):
        if max(z) == z[i]:
            break
    if max(z) != 10:
        ja = max(z)
    else:
        ja = None
    return ((i+1),ja)


def senca(ovire):
    seznam = []
    b = 0
    for y in ovire:
        if (y[1] > b):
            b = y[1]
    i=1
    while i <= b:
        y = True
        for x in ovire:
            if(i >= x[0] and i <= x[1]):
                y = False
        i += 1
        seznam.append(y)
    return seznam



ovire1 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]

ovire2 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]

ovire3 = [(1, 3, 6), (2, 4, 3),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]


class Test(unittest.TestCase):
    def test_stevilo_ovir(self):
        self.assertEqual(7, stevilo_ovir(ovire1))
        self.assertEqual(6, stevilo_ovir(ovire2))
        self.assertEqual(0, stevilo_ovir([]))

    def test_dolzina_ovir(self):
        self.assertEqual(19, dolzina_ovir(ovire1))
        self.assertEqual(15, dolzina_ovir(ovire2))
        self.assertEqual(0, dolzina_ovir([]))

    def test_sirina(self):
        self.assertEqual(10, sirina(ovire1))
        self.assertEqual(9, sirina(ovire1[:-2]))
        self.assertEqual(6, sirina(ovire1[:-3]))
        self.assertEqual(3, sirina(ovire1[:1]))

    def test_pretvori_vrstico(self):
        self.assertEqual([(3, 5)], pretvori_vrstico("..###."))
        self.assertEqual([(3, 5), (7, 7)], pretvori_vrstico("..###.#."))
        self.assertEqual([(1, 2), (5, 7), (9, 9)], pretvori_vrstico("##..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#"))
        self.assertEqual([], pretvori_vrstico("..."))
        self.assertEqual([], pretvori_vrstico(".."))
        self.assertEqual([], pretvori_vrstico("."))

    def test_dodaj_vrstico(self):
        self.assertEqual([(3, 4, 3), (6, 8, 3), (11, 11, 3)], dodaj_vrstico([(3, 4), (6, 8), (11, 11)], 3))

    def test_pretvori_zemljevid(self):
        zemljevid = [
            "......",
            "..##..",
            ".##.#.",
            "...###",
            "###.##",
        ]
        self.assertEqual([(3, 4, 2), (2, 3, 3), (5, 5, 3), (4, 6, 4), (1, 3, 5), (5, 6, 5)], pretvori_zemljevid(zemljevid))

        global pretvori_vrstico
        pretvori = pretvori_vrstico
        try:
            def pretvori_vrstico(vrstica):
                return [(i, i) for i, c in enumerate(vrstica) if c == "#"]
            self.assertEqual([(2, 2, 2), (3, 3, 2), (1, 1, 3), (2, 2, 3), (4, 4, 3), (3, 3, 4), (4, 4, 4),
                              (5, 5, 4), (0, 0, 5), (1, 1, 5), (2, 2, 5), (4, 4, 5), (5, 5, 5)],
                             pretvori_zemljevid(zemljevid),
                             "Funkcija pretvori_zemljevid naj kar lepo uporabi pretvori_vrstico")
        finally:
            pretvori_vrstico = pretvori

        global dodaj_vrstico
        dodaj = dodaj_vrstico
        try:
            def dodaj_vrstico(ovire, vrstica):
                return [(*o, 2 * vrstica) for o in ovire]

            self.assertEqual([(3, 4, 4), (2, 3, 6), (5, 5, 6), (4, 6, 8), (1, 3, 10), (5, 6, 10)],
                             pretvori_zemljevid(zemljevid),
                             "Funkcija pretvori_zemljevid naj kar lepo uporabi dodaj_vrstico")
        finally:
            dodaj_vrstico = dodaj

    def test_globina(self):
        self.assertEqual(3, globina(ovire1, 3))
        self.assertEqual(5, globina(ovire1, 6))
        self.assertEqual(7, globina(ovire2, 6))
        self.assertIsNone(globina(ovire3, 6))

    def test_naj_stolpec(self):
        self.assertEqual((5, 7), naj_stolpec(ovire1))
        self.assertEqual((7, None), naj_stolpec(ovire2))
        self.assertEqual((5, None), naj_stolpec(ovire3))

    def test_senca(self):
        self.assertEqual([False] * 10, senca(ovire1))
        self.assertEqual([False, False, False, False, False, False, True, True, False, False], senca(ovire2))
        self.assertEqual([False, False, False, False, True, True, True, True, False, False], senca(ovire3))
        self.assertEqual([False] * 6, senca(ovire2[:-3]))
        self.assertEqual([False] * 3, senca(ovire3[:1]))


if __name__ == "__main__":
    unittest.main()