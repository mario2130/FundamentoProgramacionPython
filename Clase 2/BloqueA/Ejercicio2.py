'''
Escriba un programa que entregue todos los divisores de un número
entero ingresado. Su programa deberá validar que el número ingresado
sea positivo (> 0). En caso que cero o negativo, deberá mostrar un
mensaje de error.
'''

valor = int(input("Ingrese un numero:"))

if(valor <= 0):
    print("Error, debe ingresar un numero mayor a 0")
else:
    contador = 0

    print("los divisores de ", valor)

    for divisor in range(1, valor + 1):

        if (valor % divisor) == 0:
            print(divisor)

            contador += 1
