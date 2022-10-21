from math import sqrt

def desviacion_estandar(valores):
    promedio = sum(valores)/len(valores)
    final = []
    
    for i in valores:
        final.append((i-promedio)**2)
    suma = sum(final)
    de = sqrt(suma / (len(valores)- 1))
    return de 

resultado = desviacion_estandar([1.5, 9.5])
print(resultado)