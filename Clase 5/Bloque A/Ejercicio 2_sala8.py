'''
Los resultados de un campeonato de fútbol se almacenan en un diccionario. Las
llaves son los partidos, y los valores los resultados. Revise el archivo
“campeonato_C5.py”



Escriba las siguientes funciones!

Trabajo grupal – Ejercicio #2

#>>> obtener_lista_equipos(resultados)
['Honduras', 'Suiza', 'Espana', 'Chile']

#>>> calcular_puntos('Chile', resultados)

6

#>>> calcular_puntos('Suiza', resultados)

4
'''

resultados = {
    ('Honduras', 'Chile'): (0, 1),
    ('Espana', 'Suiza'): (0, 1),
    ('Suiza', 'Chile'): (0, 1),
    ('Espana', 'Honduras'): (3, 0),
    ('Suiza', 'Honduras'): (0, 0),
    ('Espana', 'Chile'): (2, 1)
}


def obtener_lista_equipos(resultados):
    a = set()
    b = set()
    for key, values in resultados.items():
        a.add(key[0])
        b.add(key[1])
    print(a | b)

def evalua_resultado_partido(equipos, resultados, pais_evaluado):
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
            match_result += evalua_resultado_partido(equipos, resultados[equipos], equipos[0])
        if(equipos[1] == pais):
            match_result += evalua_resultado_partido(equipos, resultados[equipos],equipos[1])

    print(match_result)


obtener_lista_equipos(resultados)
calcular_puntos('Chile', resultados)
calcular_puntos('Suiza', resultados)
calcular_puntos('Espana', resultados)
calcular_puntos('Honduras', resultados)