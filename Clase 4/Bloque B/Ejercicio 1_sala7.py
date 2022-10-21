a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9)
z, w = x
v = (x, a)


print(a < b)  #ok
print(y + w)    #ok
print(x + a)    #ok
print(len(v))   #ok
print(v[1][1])  #ok
print(c[0]) #ok
print(a + b[1:5])   #ok
print((a + b)[1:5]) #ok
print(str(a[2]) + str(b[2])) #ok 2-1
print(str(a[2] + b[2])) #ok
print(str((a + b)[2]))  #ok
print(str(a + b)[2][0]) #ok
