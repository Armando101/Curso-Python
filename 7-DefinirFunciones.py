################## Definir funciones #################

"""

Las funciones se encargan de contener el código necesario para hacer algo en específico

"""

# Definición de una función
# Se definen con la palabra reservada def
# Podemos usar funciones dentro de una función
# print es una función
def saludar():
	print("Hola Mundo!")

# Llamar una función
# Colocamos el nombre de la función seguido de paréntesis
saludar()

################ Múltiples valores de entrada y salida ####################

# A los datos de entrada se les conoce como parámetros
# Los parámetros se colocan dentro de los paréntesis
# Los valores de salida se regresan con la palabra return
def crear_mensaje(nombre):
	return "Hola {}, bienvenido al curso de python 3".format(nombre) 

# Los valores que se pasan a la función se les nombra argumentos
# nombre es un parámetro, "Armando" es un argumento
nuevo_mensaje = crear_mensaje("Armando")
print(nuevo_mensaje)


# Podemos definir funciones que reciban N parámetros
def suma(val1, val2, val3):
	return val1 + val2 + val3

resultado = suma(10, 20, 30)
print(resultado)

# Podemos definir funciones que retornen N valores
def obtener_curso():
	return "Curso de Python", "Básico", 3.6

curso, nivel, version = obtener_curso()
print(curso, nivel, version)

################ Recibir N cantidad de parámetros ####################

def crear_usuario(nombre, apellido, edad):
	return {
		'nombre':nombre,
		'apellido':apellido,
		'nombre_completo':"{} {}".format(nombre, apellido),
		'edad':edad
	}

armando = crear_usuario("Armando", "Rivera", 22)

print(armando["nombre"])
print(armando["apellido"])
print(armando["edad"])

# Podemos colocar un valor por default
# def crear_usuario(nombre, apellido, edad=0):
# De esta manera si omitimos ese argumento no marcará error
# También se puede hacer la asignación de argumentos en desorden de la siguiente manera
# armando = crear_usuario(edad = 22, apellido = "Rivera", nombre = "Armando")
 
################ Args keyword ###############################

# Si no sabemos cuántos parámetros tendrá la función lo hacemos de la siguente manera
# args representa una tupla con todos los argumentos que le estamos pasando a la función
def suma(parametro_requerido, *args):
	total = 0
	print(parametro_requerido)
#	print(args)    # Aquí vemos que es una tupla
	for valor in args:
		total += valor
	return total

resultado = suma("Este es un argumento requerido ",10, 20, 30, 40, 50, 60, 70)
print(resultado)

# kwargs agrupa los parámetros y valores en un diccionario
def usuarios_autenticados(**kwargs):
	print(kwargs)

usuarios_autenticados(nombre = "Armando", apellido ="Rivera")

def combinacion(requerido, *args, **kwargs):
	print(requerido)
	print(args)
	print(kwargs)

combinacion("Valor rquerido", 10, 20, 30, 40, 50, nombre = "Armando", apellido = "Rivera")

################ Formas de terminar una función ###############################

# Una función termina cuando la última línea que se encuentra en la función sea ejecutada

def mi_funcion():
	print("Un mensaje")
# Si no especifico un valor de retorno por defecto regresa None

resultado = mi_funcion()
print(resultado)

# Una función con un valor de retorno termina cuando se encuentra con la palabra reservada return

def mi_funcion(parametro):
	if parametro:
		return 100
	print("Esta mensaje se muestra si el parametro es falso")

resultado = mi_funcion("a")
print(resultado)

################ Alcance global ###############################

# Todas las variables declaradas fuera de funciones se les conoce como variables globales
animal = 'León'

# Las variables globales se pueden utilizar dentro de funciones
def mostrar_animal():
	print(animal)

mostrar_animal()
print(animal)

# Si modificamos un valor dentro de una función, ésta solo se modificará dentro de la función, fuera de ésta el valor no es modificado
def mostrar_animal():
	animal = 'Ballena'
	print(animal)

mostrar_animal()	# Imprime Ballena
print(animal)		# Imprime Leon

# Si queremos modificar la variable global dentro de la función la declaramos como variable global de la siguiente manera
def mostrar_animal():
	global animal 
	animal = 'Ballena'
	print(animal)

mostrar_animal()	# Imprime Ballena
print(animal)		# Imprime Ballena

print("\n")
print("\n")
################ Expresiones Lambda ###############################

# Declaro una función que convierte grados centigrados a farenheit
def centigrados_a_farenheit(grados):
	return grados * 1.8 + 32

# Puedo asignar una función a una variable
# La variable funcion_variable ahora es la función centigrados_a_farenheit
funcion_variable = centigrados_a_farenheit
resultado = funcion_variable(32)
print(resultado)

# Las funciones Lambda son también conocidas como funciones anónimas
# Estas funciones son expresadas en una línea de código ya que realizan tareas muy pequeñas

