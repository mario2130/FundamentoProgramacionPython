'''
El banco CBI necesita implementar mejoras en sus mecanismos de seguridad, precisamente en los
que están relacionados con la generación de claves iniciales para sus clientes de tarjetas de crédito.
Para esto, desarrolle un programa que permita generar una clave de 4 dígitos, usando el siguiente
algoritmo:

• Leer tantos números como sea necesario para generar la clave.

• Para cada número deberá recorrer su dígitos y encontrar el menor.

• Si el dígito menor es par, pasará a formar parte de la clave, en caso contrario, se procesa el
siguiente número hasta formar la clave de 4 dígitos.

• Mostrar la clave obtenida.

538967412

'''



clave = ""
condicion = True
while condicion:
    ingresado = int(input("Ingrese un número: "))
    menor = 99
    claveTemporal = ""
    for i in str(ingresado):
        digito = int(i)
        print("digito analizado: ", digito)
        if (digito < menor):
            menor = digito
            print("digito encontrado menor: ", menor)
        if(menor % 2 == 0 and len(claveTemporal) == 0):
            claveTemporal += str(menor)
            print("digito menor par: ", claveTemporal)

    clave += claveTemporal
    if(len(clave) == 4):
        condicion = False
        print("Clave encontrada: ", clave)