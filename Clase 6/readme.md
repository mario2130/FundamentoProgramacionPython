# Clase 6 - Lectura de archivo

puntos importantes de esta clase:
- lectura
- escritura
- recorrido de archivos


## lectura
```
file = open("quijote.txt")
```

## escritura

```
archivo.write(key + " : max " + str(max) + ", min " + str(min) + "\n")
```

## recorrido de archivos

```
for row in file:
    leters_count += len(row.strip())
    word_count += len(row.strip().split())
    line_count += 1

file.close()
```
