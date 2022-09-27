'''
Un viajero desea saber cuánto tiempo tomó el viaje que realizó. Él tiene la duración
en minutos de cada uno de los tramos del viaje.
Escriba un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado, el tiempo total de viaje en formato horas:minutos .
'''


suma = 0
continuar = True

while continuar:
    minutos = int(input("duración del tramo en minutos:"))
    if minutos == 0:
        continuar = False
    else:
        suma += minutos

hora = suma//60  # el operador // obtiene la parte entera de la división
minutos = suma % 60  # el operador % nos da el resto de la división (los minutos)


print("la suma total del viaje:", hora," horas y ",minutos,"minutos")