'''
A partir de un número cualquiera (entrada) es posible hacer una sucesión de
números que termina en 1, para ello deberá seguir las siguientes instrucciones:

- Si el número es par, se debe dividir por 2
- Si el número es impar, se debe multiplicar por 3 y sumarle 1.

Con esto se obtiene el siguiente número de la sucesión, al cual se le aplican las
mismas operaciones. La sucesión termina cuando el número obtenido es 1.

Escriba un programa que muestre cada número de la sucesión generada, hasta
llegar a 1.
'''


valor = int(input("Ingrse valor:"))


while valor != 1:
    if(valor%2 == 0):
        print("el numero es par:",valor)
        valor = valor / 2
    else:
        print("el numero es inpar", valor)
        valor = (valor * 3) + 1
print(valor)