# Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario.
numero = int(input('Ingrese un numero: '))
for i in range(0, 11):
    resultado = i * numero
    print(numero,'X', i, ' = ', resultado)
