def producto_interno(a, b):
    final = []
    for i in range(len(a)):
        final.append(a[i]*b[i])
    return sum(final)
    
a = [7, 1, 4, 9, 8]
b = range(5)
print(producto_interno(a, b))
