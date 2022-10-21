#A partir de un número cualquiera (entrada) es posible hacer una sucesión de
#números que termina en 1, para ello deberá seguir las siguientes instrucciones:

numero = int(input('Ingrese numero: '))
while numero != 1:
	if numero % 2 == 0:
		numero = numero // 2
	else:
		numero = numero * 3 + 1
	print(numero)