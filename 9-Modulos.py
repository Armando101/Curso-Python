"""

Un módulo es un archivo que contiene código
Un módulo tiene funciones
Los módulos nos permiten reutilizar código

"""
# Usamos la palabra reservada import seguida del nombre del archivo donde tenemos las funciones
import calculadora

# Ahora podemos usar las funciones que tenemos previamente programadas en el módulo
# Tenemos que especificar el módulo del cual estamos importando las funciones
resultado = calculadora.suma(10, 20)
print(resultado)


############################ Formas de Import ######################

# Otra forma de importar modulos es con la palabra reservada from
# El asterisco hace referencia a que voy a importar todas las funciones
from calculadora import *

# De esta manera ya no es necesario indicar el módulo al cual pertenecen las funciones

resultado = resta(10,20)
print(resultado)

# Podemos especificar solo la función que queremos importar, esto para evitar importar todas las funciones de un módulo siendo que solo vamos a ocupar una o dos

from calculadora import multiplicacion, division

resultado = multiplicacion(10,20)
print(resultado)


# Si queremos usar importar muchas funciones a partir de un módulo podemos indicarlas con saltos de línea

"""
from calculadora import (multiplicacion,
						resta, 
						suma, 
						division)

"""

# También es posible colocar un alias a las funciones

from calculadora import suma as nueva_suma

resultado = nueva_suma(10, 20)
print(resultado)

############################ Documentar módulos en Python ######################

"""

Cuando nos encontremos trabajando con módulos, es una buena práctica de programación que nosotros documentamos estos, más aún, cuando pensamos en liberarlos.

Para documentar un módulo requerimos trabajar con comentarios.

"""

"""
Documentación del módulo.
Esta es una anotación la cual debe de encontrarse
en la parte superior de nuestro script.
Esta anotación tiene cómo objetivo describir el módulo
"""

__author__ = "Rivera Negrete Manuel Armando"
__copyright__ = "Copyright 2019"
__credits__ = ["Armando Rivera", "PROTECO", "BAM"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Team PROTECO"
__email__ = "rivera.armando997@gmail.com"
__status__ = "Production"

def funcion_a():
  """Cómo sabemos podemos documentar una función de esta manera."""
  pass

def funcion_b():
  """Podemos
    colocar
    saltos de línea
  """
  pass

def funcion_c(a=0, b=0):
  """Podemos dar más detalles de los parámetro
    a -- parámetro (default 0)
    b -- parámetro (default 0)
  """
  pass

class MyModulo:
  """Documentación de nuestra clase"""

  def metodo(self):
    """Documentación de nuestro método"""
    pass


"""
El primer comentario es de suma importancia ya que es aquí donde describiremos al módulo, que es lo que hace, que es lo que no hace, cómo funciona, cómo usarlo, entre otras anotaciones que necesitemos colocar, posteriormente podemos colocar algunos metadatos. Los metadatos más comunes son los ocho que podemos observar, sin embargo, si nosotros lo necesitamos podemos agregar los nuestros.

    Para que pueda considerarse un metadato debemos de colocar doble guión bajo al inicio y doble guión bajo al final.

Una vez hayamos documentado el script podemos pasar a documentar puntualmente las funciones y las clases.

"""

# Si requerimos visualizar la documentación de un módulo basta con un utilizar la función help.
#help(calculadora)

# También podemos visualizar la documentación de una función
#help(calculadora.suma)

# Para salir de la documentación basta con presionar q
# De esta forma estaremos documentando nuestros módulos sin requerir utilizar algún software adicional.


#################################### Archivos PYC ####################

"""
Un archivo pyc se genera cuando un módulos es importado por primera vez

También se generan cuando el módulo es modificado

Este archivo es un compilado del módulo, esto significa que cuando volvamos a llamar al módulo, python ya no tendrá que volver a interpretar todo sino que usará éste que ya está compilado

Python es un lenguaje de programación tanto interpretado como compilado y este archivo es la prueba
"""

############################### Atributo __name__ ####################

# dir es una función que me devuelve una lista con los objetos que se encuentran dentro de un módulo

print(dir(calculadora))

# Aparte de las funciones que ya definimos encontramos otras más
# __name__ me devuelve el nombre del módulo
print(calculadora.__name__)

# Si lo ejecutamos en el archivo actual me devuelve __main__ y no el nombre del archivo actual
print(__name__)

# Una forma de saber si un archivo lo estamos ocupando como módulo o como archivo principal es e la siguiente manera

if __name__ == "__main__":
	print("Soy un archivo principal")
else:
	print("Soy un módulo")


############################### Paquetes ############################

"""
Un paqute no es más que un folder/carpeta el cual contiene módulos
Un paqute agrupa módulos
Usamos paqutes cuando trabajamos con proyectos grandes

Para crear un paqute creamos una nueva carpeta y agregamos un archivo __init__.py y por lo menos un módulos
Con este archivo python ya sabe que es un paqute
"""

# Para utilizar el paqute lo hacemos con la siguiente sintaxis
# from PAQUETE.MÓDULO import FUNCIÓN, CLASE, VARIBLE, etc 
from animales.aves import Pinguino

pinguino = Pinguino()

pinguino.nadar()

############################### Archivo __init__ ############################

"""
Este archivo es necesario para que python sepa que se trata de un paqute
Este script se ejecuta cuando el paquete es importado

Si colocamos la siguiente línea ya no será necesario indicar el módulo al momento de imprtar el paquete

from .felinos import Jaguar
"""

from animales import Jaguar, leon, mi_funcion

# Instanciamos un objeto
jaguar = Jaguar()

# Ejecutamos su método
jaguar.cazar()

# Si un objeto ya está instanciado en el archivo init, podemos hacer uso de sus métodos
leon.rugir()

# Podemos ocupar una función que esté en el archivo init
mi_funcion()