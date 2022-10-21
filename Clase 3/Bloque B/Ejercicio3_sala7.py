def codigo_palabra(codigo):
    invertido = codigo[::-1]
    return invertido[::2]

codigo = input(str("ingrese codigo para invertir: "))
print(codigo_palabra(codigo))