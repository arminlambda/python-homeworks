import fileinput
import os
import warnings
from random import randint
from datetime import datetime
import unittest




def zapisi_ovire(ime_datoteke, ovire):
    datoteka = open(ime_datoteke, 'w')
    for i in ovire:
        vrstica = f'{i:03d}:'
        for vrstica_i in ovire[i]:
            vrstica = vrstica + f'{vrstica_i[0]:4d}-{vrstica_i[1]:<4d}'
        datoteka.write(vrstica + '\n')
    datoteka.close()
    return datoteka

def preberi_ovire(ime_datoteke):
    slovar_ovir = {}
    vsebina_datoteke = open(ime_datoteke).read()
    vsebina_datoteke = vsebina_datoteke.split('\n\n')
    for i in vsebina_datoteke:
        i = list(map(int, i.splitlines()))
        y = i[0]
        slovar_ovir[y] = list(zip(i[1::2], i[2::2]))     #i[1:-1], i[2:]
    return slovar_ovir



#def preberi_ovire(ime_datoteke):
   # slovar_ovir = {}
    #vsebina_datoteke =open(ime_datoteke, 'r')
     #   for vrstica in f:
       #     vsebina_vrstice = vrstica.strip().split()
         #   slovar_ovir[vsebina_vrstice[0]].append((vsebina_vrstice[1], vsebina_vrstice[2]))

class TestZapis(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

        self.ovire = {4: [(5, 6), (9, 11)],
                      5: [(9, 11), (19, 20), (30, 34)],
                      13: [(5, 8), (9, 11), (17, 19), (22, 25), (90, 100)]}

        self.ovire2 = self.ovire | {randint(100, 200): [(1, 2)]}
        with open("ovire.txt", "wt") as f:
            lf = "\n"
            f.write("\n\n".join(fr"{y}{lf}{lf.join(fr'{x0}{lf}{x1}' for x0, x1 in xs)}" for y, xs in self.ovire2.items()))

    def test_01_obvezna_zapisi_ovire(self):
        ime_datoteke = f"ovire{datetime.now().strftime('%m-%d-%H-%M-%S')}.txt"
        zapisi_ovire(ime_datoteke, self.ovire)
        with open(ime_datoteke) as f:
            self.assertEqual("""
004:   5-6      9-11
005:   9-11    19-20    30-34
013:   5-8      9-11    17-19    22-25    90-100
""".strip("\n"), "\n".join(map(str.rstrip, f)))

        self.ovire[101] = self.ovire[5]
        zapisi_ovire(ime_datoteke, self.ovire)
        with open(ime_datoteke) as f:
            self.assertEqual("""
004:   5-6      9-11
005:   9-11    19-20    30-34
013:   5-8      9-11    17-19    22-25    90-100
101:   9-11    19-20    30-34
""".strip("\n"), "\n".join(map(str.rstrip, f)))

        os.remove(ime_datoteke)

    def test_02_dodatna_preberi_ovire(self):
        self.assertEqual(preberi_ovire("ovire.txt"), self.ovire2)


if __name__ == "__main__":
    unittest.main()
