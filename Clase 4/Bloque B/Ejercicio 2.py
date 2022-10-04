'''
Un supermercado utiliza las siguientes estructuras de datos para manejar su
inventario. Las estructuras se encuentran en el archivo supermercado.py.

Basado en esas estructuras (listas de tuplas), desarrolle las siguientes
funciones:

#>>> producto_mas_caro(productos)
‘Vuvuzela’
#>>> valor_total_bodega(productos)
1900570
#>>> ingreso_total_por_ventas(itemes, productos)
13944
'''


from supermercado_c4 import *

def producto_mas_carov1(productos):
    nombreCaro = ""
    masCaro = 0
    for id_producto, nombre, precio, cantidad_bodega in productos:
        if(precio > masCaro):
            masCaro = precio
            nombreCaro = nombre
    return nombreCaro

def producto_mas_carov2(productos):
    lista = []
    for id_producto, nombre, precio, cantidad_bodega in productos:
        lista.append((precio, nombre))
    lista.sort()
    return lista[-1][1]

def valor_total_bodega(productos):
    valorTotal = 0
    for id_producto, nombre, precio, cantidad_bodega in productos:
        valorTotal += cantidad_bodega*precio
    return valorTotal

def ingreso_total_por_ventas(itemes, productos):
    ingreso_total = 0
    for num_boleta, iid_producto, icantidad in itemes:
        for id_producto, nombre, precio, cantidad_bodega in productos:
            if(iid_producto == id_producto):
                ingreso_total += precio*icantidad
    return ingreso_total


print(producto_mas_carov1(productos))
print(producto_mas_carov2(productos))
print(valor_total_bodega(productos))
print(ingreso_total_por_ventas(itemes, productos))