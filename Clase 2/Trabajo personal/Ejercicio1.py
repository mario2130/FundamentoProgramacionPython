'''
Una fundación de ayuda a la comunidad está haciendo una campaña para la
recolección de dinero para poner máquinas de ejercicios en un parque. Para esto se
considera que podría haber un total de N benefactores o juntar un monto total de M
pesos (cualquiera de las dos condiciones se debe cumplir).

Escriba un programa que ingrese la cantidad total de benefactores N y el monto total
a recaudar M. Su programa debe solicitar el nombre y el monto que donará cada
benefactor, uno por uno. Su programa debe detenerse una vez que se alcance el
monto total M, o cuando se terminen de ingresar los N benefactores.

Indique cuál es el monto mayor donado y qué benefactor lo donó.
'''

benefactores = int(input("Ingresa la cantidad de benefactores: "))
montoTotal = int(input("Ingrese monto total a recolectar: "))

montoRecaudado = 0
metaCumplida = False
i = 1
montoMayorDonado = 0
nombreMayorDonacion = ""

while not metaCumplida and i <= benefactores:
    nombreBenefactor = input("Ingrese nombre del benefactor" + str(i) +" :")
    montoBenefactor = int(input("Ingrese monto del benefactor" + str(i)+" :"))
    montoRecaudado += montoBenefactor
    if(montoBenefactor > montoMayorDonado):
        montoMayorDonado = montoBenefactor
        nombreMayorDonacion = nombreBenefactor
    if(montoRecaudado >= montoTotal):
        metaCumplida = True
    i += 1

if(metaCumplida):
    print("Se ha cumplido la meta, el mayor benefactor es:", nombreMayorDonacion, "con un monto de:", montoMayorDonado)
else:
    print("la meta no se ha cumplido, lo lamentamos")