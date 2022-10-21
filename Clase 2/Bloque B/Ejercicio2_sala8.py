'''
En estadística descriptiva, se define el rango de un conjunto de datos reales
como la diferencia entre el mayor y el menor de los datos.

Por ejemplo, si los datos son [5.96, 6.74, 7.43, 4.99, 7.20, 0.56,
2.80] entonces el rango será: 7.43 – 0.56 = 6.87

Escriba un programa que; (1) pregunte al usuario cuántos datos ingresará, (2)
pida los datos uno por uno y (3) entregue como resultado el rango de los
datos (suponga que todos los datos que ingrese serán válidos).
'''

cantidad = int(input("Ingrese n: "))
mayor = 0
i = 1
posicion = 0
menor = 9999999999
while i < cantidad + 1:
    ingresado = float(input("Ingrese numero " + str(i) + " :"))
    if(ingresado > mayor):
        mayor = ingresado
    if(ingresado < menor):
        menor = ingresado
    i += 1
print("El rango será:" ,mayor,"-",menor, mayor- menor)