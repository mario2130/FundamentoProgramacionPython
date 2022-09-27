'''
Escriba un programa que permita determinar el número mayor de n
números solicitados al usuario.
'''

cantidad = int(input("Ingrese n: "))
mayor = 0
i = 1
posicion = 0
while i < cantidad + 1:
    ingresado = int(input("Ingrese numero " + str(i) + " :"))
    if(ingresado > mayor):
        mayor = ingresado
        posicion = i
    i += 1
print("El mayor es el", mayor, "que corresponde al numero",posicion)