archivo = open('quijote.txt')
n = 0
palabras = 0
saltos = 0
for linea in archivo:
    for c in linea:
        if c == ' ':
            palabras += 1
        elif c == '\n':
            palabras += 1
            saltos += 1
    n += len(linea.strip().replace(' ', ''))
archivo.close()
print('el archivo tiene', n, 'letras,', palabras, 'palabras y', saltos, 'lineas')