# Se coloca la palabra reservada lambda seguida de los parámetros, si tenemos más de uno se separan por comas, si hay valores por defecto se asignan, después colocamos dos puntos : y el valore de retorno
# Las funciones lambda no tienen la palabra reservada return ya que todas regresan algo
mi_funcion = lambda grados=0 : grados * 1.8 + 32
resultado = mi_funcion(32)
print(resultado)

"""

Ejemplos de lambdas

sin_parametros = lambda : True

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

con_asterisco = lambda *args : args[0]

con_doble_asterisco = lambda **kwargs : kwargs[0]

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)

"""

################ Función map ###############################

#En Python, la función map nos permite aplicar una función sobre los items de un objeto iterable (lista, tupla, etc...).

#Sintaxis:		map(function, objeto iterable)

# La función retornará un objeto map que posteriormente podemos convertir a una lista o tupla.

def cuadrado(numero):
 return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)

lista_resultado = list(resultado)
print(lista_resultado)

# Es posible utilizar map junto con una función lambda. En lo personal considero esta la mejor opción.

lista = [1,2,3,4,5]
resultado = map(lambda numero: numero * numero , lista)

lista_resultado = list(resultado)
print(lista_resultado)

################ Funciones anidadas ###############################

# No puedo modificar un valor que está fuera de una función anidada, para hacerlo tengo que usar la palabra reservada nonlocal

def comenzar_play_list(lista):
	# Función anidada
	def reproducir():
		nonlocal lista
		lista = [1, 2, 3]
		for val in lista:
			print(val)
	reproducir()
	print(lista)

# La función reproducir sólo puede ser Llamada dentro de la función donde se encuentra
lista = ['track 1', 'track 2', 'track 3', 'track 4']
comenzar_play_list(lista)

################ Closures ###############################

# Un Closure es una función que genere dinámicamente otra función y que esta nueva función pueda acceder a las variables locales aún cuando la primera función haya finalizado

def mostrar_mensaje(mensaje):
	mensaje = mensaje.title()  # variable local

	def mostrar():
		print(mensaje)

	return mostrar


nueva_funcion = mostrar_mensaje("Hola Mundo!")
nueva_funcion()

############################# Decoradores ###############################

# Los decoradores permiten extender las funciones

def decorador(funcion):
	def nueva_funcion():
		print("Podemos agregar código antes")
		funcion()
		print("Podemos agregar código después")
	return nueva_funcion

@decorador
def funcion_a_decorar():
	print("Este es una función a decorar")

funcion_a_decorar()

############################# Generadores ###############################

# Un generador es un tipo especial de función que podemos usar para la creación de una secuencia de datos
# La palabra yield es simalar a return con la diferencia que yield no hace terminar la función
# yield regresa un objeto de tipo generador que puede ser transformado a una lista
def tabla_multiplicar(numero=1, maximo=10):
	for posicion in range(1,maximo+1):
		yield numero * posicion

for resultado in tabla_multiplicar(9):
	print(resultado)

resultado = tabla_multiplicar(9)
resultado = list(resultado)
print(resultado)


# También es posible regresar más de un valor con yield, estos valores son almacenados en una tupla
def tabla_multiplicar(numero=1, maximo=10):
	for posicion in range(1,maximo+1):
		yield numero * posicion, numero, posicion

for resultado, numero, posicion in tabla_multiplicar(9):
	print(numero, "*", posicion, "=", resultado)


############################# Documentación de las funciones  ######################

"""

Cómo mencionamos anteriormente, una vez que nosotros definimos una función, podemos llamarla n cantidad de veces, inclusive, fuera de nuestro script, cómo lo veremos más adelante (módulos y paquetes) es por ello que una muy buena practica de programación es documentar nuestras funciones.

Para que nosotros podamos documentar una función lo haremos mediante un comentario, el cual debe de encontrarse dentro de la función y utilizando triples comillas dobles, cómo podemos observar en el siguiente ejemplo.

"""

def mi_funcion(*args):
  """Esta es la documentación de mi_función"""
  print(args)

# Podemos trabajar con la documentación a través de su atributo __doc__
print(mi_funcion.__doc__)

# Ahora veamos un ejemplo en el cual podemos sacar provecho a nuestra documentación. 

def suma(a, b):
  """Función suma"""
  return a + b

def resta(a, b):
  """Función resta"""
  return a - b

opciones = {'a' : suma, 'b': resta}
print("Ingrese la opción deseada")

for opcion, funcion in opciones.items():
  mensaje = '{}) {}'.format(opcion, funcion.__doc__)
  print(mensaje)

opcion = input("Opción : ")
# Almacenamos las funciones dentro de nuestro diccionario, posteriormente iteramos los elementos del diccionario y en cada iteración imprimimos la documentación.