sueldo = float(input('Ingrese su sueldo: '))
if sueldo >=4000:
    print('Usted pagara', sueldo * 0.12, 'de impuesto')
if sueldo < 4000 and sueldo >= 2000:
    print('Usted pagara', sueldo * 0.10, 'de impuesto')
if sueldo < 2000 and sueldo >= 1000:
    print('Usted pagara', sueldo * 0.05, 'de impuesto')
elif sueldo < 1000:
    print('Usted pagara', sueldo * 0, 'de impuesto')