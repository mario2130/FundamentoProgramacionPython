#Escriba un programa que el área de un triángulo a partir de la longitud de sus lados (a,b,c) y de su semiperimetro
#mediante la siguiente fórmula
# a = raiz s(s-a)(s-b)(s-c)

l1 = float(input("Ingrese la longitud del lado 1:"))
l2 = float(input("Ingrese la longitud del lado 2:"))
l3 = float(input("Ingrese la longitud del lado 3:"))


s = (l1 +l2 + l3) /2
d1 = s -l1
d2 = s -l2
d3 = s -l3


prod = s * d1 * d2 * d3
area = prod ** 0.5  # evelado a 0,5
print("El área del triangulo es:", area)
