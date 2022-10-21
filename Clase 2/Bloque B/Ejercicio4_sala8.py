'''
Un jugador debe lanzar dos dados numerados del 1 al 6, y su puntaje es la suma de
los valores obtenidos.

Un puntaje dado, puede ser obtenido con varias combinaciones posibles. Por
ejemplo, el puntaje 4 se logra con 3 combinaciones;1+3, 2+2, 3+1

Escriba un programa que pregunte al usuario un puntaje, y muestre como resultado
la cantidad de combinaciones con las que se puede obtener dicho puntaje.
'''


puntaje = int(input("Ingrse el puntaje: "))
dado1 = 1
combinaciones = 0

while dado1 <= 6:

    dado2 = 1
    while dado2 <= 6:

        if(dado1 + dado2 == puntaje):
            combinaciones += 1
            print("combinacion encontrada:", dado1,":",dado2)
        dado2 += 1
    dado1 += 1

print("hay",combinaciones,"combinaciones para obtener",puntaje)

