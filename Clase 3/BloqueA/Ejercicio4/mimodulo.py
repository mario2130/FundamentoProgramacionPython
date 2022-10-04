def factorial_reciproco(n):
    i = 1
    prod = 1
    while i <= n:
        prod *= i
        i *= 1
    return 1/prod

''''''
def signo(n):
    return 1 if n % 2 == 0 else -1


