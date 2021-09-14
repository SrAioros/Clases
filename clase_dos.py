# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:22:46 2021

@author: Administrador
"""

#Condicionales

# Tabla de verdad

#Tabla del "AND"

# v and v = v
# v and f = f
# f and v = f
# f and f = f

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# Tabla del OR

# v or v = v
# v or f = v
# f or v = v
# f or f = f


print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# Negación

print(not True)  # False
print(not False)  #True


# Más de dos condiciones al mismo tiempo

print(True and False and True or False or True or True)  # True
print(True and (False and True) or False or (True or True))  #True

# Jerarquía de operaciones
# 1. Paréntesis y llaves
# 2. Potencias y Raices
# 3. Multiplicación y División
# 4. sumas y Restas

# Jerarquía de operaciones booleanas
# 1. Paréntesis y llaves
# 2. Tabla de verdad

# Estructura if

x = 1
if(x > 0):
    print('1')
else:
    print('2')

#HUA que dada la edad de una persona indique si es mayor o menor de edad

edad = int(input('Digite edad: '))

if(edad >= 18):
    print('Es mayor de edad')
else:
    print('Es menor de edad')
    
# HUA que indique si un estudiante aprobó o reprobó una asignatura
# teniendo en cuenta que aprueba con mínimo una calificación de 3.0 hasta 5.0

nota = float(input('Digite nota final: '))
if (nota >= 3.0 and nota <= 5.0):
    print('Aprobó')
elif(nota < 3.0 and nota > 0):
    print('Reprobó')
else:
    print('La nota ingresada no es válida')

# HUA que dado un número n diga si es negativo, positivo o cero

n = float(input('Digite un número: '))
if (n > 0):
    print('{n} es un número positivo')
elif(n < 0):
    print('{n} es un número negativo')
else:
    print('Es cero')
    

# Ciclos

# Ciclos for
# Range

for valor in range(11):
    print(valor)


for valor in range(1, 11):
    print(valor)

for valor in range(2, 11, 2):
    print(valor)

for valor in range(11):
    print(valor)
    print(valor + 1)

for valor in range(11):
    print(valor)
print(valor + 1)

# HUA que de las n notas de un estudiante y calcule el promedio
# académico final

num_notas = int(input('Digite el número de notas a promediar: '))
if (num_notas >= 0):
    acumulador = 0
    
    for x in range(num_notas):
        nota = float(input(f'Digita la nota { x + 1}:'))
        acumulador = acumulador + nota
    promedio = acumulador / num_notas
    promedio = round(promedio, 2)
    print(f'el promedio final es: {promedio}')
else:
    print('El número de notas no puede ser menor o igual a cero')








