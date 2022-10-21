resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}

def obtener_lista_equipos(result):
	Lista = []
	for countries in result:
		for pais in countries:
			if pais not in Lista:
				Lista.append(pais)
	print(Lista)

def calcular_puntos(pais, result2):
	puntos = 0
	for countries2 in result2:
		if pais in countries2:
			i = countries2.index(pais)
			if i==0:
				j=1
			else:
				j=0
			if int(result2[countries2][i])>int(result2[countries2][j]):
				puntos += 3
			elif int(result2[countries2][i])== int(result2[countries2][j]):
				puntos += 1
			else:
				puntos += 0
	print(str(puntos))

obtener_lista_equipos(resultados)
calcular_puntos('Chile', resultados)
calcular_puntos('Suiza', resultados)
calcular_puntos('Espana', resultados)
calcular_puntos('Honduras', resultados)