"""

Las tuplas son una estructura de datos similar a las listas, nos permiten almacenar distintos tipos de datos incluso listas y tuplas.

La diferencia enre una tupla y una lista es que las tuplas son inmutables.

Si asignamos valores a una tupla, éstos no se podrán modificar y quedarán así el resto del programa

"""

# Sintaxis de declaración

# Nombre de la variable, signo igual, paréntesis

tupla = ()

# Los datos se colocan dentro del paréntesis

tupla = ('Armando', 2, 4.5, True)

# En las tuplas no existen métodos como append, remove o insert

# La ventaja de las tuplas por encima de las listas es que son más rápidas para obtener elementos

##### Valores por índices ####

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# Para acceder a los elementos de la tupla colocamos entre corchetes el índice del valor deseado
elemento = tupla[4]

print(tupla)
print(elemento)

# Podemos usar la misma sintaxis que con las listas

# Obtener los elementos del primero hasta el índice 9 con saltos de dos en dos
elementos = tupla[:9:2]
print(elementos)

# Si intentamos modificar las tuplas obtenemos un error

# tupla[1] = 20

######## Comprimir y descomprimir tuplas ######

# Podemos declarar varias variables en una sola línea de código accediendo desde los índices
tupla = (1, 2, 3, 4)
uno, dos, tres, cuatro = tupla[0], tupla[1], tupla[2], tupla[3]

print(uno)
print(dos)
print(tres)
print(cuatro)

# La línea anterior se puede simplificar

uno, dos, tres, cuatro = tupla

print(uno)
print(dos)
print(tres)
print(cuatro)

# Si tenemos más valores que variables a asignar lo hacemos de la siguiente manera
tupla = (1, 2, 3, 4, 5, 6)
uno, dos, tres, *cuatro = tupla

# Con el asterisco indicamos que la variable cuatro toma los valores que "sobran"

print(cuatro)

# El asterisco se puede colocar en cualquier variable

# Podemos generar nuevas tuplas a partir de listas
lista = [10, 20, 30, 40]

# Utilizamos la función zip
# La función zip nos regresa una tupla que contiene tuplas, estas tuplas tiene un valor de la primera y segunda estructura de datos que se pasó como parámetro
# La función zip nos regresa un objeto de tipo zip

# La función zip puede recibir N cantidad de listas, N cantidad de tuplas o N cantidad de tuplas y listas

resultado = zip(tupla, lista)

# Para convertir el objeto resultado en una tupla usamos la función tuple()

resultado = tuple(resultado)
print(resultado)

# Podemos convertir el objeto resultado a una lista
resultado = list(resultado)
print(resultado)

tupla_dos = (100, 200, 300, 400)
resultado = zip(tupla, lista, tupla_dos)
resultado = tuple(resultado)
print(resultado)


# Con la función zip podemos obtener elementos de una tupla y generar nuevas tuplas

# Qué pasa si tengo una tupla mucho más grande y necesito obtener tres elementos (el primero, el segundo y el último).

tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)

# Lo que podemos hacer es utilizar el guión bajo _ junto con el asterisco * y aplicar lo que hemos visto anteriormente.

primero, segundo, *_, ultimo = tupla

# El guión bajo hace referencia a una variable que no necesitamos y no vamos a usar


######### De listas a tuplas #######

# Es posible convertir una lista a una tupla y viceversa

lista = ["Curso", "Python", "Proteco"]
tupla = ("Introducción", "Básico", "Listas", "Tuplas")

# Convertir una tupla a lista
nueva_lista = list(tupla)
print(nueva_lista)

# Convertir una lista a una tupla
nueva_tupla = tuple(lista)
print(nueva_tupla)

# Se puede convertir una string a una tupla o a una lista

mensaje = "Este es el curso de python"

mensaje_lista = list(mensaje)
mensaje_tuple = tuple(mensaje)

print(mensaje_lista)
print(mensaje_tuple)