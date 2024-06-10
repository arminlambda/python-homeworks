import unittest
from unittest.mock import patch

class Steza:

    def __init__(self, x, y, ovire):
        self.x = x
        self.y = y
        self.ovire = ovire

    def zaprto(self, x, y):
        for ovira in self.ovire:
            y0, x0, x1 = ovira
            if x0 <= x <= x1 and y == y0:
                return True
        return False

    def konec(self, x, y, smer):
        if smer == ">":
            for x in range(x, self.x + 1):
                if self.zaprto(x, y):
                    return (x - 1, y)
            return (self.x, y)
        elif smer == "<":
            for x in range(x, 0, -1):
                if self.zaprto(x, y):
                    return (x + 1, y)
            return (1, y)
        elif smer == "v":
            for y in range(y, self.y + 1):
                if self.zaprto(x, y):
                    return (x, y - 1)
            return (x, self.y)
        elif smer == "^":
            for y in range(x, 0, -1):
                if self.zaprto(x, y):
                    return (x, y + 1)
            return (x, 1)

class Kolesar:

    def __init__(self, x, y, Steza):
        self.x = x
        self.y = y
        self.Steza = Steza
        self.prevozena_razdalja = 0

    def pozicija(self):
        return (self.x, self.y)

    def premik(self, smer):  # (self.Steza.konec(self.x,self.y, smer)
        x, y = self.Steza.konec(self.x, self.y, smer)
        self.prevozena_razdalja += abs(x - self.x) + abs(y - self.y)
        self.x = x
        self.y = y

    def prevozeno(self):
        return self.prevozena_razdalja


"""class AvtonomniKolesar(Kolesar):

    def __init__(self,x,y,Steza,nacrt):
        super().__init__(x,y,Steza)
        self.nacrt = nacrt"""










class TestBase(unittest.TestCase):
    ovire = [(1, 1, 3), (1, 5, 6), (1, 8, 8), (1, 10, 10),
             (2, 5, 6), (2, 13, 16),
             (4, 9, 11), (4, 13, 14),
             (5, 1, 3), (5, 15, 17),
             (6, 5, 6), (6, 8, 9),
             (7, 12, 13),
             (8, 10, 10),
             (9, 1, 2), (9, 14, 16),
             (10, 4, 4), (10, 12, 12),
             (11, 17, 17),
             (12, 13, 15),
             (13, 1, 5), (13, 7, 11), (13, 17, 17),
             (14, 16, 16),
             (15, 3, 4), (15, 10, 11),
             (16, 15, 15),
             (17, 2, 3), (17, 5, 9), (17, 11, 13), (17, 16, 16)]

    ovire2 = [(1, 1, 3), (1, 5, 6), (1, 8, 8), (1, 10, 10),
             (2, 5, 6),
             (4, 9, 11),
             (5, 1, 3),
             (6, 5, 6), (6, 8, 9),
             ]


class Test06(TestBase):
    def test_zaprto(self):
        steza = Steza(17, 19, self.ovire)
        self.assertTrue(steza.zaprto(10, 1))
        self.assertTrue(steza.zaprto(9, 4))
        self.assertTrue(steza.zaprto(10, 4))
        self.assertTrue(steza.zaprto(11, 4))
        self.assertTrue(steza.zaprto(8, 6))
        self.assertTrue(steza.zaprto(9, 6))

        self.assertFalse(steza.zaprto(7, 1))
        self.assertFalse(steza.zaprto(9, 1))
        self.assertFalse(steza.zaprto(8, 4))
        self.assertFalse(steza.zaprto(12, 4))

    def test_konec(self):
        steza = Steza(18, 20, self.ovire)
        self.assertEqual((9, 7), steza.konec(9, 10, "^"))
        self.assertEqual((9, 12), steza.konec(9, 10, "v"))
        self.assertEqual((11, 10), steza.konec(9, 10, ">"))
        self.assertEqual((5, 10), steza.konec(9, 10, "<"))

        self.assertEqual((7, 1), steza.konec(7, 10, "^"))
        self.assertEqual((18, 15), steza.konec(14, 15, ">"))
        self.assertEqual((14, 20), steza.konec(14, 15, "v"))
        self.assertEqual((1, 11), steza.konec(16, 11, "<"))

        self.assertEqual((16, 11), steza.konec(16, 11, ">"))
        self.assertEqual((14, 13), steza.konec(14, 13, "^"))
        self.assertEqual((14, 11), steza.konec(14, 11, "v"))
        self.assertEqual((12, 13), steza.konec(12, 13, "<"))


