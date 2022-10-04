'''
Cree una función codigo_hora(codigo) que reciba un código cifrado de
sólo números y el caracter ‘:’ y entregue el código descrifrado. La regla de
descifrado es la siguiente: sumar cada dígito anterior al caracter ‘:’ y
calcular el resto de la división entera entre esa suma y 24. Luego, lo mismo
con los dígitos después del carácter ‘:’, pero ahora el resto de la división es
entre esa suma y 60.

#>>> codigo_hora(‘776199:68556’)
‘15:30’
'''

def codigo_hora(codigo):
    '''
    7+7+6+1+9+9 = 39 / 24 = 1
                    15
    :param codigo:
    :return:
    '''
    position = codigo.find(':')
    print("position: ", position)
    hours = codigo[0:position]
    print("hours: ", hours)
    minutes = codigo[position+1::]
    print("minutes: ", minutes)

    hourConverted = int(hours) % 24
    print(hourConverted)

    minuteConverted = int(minutes) % 60sfdsdf
    print(minuteConverted)

    return str(hourConverted) + ":" + str(minuteConverted)



codigo = input(str("ingrese codigo: "))
print(codigo_hora(codigo))

