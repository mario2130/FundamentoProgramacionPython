'''
A cada cadena le corresponde una cadena complementaria, que se obtiene
intercambiando las adeninas con las timinas, y las citosinas con las guaninas.

cadena = ‘cagcccatgaggcagggtg’
complemento = ‘gtcgggtactccgtcccac’

Escriba la función complementaria(c) que entregue la cadena complementaria
de c.

#>>> cadena = ‘cagcccatgaggcagggtg’
#>>> complementaria(cadena)
‘gtcgggtactccgtcccac’
'''

def complementario(cadena):
    cadena = cadena.replace('a', 'T').replace('t', 'A').replace('c', 'G').replace('g', 'C')
    return cadena.lower()


cadena = input('Ingrese cadena: ')
print(complementario(cadena))