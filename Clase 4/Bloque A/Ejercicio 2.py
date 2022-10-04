'''

El producto interno de dos listas de números es la suma de los productos de
los términos de ambas. Por ejemplo, si: a = [5, 1, 6] y b = [1, -2, 8]
entonces el producto interno entre a y b es: (5 * 1) + (1 * -2) + (6 * 8)

Escriba la función producto_interno(a, b) que entregue el producto interno
entre a y b.

#>>> a = [7, 1, 4, 9, 8]
#>>> b = range(5)
#>>> producto_interno(a, b)
68
'''

def producto_interno(a, b):

    resultado = 0
    for i in range(len(a)):
        resultado += a[i] * b[i]

    return resultado

a = [7, 1, 4, 9, 8]
b = range(5)
print(producto_interno(a, b))