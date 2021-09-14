# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:26:12 2021

@author: Administrador
"""

# Tipos de Colecciones
"""
Listas o Vectores
Son tipos de datos mutable y ordenado

"""

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















