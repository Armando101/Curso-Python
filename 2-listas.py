"""
Las listas son una estructura de datos. Es un tipo de dato que nos permite trabajar con grandes cantidades de datos.

Pueden almacenar datos de cualquier tipo como string, int, float, boolean, etc.

Las listas son parecidos a los arreglos en otros lenguajes de programación con la diferencia de que las listas pueden cambiar de tamaño en tiempo de ejecución

Las listas pueden alterar los datos que están en esta.

No es común trabajar con listas que contengan información de distintos tipos.

El índice de las listas comienza en 0

"""

# Declaración de una lista
# nombre de la variable, signo igual, corhetes


lista = ["Armando", 22, True, 23.5]

cursos = ["python", "django", "flask", "C", "C++", "C#","java", "php"]

curso = cursos[0]
print(curso)

# Si coloco el indice -1 accedo al último elemento de la lista

curso = cursos[-1]
print(curso)

# Si colocamos un índice que no existe marca un error

# curso = cursos[10]

# Podemos generar sublistas a través de una lista

# Coloco el indice donde empiza mi lista, dos puntos y el índice donde termina la lista

# Para obtener datos con saltos usamos la siguiente sintaxis

# sub6 = cursos[1:7:2]

# Recorre la lisa desde el índice 1 hasta el 6 con saltos de dos en dos

# Para imprimir la lista al revés usamos la siguiente sintáxis

# sub7 = cursos[::-1]

# Recorre la lista desde el primer índice hasta el último con saltos de -1

sub = cursos[0:3]
sub2 = cursos[:7]
sub3 = cursos[4:7]
sub4 = cursos[5:]
sub5 = cursos[:]
sub6 = cursos[1:7:2]
sub7 = cursos[::-1]


print(sub)
print(sub2)
print(sub3)
print(sub4)
print(sub5)
print(sub6)
print(sub7)


######## Sub listas ####

"""

Estas son las formas en las cuales nosotros podemos crear una nueva lista a partir de otra.

    [:] Todos los elementos.
    [start:] Todos los elementos desde el índice establecido(start).
    [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
    [start:end] Todos los elementos de un rango de índices.
    [start:end:step] Todos los elementos de un rango de índices con saltos.

    De igual forma, este listado es aplicable a las tuplas y los strings.

"""
print("\n")
print("\n")
########## Operaciones comunes ##########

lista = [8.17, 90, 1, 5, 44, 1.32]
print(lista)

# Ordenar una lista de forma ascendente
lista.sort()
print(lista)

# Ordenar una lista de forma descendente
lista.sort(reverse = True)
print(lista)

# Obtener el valor mayor
mayor = lista[0]
print(mayor)

# Obtener el valor menor
menor = lista[-1]
print(menor)


### Otras formas más eficientes para obtener el valor mayor y menor

mayor = max(lista)
menor = min(lista)

print(mayor)
print(menor)

# Longitud de la lista
longitud = len(lista)
print(longitud)

# Saber si un valor está en la lista

# Resultado es un valor booleano
resultado = 8 in lista
print(resultado)

resultado = 8.17 in lista
print(resultado)

# Saber el índice de un valor en una lista
indice = lista.index(8.17)
print(indice)

# Cuántos veces se repite un valor en la lista
contador = lista.count(5)
print(contador)

# Insertar un valor en cierta posición
#lista.insert(posición, valor)
lista.insert(2, 8)
print(lista)

# Eliminar un valor de la lista
#lista.remove(valor a remover)
lista.remove(5)
print(lista)

# Añadir un valor al final de la lista
lista.append(10)
print(lista)

# Elimina los datos de la lista
lista.clear()
print(lista)


# Estos métodos también se aplican para listas que contienen strings

print("\n")
print("\n")
################# Matrices ##########

# Declaración de una matriz

fila_uno = [10, 20]
fila_dos = [30, 40]

matriz = [fila_uno, fila_dos]

# Obtener un valor de la matriz
primer_elemento = matriz[0][0]
print(primer_elemento)