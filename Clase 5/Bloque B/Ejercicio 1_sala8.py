'''
Considere las siguientes asignaciones
#>>> a = {5, 2, 3, 9, 4}
#>>> b = {3, 1}
#>>> c = {7, 5, 5, 1, 8, 6}
#>>> d = [6, 2, 4, 5, 5, 3, 1, 3, 7, 8]
#>>> e = {(2, 3), (3, 4), (4, 5)}
#>>> f = [{2, 3}, {3, 4}, {4, 5}]

Sin ayuda del computador discuta en su grupo el resultado de lo siguiente:
1. len(c)
2. len(set(d))
3. a & (b | c)
4. (a & b) | c
5. c – a
6. max(e)
7. f[0] < a
'''

a = {5, 2, 3, 9, 4}
b = {3, 1}
c = {7, 5, 5, 1, 8, 6}
d = [6, 2, 4, 5, 5, 3, 1, 3, 7, 8]
e = {(2, 3), (3, 4), (4, 5)}
f = [{2, 3}, {3, 4}, {4, 5}]

# & son la intercepción
# | la union
print('1. len(c): ',len(c))                   #5
print('2. len(set(d)): ',len(set(d)))         #5
print('3. a & (b | c): ',a & (b | c))         #{3,5}
print('4. (a & b) | c: ',(a & b) | c)         #{7,3,5,1,8,6}
print('5. c – a: ', c - a)                    #{7, 1, 8, 6}
print('6. max(e): ',max(e))                   #{4,5}
print('7. f[0] < a: ',f[0] < a)               #True