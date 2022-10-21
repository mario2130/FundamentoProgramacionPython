# Escriba un programa que pida al usuario dos palabras, e indique cual de ellas es la mas larga, y por cuantas letras lo es.
p1 = input('Ingrese palabra 1: ')
p2 = input('Ingrese palabra 2: ')
a = len(p1)
b = len(p2)
if a > b:
    print(p1, 'Es mas larga que', p2, 'por', (a-b), 'letras(s)')
elif a == b:
    print(p1, 'Tiene el mismo largo que', p2)
else:
    print(p2, 'Es mas largo que', p1, 'por', (b-a), 'letra(s)')
