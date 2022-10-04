'''
Una cadena de ADN es una secuencia de bases nitrogenadas llamadas: (1) adenina, (2) citosina, (3) timina y
(4) guanina. En un programa una cadena se representa como un string de caracteres ‘a’, ‘c’, ‘t’ y ‘g’. Escriba
la función cadena_al_azar(n) que retorne una cadena aleatoria de ADN de largo n.

#>>> cadena_al_azar(10)
‘acgtccgcct’
#>>> cadena_al_azar(10)
‘tgttcgcatt’

Hint:
#>>> from random import choice
#>>> choice(‘atcg’)
‘t’
#>>> choice(‘atcg’)
‘g’
'''

from random import choice

def cadena_al_azar(n):
    i = 0
    secuencia = "dctg"
    resultado = ""
    while i < n:
        random = choice(secuencia)
        resultado += random
        i += 1
    return resultado


valor = int(input("Ingrese largo: "))
print(cadena_al_azar(valor))
