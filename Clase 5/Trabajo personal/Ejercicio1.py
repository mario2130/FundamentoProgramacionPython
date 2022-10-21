'''
Considerando el archivo “campeonato_C5.py” con el siguiente diccionario
realice las siguientes funciones:

resultados = {

(‘Honduras’, ‘Chile’): (0, 1),
(‘Espana’, ‘Suiza’): (0, 1),
(‘Suiza’, ‘Chile’): (0, 1),
(‘Espana’, ‘Honduras’): (3, 0),
(‘Suiza’, ‘Honduras’): (0, 0),
(‘Espana’, ‘Chile’): (2, 1)

}

Trabajo post-clase – Ejercicio #1A

La diferencia de goles de un equipo es el total de goles que anotó menos el total de
goles que recibió.

Escriba la función calcular_diferencia_de_goles(equipo, resultados) que
entregue la diferencia de goles de un equipo.

#>>> calcular_diferencia_de_goles(‘Chile’, resultados)
1

#>>> calcular_diferencia_de_goles(‘Honduras’, resultados)
-4
'''

from campeonato_C5 import *

def evalua_resultado_partido(equipos, resultados, pais_evaluado):
    equipo1 = equipos[0]
    resultado_equipo1= resultados[0]
    resultado_equipo2 = resultados[1]
    # evaluamos equipo local
    if equipo1 == pais_evaluado:
        return resultado_equipo1 - resultado_equipo2
    # evaluamos equipo como visita
    else:
        return resultado_equipo2 - resultado_equipo1


def calcular_diferencia_de_goles(pais, resultados):
    match_result = 0

    for equipos, resultado in resultados.items():
        if (equipos[0] == pais):
            match_result += evalua_resultado_partido(equipos, resultados[equipos], equipos[0])
        if (equipos[1] == pais):
            match_result += evalua_resultado_partido(equipos, resultados[equipos], equipos[1])

    print(match_result)


calcular_diferencia_de_goles('Chile', resultados)
calcular_diferencia_de_goles('Honduras', resultados)
