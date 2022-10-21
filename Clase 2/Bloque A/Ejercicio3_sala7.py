# Escriba un programa que determine si un número es primo o compuesto (no primo).
n = int(input('Ingrese un numero: '))
divisor = 2
while n > divisor:
    if n % divisor == 0:
        print('El numero no es primo')
        break
    elif n % divisor != 0:
        divisor = divisor + 1
if n == divisor:
    print('El numero es primo')


