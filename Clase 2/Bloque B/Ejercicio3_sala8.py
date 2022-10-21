'''Escriba un programa que pida al usuario un valor entero n e
imprima un patrón triangular de n líneas como el que se muestra a
continuación:'''


cantidad = int(input("Ingrse n: "))
i = 1
cruces = "+"

while i <= cantidad:

    print(cruces)
    cruces = cruces + "+"
    i += 1
