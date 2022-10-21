'''
Escriba un programa que abra el archivo quijote.txt y cuente:

- Cuántas letras tiene

- Cuántas palabras tiene

- Cuántas líneas tiene
'''

file = open("quijote.txt")
leters_count = 0
word_count = 0
line_count = 0

for row in file:
    leters_count += len(row.strip())
    word_count += len(row.strip().split())
    line_count += 1

file.close()

print("Cuántas letras tiene: ", leters_count)
print("Cuántas palabras tiene: ", word_count)
print("Cuántas líneas tiene; ", line_count)


