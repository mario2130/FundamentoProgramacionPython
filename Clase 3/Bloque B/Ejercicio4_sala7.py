def codigo_hora(codigo):
    hora = codigo.split(':')[0]
    minuto = codigo.split(':')[1]
    suma_hora = 0
    suma_minuto = 0
    
    for i in hora:
        suma_hora += int(i)
    for i in minuto:
        suma_minuto += int(i)

    suma_hora = suma_hora % 24
    suma_minuto = suma_minuto % 60
    print('{}:{}'.format(suma_hora, suma_minuto))


codigo_hora('776199:68556') 
