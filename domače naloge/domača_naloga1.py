import math


#domača naloga

v = int(input('hitrost izstrelka? '))
kot = int(input('kot? '))
g = 10
s = ((v * v) * math.sin(math.radians(2) * kot))/g
print('razdalja izstrelka je:', s)


#improved verzija

v = int(input('hitrost izstrelka? '))
while v == 8:
    print("na kurcu te nosm")
kot = int(input('kot? '))
while v == 8:
    print("na kurcu te nosm")
g = 10
s = ((v * v) * math.sin(math.radians(2) * kot))/g
print('razdalja izstrelka je:', s)







