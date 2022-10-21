from math import sqrt

def ecuacion (a, b, c):
    d = b**2 - 4 * a * c

    if d < 0:
        print('No tiene Solución')
        
    elif d == 0:
        x1 = (-b - sqrt(b**2 - 4 * a * c))/2 * a
        x2 = (-b + sqrt(b**2 - 4 * a * c))/2 * a
        print('Solución única',  x1)
        
    else:
        x1 = (-b - sqrt(b**2 - 4 * a * c))/2 * a
        x2 = (-b + sqrt(b**2 - 4 * a * c))/2 * a
        print('Tiene dos soluciones', x1, x2)
        


a = float(input('Ingrese a:'))
b = float(input('Ingrese b:'))
c = float(input('Ingrese c:'))

ecuacion (a, b, c) 
