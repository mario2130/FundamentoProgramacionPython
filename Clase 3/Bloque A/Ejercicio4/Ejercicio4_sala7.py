def factorial_reciproco(n):
    divisor = 1
    for i in range(n):
        divisor *= i+1
    return (1/divisor)

def signo(n):
    if n%2==0:
        s = 1
    else:
        s = -1
    return s

def seno_aprox(x, m):
    resp=0
    init = 1
    for i in range(m):
        resp += signo(i)*(x**init)*factorial_reciproco(init)
        init += 2
    print(resp)

def coseno_aprox(x, m):
    resp = 0
    init = 0
    for i in range(m):
        resp += signo(i) * (x ** init) * factorial_reciproco(init)
        init += 2
    print(resp)

seno_aprox(2, 3)
coseno_aprox(2, 3)