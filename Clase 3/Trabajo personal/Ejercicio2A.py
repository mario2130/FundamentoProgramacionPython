# Escriba la función valida(cadena) que reciba un string con una cadena
# de ADN y retorne True si la cadena es válida o False si no lo es. Una
# cadena no es válida cuando aparecen bases nitrogenadas distintas a las
# indicadas previamente (Adenina, Citosina, Guanina y Timina)

def valida(cadena):
    cadenas_validas = 'CTGA'
    for i in set(cadena.replace(' ', '')):
        if i not in cadenas_validas:
            return False

    return True

if __name__ == '__main__':

    secuencia = str(input('Ingrese secuencia de adn: '))
    #secuencia = "CTGA CTGA AATT GGGC CTGG CCCC"

    print(valida(secuencia))

