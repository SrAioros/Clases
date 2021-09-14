# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:26:12 2021

@author: Administrador
"""

# Tipos de Colecciones
"""
LISTAS O VECTORES
Son tipos de datos mutable y ordenado

"""

a = []  # Array vacío
a = [2, 3, 4]
b = [2, True, 'Hola', 3.4]
c = [2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6]]

for valor in a:
    print(valor)
    
for valor in b:
    print(valor)
    
for valor in c:
    print(valor)
    
a[0] = 7
print(b[2])
print(c[2][1])
print(c[3][1][1])

a.append(5)  # Agrega el elemento al final de la lista
a.remove(3)  # Elimina el elemento que coincida con el valor
a.pop()      # Elimina el último elemento del vector
a.pop(2)     # Elimina un elemento por posición
a.clear()    # Elimina todos los elementos del vector
# del a        Elimina el objeto

4 in a  # Busca el elemento 4 dentro de a
len(a)  # Cantidad de elmentos del vector
a = b   # Asignación de b en el mimso espacio de memoria de a
id(a)   # Convierte el decimal la dirección en memoria de un objeto
a = b.copy()    #  Copia los elementos de b en a 
b = a[:]
b = a[0:3]  # Copia los primeros 3 elementos de a
b = a[:6]   # Copia los elementos de la pocisión 0 hasta la pocisión 5
b = a[2:]   # Copia los elementos desde la posición 2 hasta el final del vector


"""
TUPLAS
Son un tipo de datos INMUTABLE y ordenado

"""

a = (1, 2, 3, 4)
a = ()  # Tupla vacía
print(a[1])
a = (2, 3, 4)
b = (2, True, 'Hola', 3.4)
c = (2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6])
4 in a

"""
SET
Mutable pero no ordenado
Un set no permite arrays en su interior

"""

a = {1, 2, 3, 4, 5, 4 , 2, 1, 9, 7}
a = set()  # set vacío

"""
DICCIONARIO
Mutable pero no ordenado

"""

a = {'nombre': 'Daniel', 'apellido': 'Vega'}
a = {1: 'Daniel', 2: 'Vega'}
a = {}  # Diccionario vacío

a['nombre']

for valor in a:
    print(valor)

for valor in a.values():
    print(valor)
    
for valor in a.keys():
    print(valor)

for valor in a.items():
    print(valor)

for llave, valor in a.items():
    print(f'Llave: {llave}, Valor:{valor}')
    
"""
FUNCIONES

"""

def nombre_funciion():
    pass

def saludar():
    print('Hola Mundo')


def saludar(nombre):
    print(f'Hola {nombre}')
# Python no permite la sobrecarga de métodos

# Parámetros Opcionales

def saludar(nombre = 'Mundo'):
    print(f'Hola {nombre}')


def saludar(nombre, apellido = ""):
    print(f'Hola {nombre} {apellido}')


def saludar(nombre = "", apellido = ""):
    print(f'Hola {nombre} {apellido}')

# Python no deja tener un parámetro  obligatorio después de un parámetro opcional

#def saludar(nombre, apellido="", segundo_apellido):
#    print(f'Hola {nombre} {apellido} {segundo_apellido}')


# Parámetros ilimitados
# Imprime tuplas
def saludar(*nombres):
    print(f'Hola {nombres}')

def saludar(*nombres):
    for nombre in nombres:
        print(f'Hola {nombre}')


def saludar(*nombres, apellido=""):
    for nombre in nombres:
        print(f'Hola {nombre}')
    print(f'Apellido {apellido}')


def saludar(*nombres, apellido):
    for nombre in nombres:
        print(f'Hola {nombre}')
    print(f'Apellido {apellido}')


# Espera un keyword o un diccionario como parámetro
def saludar (**nombres):        #saludar(nombre1='Daniel', nombre2='Esteban')
    print(nombres)              # Espera un llave : valor


# Se puede jugar con los parámetros

def resta(a, b):
    print(a - b)

# En consola:
# resta(3, 4) | resultado -1
# resta(4, 3) | resultado 1
# resta(b=4, a=3) | resultado -1

def operaciones(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    return suma, resta, mult, div

resultados = operaciones(4, 5)

suma, res, mul, div = operaciones(4, 5)

suma, _, _, div = operaciones(4, 5)








