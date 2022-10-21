'''
Escriba un programa que determine si un número es primo o
compuesto (no primo).
'''

valor = int(input("Ingrese un numero:"))
encontrado = False
for n in range(2, valor):
    if valor % n == 0:
        print("No es primo", n, "es divisor")
        encontrado = True
        break

if encontrado == False:
    print("Es primo")