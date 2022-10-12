'''
Escriba la función posiciones(resultados) que reciba como parámetro el
diccionario de resultados, y retorne una lista con los equipos ordenados por
puntaje de mayor a menor. Los equipos que tienen el mismo puntaje deben ser
ordenados por diferencia de goles de mayor a menor. Si tienen los mismos
puntos y la misma diferencia de goles, deben ser ordenados por los goles
anotados.

# >>> posiciones(resultados)
[‘Espana’, ‘Chile’, ‘Suiza’, ‘Honduras]
'''

from campeonato_C5 import *

def evalua_puntos_partido(equipos, resultados, pais_evaluado):
    equipo1 = equipos[0]
    resultado_equipo1= resultados[0]
    resultado_equipo2 = resultados[1]
    if equipo1 == pais_evaluado:
        if resultado_equipo1 > resultado_equipo2:
            return 3
        elif resultado_equipo1 < resultado_equipo2:
            return 0
        else:
            return 1
    else:
        if resultado_equipo1 > resultado_equipo2:
            return 0
        elif resultado_equipo1 < resultado_equipo2:
            return 3
        else:
            return 1

def calcular_puntos(pais, resultados):
    match_result = 0

    for equipos, resultado in resultados.items():
        if(equipos[0] == pais):
            match_result += evalua_puntos_partido(equipos, resultados[equipos], equipos[0])
        if(equipos[1] == pais):
            match_result += evalua_puntos_partido(equipos, resultados[equipos],equipos[1])

    return match_result

def listados_equipos(resultados):
    equipos = set()
    for e, resul in resultados.items():
        equipos.add(e[0])
        equipos.add(e[1])

    return equipos

def obtener_resultado_por_equipo(resultado):
    resultados_por_equipo = dict()
    equipos = listados_equipos(resultados)
    for equipo in equipos:
        valores = ()
        resultado_obtenido = calcular_puntos(equipo, resultados)
        diferencia_obtenida = calcular_diferencia_de_goles(equipo, resultados)
        valores = (resultado_obtenido, diferencia_obtenida)
        resultados_por_equipo[equipo] = valores

    return resultados_por_equipo



def calcular_diferencia_de_goles(pais, resultados):
    match_result = 0

    for equipos, resultado in resultados.items():
        if (equipos[0] == pais):
            match_result += evalua_resultado_partido(equipos, resultados[equipos], equipos[0])
        if (equipos[1] == pais):
            match_result += evalua_resultado_partido(equipos, resultados[equipos], equipos[1])

    return match_result


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

def posiciones(resultados):
    final = list()
    equipo_mayor = ''
    mayores = tuple()
    evaluacion_equipos = obtener_resultado_por_equipo(resultados);
    quedan_elementos = True

    while(quedan_elementos):
        for equipo, resultado in evaluacion_equipos.items():
            if resultado > mayores:
                equipo_mayor = equipo
                mayores = resultado
        final.append(equipo_mayor)

        del evaluacion_equipos[equipo_mayor]
        mayores = tuple()
        if len(evaluacion_equipos) == 0:
            quedan_elementos = False

    print(final)


# se omite el último factor porque no es necesario
posiciones(resultados)