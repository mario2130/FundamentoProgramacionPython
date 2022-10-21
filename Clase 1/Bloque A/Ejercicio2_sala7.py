# Escriba un programa que determine el area de un circulo a partir de su radio
from math import pi
radio = (float(input('Ingrese radio: ')))
area = pi * (radio **2)
print(round(area, 2))
