#Escriba programa que genere aleatoriamente el lanzamiento de una moneda
#y muestre por pantalla su resultado
import random

opcion = random.randint(0,1)

if opcion == 0:
    print("cara")
else:
    print("cruz")