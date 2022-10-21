'''
Escriba una función que determine si un número es par o no.

#>>> es_par(2)
True

#>>> es_par(7)
False
'''

from Libreria import es_par

valor = int(input("Ingrese un valor: "))

esPar = es_par(valor)
print(esPar)
