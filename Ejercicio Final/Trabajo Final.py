from random import randint
from random import uniform
from time import sleep

def temp_sec(T,cal):
    tsec = uniform(0, 2)
    if cal:
        T += tsec
    else:
        T -= tsec
    return round(T, 1)

T_total = int(input('Cuanto es el tiempo total a analizar (seg):'))
T_medicion = int(input('Cada cuanto se realizara una medicion (seg):'))
T_calef = int(input('A que temperatura se desea ajustar el calefactor (°C):'))

Temp = randint(0, 35)
Name_File = 'log-tempinicial-{}-tempcalefactor_{}-tiempototal_{}-tiempomedicion_{}.csv'.format(Temp, T_calef, T_total, T_medicion)

Archivo = open(Name_File, 'w')

tiempo = 0

print('Tiempo (seg)    Temperatura (°C)    Estado Calefactor')

while tiempo <= T_total:
    Calf = Temp < T_calef
    print(tiempo, '   ', Temp, '   ', Calf)
    Linea = str(tiempo) + ';' + str(Temp) + ';' + str(Calf) + '\n'
    Archivo.write(Linea)
    tiempo += T_medicion
    Temp = temp_sec(Temp, Calf)
    sleep(T_medicion)

Archivo.close()



