# -*- coding: utf-8 -*-
"""
Created on Thu May  8 12:09:52 2025

@author: physicist

Inicialización y visualización de partículas en una caja cuadrada, colocadas de forma ordenada
pero con velocidades iniciales aleatorias. No hay evolución temporal.

"""

from numpy import zeros, sqrt
from random import random
from pylab import scatter, xlim, ylim, title, show, figure

# Parámetros
L = 4                    # Tamaño de la caja (longitud del lado)
N = 16                   # Número de partículas
v0 = 1.0                 # Magnitud máxima de la velocidad inicial

# Inicialización de arrays
x = zeros(N, float)      # Posiciones en x
y = zeros(N, float)      # Posiciones en y
vx = zeros(N, float)     # Velocidades en x
vy = zeros(N, float)     # Velocidades en y

# Distribuir las partículas en una red cuadrada con pequeño ruido
n = 0
lado = int(sqrt(N))
for i in range(lado):
    for j in range(lado):
        if n < N:
            x[n] = i + 0.5 + 0.1 * (random() - 0.5)
            y[n] = j + 0.5 + 0.1 * (random() - 0.5)
            vx[n] = 2 * v0 * (random() - 0.5)
            vy[n] = 2 * v0 * (random() - 0.5)
            n += 1

# Visualización de las posiciones iniciales
figure()
scatter(x, y)
xlim(0, L)
ylim(0, L)
title("Distribución inicial de partículas")
show()
