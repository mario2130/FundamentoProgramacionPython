archivo = open('pacientes.csv')
FileJov = open('jovenes_sala7.txt', 'w')
FileMay = open('mayores_sala7.txt', 'w')
for linea in archivo:
    valores = linea.strip().split(';')
    edad = int(valores[2])
    if edad <= 30:
        FileJov.write(linea)
    elif edad >= 60:
        FileMay.write(linea)
archivo.close()
FileJov.close()
FileMay.close()