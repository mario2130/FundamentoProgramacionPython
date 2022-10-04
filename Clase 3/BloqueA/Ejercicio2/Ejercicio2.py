'''
Escriba un programa que resuelva una ecuación de segundo grado de la
forma:

Recuerde que primero debe calcular el discriminante (d=b**2–4*a*c)
para determinar si la ecuación, (1) no tiene solución real (d<0), (2) tiene
solución única (d==0) o (3) tiene 2 soluciones (d>0).

Use alguna función ☺
'''

import math

def dis(a,b,c):
    return (b ** 2) - 4 * a * c

def cuadratic_ecuation(a,b,c):
    d = dis(a, b, c)
    if(d < 0):
       return d
    else:
        x = -1 * b * -1 * math.sqrt(d)
        x = x / (2 * a)
        return x

# 1,-5, 6 => dos soluciones
# 1,-2, 1 => una solución
# 1, 1, 1 => no tiene solucion en los reales

valA = int(input("Ingrese A: "))
valB = int(input("Ingrese B: "))
valC = int(input("Ingrese C: "))


resul = cuadratic_ecuation(valA,valB, valC)

if(resul < 0):
    print("no tiene resultado real: ",resul)
elif(resul ==0):
    print("solucion unica: ",resul)
else:
    print("tiene dos soluciones: ", resul)