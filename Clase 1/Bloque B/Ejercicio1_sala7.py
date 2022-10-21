# Escriba un programa que genere aleatoriamente el lanzamiento de una moneda y muestre por pantalla su nresultado(CARA o SELLO).

from random import randint
moneda = randint(0,1)
if moneda == 0:
    print('El resultado es Sello')
else:
    print('El resultado es Cara')