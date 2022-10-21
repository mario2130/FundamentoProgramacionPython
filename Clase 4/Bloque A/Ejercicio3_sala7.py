from Ejercicio2_sala7 import producto_interno
def son_ortogonales(a, b):
    resultado = producto_interno(a, b)
    if resultado == 0:
        return True
    else:
        return False 


print(son_ortogonales([2, 1], [-3, 6]))