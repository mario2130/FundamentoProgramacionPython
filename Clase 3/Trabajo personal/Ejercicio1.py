'''
Escriba un programa que lea una cantidad de palabras y calcule el largo de
cada una, sin considerar las letras repetidas, determinando la más larga
y más corta. Por ejemplo, la palabra “casa” es más corta que la palabra
“reno”, ya que tiene 3 letras distintas (c, a y s). Mientras que “reno” tiene 5.

Ingrese n: 3
palabra 1: sabanas
palabra 2: canales
palabra 3: cojines
La palabra mas larga es: cojines
La palabra mas corta es: sabanas
'''


def exist_leters(leter, word):
    return leter in word

def count_word(word):
    countLetters = 0
    for i in word:
        countLetters +
