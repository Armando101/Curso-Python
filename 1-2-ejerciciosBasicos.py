# Ejercicios conceptos básicos Python

"""
Los siguientes, son una serie de ejercicios que tienen como finalidad el que tu practiques los conocimientos adquiridos a lo largo de este segundo bloque.

"""

# Ejercicio 1: Dado de los valores ingresados por el usuario (base, altura) calcular y mostrar en pantalla el área de un triángulo.

base = float(input("Ingrese la base de un triangulo\n"))

altura = float(input("Ingrese la altura de un triangulo\n"))

area = base*altura
print("El area del triangulo es: ", area)

print()
# Convertir la cantidad de dólares ingresados por un usuario a pesos colombianos y mostrar el resultado en pantalla.

dolar_pesoColombiano = 3298

dolares = float(input("Ingrese una cantidad en dolares\n"))

pesos_colombianos = dolar_pesoColombiano*dolares

print(dolares, " dolares son: ", pesos_colombianos, " pesos colombianos")

print()
# Convertir los grados centígrados ingresados por un usuario a grados Fahrenheit y mostrar el resultado en pantalla


centigrados = float(input("Ingrese una cantidad de grados centigrados "))

fahrenheit = centigrados*(9/5) + 32
print(centigrados, " grados centigrados son: ", fahrenheit, " grados farenheit")


print()
# Mostrar en pantalla la cantidad de segundos que tiene un lustro.

segundos_hora = 3600

print("Un lustro tiene ", segundos_hora*24*30*12*5, " segundos")

print()
# Calcular la cantidad de segundos que le toma a la luz viajar del sol a Marte y mostrar el resultado en pantalla.

distancia_sol_marte = 227940000000
velocidad_luz = 3e8
tiempo_sol_marte = distancia_sol_marte/velocidad_luz

print("La luz tarda ", tiempo_sol_marte, " segundos en viajar del sol a marte")

print()
# Calcular el número de vueltas que da una llanta en 1 km, dado que el diámetro de la llanta es de 50 cm, mostrar el resultado en pantalla.

distancia = 1000
diametro = 0.5

numero_vueltas = distancia/diametro
print("Una llanta da ", numero_vueltas, " vueltas en ", distancia, " metros")

print()
# Mostrar en pantalla True o False si la edad ingresada por dos usuarios es la misma.

edad1 = int(input("Ingrese la edad del primer usuario "))

edad2 = int(input("Ingrese la edad del segundo usuario "))

print(edad1 == edad2)

print()
# Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.

from datetime import date
from datetime import datetime

# Dia actual
today=date.today()

# Fecha actual
now = datetime.now()

month = int(input("En qué número de mes naciste? "))
year = int(input("¿En qué año naciste? "))

meses_transcurridos = (today.year-year)*12+today.month-month

print("Han pasado ", meses_transcurridos, " meses desde que naciste")