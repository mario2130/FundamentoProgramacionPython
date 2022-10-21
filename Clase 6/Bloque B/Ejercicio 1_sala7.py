archivo = open('notas.txt')
archivo2 = open('reporte_sala7.txt', 'w')
for linea in archivo:
    valores = linea.strip().split(':')
    nombre = valores[0]
    notas = map(float, valores[1:])
    notas2 = list(map(float, valores[1:]))
    promedio = sum(notas)/len(notas2)
    if promedio >= 4:
        estado = 'aprobado'
    else:
        estado = 'reprobado'
    linea = '{} {}\n'.format(nombre, estado)
    archivo2.write(linea)
archivo.close()
archivo2.close()