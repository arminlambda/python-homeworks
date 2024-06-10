"""visina = []
zacetek = []
konec = []
for x in zemljevid:
    for i, znak in enumerate(zemljevid):
        if i == 0 and znak == '#':
            zacetek.append(i+1)
        elif znak == '#' and zemljevid[i-1]== '.':
            zacetek.append(i+1)
        elif znak == '#' and i+1 !=len(zemljevid) and zemljevid[i+1]== '.':
            konec.append(i+1)
        elif znak == '#' and len(zemljevid) - 1 == i:
            konec.append(i+1)
print(list(zip(zacetek, konec, visina)))"""

"""ovire = "##...#.###..##"


ovire = "." + ovire + "."
bloki = []
for i, znak in enumerate(ovire):
    if znak == "#":
        if ovire[i - 1] == ".":
            zacetek = i
        if ovire[i + 1] == ".":
            bloki.append((zacetek, i))
print(bloki)"""

zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]


bloki = []
for y, ovire in enumerate(zemljevid):
    ovire = "." + ovire + "."
    for i, znak in enumerate(ovire):
        if znak == "#":
            if ovire[i - 1] == ".":
                zacetek = i
            if ovire[i + 1] == ".":
                bloki.append((zacetek, i, y + 1))
print(bloki)







