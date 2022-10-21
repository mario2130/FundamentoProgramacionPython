'''
Laboratorio Final: Fundamentos de programación
Nombre: Mario Villanueva
Rut: 16114292-1
'''

import random
from datetime import datetime, timedelta
import time

temperatura_calefactor = 0
temperatura_actual = 0


def estado_calefactor(temperatura_actual):

    factor = random.uniform(0.00, 2.00)
    es_encendido = temperatura_actual < temperatura_calefactor
    print(round(temperatura_actual,1), " ", es_encendido)
    if es_encendido:
        temperatura_actual = round(temperatura_actual + factor, 1)
    else:
        temperatura_actual = round(temperatura_actual - factor, 1)

    return temperatura_actual


tiempo_total = int(input("ingrese el tiempo total (en segundos) el cual durará la medición: "))
tiempo_medicion = int(input("ingrese el intervalo de tiempo (en segundos) el cual se realizarán las mediciones: "))
temperatura_calefactor = int(input("ingrese la t° de encendido del calefactor: "))

tiempo_fin = datetime.now() + timedelta(seconds=tiempo_total)
temperatura_actual = float(random.randint(0, 35))

while datetime.now() < tiempo_fin:
    temperatura_actual = estado_calefactor(temperatura_actual)
    time.sleep(tiempo_medicion)


