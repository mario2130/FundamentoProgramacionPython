'''
Cree una función codigo_palabra(codigo) que reciba un código cifrado de sólo
letras y entregue el mensaje descifrado. La regla de descifrado es la siguiente: la
palabra descifrada se obtiene recorriendo desde el final de la palabra hasta el
comienzo, considerando las letras solo en ubicaciones impares. Empezando desde
la última letra.

#>>> codigo_palabra(‘aczaarltp’)
‘plaza’

#>>> codigo_palabra(‘axruatgrrreov’)
‘vergara’
'''


def codigo_palabra(codigo):
    codigoInvertido = codigo[::-1]
    return codigoInvertido[::2]



codigo = input(str("ingrese codigo: "))
print(codigo_palabra(codigo))