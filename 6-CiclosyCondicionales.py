
"""

Python cuenta con un tipo de dato llamado none
Utilizamos none para representar la ausencia de un valor

Los valores tomados como False en python son:
	- False
	- None
	- 0
	- 0.0
	- string vacío ""
	- Lista vacía []
	- Tupla vacía ()
	- Diccionrio vacío {}

Cualquier otro valor es tomado como verdadero

"""

# Se puede asignar none a una variable
variable = None
print(variable)

# También se puede resetear una variable
variable = [1, 2, 3, 4]
variable = None
print(variable)

######################### Condicionales ###########################

color_luz = 'roja'
if color_luz == 'verde':
	print('Puede continuar')
elif color_luz == 'amarillo':
	print('Alto parcial')
else:
	print('Alto total')


variable = True
if variable:
	print('Es verdader')
else:
	print('Es falso')

######################### Ciclo while ###########################
numero = 123456789
contador = 0

# Con el else podemos emular un ciclo do while
while numero >=1:
	contador += 1
	numero = numero / 10
# El código después del else se ejecuta cuando la condición del while no se cumple
else:
	print("La cantidad de dígitos del número es ", contador)

######################### Ciclo for ###########################

numeros = [1, 2,3 ,4 ,5, 6, 7, 8,9, 10]
for numero in numeros:
	print(numero)

diccionario = {'a':1, 'b':2}
for llave in diccionario:
	print(llave)

valores = ( (10, 20), ["strings", "strings"], (True, False) )
# Imprimir cada valor de la tupla
for valor in valores:
	print(valor)

# Si cada objeto dentro de la tupla tiene dos valores y queremos obtener esos valores lo hacemos de la siguiente manera
for valor1, valor2 in valores:
	print(valor1, valor2)

# Para obtener tres valores:
valores = ( (10, 20, 30), ["strings", "strings", "strings"], (True, False, True) )
for valor1, valor2, valor3 in valores:
	print(valor1, valor2, valor3)

######################### Función range y enumerate ###########################
# Con la función range podemos generar números para iterar sobre estos

# For que se repite 10 veces
# range(10) genera 10 números
for valor in range(10):
	print(valor)

# Definir un rango
# range(número de inicio, número final)
for valor in range(5, 10):
	print(valor)

# Es posibel definir rango con número negativos
for valor in range(-10, 11):
	print(valor)

# Definir saltos
# range(inicio, final, saltos)
for valor in range(1, 101, 2):
	print(valor)

# Combinar range con len
lista = [1, 2, 3, 4, 5, 6]
for indice in range(len(lista)):
	print("Indice: ", indice, " valor: ", lista[indice])

# enumerate nos devuelve el índice y el valor que se encuentra en ese índice
for indice, valor in enumerate(lista):
	print("Indice: ", indice, " valor: ", valor)

print("\n")
print("\n")
######################### Break y continue ###########################

titulo = "Curso de Python 3"

# La palabra break rome el ciclo, todo lo demás ya no se ejecuta
for caracter in titulo:
	if caracter == "P":
		break
	print(caracter)

# Continue salta una iteración
# Cuando caracter == "P" no se ejecuta lo demás y salta a la siguiente iteración
for caracter in titulo:
	if caracter == "P":
		continue
	print(caracter)

######################### Asignación de valores mediante if ###########################

calificacion = 10 #input
color = None
if calificacion >= 7:
	color = 'verde'
else:
	color = 'rojo'

print(calificacion, color)

# Otra forma más eficiente de ejecutar el código anterior es la siguiente
color = 'rojo'
if calificacion >= 7:
	color = 'verde'
print(calificacion, color)

# Una forma aún más eficiente es la siguiente
color = 'verde' if calificacion >= 7 else 'rojo'
print(calificacion, color)
