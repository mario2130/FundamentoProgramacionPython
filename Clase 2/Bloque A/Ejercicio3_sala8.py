'''
Escriba un programa que determine si un número es primo o
compuesto (no primo).
'''

valor = int(input("Ingrese un numero:"))
for n in range(2, valor):
    if valor % n == 0:
        print("No es primo", n, "es divisor")
        break
    print("Es primo")
    break