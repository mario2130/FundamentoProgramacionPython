# Escriba un programa que invierta un numero entero de tres digitos
numero = int(input('Ingrese un numero de tres digitos: '))
d3 = int(numero % 10)
d2 = int((numero % 100)/10)
d1 = int((numero-(numero % 100))/100)
inv = str(d3) + str(d2) + str(d1)
print('El numero invertido es: ', inv)
