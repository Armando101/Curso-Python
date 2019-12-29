"""

La programación orientada a objetos es un paradigma de programación.
Las entidades son conocidas como objetos
Cada objeto tiene ciertas características particulares que los diferencias de otro objetos

Un objeto es una entidad que poseé características que lo hacen diferentes de otro objeto, los objetos pueden realizar ciertas acciones.

Las características son conocidas como atributos
Las acciones que realiza un objeto son conocidas como métodos

Una clase es una plantilla con la que se pueden hacer objetos

En python todo es un objeto, los númeero, flotantes, booleanos, listas, tuplas, etc.

Un objeto es la instancia de una clase
"""


#################### Crear clases ######################

# Se declaran con la palabra reservada class y se utiliza upper camel case
class Usuario:
	pass

# Una vez creada la clase podemos crear N cantidad de objetos
armando = Usuario()

# Podemos ver que el objeto es de tipo Usuario
print(type(armando))


#################### Métodos ######################

# Un objeto puede realizar ciertas acciones, estas acciones se realizan con métodos
# Un método es una función que se encuentra dentro de la clase
# Todos los métodos reciben un parámetro, por convención es self
# self hace referencia al objeto
# Los métodos pueden recibir otros parámetros

class Usuario:
	def saluda(self, nombre):
		print("Hola, soy un usuario ", nombre)

armando = Usuario()
armando.saluda("Armando")

#################### Atributos ######################

# Podemos crear atributos fuera y dentro de la clase
class Usuario:
	def saluda(self, nombre):
		print("Hola, soy un usuario ", nombre)

	def mostrar_username(self):
		print(self.username)

	# Con un método creo un atributo
	def crear_nombre(self, nombre):
		self.nombre = nombre

	# Con un método imprimo el nombre
	def mostrar_nombre(self):
		print(self.nombre)

# Creo un objeto de tipo Usuario
armando = Usuario()

# Creo atributos del objeto fuera de la clase
armando.username = "Armando101"
armando.correo='rivera.armando@gmail.com'

# Mando llamar las funciones que permiten crear atributos dentro de la clase
armando.crear_nombre("Armando")
armando.mostrar_nombre()

armando.mostrar_username()

# Es buena práctica definir un método __init__() para declar los atributos
# De esta manera nos evitamos las asignaciones fuera de la clase

class Usuario:

	def __init__(self, username="", correo="", nombre=""):
		self.username = username
		self.correo = correo
		self.nombre = nombre

	def saluda(self):
		return "Hola, soy un usuario y mi nombre es " + self.nombre

	def mostrar_username(self):
		print(self.username)

	def mostrar_nombre(self):
		print(self.nombre)

armando = Usuario("Armando101", "rivera.armando@gmail.com", "Armando")

resultado = armando.saluda()
armando.mostrar_username()
print(resultado)


#################### Tipos de Atributos ######################

# Podemos tener dos tipos de variables
# Variables de instancia y de clase
# El valor de una variable de instancia pertenecen a su respectivo objeto
# Si modificamos una variable de instancia no se modifica en todos los objetos sino solo sobre el cual estamos instanciando

# Las varibles de clase le pertenecen a la clase, no a una instancia
class Circulo:
	pi = 3.14159265 # Variable de clase
	def __init__(self, radio):
		self.radio = radio    # Variable de instancia

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio=100

print(circulo_a.radio)
print(circulo_b.radio)

print(circulo_a.pi)
print(circulo_b.pi)

# Las variable de clase se pueden obtener sin instanciar un objeto
print(Circulo.pi)

#################### Métodos estáticos ######################

# Los métodos estáticos pueden ser utilizados sin necesidad de instanciar una clase
# Para declarar un método de estático primero colocamos un decorador
# Al ser un método estático y no pertenece a ninguna instancia no necesitams self
# Al utilizar métodos estáticos no podemos usar variables de instancia pero sí variables de clase

class Triangulo:
	numero = 2    # Variable de clase
	# Método estático
	@staticmethod
	def area(base, altura):
		return (base * altura) / Triangulo.numero   # Puedo utilizar variables de clase

# Si necesito calcular el área de N triangulo no necesito instanciar N triangulos
# Solo ejecuto el método estático N veces

resultado = Triangulo.area(10, 20)
print(resultado)

#################### Métodos de calse ######################

