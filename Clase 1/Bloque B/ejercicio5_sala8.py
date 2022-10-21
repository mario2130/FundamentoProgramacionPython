#Escriba un programa que permita ingresar 5 números enteros y
#determine cuál de los cuatro números es el más lejano al primero.



numero1 = int(input("ingrese numero1: "))
numero2 = int(input("ingrese numero2: "))
numero3 = int(input("ingrese numero3: "))
numero4 = int(input("ingrese numero4: "))
numero5 = int(input("ingrese numero5: "))

# n1 = 1 y n2 = 3, diff = 2
# n1 = 1 y n4 = 5, diff = 4

diff1and2 = abs(numero1 - numero2)
diff1and3 = abs(numero1 - numero3)
diff1and4 = abs(numero1 - numero4)
diff1and5 = abs(numero1 - numero5)

if(diff1and2 > diff1and3 and diff1and2 > diff1and4 and diff1and2 > diff1and5):
    print("mayor distancia es el nro 2:", numero2)
elif(diff1and3 > diff1and4 and diff1and3 > diff1and5):
    print("mayor distancia es el nro 3:",numero3)
elif(diff1and4 > diff1and5):
    print("mayor distancia es el nro 4:",numero4)
else:
    print("mayor distancia es el nro 5:",numero5)


