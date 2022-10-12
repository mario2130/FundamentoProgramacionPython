'''
Escriba las funciones necesarias para que el programa del archivo
“artistas_C5.py” funcione.
'''

from artistas_C5 import *

def cantidad_de_artistas(dia):
    return len(artistas_por_dia[dia])


def nombre_primer_artista(dia):
    ids_artistas_dia = artistas_por_dia[dia]
    primer_artista = ids_artistas_dia[0]
    for llave, valor in artistas.items():
        for cod in valor:
            if cod == primer_artista:
                return llave
    return ''

def nombre_primer_artistav2(dia):
    '''
    version profe
    :param dia:
    :return:
    '''
    codigo = artistas_por_dia[dia][0]

    for nombre in artistas:
        codigo_a = artistas[nombre][0]
        if(codigo == codigo_a):
            return nombre

def pais_origen_ultimo(dia):
    ids_artistas_dia = artistas_por_dia[dia]
    ultimo_artista = ids_artistas_dia[-1]

    for cod, pais, minutos in artistas.values():
        if cod == ultimo_artista:
            return pais
    return ''

def tiempo_total(dia):
    total_minutos = 0
    for cod_artistas in artistas_por_dia[dia]:
        for key, values in artistas.items():
            if( values[0] == cod_artistas):
                total_minutos += values[2]

    return total_minutos

def tiempo_totalv2(dia):
    suma = 0
    codigos = artistas_por_dia[dia]
    for codigo in codigos:
        for nombre in artistas:
            codigo_artista, pais_artista, minutos_artista = artistas[nombre]
            if codigo_artista == codigo:
                suma += minutos_artista
    return suma


dia = 'Lunes' #input('Ingrese dia: ')
print('Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas')
print('El primer artista del dia sera', nombre_primer_artistav2(dia))
print('El ultimo artista del dia viene de', pais_origen_ultimo(dia))
print('Ese dia el concierto completo durara', tiempo_total(dia),'minutos')

