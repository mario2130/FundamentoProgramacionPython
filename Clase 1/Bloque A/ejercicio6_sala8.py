#Escriba un programa que transforme una temperatura ingresada por usuario de grandos F a C,
#usando la siguiente formula C= F-32*(5/9)

f = float(input("Temp. en Fahrenheit: "))
c = (f -32) * 5 /9
print("los",f,"F en grados celsius son",round(c),"C")
                