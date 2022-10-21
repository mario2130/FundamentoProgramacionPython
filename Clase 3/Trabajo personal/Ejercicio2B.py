def cantidad(cadena, base):
    count = {i: cadena.count(i) for i in set(cadena)}
    return count[base]

if __name__ == '__main__':
    print(cantidad('CTGA CTGA AATT GGGC CTGG CCCC', 'A'))