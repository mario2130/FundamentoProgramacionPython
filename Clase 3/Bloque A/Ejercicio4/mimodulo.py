def factorial_reciproco(n):
    prod = 1
    for i in range(n):
        prod += prod*i

    return 1/prod

''''''
def signo(n):
    return 1 if n % 2 == 0 else -1


#print(factorial_reciproco(7)) # 1*2 = 2 / 3->6 / 6*4 ->24
#print(signo(2))
#print(signo(3))