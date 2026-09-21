# -*- coding: utf-8 -*-
"""
Created on Sun Mar 9 16:49:54 2025

@author: physicist

Programa que genera un paseo aleatorio en una dimensión.
"""
# Llamada a funciones externas
from numpy import zeros
from random import random, seed
from pylab import plot, show, figure, xlim, xlabel, ylabel, title

# Inicialización de variables, tablas y listas
n = 100
x = zeros(n, float)
x2 = zeros(n, float)
x[0] = 0
x2[0] = x[0] * x[0]
paso = 0

seed(10) # Semilla del generador

# Bucle principal para los "n" pasos
for i in range(n-1):
    r = random()            # Se escoge número aleatorio
    if r < 0.5:             # Condición
        paso = 1            # Suma un paso hacia +x
    else:
        paso = -1           # Suma un paso hacia -x
    x[i+1] = x[i] + paso    # Posición después de i+1 pasos
    x2[i+1] = x[i+1]**2     # Cuadrado de la posición anterior
    print(r, " ", paso, " ", x[i+1], " ", x2[i+1])

# Representación de las posiciones al cuadrado en función de los pasos
figure(2)
plot(x2, "ro")
xlim(0)
xlabel("Pasos")
ylabel(r"$x^{2}$")
title('Paseo aleatorio de un caminante en una dimensión')
show()

# Representación de las posiciones en función de los pasos
figure(1)    
plot(x, "o")
xlabel("Pasos")
ylabel(r"$x$")
title('Paseo aleatorio de un caminante en una dimensión')
xlim(0)
show()