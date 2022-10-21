'''
Las funciones seno y coseno, pueden ser representadas por sumas infinitas:

1) Escriba la función factorial_reciproco(n), que retorne el valor de 1/n!
2) Escriba la función signo(n) que retorne 1 cuando n es par, y -1 cuando n
es impar.
3) Escriba las funciones seno_aprox(x, m) y coseno_aprox(x, m) que
aproximen el seno y el coseno de x, usando los primeros m términos de las
sumatorias.
'''
from mimodulo import *

def seno_aprox(x, m):
    sum = 0
    factor = 1
    for i in range(m):
        sum += signo(i) * (x**factor)*factorial_reciproco(factor)
        factor += 2
    return sum

def coseno_aprox(x, m):
    sum = 0
    factor = 0
    for i in range(m):
        sum += signo(i) * (x ** factor) * factorial_reciproco(factor)
        factor += 2
    return sum

print('seno_aprox: ', seno_aprox(2, 3))
print('coseno_aprox: ', coseno_aprox(2, 3))

