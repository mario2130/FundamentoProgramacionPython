'''
Una consulta médica mantiene un archivo pacientes.csv con los datos
personales de sus pacientes. Cada línea del archivo tiene el rut, nombre y
edad de un paciente, separados por un símbolo ;

Escriba un programa que construya dos nuevos archivos.

- jovenes.txt, con los datos de los pacientes menores de 30 años.

- mayores.txt, con los datos de todos los pacientes mayores de 60 años.
'''


file = open("pacientes.csv")
outputyoungfile = open("jovenes_sala8.csv","w")
outputolderfile = open("mayores_sala8.csv", "w")

for row in file:
    id, name, age = row.split(";")
    if int(age) < 30:
        outputyoungfile.write(row)
    if int(age) > 60 :
        outputolderfile.write(row)
file.close()
outputyoungfile.close()
outputolderfile.close()