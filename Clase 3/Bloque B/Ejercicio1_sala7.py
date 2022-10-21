from random import  choice


def cadena_al_azar(n):
    cadena = ''    
    for i in range(n):
        cadena += choice('atcg')
    print(cadena)


n = int(input('Ingrese largo cadena:'))
cadena_al_azar(n)
 
