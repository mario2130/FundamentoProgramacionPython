#Escriba un programa que invierta un número entero de tres digitos

numero = str(input("ingrese un numero de tres digitos:"))
numeroInvertido = ""
while len(numero)>0:
    aux = numero[0]
    newNumero = numeroInvertido + aux
    numero = newNumero
print(numeroInvertido)
