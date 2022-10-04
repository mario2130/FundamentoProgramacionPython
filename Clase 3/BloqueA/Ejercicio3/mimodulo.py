
def invert_number(n):
    final = ""
    while n > 0:
        digito = n % 10
        n = n // 10
        final += str(digito)
    return int(final)