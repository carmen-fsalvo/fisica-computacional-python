# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 13:27:26 2025

@author: physicist

Código que realiza la integral definida de una función traviesa y 
la de una parábola como comparación utilizando el Método de MonteCarlo.
"""
# Llamada a librerías y funciones externas
from math import sin
from random import random

def f(x): # Parábola
    return x*x

def g(x): # Función traviesa
    return sin(1/(x*(2-x)))*sin(1/(x*(2-x)))

AreaTotalf = 8   # Area total del rectángulo límite x = 2 e y = x*x
AreaTotalg = 2   # Función traviesa
Af = AreaTotalf             # Área total del intervalo o tablero de "f"
Ag = AreaTotalg             # Área total del intervalo o tablero de "g"
fmax = 4
gmax = 1
NT = 1000                   # Número total de dardos
NC = 0                      # Inicialización de los dardos bajo la curva

for i in range(NT):
    x = random()            # Se escoge un número del 0 al 1
    x = 2 * x               # Ese número es ahora del 0 al 2
    y = random()            # Se escoge un número del 0 al 1
    y = fmax * y            # Ese número es ahora del 0 al 4: f(2) = 4
    if y < f(x):            # Se compara un número con f(x)
        NC += 1             # Si es menor, se suma al contador NC
If = Af * (NC/NT)           # Se multiplica por el área y esa es la integral
print("I(f) Analítica: ", 2.6706, "I(f) Monte Carlo: ", If)  # Se imprime la integral

NC = 0
for i in range(NT):
    x = random()            # Se escoge un número del 0 al 1
    x = 2 * x               # Ese número es ahora del 0 al 2
    y = random()            # Se escoge un número del 0 al 1
    y = gmax * y            # Ese número es ahora del 0 al 1
    if y < g(x):            # Se compara un número con g(x)
        NC += 1             # Si es menor, se suma al contador NC
Ig = Ag * (NC/NT)           # Se multiplica por el área y esa es la integral
print("I(g) Analítica: ", 1.4514, "I(g) Monte Carlo: ", Ig)    # Se imprime la integral