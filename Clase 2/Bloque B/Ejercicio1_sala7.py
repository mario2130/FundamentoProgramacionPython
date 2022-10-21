i = 0
n = int(input('Ingrese cantidad de números:'))

mayor = 0

while i < n :
    i += 1
    valor = float(input('Ingrese valor {}:'.format(i)))
    
    if valor > mayor:
        mayor = valor
print (mayor)
