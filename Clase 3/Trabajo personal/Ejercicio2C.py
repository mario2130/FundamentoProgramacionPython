'''
Los científicos encontraron un patrón de clasificación, que se deduce de la cantidad
mayoritaria de cierto grupo de bases. Si la suma de las cantidades de Citosina y Guanina
es mayor a la de Adenina y Timina, es una especie vegetal, en caso contrario es una
especie animal. Escriba un programa que pregunte la cantidad de cadenas de ADN a
evaluar, luego solicite las cadenas y finalmente muestre las cantidades de cada especie
y cadenas no válidas. Use las funciones anteriores.

Cantidad de cadenas a ingresar: 3
Ingrese cadena 1: CGTA CAGT TTGG GGTA AATG CATG
Ingrese cadena 2: CACC CTGA GGAA ACAA XTFC ATGG
Ingrese cadena 3: TGTG TTGA ATGA CTAT ATTT
Cantidad animales: 2
Cantidad vegetales: 0
Cantidad no validas: 1
'''



from Ejercicio2A import valida
from Ejercicio2B import cantidad

def get_type_species(cadena):

    if valida(cadena) == False:
        return 'No valida'

    bases = set(cadena)
    family_type = dict()
    for base in bases:
        family_type[base] = cantidad(cadena, base)

    if(family_type['C'] + family_type['G'] > family_type['A'] + family_type['T'] ):
        return 'Vegetal'
    else:
        return 'Animal'

resultadofinal = list()
cantidad_cadenas_totales = int(input('Cantidad de cadenas a ingresar:'))
cantidad_candenas_ingresadas = 0

while cantidad_candenas_ingresadas < cantidad_cadenas_totales:
    cantidad_candenas_ingresadas += 1
    cadena = input('Ingrese cadena {}:'.format(cantidad_candenas_ingresadas))
    resultado_cadena = get_type_species(cadena)
    resultadofinal.append(resultado_cadena)


print('Cantidad animales: ', resultadofinal.count('Animal'))
print('Cantidad vegetales: ', resultadofinal.count('Vegetal'))
print('Cantidad no validas: ', resultadofinal.count('No valida'))


# Estimado revisador de código, si ha llegado revisando código 1 por 1
# hasta este punto, lo admiro. una cerveza para a usted. Atte Anónimo