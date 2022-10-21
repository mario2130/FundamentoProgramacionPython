# Escriba un programa que calcule el área de un triángulo a partir de la longitud de sus lados (a, b y c), y de su semiperímetro (s) mediante la siguinete fórmula: A=sqrt(s(s-a)(s-b)(s-c). s=(a+b+c)/2a = a
from math import sqrt
a = float(input('Ingrese lado a: '))
b = float(input('Ingrese lado b: '))
c = float(input('Ingrese lado c: '))
s = (a + b + c)/2
A = (sqrt(s*(s-a)*(s-b)*(s-c)))

print('El area del triangulo es:', round(A, 2))


