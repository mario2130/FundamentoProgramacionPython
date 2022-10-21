def complementario(cadena):
    return cadena.replace('t', 'A').replace('a', 'T').replace('c', 'G').replace('g', 'C').lower()


cadena = input('Ingrese cadena para ser reemplazada: ')
print(complementario(cadena))