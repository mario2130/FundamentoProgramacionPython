'''
Desarrolle una función llamada desviacion_estandar(valores) cuyo parámetro
valores sea una lista de números reales. La función debe retornar la desviación estándar
de los valores:

Donde n es la cantidad de valores, xҧes el promedio, y los xi son cada uno de los
valores. Esto significa que hay que hacerlo siguiendo los siguientes pasos:

1. Calcular el promedio de los valores
2. A cada valor, restarle el promedio, y el resultado elevarlo al cuadrado
3. Sumar todos los valores obtenidos
4. Dividir la suma por la cantidad de valores y sacar la raíz cuadrada del resultado.
'''


from math import sqrt

def desviacion_estandar(valores):
    n = len(valores)
    x = sum(valores) / n

    deviacion = 0.0
    for i in valores:
        print("evaluando a: ", i)
        deviacion += ((i - x) ** 2)

    division = deviacion / (n-1)
    raiz = sqrt(division)
    return raiz

resultado = desviacion_estandar([1.5, 9.5])
print(resultado)