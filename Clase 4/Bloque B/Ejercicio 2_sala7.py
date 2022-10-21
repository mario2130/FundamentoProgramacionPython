from supermercado_c4 import productos
from supermercado_c4 import itemes

def producto_mas_caro(p):
    precioinit = 0
    for id, name, precio, cant in p:
        if precio > precioinit:
            nombre = name
            precioinit = precio
    return nombre

def valor_total_bodega(p):
    bodega = 0
    for id, name, precio, cant in p:
        bodega += precio*cant
    return bodega

def ingreso_total_por_ventas(i, p):
    venta=0
    for boleta, id, cant in i:
        for id2, name, precio, cant2 in p:
            if id == id2:
                venta += precio*cant
    return venta

print('producto mas caro es:',producto_mas_caro(productos))
print('El valor total de la bodega es:',valor_total_bodega(productos))
print('La venta total fue de:',ingreso_total_por_ventas(itemes, productos))