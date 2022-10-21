'''
Las temperaturas mínimas y máximas de algunas ciudades están guardadas en un diccionario cuyas llaves son
ciudades, y sus valores son tuplas (mínima, máxima).
temp = {

‘Vina del mar’: (9, 26),
‘Valparaiso’: (10, 24),
‘Quilpue’: (7, 30),
‘Quintero’: (4, 22)

}
Escriba la función crear_reporte(temperaturas), cuyo parámetro es el diccionarios de temperaturas, y que
genere el archivo de texto con el formato del ejemplo.

Ejemplo archivo generado: reporte.txt

Quilpue: max 30, min 7
Valparaiso: max 24 min 10
Quintero: max 22 min 4
Vina del mar: max 26 min 9
'''


from temperaturas import *

def crear_reporte(temperaturas):

    archivo = open("reporte_sala8.txt", "w")

    for key in temperaturas:
        min, max = temperaturas[key]
        archivo.write(key + " : max " + str(max) + ", min " + str(min) + "\n")
    archivo.close()

crear_reporte(temp)
