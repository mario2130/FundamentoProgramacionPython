# Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y el entrgue la condición de riesgo.Considere que el IMC se calcula como: peso/estatura**2.
estatura = float(input('Ingrese estatura: '))
peso = float(input('Ingrese peso: '))
edad = int(input('Ingrese edad: '))
imc = (peso / estatura **2)
print('la masa corporal es: ', round(imc, 2))
if edad >= 45:
    if imc>= 22.0:
        print('IMC: ALTO')
    else:
        print('IMC: MEDIO')
if edad < 45:
    if imc >= 22.0:
        print('IMC: MEDIO')
    else:
        print('IMC: BAJO')



