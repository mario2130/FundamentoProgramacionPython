paises = {
'Juan': {'Chile', 'Argentina'},
'Pedro': {'Francia', 'Suiza', 'Chile'},
'Diego': {'Chile', 'Italia', 'Francia', 'Peru'},
}

def cuantos_en_comun(a,b):
    print(str(len(paises[a] & paises[b])))

cuantos_en_comun('Juan', 'Pedro')
cuantos_en_comun('Diego', 'Pedro')
cuantos_en_comun('Diego', 'Juan')