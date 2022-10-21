'''
El diccionario países asocia cada persona con el país que ha visitado.

paises = {

‘Juan’: {‘Chile’, ‘Argentina’},
‘Pedro’: {‘Francia’, ‘Suiza’, ‘Chile’},
‘Diego’: {‘Chile’, ‘Italia’, ‘Francia’, ‘Peru’},

}

Escriba una función cuantos_en_comun(a, b), que indique cuántos países en común han
visitado la persona a y la persona b.

#>>> cuantos_en_comun(‘Juan’, ‘Diego’)
1
#>>> cuantos_en_comun(‘Diego’, ‘Pedro’)
'''

paises = {
    "Juan": {"Chile", "Argentina"},
    "Pedro": {"Francia", "Suiza", "Chile"},
    "Diego": {"Chile", "Italia", "Francia", "Peru"},
}

def cuantos_en_comun(nombre1, nombre2):
    a = paises[nombre1]
    b = paises[nombre2]
    return len(a & b)

print(cuantos_en_comun("Juan", "Diego"))
print(cuantos_en_comun("Diego", "Pedro"))