class Test07(TestBase):
    def test_prevozeno(self):
        steza = Steza(19, 17, self.ovire)
        kolesar = Kolesar(11, 1, steza)

        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(16, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.premik("^")
        self.assertEqual((1, 2), kolesar.pozicija())
        self.assertEqual(29, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((4, 2), kolesar.pozicija())
        self.assertEqual(32, kolesar.prevozeno())
        kolesar.premik("^")
        self.assertEqual((4, 1), kolesar.pozicija())
        self.assertEqual(33, kolesar.prevozeno())



        steza2 = Steza(13, 15, self.ovire2)
        kolesar = Kolesar(4, 2, steza2)
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((4, 15), kolesar.pozicija())
        self.assertEqual(13, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((13, 15), kolesar.pozicija())
        self.assertEqual(22, kolesar.prevozeno())

    def test_uporaba_steza(self):
        steza = Steza(19, 17, self.ovire)
        kolesar = Kolesar(11, 1, steza)

        steza.konec = lambda *_, **__: (15, 1)

        kolesar.premik(">")
        self.assertEqual((15, 1), kolesar.pozicija(), "Kolesar.premik naj kliče Steza.konec!")
        self.assertEqual(4, kolesar.prevozeno(), "Kolesar.premik naj kliče Steza.konec!")


class Test08(TestBase):
    def test_avtonomni(self):
        kolesar = AvtonomniKolesar(12, 1, Steza(17, 18, self.ovire), "><<>><>")
        self.assertEqual((12, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((12, 6), kolesar.pozicija())
        self.assertEqual(5, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 6), kolesar.pozicija())
        self.assertEqual(10, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((17, 10), kolesar.pozicija())
        self.assertEqual(14, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((13, 10), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((13, 11), kolesar.pozicija())
        self.assertEqual(19, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 11), kolesar.pozicija())
        self.assertEqual(31, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 12), kolesar.pozicija())
        self.assertEqual(32, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((12, 12), kolesar.pozicija())
        self.assertEqual(43, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((12, 16), kolesar.pozicija())
        self.assertEqual(47, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((14, 16), kolesar.pozicija())
        self.assertEqual(49, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((14, 18), kolesar.pozicija())
        self.assertEqual(51, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(64, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(64, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 18), kolesar.pozicija())
        self.assertEqual(80, kolesar.prevozeno())



        kolesar = AvtonomniKolesar(12, 1, Steza(17, 18, self.ovire), "><<")
        self.assertEqual((12, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((12, 6), kolesar.pozicija())
        self.assertEqual(5, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 6), kolesar.pozicija())
        self.assertEqual(10, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((17, 10), kolesar.pozicija())
        self.assertEqual(14, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((13, 10), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((13, 11), kolesar.pozicija())
        self.assertEqual(19, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 11), kolesar.pozicija())
        self.assertEqual(31, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 12), kolesar.pozicija())
        self.assertEqual(32, kolesar.prevozeno())
        kolesar.premik()  # > (ponavljanje!)
        self.assertEqual((12, 12), kolesar.pozicija())
        self.assertEqual(43, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((12, 16), kolesar.pozicija())
        self.assertEqual(47, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 16), kolesar.pozicija())
        self.assertEqual(58, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(60, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(60, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(60, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 18), kolesar.pozicija())
        self.assertEqual(76, kolesar.prevozeno())



        kolesar = AvtonomniKolesar(13, 1, Steza(17, 18, self.ovire), "><")
        self.assertEqual((13, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik()  # v - ne gre nikamor!
        self.assertEqual((13, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 1), kolesar.pozicija())
        self.assertEqual(4, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((17, 4), kolesar.pozicija())
        self.assertEqual(7, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((15, 4), kolesar.pozicija())
        self.assertEqual(9, kolesar.prevozeno())
        kolesar.premik()  # v - ne gre nikamor!
        self.assertEqual((15, 4), kolesar.pozicija())
        self.assertEqual(9, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 4), kolesar.pozicija())
        self.assertEqual(11, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((17, 4), kolesar.pozicija())
        self.assertEqual(11, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((15, 4), kolesar.pozicija())
        self.assertEqual(13, kolesar.prevozeno())
        kolesar.premik()  # v - ne gre nikamor!
        self.assertEqual((15, 4), kolesar.pozicija())
        self.assertEqual(13, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 4), kolesar.pozicija())
        self.assertEqual(15, kolesar.prevozeno())

    @patch.object(Kolesar, "premik")
    def test_klic_super(self, premik):
        self.assertIsNot(Kolesar.premik, AvtonomniKolesar.premik, "AvtonomniKolesar nima svoje metode premik?")
        kolesar = AvtonomniKolesar(12, 1, Steza(17, 18, self.ovire), "><<>><>")
        kolesar.premik()  # v
        self.assertEqual(1, premik.call_count, "AvtonomniKolesar mora (enkrat) klicati podedovani premik!")


class Test09(TestBase):
    def test_prevozeno(self):
        steza = Steza(19, 17, self.ovire)
        kolesar = VzvratniKolesar(11, 1, steza)

        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(16, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.premik("^")
        self.assertEqual((1, 2), kolesar.pozicija())
        self.assertEqual(29, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 3), kolesar.pozicija())
        self.assertEqual(26, kolesar.prevozeno())



        steza = Steza(19, 17, self.ovire)
        kolesar = VzvratniKolesar(11, 1, steza)

        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())

    @patch.object(Kolesar, "premik")
    def test_klic_super(self, premik):
        kolesar = VzvratniKolesar(12, 1, Steza(17, 18, self.ovire))
        kolesar.premik("v")
        self.assertEqual(1, premik.call_count, "VzvratniKolesar mora (enkrat) klicati podedovani premik!")


class Test10(TestBase):
    def test_pametni_kolesar(self):
        kolesar = PametniKolesar(12, 1, Steza(17, 18, self.ovire))
        self.assertEqual((23, 'v<v>v>v>v'), kolesar.nacrt())
        self.assertEqual((12, 1), kolesar.pozicija())

        kolesar = PametniKolesar(11, 1, Steza(17, 18, self.ovire))
        self.assertEqual((46, 'v<v>v>v<v>v>v'), kolesar.nacrt())
        self.assertEqual((11, 1), kolesar.pozicija())

        kolesar = PametniKolesar(16, 3, Steza(17, 18, self.ovire))
        self.assertEqual((49, '<v>v>v<v>v>v'), kolesar.nacrt())

        kolesar = PametniKolesar(1, 2, Steza(17, 18, self.ovire))
        self.assertEqual((31, '>v<v>v>v'), kolesar.nacrt())

        kolesar = PametniKolesar(4, 14, Steza(17, 18, self.ovire))
        self.assertEqual((7, '<v'), kolesar.nacrt())


if __name__ == "__main__":
    unittest.main()
