# Un viajero desea saber cuánto tiempo tomó el viaje que realizó. Él tiene la duración
# en minutos de cada uno de los tramos del viaje.
# Escriba un programa que permita ingresar los tiempos de viaje de los tramos y
# entregue como resultado, el tiempo total de viaje en formato horas:minutos .

tramo = True
suma = 0
while tramo:
    tv = int(input('Duracion del tramo: '))
    if tv == 0:
        tramo = False

    else:
        suma = suma + tv
horas = suma // 60
minutos = suma % 60
print('Tiempo total de viaje:', str(horas) + ':' + str(minutos), 'horas')