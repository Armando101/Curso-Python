"""

Los diccionarios son una estructura de datos que nos permitirá almacenar
valores de todo tipo incluso tuplas, listas o diccionarios.

Los diccionarios son mutables.

No podemos obtener valores almacenados mediante índices
Accedemos a los valores a partir de llaves

diccionario = {"total": 33}

"total" es la llave y 33 es el valor

Podemos usar más de una llave-valor separandolos por comas.
diccionario = {"total":55, "desc":True, "subtotal":15}

"""

############## Cómo funcionan los diccionarios ################

# Declaración
diccionario = {}

# Agregar una llave con su valor
diccionario["nombre"] = "Armando"
print(diccionario)

# Obtener el valor con respecto a una llave
valor = diccionario["nombre"]
print(valor)

# Si usamos una llave que ya existe, ésta se reemplaza con el último valor
# No pueden existir llaves duplicadas
diccionario = {"a":1, "b":2, "c":3, "a":4}
print(diccionario["a"])

############## Obtener elementos de un diccionario ####################

# Si intentamos acceder a un valor cuya llave no existe obtenemos un problema
#valor = diccionario["z"]

# Para saber si una llave existe usamos la palabra in
resultado = "z" in diccionario
print(resultado)

# El método get nos regresa el valor dado una llave
# Si la llave no existe nos regresa none
resultado = diccionario.get("z")
print(resultado)

# El método get puede recibir un segundo parámetro que recibe el valor que se regresa en dado caso que no se encuentre la llave
resultado = diccionario.get("z", "Llave no encontrada")
print(resultado)

# Con el método setdefault puedo asignar un valor a una llave que no existe
# El método setdefault me regresa el valor
resultado = diccionario.setdefault("z", 5)
print(diccionario)
print(resultado)

###################################  Llaves ítems y valores ####################
diccionario = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

# Obtener las llaves de un diccionario
# El método keys nos regresa un objeto de tipo dict_keys con las llaves
resultado = diccionario.keys()
print(resultado)

# Podemos convertir el objeto en una lista o tupla
resultado = list(resultado)
print(resultado)

# Obtener los valores de un diccionario
# El método values nos regresa un objeto de tipo dict_values con los valores
resultado = diccionario.values()
print(resultado)

# Podemos convertir el objeto en una lista o tupla
resultado = list(resultado)
print(resultado)

# El método items nos regresa un objeto de tipo dict_items
# Este objeto contiene las llaves y valores respectivamente en tuplas
resultado = diccionario.items()
print(resultado)

# Podemos convertir el objeto en una lista o tupla
resultado = list(resultado)
print(resultado)

print("\n")
print("\n")
############################ Eliminar elementos ######################

print(diccionario)
print(len(diccionario))

# Eliminar una llave junto con su valor
del diccionario["a"]
print(diccionario)
print(len(diccionario))

# El método pop nos permite eliminar un valor
# El método regresa el valor eliminado
valor_eliminado = diccionario.pop("b")
print(diccionario)
print(len(diccionario))
print(valor_eliminado)

# Para eliminar todo el diccionario podemos sobreescribirlo con un diccionario vacío
#diccionario = {}

# También es posible eliminar los valores del diccionario con el método clear
diccionario.clear()
print(diccionario)








