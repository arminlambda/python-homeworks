#gorivo?
#teza tovora je 756
teza_tovora = int(input('koliko je teza tovora: '))

gorivo = 0

while teza_tovora > 0:
    teza_tovora = teza_tovora // 3 - 2
    print(teza_tovora)
    gorivo = gorivo + 1



print('koliko goriva bomo potrebovali? [v tonah]: ', gorivo)