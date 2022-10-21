# Escriba un programa que permita ingresar 5 números entreros y determine cuál de los cuatro es más lejano al primero.
num1 = int(input('Primer numero: '))
num2 = int(input('Ingrese numero: '))
num3 = int(input('Ingrese numero: '))
num4 = int(input('Ingrese numero: '))
num5 = int(input('Ingrese numero: '))

rest2 = abs(num2 - num1)
rest3 = abs(num3 - num1)
rest4 = abs(num4 - num1)
rest5 = abs(num5 - num1)

if rest2 > rest3 and rest2 > rest4 and rest2 > rest5:
    print('El numero mas lejano al primero es el', num2)
if rest3 > rest2 and rest3 > rest4 and rest3 > rest5:
    print('El numero mas lejano al primero es el', num3)
if rest4 > rest2 and rest4 > rest3 and rest4 > rest5:
    print('El numero mas lejano al primero es el', num4)
if rest5 > rest2 and rest5 > rest3 and rest5 > rest4:
    print('El numero mas lejano al primero es el', num5)