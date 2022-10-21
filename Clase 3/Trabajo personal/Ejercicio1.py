'''
Escriba un programa que lea una cantidad de palabras y
calcule el largo de cada una, sin considerar las letras repetidas,
determinando la más larga y más corta. Por ejemplo, la palabra “casa” es más corta que la palabra “reno”,
 ya que tiene 3 letras distintas (c, a y s). Mientras que “reno” tiene 4.
'''
n = int(input('Ingrese cantidad de palabras:'))

dic_palabras = {}

for i in range(n):
    palabra = input('palabra {}:'.format(i+1))
    dic_palabras[len(''.join(set(palabra)))] = palabra

print('La palabra mas larga es: {}'.format(dic_palabras[max(dic_palabras)]))
print('La palabra mas corta es: {}'.format(dic_palabras[min(dic_palabras)]))
