'''
Considere las siguientes asignaciones:

#>>> a = (2, 10, 1991)
#>>> b = (25, 12, 1990)
#>>> c = (‘Donald’, True, b)
#>>> x, y = ((27, 3), 9)
#>>> z, w = x
#>>> v = (x, a)

Si usar el computador, indiquen en grupo cuál es el resultado y el tipo de las siguientes expresiones. Luego,
verifique en el computador.

1. a < b
2. y + w
3. x + a
4. len(v)
5. v[1][1]
6. c[0] 12. str(a + b)[2][0]
7. a + b[1:5]
8. (a + b)[1:5]
9. str(a[2]) + str(b[2])
10. str(a[2] + b[2])
11. str((a + b)[2])
12. str(a + b)[2][0]
'''

a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9)         #=> y= 9
z, w = x                    #27,3 = x
v = (x, a)


print("1. a < b: ", a < b)                               #rogelio, ruben, mario = (True, True, True)
print("2. y + w: ",y + w)                                #rogelio, ruben, mario = (12, 12, 12)
print("3. x + a: ",x + a)                                #rogelio, ruben, mario = ((27,3,1991), ((29,2),5,19)), (29,13,1991))
print("4. len(v): ",len(v))                              #rogelio, ruben, mario = (2, 2, 1)
print("5. v[1][1]: ",v[1][1])                            #rogelio, ruben, mario = (10, (27,3), 3)
print("6. c[0]: ",c[0])                                  #rogelio, ruben, mario = ('Donald', 'Donald', 'Donald')
print("7. a + b[1:5]: ",a + b[1:5])                      #rogelio, ruben, mario = ('Error', 'Error', 'Error')
print("8. (a + b)[1:5]: ",(a + b)[1:5])                  #rogelio, ruben, mario = ((10, 1991, 25, 12 ), (2, 10, 1991, 25, 12 ), (10, 1991, 25, 12 ))
print("9. str(a[2]) + str(b[2]): ",str(a[2]) + str(b[2]))#rogelio, ruben, mario = ( '19911990','19911990', '19911990')
print("10. str(a[2] + b[2]): ",str(a[2] + b[2]))         #rogelio, ruben, mario = (3981, 3981, 3981)
print("11. str((a + b)[2]): ",str((a + b)[2]))           #rogelio, ruben, mario = (1991, 1991, 1991)
print("12. str(a + b)[2][0]: ", str(a + b)[2][0])        #rogelio, ruben, mario = ('Error out index', 'Error general', 'Error not convert to str')
