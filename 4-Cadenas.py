########### Cadenas de caracteres #################333

# Declaración de una cadena
curso = "Curso de python 3"

# Longitud de una cadena
resultado = len(curso)
print(resultado)

# Obtener una letra de la cadena
resultado = curso[0]
print(resultado)

resultado = curso[4]
print(resultado)

resultado = curso[-2]
print(resultado)

# Si colocamos un índece que no existe obtenemos un error
#resultado = curso[100]

# Podemos obtener sub-strings
resultado = curso[1:16:2]
print(resultado)

# Al igual que las tuplas, las string son inmutables
# La siguiente línea marca un error
#curso[0] = "E"

############## Trabajo de strings como listas ##########

lenguajes = "python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

# El método split retorna una nueva lista a partir de una string
# El método separa la cadena mediante un caracter que pasamos como parámetro

resultado = lenguajes.split()
print(resultado)

resultado = lenguajes.split("; ")
print(resultado)

# Es fuena práctica evitar el "hardcodeo"
separador="; "
resultado = lenguajes.split(separador)
print(resultado)

# Con el método join podemos generar una string a partir de una lista
# En este punto resultado es una lista
# El método join regresa un string
# Los elementos de la lista se separan por la string que le paso

nuevo_string = " ".join(resultado)
print(nuevo_string)

# Puedo definir como separador un guión bajo
nuevo_string = "_".join(resultado)
print(nuevo_string)

# Para regresar a la lista original hacemos lo siguiente
nuevo_string = separador.join(resultado)
print(nuevo_string)
print(lenguajes)

# Una cadena con múltiples líneas
texto = """ Este es un texto
con saltos
de
linea"""

# Convertir la cadena en una lista
resultado = texto.splitlines()
print(resultado)
print("\n")
print("\n")

######################################### Formato para cadenas ############
texto = "curso de Python3"

# Convertir la primera letra de la cadena en mayúscula
resultado = texto.capitalize()
print(resultado)

# Convertir mayúsculas a minúsculas y minúsculas a mayúsculas
resultado = texto.swapcase()
print(resultado)

# Convertir todas las letras a mayúsculas
resultado = texto.upper()
print(resultado)

# Convertir todas las letras a minúsculas
resultado = texto.lower()
print(resultado)

# Saber si nuestra string está en minúsculas o mayúsculas
print(resultado.isupper())
print(resultado.islower())

# Convertir a formato de título
resultado = texto.title()
print(resultado)

# Remplaza una string por otra
# Requiere dos parámetros
# El primero es el valor a reemplazar
# El segundo valor será por el cual será reemplazado
resultado = texto.replace("Python3", "Ruby")
print(resultado)

# Indicar cuántas veces queremos que se reemplaze en dado caso de que haya más de una coincidencia
# Indicamos como tercer parámetro el número
texto = "curso de Python3, Python3 Básico"
resultado = texto.replace("Python3", "Ruby", 1)
print(resultado)

# El método strip retorna una string sin los espacios que pudieran ser colocandos al inicio o final de la cadena
texto = "		curso de Python3, Python3 Básico         "
resultado=texto.strip()
print(resultado)

# Usar una cadena con formato usando variables
curso = "Python"
version = "3"

# Colocar la string seguido de un porcentaje y parentésis
resultado = "Curso de %s %s" %(curso, version)
print(resultado)

# También es posible con format
resultado = "Curso de {} {}".format(curso, version)
print(resultado)

# Otra forma es darle valores a los paréntesis
resultado = "Curso de {a} {b}".format(b=version, a=curso)
print(resultado)

################################## Concatenación ####################
curso = "Curso de Python"

# No podemos modificar una string pero podemos usar la concatenación
# Generamos una nueva cadena concatenando lo que queremos modificar
curso = "c" + curso[1:]
print(curso)

curso = "c" + curso[1:] + " " + "en PROTECO"
print(curso)

# No es posible concatenar una string con un entero
#curso = "c" + curso[1:] + 3 + " " + "en PROTECO"

# Pero es posible hacer un casteo de entero a string
curso = "c" + curso[1:] + str(3) + " " + "en PROTECO"

# Podemos colocar un valor flotante, booleano y entero

################################## Búsqueda ####################

mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"

# Con el método count vemos cuantas veces se repite una cadena en el texto
resultado = mensaje.count("e")
print(resultado)

# Para saber si una subcadena está en la string usamos in
resultado = "texto" in mensaje
print(resultado)

# El método find nos devuelve un valor entero
# Dicho valor hace referencia a la primera posición en la cadena donde aparece la primera letra
palabra_buscar="texto"
resultado = mensaje.find(palabra_buscar)
print(resultado)

# Comprobemos el métodofind
resultado = mensaje[resultado: resultado + len(palabra_buscar)]
print(resultado)

# Si el texto no se encuentra el método find devuelve un -1

# Saber si una cadena empieza con cierta subcadena
primera_palabra = "Este"
resultado = mensaje.startswith(primera_palabra)
print(resultado)


primera_palabra = "este"
resultado = mensaje.startswith(primera_palabra)
print(resultado)

# Saber si una cadena termina con cierta subcadena
ultima_palabra ="e"
resultado = mensaje.endswith(ultima_palabra)
print(resultado)


ultima_palabra ="E"
resultado = mensaje.endswith(ultima_palabra)
print(resultado)