# Los métodos de clase son similares a los métodos estáticos
# Son llamados sin la necesidad de instanciar un objeto
# Los métodos de clase son decorados y por convención reciben un parámetro llamado cls
# cls hace referencia a la clase
# Utilizamos métodos de clase cuando necesitemos usar variables de clase

class Circulo:
	pi = 3.14159265

	@classmethod
	def area(cls, radio):
		return cls.pi * radio**2

resultado = Circulo.area(10)
print(resultado)


############################# Herencia ################################

# La Herencia nos permite crear clases a partir de clases ya existentes pero con ciertos cambios
# La Herencia sirve para reutilizr código

class Animal:
	def comer(self):
		print("Comiendo")

	def dormir(self):
		print("Durmiendo")

# Si queremos que la calse Perro tenga el método comer y dormir podemos copiar esos métodos de la clase animal y pegarlos en Perro, evidentemente esta no es una solución eficiente
# Es por eso que recurrimos a la herencia
# Hacemos que Perro herede de Animal, esto lo hacemos pasando el nombre de la clase entre paréntesis

class Perro(Animal):
	def __init__(self, nombre):
		self.nombre = nombre

	def ladrar(self):
		print("Ladrando")

	def comun(self):
		print("Este es un método de Animal")

firulais = Perro("Firulais")

# Al instanciar un objeto de tipo Perro también puedo ocupar métodos de la clase Animal ya que Perro hereda de ésta
firulais.ladrar()
firulais.comer()
firulais.dormir()

# Una clase padre puede ser padre de varias clases
class Gato(Animal):
	def __init__(self, nombre):
		self.nombre = nombre

	def ronronear(self):
		print("ronroneando")

bongo = Gato("Bongo")

bongo.ronronear()
bongo.comer()
bongo.dormir()

############################# Herencia múltiple ################################

# Python es uno de los pocos lenguajes de programación que permiten la herencia múltiple

class Mascota:
	def fecha_adopcion(self, fecha):
		self.fecha_de_adopcion=fecha

	def comun(self):
		print("Este es un método de Mascota")

# Si quiero que mi clase Perro herede tanto de Mascota como de Animal agrego las dos clases
class Perro(Animal, Mascota):
	def __init__(self, nombre):
		self.nombre = nombre

	def ladrar(self):
		print("Ladrando")

	def comun(self):
		print("Este es un método de Perro")

firulais = Perro("Firulais")

firulais.fecha_adopcion("Hoy")
print(firulais.fecha_de_adopcion)

# Es muy importante el orden de las clases
# Las clases padre siempre van antes que las hijas

# Si dos clases Padre tiene un método en común que hacen cosas distintas toma el método de la clase principal, después busca de izquierda a derecha en las clases Padre como fueron asignadas

firulais.comun()

############################# Sobre escritura de métodos ##########################

# Quiero modificar el método dormir
# Simplemente modifico el método dentro de la clase
# Busca el método dormir en la calse principal, si no lo encuentra busca en las clases padre y si tampoco lo encuentra  marca un error

class Perro(Animal, Mascota):
	def __init__(self, nombre):
		self.nombre = nombre

	def ladrar(self):
		print("Ladrando")

	def comun(self):
		print("Este es un método de Perro")

	def dormir(self):
		print(self.nombre, " está durmiendo")
		Animal.dormir(self)	# Mando llamar el método de la calse Padre
		print("No molestar")	# Puedo añadir más funcionalidades

firulais = Perro("Firulais")
firulais.dormir()

############################# Clase Object ##########################

# Todas las clases que declaremos heredan de la clase object
# Los métdos de la clase object tienen doble guión bajo al inicio y final de sus métdos

class Gato:
	def __init__(self, nombre):
		self.nombre = nombre

	def __str__(self):
		return self.nombre

class Pato(object):
	def __init__(self, nombre):
		self.nombre = nombre

	def __str__(self):
		return self.nombre

gato = Gato("Bigotes")
pato = Pato("Lucas")

# Visualizamos el nombre de los objetos ya que reescribimos el método __str_
# Si no sobreescribimos el método __str__ se muestra la dirección de memoria de los objetos
print(gato)
print(pato)

# El atributo dict nos permite conocer los atributos de nuestro objeto
gato.edad = 6

print(gato.__dict__)
print(pato.__dict__)