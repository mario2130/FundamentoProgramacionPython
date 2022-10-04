'''
Dos listas de números son ortogonales si su producto interno es cero. Escriba
la función son_ortogonales(a, b) que indique si a y b son ortogonales.

#>>> son_ortogonales([2, 1], [-3, 6])
True
'''

def son_ortogonales(a, b):

    resultado = 0
    for i in range(len(a)):
        resultado += a[i] * b[i]

    return True if resultado == 0 else False


print(son_ortogonales([2, 1], [-3, 6]))