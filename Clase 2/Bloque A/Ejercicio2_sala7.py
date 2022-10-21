#Escriba un programa que entregue todos los divisores de un número entero ingresado. Su programa deberá validar que el número ingresado sea positivo (> 0). En caso que cero o negativo, deberá mostrar un mensaje de error.
numero = int(input('Ingrese un numero: '))
if numero < 0:
    print('Debe ingresar un numero mayor a 0')

div = ''
for i in range(1, numero + 1):
    if numero % i == 0:
        div += str(i) + ' '
        print(div)

