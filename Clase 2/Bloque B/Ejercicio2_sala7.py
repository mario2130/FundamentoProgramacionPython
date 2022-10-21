i = 1
n = int(input('Ingrese cantidad de números:'))

valor = float(input('Ingrese valor {}:'.format(i)))
mayor = valor
menor = valor 

while i < n :
    i += 1
    valor = float(input('Ingrese valor {}:'.format(i)))
    
    if valor > mayor:
        mayor = valor
    if valor < menor :        
        menor = valor
print (mayor, menor)
print('Rango:', mayor - menor)
