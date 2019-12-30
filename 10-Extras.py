
################# Guía de codificación Python #############

"""
Es de suma importancia que nosotros tengamos una forma estandarizada de codificación y siempre nos concentremos en codificar de la misma manera, recordemos que muy probablemente a nuestros proyectos les tengamos que dar mantenimiento o tengamos que incorporar más desarrolladores al mismo, en cualquier caso, codificar bajo un estándar nos permitirá crear proyectos de más alta calidad.

En Python existe los PEP's, Mejoras de propuestas de Python, de los cuales al momento de codificar nos interesa PEP8.

PEP8 Es una guía de codificación, la cual nos permite escribir código Python de una manera, mucho más legible y de forma consistente, a través de ciertas "reglas" y recomendaciones. Por ejemplo, en la guía podemos encontrar:

    utilizar espacios sobre tabs.
    utilizar la nomenclatura de snake case para nombrar variables.
    utilizar palabras en mayúsculas para las constantes.

    Colocó "reglas" entre comillas ya que nosotros podemos crear un programa cien por ciento funcional sin habernos guiado de PEP8, simplemente siendo constantes al momento de codificar.

Si por algún motivo creemos que nuestra forma de codificar Python es errónea o queremos implementar al pie de la letra la guía, podemos validar nuestro código en la siguiente página web  http://pep8online.com/, basta con copiar el código del cual tenemos duda y validar.

    Si quieres crear una librería, te recomiendo validar todo tu código.

PEP8: https://www.python.org/dev/peps/pep-0008/

"""

################# Anotaciones ##################################

# Las anotaciones son únicamente informativas
# Se coloca después de los dos puntos el tipo de dato recibido
# Se coloca con una flecha el valor de retorno
# Las anotaciones sirven como guía

def saludo(nombre: str) -> None:
	print("Hola " + nombre)

nombre = "Armando"
saludo(nombre)

# También podemos incluir valores por defecto
def suma(num1 : int, num2 : int = 100) -> int:
	return num1 + num2


print(suma(10, 20))

#################################### Comprenhension ##################################

"""
lista = []

for x in range(0, 101):
	lista.append(x)

print(lista)
"""

# Podemos hacer el código anterior más simple usando Comprenhension
# La sintaxis es:
# Colocamos la variable y corchetes para listas, paréntesis para tuplas o llaves para diccionarios
# Después colocamos el valor que queremos almacenar
# Después colocamos el ciclo for

estructura = [ valor_a_almacenar for valor_a_almacenar in range(0, 101) ]
print(estructura)

print()
# Para una tupla usamos la palabra reservada tuple
estructura = tuple( (valor_a_almacenar for valor_a_almacenar in range(0, 101)) )
print(estructura)

print()
# Podemos hacer sentencias más complejas por ejemplo
# Guardar los números pares del 0 al 100
estructura = tuple( (x for x in range(0, 101) if x%2 == 0) )
print(estructura)


print()
# Podemos hacerlo todavía más complejo
# Guardar todos los números pares menores a 50
estructura = [x for x in range(0, 101) if x % 2 == 0 if x < 50]
print(estructura)

# Sin embargo por temas de legibilidad es mejor usar Comprenhension con una o máximo dos condicionales

print()
# Para un diccionario lo hacemos de la siguiente manera
diccionario = {indice: valor for indice, valor in enumerate(estructura)}
print(diccionario)


print()

#################################### Fechas con Python ##################################

"""
Para que nosotros podamos trabajar con fechas utilizando Python haremos uso de la librería datetime. En esta ocasión listaremos un par de ejemplos que pueden ayudarte a comprender de una mejor manera dicha librería.
"""

# Obtener la fecha actual.

#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)


print()
# Atributos

# Una vez obtengamos la fecha actual podremos obtener el día, mes, año, hora, minutos, segundos de esta.

#Date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))


print()
#Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))


print()
#Nueva fecha

# Si nosotros así lo deseamos podemos trabajar con una fecha en particular.

new_date = datetime(2019, 2, 28, 10, 15, 00, 00000)

# Los argumentos serán: Año, Mes, Día, Hora, Minutos, Segundos, Milisegundos.


print()
# Operaciones

# En ocasiones tendremos la necesidad de realizar ciertas operaciones con fechas, ya sea agregar días, restar años o simplemente realizar comparaciones. Con Python todas estas operaciones podremos realizarlas sin ningún problema.

from datetime import datetime
from datetime import timedelta

# Sumar dos días a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

# Comparación
if now < new_date:
    print("La fecha actual es menor que la nueva fecha")



print()
# Formato de fechas

# Aunque las fechas en Python ya poseen un formato legible para los humanos, en ocasiones necesitaremos ser más explícitos para no dejar espacio a la ambiguuedad, para ello, haremos uso del método strftme.

now = datetime.now()
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)

#	%d Día
#	%m Mes
#	%Y Año
#	%H Hora
#	%M Minutos
#	%S segundos

# Algo que en lo particular me gusta hacer es definir una función que me permita obtener un formato mucho más amigable.

from datetime import datetime

def current_date_format(date):
	months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
	day = date.day
	month = months[date.month - 1]
	year = date.year
	messsage = "{} de {} del {}".format(day, month, year)

	return messsage

now = datetime.now()
print(current_date_format(now))

