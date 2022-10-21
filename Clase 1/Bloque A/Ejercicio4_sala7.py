# Escriba un programa que convierta de centimetros a pulgadas. Una pulgada es igual a 2.54 centimetros.

cent = float(input('Ingrese logitud: '))
pulg = cent / 2.54
print('los', cent, 'cm', 'son', round(pulg, 4),'in')