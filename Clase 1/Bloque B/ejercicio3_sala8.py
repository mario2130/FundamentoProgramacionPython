#Escriba programa que reciba como entrada la estatura, el peso y la edad de una persona
# y le entregue la condición de riesgo.
#Considere que el IMC se calcula: peso / estatura ** 2

estatura = float(input("ingrese su altura en m: "))
peso = float(input("ingrese su peso en k: "))
edad = int(input("ingrese su edad: "))

imc = peso /(estatura ** 2)
print("imc calculado:", imc)

resultado = ""
if(edad < 45):
    if(imc < 22.0):
        resultado = "bajo (menor 45)"
    else:
        resultado = "medio (menor 45)"
else:
    resultado = "medio (mayor igual 45)" if(imc < 22.0) else "alto (mayor igual 45)"

print("su riesgo es:", resultado)


