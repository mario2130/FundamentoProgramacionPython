'''
Cree un módulo llamado “mimodulo.py” y agregue la función
invertir_digitos(n) que reciba un número entero n, y entregue como
resultado el número n, con los dígitos en orden inverso.

Luego desarrolle un programa principal que use la función de dicho
módulo.
'''

from mimodulo import invert_number

valor = int(input("Ingrese numero: "))
numberInverted = invert_number(valor)
print("number inverted is: ", numberInverted)