puntaje = int(input('Ingrese el puntaje:'))
i = 1
j = 1

comb = 0

while i <= 6:
    while j <= 6:
        if i + j == puntaje:
            comb += 1
        j += 1
    j = 1
    i += 1

print('Hay {} combinaciones para obtener {}'.format(comb, puntaje))