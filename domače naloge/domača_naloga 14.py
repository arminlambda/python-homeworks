import risar
import random

risar.maxX = risar.widget.view.width()
risar.maxy = risar.widget.view.height()

gameOver = False
ovire = []

def ustvarjanje():
    if len(ovire) < 20:
        if random.random() < 0.02:
            sirina = random.randrange(0, 700)
            dodatek = random.randrange(30, 80)
            ovire.append(risar.pravokotnik(sirina, 0, sirina+dodatek, 25, barva=risar.rjava ))


def padajo():
    i = 0
    while i < len(ovire):
        if ovire[i].y() >= risar.widget.view.height():
            risar.odstrani(ovire[i])
            ovire.pop(i)
        else:
            ovire[i].setPos(ovire[i].x(), ovire[i].y()+1)
            i += 1
    return ovire


while gameOver == False:
    ustvarjanje()
    padajo()
    risar.cakaj(0.002)



risar.stoj()

