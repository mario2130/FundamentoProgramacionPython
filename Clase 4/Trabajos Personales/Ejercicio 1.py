from supermercado_c4 import itemes
from supermercado_c4 import productos
from supermercado_c4 import clientes
from supermercado_c4 import ventas

def producto_con_mas_ingresos(it, pr):
    lista = []
    for id, nombre, precio, cantidad in productos:
        valor = 0
        for boleta, id2, cant in itemes:
            if id == id2:
                valor+= cant*precio
        lista.append([valor,nombre])
    lista.sort(reverse=True)
    return lista[0][1]

def cliente_que_mas_pago(it, pr, cl,ve):
    lista = []
    for rut, nombre in cl:
        valor = 0
        for boleta, fecha, rut2 in ve:
            if rut == rut2:
                for boleta2, id2, cant in it:
                    if boleta == boleta2:
                        for id, nombre2, precio, cantidad in pr:
                            if id == id2:
                                valor += precio*cant
        lista.append([valor, nombre])
    lista.sort(reverse=True)
    return lista[0][1]

def ingreso_total_por_ventas(it, pr):
    venta=0
    for boleta, id, cant in it:
        for id2, name, precio, cant2 in pr:
            if id == id2:
                venta += precio*cant
    return venta

def total_ventas_del_mes(ano, mes, it, pr, ve):
    valor = 0
    for boleta, fecha, rut2 in ve:
        if ano == fecha[0] and mes == fecha[1]:
            for boleta2, id2, cant in it:
                if boleta == boleta2:
                    for id, nombre2, precio, cantidad in pr:
                        if id == id2:
                            valor += precio * cant
    return valor

def fecha_ultima_venta_producto(idprod, it, ve):
    lista = []
    for boleta2, id2, cant in it:
        if id2 == idprod:
            for boleta, fecha, rut2 in ve:
                if boleta == boleta2:
                    lista.append(fecha)
    lista.sort(reverse=True)
    return lista[0]

print('El producto con mas ingresos es:', producto_con_mas_ingresos(itemes, productos))
print('El cliente que mas pago es:', cliente_que_mas_pago(itemes, productos, clientes, ventas))
print('Los ingresos por venta son:', ingreso_total_por_ventas(itemes, productos))
print('El total de ventas del mes: ', total_ventas_del_mes(2010, 10, itemes, productos, ventas))
print('La fecha de ultima venta del producto es:', fecha_ultima_venta_producto(47470, itemes, ventas))
