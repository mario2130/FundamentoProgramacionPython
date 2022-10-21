'''
Las notas de un ramo están almacenadas en el archivo “notas.txt”. Cada línea tiene
el nombre del alumno y sus seis notas, separadas por dos puntos (“:”)

Escriba un programa que cree un nuevo archivo llamado “reporte.txt”, en que
cada línea indique si el alumno está aprobado (promedio >= 4.0) o reprobado
(promedio < 4.0)

Resultado a obtener en archivo reporte.txt

Pepito aprobado
Yayita aprobado
Fulanita aprobado
Moya reprobado
'''


file = open("notas.txt")
outputfile = open("reporte_sala8.txt","w")

for row in file:
    student_info = row.strip().split(":")
    name = student_info[0]
    point = list(map(float, student_info[1::]))
    average = sum(point)/len(point)
    if average >= 4.0:
        outputfile.write(name + " aprobado \n")
    else:
        outputfile.write(name + " reprobado \n")

file.close()
outputfile.close()