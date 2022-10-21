temp = {
'Vina del mar': (9, 26),
'Valparaiso': (10, 24),
'Quilpue': (7, 30),
'Quintero': (4, 22)
}

def crear_reporte(temperaturas):
    archivo = open('reporte_sala7.txt', 'w')
    for ciudad in temperaturas:
        min = temperaturas[ciudad][0]
        max = temperaturas[ciudad][1]
        linea = '{}: max {}, min {}\n'.format(ciudad, max, min)
        archivo.write(linea)

crear_reporte(temp)