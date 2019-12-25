########### Variables

# Una variable es un espacio reservado en la memoria
nombre_instructor = "Armando"

print(nombre_instructor)

# Estructura de una variable
#	Nombre de la variable
#	Signo igual
#	Valor de la variable

# Es una buena practica nombrar las variables de tal manera que sean descriptivas

# Si queremos usar dos palabras para nombrar una variable usamos la comvención Snake case que consiste en usar minúsculas y separar las palabras por guión bajo

###### Constatntes
# Nos permiten guardar un valor que no puede ser modificado
# Las letras de la varibale se colocan en mayúsculas

CONSTANTE = "soy una constante"
print(CONSTANTE)

# Python nos permite modificar las constantes sin embargo esto no se debe hacer


######## Asignación múltiple
"""
valor_uno = 10
valor_uno = "Armando"
valor_tres = 10*20
"""

# Las tres líneas anteriores pueden ser reducidas como sigue

valor_uno, valor_dos, valor_tres = 10, "Armando", 10*20

print(valor_uno)
print(valor_dos)
print(valor_tres)

# No es recomendabe declarar muchas variables en una sola línea de código
# Esto por una razón de legibilidad

############ Operadores relacionales y lógicos

# Son símbolos que comparan dos valores y me devuelven un valor booleano

variable_uno = 10
variable_dos = 20

mayor = valor_uno > variable_dos
menor = valor_uno < variable_dos
mayor_igual = valor_uno >= variable_dos
menor_igual = valor_uno <= variable_dos
igual = valor_uno == variable_dos
diferente = valor_uno != variable_dos

print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)

# Operadores logicos

resultado = True and True and diferente
print(resultado)

resultado = True and True and mayor
print(resultado)

#### Entrada de datos por teclado
# Cadenas

#print("¿Cuál es tu nombre?")
nombre = input("¿Cuál es tu nombre? ")

# Enteros
print("¿Cuál es tu edad")
edad = int(input())

# Flotantes
print("¿Cuál es tu peso?")
peso = float(input())

# Booleanos
print("¿Estás autorizado (si/no)?")
autorizado = input() == "si"

print("Hola ", nombre)
print("Edad: ", edad)
print("Peso: ", peso)
print("Autorizado: ", autorizado)

#### Comentarios

# Los comentarios los ponemos con #
# Las líneas comentadas no son ejecutadas por python

"""
	Esto
	Es un comentario
	De varias líneas
	En python

	Es buena práctica comentar código en python ya que ayuda a la legibilidad del código

"""