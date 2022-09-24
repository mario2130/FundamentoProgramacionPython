#Escriba programa que pida al usuario dos palabras, e indique cual de ellas es la más larga
#y por cuantas letras lo es

palabra1 = input("ingrese palabra 1: ")
palabra2 = input("ingrese palabra 2: ")

cantidadLetrasPalabra1 = len(palabra1)
cantidadLetrasPalabra2 = len(palabra2)

if cantidadLetrasPalabra1 > cantidadLetrasPalabra2:
    print("palabra 1 es mayor a la palabra 2, por:", cantidadLetrasPalabra1 - cantidadLetrasPalabra2)
elif cantidadLetrasPalabra1 < cantidadLetrasPalabra2:
    print("palabra 2 es mayor a la palabra 1, por:", cantidadLetrasPalabra2 - cantidadLetrasPalabra1)
else:
    print("ambas palabras son iguales con el mismo largo:", cantidadLetrasPalabra1)